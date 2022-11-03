import argparse
import json
import os

import requests
import psycopg2

from dotenv import load_dotenv


load_dotenv()


class ArgumentError(Exception):
    pass


def connect_to_database():
    database_name = os.getenv("DATABASE_NAME")
    database_password = os.getenv("DATABASE_PASSWORD")
    conn = psycopg2.connect(dbname=database_name, user='postgres', host='localhost', password=database_password)
    cur = conn.cursor()
    return cur, conn


def poke_berries(args):
    if (args.id and args.name) or (not args.id and not args.name):
        raise ArgumentError("need to input one argument") 
    
    cur, conn = connect_to_database()
    berry_blob = get_berries_blob(cur, berry_id=args.id, berry_name=args.name)
    if berry_blob:
        return berry_blob    
    api_blob = get_berries_api(args.id or args.name)
    insert_berry_into_berries(cur, conn, api_blob)
    conn.close()
    return api_blob


def get_berries_blob(cur, berry_id=None, berry_name=None): 
    if berry_id:
        cur.execute(f"SELECT blob FROM berries WHERE id = {berry_id};")
    else:
        cur.execute(f"SELECT blob FROM berries WHERE name = '{berry_name}';")
    try:
        row = cur.fetchone()
        blob = row[0]
        blob = json.loads(blob)
        return blob
    except TypeError:
        return None


def get_berries_api(berry_id_or_name):
    response = requests.get(f"https://pokeapi.co/api/v2/berry/{berry_id_or_name}")
    try:
        blob = response.json()
        return blob
    except requests.exceptions.JSONDecodeError:
        raise ArgumentError("ID or name not in API") 


def insert_berry_into_berries(cur, conn, blob):
    berry_id = blob["id"]
    berry_name = blob["name"]
    json_blob = json.dumps(blob)
    sql_statement = f"INSERT INTO berries(name, id, blob) VALUES(%s, %s, %s);"
    cur.execute(sql_statement, (berry_name, berry_id, json_blob))
    conn.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', "--id", type=int, help='the id')
    parser.add_argument('-n', "--name", help='the name')

    args = parser.parse_args()
    print(poke_berries(args))
