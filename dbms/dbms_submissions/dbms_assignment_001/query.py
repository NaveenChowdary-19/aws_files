Q1 = "CREATE TABLE User (user_id INTTEGER PRIMRY KEY , first_name VARCHAR(200) NOT NULL , last_name VARCHAR(200) NOT NULL , address VARCHAR(300) NOT NULL , phone_number INTEGER NOT NULL)"         

Q2 = "CREATE TABLE Post (user_id INTEGER , post_id INTEGER PRIMRY KEY AUTOINCREMENT, post_content VARCHAR(500))"

Q3 = "INSERT INTO User( User_id , first_name , last_name , address , phone_number) VALUES (1 , 'tony' , 'stark' , 'new york' , 1234567890)"

Q4 = "INSERT INTO User( User_id , first_name , last_name , address , phone_number) VALUES (2 , 'john' , 'wick' , 'la' , 987654321)"

Q5 = "INSERT INTO Post (user_id , post_content) VALUES(1 , 'my first post')"

Q8 = "UPDATE User SET first_name = 'thor' SET last_name = 'ragnarok WHERE first_name = 'tony'"