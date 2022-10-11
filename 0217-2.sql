#null check
SELECT empno, IFNULL(manager,'NONE') FROM emp;

# GROUP BY
# 집계 함수와 함께 사용
#SUM, AVG, MIN, MAX

SELECT * FROM emp;

SELECT deptno, AVG(salary) FROM emp
GROUP BY deptno
HAVING AVG(salary) < 4000
AND deptno = 30;

# 이말숙과 같은 부서의 연봉의 평균을 구하시오.
SELECT AVG(salary) FROM emp
GROUP BY deptno
HAVING deptno = (SELECT deptno FROM emp WHERE empname ='이말숙');

# 이말숙과 홍영자가 속한 부서의 연봉 평균을 구하시오.
# 단 부서명, 연봉 평균을 출력하시오.

SELECT deptno, AVG(salary) AS avg FROM emp
GROUP BY deptno
HAVING deptno IN (SELECT deptno FROM emp WHERE empname IN ('이말숙', '홍영자'))
AND avg > 3500;

# 직급별 월급의 평균을 구하시오
SELECT titleno, AVG(salary/12) as msalary FROM emp
GROUP BY titleno;

# COUNT 함수
SELECT deptno, COUNT(*) AS cnt FROM emp
GROUP BY deptno;

# 우리 회사 직급의 개수를 구하시오
SELECT COUNT(DISTINCT(titleno)) FROM emp;

SELECT deptno, MIN(salary), MAX(salary) FROM emp
GROUP BY deptno;

# 이영자가 속한 부서의 평균 연봉보다 많이 받는 직원을 조회
SELECT * FROM emp
WHERE salary > (
SELECT AVG(salary) FROM emp WHERE deptno = 
(SELECT deptno FROM emp WHERE empname = '이영자'));


# CONCAT
SELECT CONCAT(titleno,'+', deptno,'+', empname, salary) FROM emp

# 순위함수

SELECT  ROW_NUMBER() OVER(ORDER BY salary DESC) AS rk,empname, salary FROM emp LIMIT 3;
SELECT  DENSE_RANK() OVER(ORDER BY salary DESC) AS rk ,empname, salary FROM emp;

# json
SELECT JSON_OBJECT('name', empname, 'sal', salary) FROM emp;







