"""

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+



SELECT DISTINCT(p1.email)
FROM Person as p1,  Person as p2
WHERE p1.Id != p2.Id AND p1.email = p2.email;



select Email
from Person
group by Email
having count(Email) > 1;


"""