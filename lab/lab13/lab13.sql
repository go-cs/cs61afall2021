.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


CREATE TABLE sevens AS
  SELECT students.seven from students, numbers 
  WHERE students.number = 7 AND numbers.'7' = "True" AND students.time = numbers.time;


CREATE TABLE avg_difference AS
  SELECT round(avg((abs(a.number - a.smallest) + abs(b.number - b.smallest))/2))
  FROM students AS a, students AS b
  WHERE a.time <> b.time;

