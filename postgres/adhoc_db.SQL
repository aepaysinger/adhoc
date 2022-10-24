CREATE TABLE candy(
    candy_id INT PRIMARY,
    name VARCHAR(20),
);

INSERT INTO candy(candy_id, candy_name)
Values (1, "Skittles"), (2, "M&M"), (3, "100 Grand"), (4, "Sour Patch Kids"), (5, "Swedish Fish"), 
(6, "Kit-Kat"), (7, "Snickers"), (8, "Starburst"), (9, "Milk Duds"), (10, "Nerds");

CREATE TABLE friends(
    friend_id INT PRIMARY,
    name VARCHAR(20)
);

INSERT INTO friends(friend_id, friend_name)
Values (1, 'Rusty'), (2, 'Lemon'), (3, 'Choco'), (4, 'King'), (5, 'Beana'), (6, 'Birdie'), (7, 'Dot'), 
(8, 'Dixie'), (9, 'Poncho'), (10, 'Lefty');


CREATE TABLE favorite_candy(
    friend_id INT,
    candy_id INT,
    PRIMARY KEY(friend_id, candy_id),
    FOREIGN KEY(friend_id) REFERENCES friends(friend_id) ON DELETE CASCADE,
    FOREIGN KEY(candy_id) REFERENCES candy(candy_id) ON DELETE CASCADE
);

INSERT INTO favorite_candy(friend_id, candy_id)
VALUES (1, 4), (1, 5), (1, 6), (2, 1), (2, 4), (2, 5), (2, 8), (2, 10), (3, 2), (3, 3), (3, 6), (3, 7), (3, 9),
(4, 3), (4, 7), (4, 10), (5, 1), (5, 2), (6, 10), (6, 8), (6, 5), (6, 4), (7, 1), (7, 10), (7, 2),
(8, 1), (8, 10), (8, 2), (9, 7), (9, 3), (9, 6), (10, 5), (10, 10), (10, 8), (10, 4);