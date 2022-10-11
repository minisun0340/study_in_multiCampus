#DROP TABLE cust;
#DROP TABLE item;

CREATE TABLE cust(
   id CHAR(5),
   pwd VARCHAR(10) NOT NULL,
   name VARCHAR(10) NOT NULL
);
ALTER TABLE cust ADD PRIMARY KEY (id);
INSERT INTO cust VALUES('id01','pwd01','이말숙');
INSERT INTO cust VALUES('id02','pwd02','김말숙');
INSERT INTO cust VALUES('id03','pwd03','정말숙');
# ------------------------------------------

CREATE TABLE item(
   id INT,
   name VARCHAR(20) NOT NULL,
   price INT  NOT NULL,
   imgname VARCHAR(20),
   regdate DATE  NOT NULL
);
ALTER TABLE item ADD PRIMARY KEY (id);
ALTER TABLE item MODIFY id INT AUTO_INCREMENT;
ALTER TABLE item AUTO_INCREMENT = 1000;

INSERT INTO item (name,price,imgname,regdate) VALUES('pants1',10000,'pants1.jpg',CURRENT_DATE());
INSERT INTO item (name,price,imgname,regdate) VALUES('pants2',20000,'pants2.jpg',CURRENT_DATE());
INSERT INTO item (name,price,imgname,regdate) VALUES('pants3',30000,'pants3.jpg',CURRENT_DATE());
INSERT INTO item (name,price,imgname,regdate) VALUES('pants4',40000,'pants4.jpg',CURRENT_DATE());

#DROP TABLE cart;
CREATE TABLE cart(
	id INT,
	custid CHAR(5),
	itemid INT,
	num INT,
	regdate DATE
);

ALTER TABLE cart ADD PRIMARY KEY (id);
ALTER TABLE cart MODIFY id INT AUTO_INCREMENT;
ALTER TABLE cart AUTO_INCREMENT = 100;
ALTER TABLE cart ADD CONSTRAINT FOREIGN KEY (custid) REFERENCES cust(id);
ALTER TABLE cart ADD CONSTRAINT FOREIGN KEY (itemid) REFERENCES item(id);


INSERT INTO cart (custid, itemid,num,regdate) VALUES ('id01',1000,10,CURRENT_DATE());