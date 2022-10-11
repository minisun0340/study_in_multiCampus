DROP TABLE itemtbl;
CREATE TABLE itemtbl(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(20),
	price INT,
	regdate DATETIME
);

# DATE만하면 년월일 -> CURDATE
# DATETIME 하면 시간까지 -> NOW

ALTER TABLE itemtbl AUTO_INCREMENT = 1000;

INSERT INTO itemtbl VALUES (id, 'shirts', 30000, NOW());
SELECT LAST_INSERT_ID();
SELECT * FROM itemtbl;

SELECT id, NAME, DATE_FORMAT(regdate, '%Y%m%d%H%i%s') FROM itemtbl;

UPDATE itemtbl SET NAME = 'pants' WHERE id = 1000;
