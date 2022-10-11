# JOIN

# 1. INNER JOIN
SELECT e.empname, d.deptname, t.titlename FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno;

SELECT e.empname, d.deptname, t.titlename, e.salary FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno
WHERE e.salary > 3000
ORDER BY e.empname;


SELECT t.titlename, AVG(e.salary) AS av FROM emp e
INNER JOIN title t
ON e.titleno = t.titleno
GROUP BY t.titlename
HAVING av > 3000;

# 부서별 사원과 대리의 연봉 평균을 구하시오
SELECT d.deptname, AVG(e.salary) AS av FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno
WHERE t.titleno IN (10, 20)
GROUP BY d.deptname;

# 2. OUTTER JOIN

INSERT INTO emp VALUES ('9999',NULL,NULL, '이신입',NULL, 3000,'2022-01-01' );
INSERT INTO emp VALUES ('9998',NULL,NULL, '김신입',NULL, 3000,'2022-01-01' );
INSERT INTO title VALUES ('50', '고문');

SELECT * FROM emp e
LEFT JOIN title t
ON e.titleno = t.titleno;

SELECT * FROM emp e
RIGHT JOIN title t
ON e.titleno = t.titleno;

# 3. SELF JOIN

# 사원정보를 조회한다. 사원의 mgr의 이름 정보도 조회한다.
SELECT e.empname, m.empname AS manager FROM emp e
LEFT JOIN emp m
ON e.manager=m.empno;






/*
1. 사원 정보를 조회 한다. 
사원의 모든 정보와 사원의 Manager 정보 까지 조회 한다.

2. 사원 정보를 조회 한다. 
사원의 모든 정보와 사원의 Manager 정보 까지 조회 한다.
추가 적으로 사원의 부서와 타이틀 정보 까지 조회 한다.*/






