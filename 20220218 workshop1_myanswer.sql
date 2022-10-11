/*1. 2000 년 이후 입사 한 사원들의 정보를 출력
사번, 이름, 타이틀, 부서, 지역*/
SELECT * FROM emp e
INNER JOIN dept d ON e.deptno = d.deptno
INNER JOIN title t ON t.titleno = e.titleno

/*2. 부서 이름 별(group by) 월급의 평균을 구하시오
단, 평균이 4000 이상인 부서만 출력*/
SELECT d.deptname, AVG(e.salary) AS avgsalary FROM emp e
INNER JOIN dept d ON e.deptno = d.deptno
GROUP BY d.deptname
HAVING avgsalary >= 3500

/*3. 대구  지역의 직원 들의 평균 연봉을 구하시오*/
SELECT AVG(e.salary) FROM emp e
INNER JOIN dept d ON e.deptno = d.deptno
WHERE d.deptloc = '대구'


/*4. 홍영자 직원와 같은 부서 직원들의 
근무 월수를 구하시오 (P245 PERIOD_DIFF()) */
SELECT *, PERIOD_DIFF(DATE_FORMAT(CURDATE(), '%Y%m'),DATE_FORMAT(hdate, '%Y%m')) FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE empname = '홍영자')
AND empname NOT IN ('홍영자');

/*5. 입사 년수가 가장 많은 직원 순으로 
정렬 하여 순위를 정한다.
이름, 부서명, 직위, 년수*/
SELECT e.empname, d.deptname, t.titlename, 
YEAR(CURDATE()) - YEAR(e.hdate) AS wyear
FROM emp e
LEFT JOIN dept d
ON e.deptno = d.deptno
LEFT JOIN title t
ON e.titleno = t.titleno
ORDER BY wyear DESC;