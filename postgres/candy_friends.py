
def show_favorite_candy():
    import psycopg2
    try:
        conn = psycopg2.connect("dbname='adhoc_db' user='postgres' host='localhost' password='RustyLemon'")
    except:
        print("I am unable to connect to the database")
    
    cur = conn.cursor()
    cur.execute("SELECT favorite_candy.friend_id, favorite_candy.candy_id, friends.friend_name, candy.candy_name FROM favorite_candy INNER JOIN friends on favorite_candy.friend_id = friends.friend_id INNER JOIN candy on candy.candy_id = favorite_candy.candy_id;")
    friends_and_candy = cur.fetchall()
    
    
    candy_they_like = {}
    for set in friends_and_candy:
        if set[3] in candy_they_like:
            candy_they_like[set[3]].append(set[2])
        else:
            candy_they_like[set[3]] = [set[2]]
    conn.close()
    return candy_they_like