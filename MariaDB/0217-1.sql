-- select 구문
/*
SQL 공부
SQL 공부
*/

SELECT empno, empname, salary/12 AS 'monthly salary' FROM emp;
SELECT empno, empname FROM emp;
DESC emp;
SELECT * FROM emp WHERE empname = '킹';
SELECT * FROM emp WHERE salary > 3000;
SELECT * FROM emp WHERE DATE_FORMAT(hdate, '%Y') > 2000; -- 데이터포맷 DATE쓰고 ctrl space
# 1월에 입사한 직원을 조회
SELECT * FROM emp WHERE DATE_FORMAT(hdate, '%d') = 01;
SELECT empname, DATE_FORMAT(hdate, '%Y%m%d') AS hdate FROM emp;

SELECT * FROM emp WHERE MONTH(hdate) = 01;
SELECT * FROM emp WHERE YEAR(hdate) = 2000;


SELECT * FROM emp;
# 월급이 4000 ~ 5000 인 직원을 조회하시오
SELECT * FROM emp WHERE salary >= 4000 AND salary <= 5000;
SELECT * FROM emp WHERE salary BETWEEN 4000 AND 5000;  -- 시작과 끝 포함(=)

# depno 가 10, 30, 40 인 직원을 조회하시오
SELECT * FROM emp WHERE deptno = 10 OR deptno = 30 OR deptno = 40;
SELECT * FROM emp WHERE deptno IN (10, 30, 40);
SELECT * FROM emp WHERE deptno NOT IN (10, 30, 40);

# 이씨를 조회
SELECT * FROM emp WHERE empname LIKE '이%';
SELECT * FROM emp WHERE empname LIKE '%이%'; -- 어딘가에 이가 있는 사람
SELECT * FROM emp WHERE empname LIKE '_영자';

# 서브 쿼리
SELECT deptno FROM emp WHERE empname = '이영자';
SELECT * FROM emp WHERE deptno = 30;

SELECT * FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE empname = '이영자');
 -- 여기서 샐러리가 3000이상
 
SELECT * FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE empname = '이영자')
AND salary >= 3000;

-- titleno 가 30 번인 직원들의 deptno와 같은 직원들의 사번과 이름을 출력
SELECT empno, empname FROM emp 
WHERE deptno IN (SELECT deptno FROM emp WHERE titleno = 30);

SELECT * FROM emp ORDER BY deptno, empname;
SELECT * FROM emp ORDER BY 3, 4;
SELECT * FROM emp ORDER BY salary DESC;

# DISTINCT
SELECT DISTINCT (titleno) FROM emp;
SELECT DISTINCT (manager) FROM emp;

# limit 
SELECT * FROM emp ORDER BY salary DESC LIMIT 5; /*상위 5개 출력*/

SELECT * FROM emp ORDER BY salary DESC LIMIT 1,3;

# CASE WHEN THEN
# salary 가 4000 이상이면 '상' 출력, 미만이면 '하' 출력
# 컬럼명은 grade 로 출력
# 단, empname, salary, grade 로 출력하시오

SELECT empname, salary, 
CASE
WHEN salary >= 4000 THEN '상'
ELSE '하'
END AS grade
FROM emp;

/*
1. 직원정보를 출력 한다. 직원의 연봉 정보와 연봉의 세금 정보를 같이 출력 한다.

세금은 10%

2. 직원정보 중 2001 이전에 입사 하였고 월급이 4000만원 미만인 직원을 조회

3. manager가 있는 직원 중 이름에 '자' 가 들어가 있는 직원정보 조회

4. 월급이 2000미만은 '하' 4000미만은 '중' 4000이상은 '고' 를 출력*/
SELECT *, salary*0.1 AS tax FROM emp;

SELECT * FROM emp WHERE DATE_FORMAT(hdate, '%Y') < 2001
AND salary < 4000;

SELECT * FROM emp WHERE manager IS NOT NULL 
AND empname LIKE '%자%';

SELECT empname , salary, 
CASE
WHEN salary < 2000 THEN '하'
WHEN salary <4000 THEN '중'
ELSE '상'
END AS grade
FROM emp;


#null check
SELECT empno, IFNULL(manager,'NONE') FROM emp;