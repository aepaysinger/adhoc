CREATE TABLE candy(
    candy_id INT PRIMARY,
    name VARCHAR(20),
);

INSERT INTO candy(candy_id, name)
Values (candy_id, name);
"candy_id"	"candy_name"
1	"Skittles"
2	"M&M"
3	"100 Grand"
4	"Sour Patch Kids"
5	"Swedish Fish"
6	"Kit-Kat"
7	"Snickers"
8	"Starburts"
9	"Milk Duds"
10	"Nerds"
CREATE TABLE friends(
    friend_id INT PRIMARY,
    name VARCHAR(20)
);

INSERT INTO friends(friend_id, name)
Values (friend_id, name);
"friend_id"	"friend_name"
1	"Rusty"
2	"Lemon"
3	"Choco"
4	"King"
5	"Beana"
6	"Birdie"
7	"Dot"
8	"Dixie"
9	"Poncho"
10	"Lefty"

CREATE TABLE favorite_candy(
    friend_id INT,
    candy_id INT,
    PRIMARY KEY(friend_id, candy_id),
    FOREIGN KEY(friend_id) REFERENCES friends(friend_id) ON DELETE CASCADE,
    FOREIGN KEY(candy_id) REFERENCES candy(candy_id) ON DELETE CASCADE
);

INSERT INTO favorite_candy(friend_id, candy_id)
VALUES(1, 4)(1, 5)(1, 6)