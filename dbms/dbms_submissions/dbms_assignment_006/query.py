Q1 = "SELECT fname , lname FROM Actor INNER JOIN Cast on id = pid WHERE mid = 12148"

Q2 = "SELECT COUNT(mid) FROM Actor INNER JOIN Cast on id = pid WHERE fname = 'Harrison (I)' AND lname = 'Ford'"

Q3 = "SELECT DISTINCT (pid) FROM Actor INNER JOIN Cast on id = pid WHERE name LIKE 'Young Latin Girls%'"