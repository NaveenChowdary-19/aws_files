
Q1 = "SELECT COUNT(name) FROM Movie WHERE year < 2000"

Q2 = "SELECT  AVG(rank) FROM Movie WHERE year =1991"

Q3 = "SELECT MIN(rank) FROM Movie WHERE year = 1991"

Q4 = "SELECT fname , lname FROM Actor INNER JOIN Cast on id = pid WHERE mid = 27"

Q5= "SELECT COUNT(mid) FROM Actor INNER JOIN Cast on id = pid WHERE fname = 'Jon' And lname = 'Dough'"

Q6 = "SELECT name FROM Movie WHERE name LIKE 'Young Latin Girls%' AND year >=2003 AND year <=2006 "

Q7 = "SELECT fname, lname FROM moviedirector inner join director on did = director.id inner join movie on movie.id = mid where name like 'Star Trek%'"

#Q9 = "SELECT fname , lname FROM moviedirector INNER JOIN Movie on `Director`.`id` = `Movie`.`id` WHERE COUNT(`Movie`.`id`) >= 4 AND year = 2001 "
 
Q9 = "SELECT fname,lname FROM Director INNER JOIN MovieDIRECTOR ON `Director`.`id`=did INNER JOIN Movie ON `Movie`.`id`=mid WHERE year = 2001 GROUP BY did HAVING COUNT(mid)>=4 ORDER BY fname ASC,lname DESC"

Q10 = "SELECT gender, COUNT(*) FROM Actor GROUP BY gender ORDER BY gender ASC;"


 
