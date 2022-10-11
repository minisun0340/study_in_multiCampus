/* 
5. 부서 별 월급의 평균을 구하시오
단, 평균이 3000 이상인 부서만 출력
6. 부서 별 대리와 사원 연봉의 평균을 구하시오
단, 평균이 2500 이상인 부서만 출력
7. 2000년 부터 2002년에 입사는 직원들의
월급의 평균을 구하시오
8. 서울에서 근무하는 직원들을 조회 하시오
9. 이영자가 속한 부서의 직원 월급평균 보다 많이 받는 직원들을  조회 하시오
10. 김강국의 타이틀과 같은 직원들의 연봉보다 많이 받는 직원 들 중 2000 이전 입사한 직원들을 조회 하시오
*/
#5
SELECT deptno, AVG(salary/12) AS average FROM emp
GROUP BY deptno
HAVING AVG(salary) >= 3000;

SELECT * FROM emp;
#6
SELECT deptno, AVG(salary) as avg_salary FROM emp 
WHERE titleno IN (10, 20)
GROUP BY deptno
HAVING avg_salary >= 2500;

#7
SELECT AVG(salary/12) FROM emp WHERE YEAR(hdate) >= 2000 AND YEAR(hdate) <= 2002; 

#8 서울에서 근무하는 직원들을 조회 하시오
SELECT * FROM emp
WHERE deptno = (SELECT deptno FROM dept WHERE deptloc = '서울');


#9
SELECT *, salary/12 AS msalary FROM emp 
WHERE (salary/12) > (
SELECT AVG(salary/12) FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE empname = '이영자'));

# 10. 김강국의 타이틀과 같은 직원들의 연봉보다 
# 많이 받는 직원 들 중 2000 이전 입사한 직원들을 조회 하시오

SELECT * FROM emp WHERE salary >
(SELECT AVG(salary) FROM emp WHERE titleno = 
(SELECT titleno FROM emp WHERE empname = '김강국'))
AND YEAR(hdate) < 2000;