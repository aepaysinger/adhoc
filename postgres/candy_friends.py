import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def show_favorite_candy():
 
    friends_and_candy = get_friends_and_candy()
    
    candy_they_like = {}
    for candy, friend in friends_and_candy:
        candy_they_like[candy] = candy_they_like.get(candy, []) + [friend]
        
    return candy_they_like


def get_friends_and_candy():
    database_name = os.getenv("DATABASE_NAME")
    database_password = os.getenv("DATABASE_PASSWORD")
    
    conn = psycopg2.connect(dbname=database_name, user='postgres', host='localhost', password=database_password)
    
    cur = conn.cursor()
    cur.execute(
        "SELECT friends.friend_name, candy.candy_name " 
        "FROM favorite_candy "
        "INNER JOIN friends on favorite_candy.friend_id = friends.friend_id " 
        "INNER JOIN candy on candy.candy_id = favorite_candy.candy_id;"
    )
    friends_and_candy = cur.fetchall()
    conn.close()
    return friends_and_candy


if __name__ == "__main__":
    print(show_favorite_candy())
