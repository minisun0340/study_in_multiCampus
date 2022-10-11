/*1. 2000 년 이후 입사 한 사원들의 정보를 출력
사번, 이름, 타이틀, 부서, 지역*/
SELECT empno, empname, titlename, deptname, deptloc FROM emp e
INNER JOIN title t
ON e.titleno = t.titleno
INNER JOIN dept d
ON e.deptno = d.deptno
WHERE YEAR(e.hdate) > 2000;

/*2. 부서 이름 별 월급의 평균을 구하시오
단, 평균이 3000 이상인 부서만 출력*/
SELECT d.deptname, AVG(salary/12) AS avgms FROM emp e
INNER JOIN dept d
ON e.deptno=d.deptno
GROUP BY e.deptno
HAVING AVG(salary) > 3000;

/*3. 대구  지역의 직원 들의 평균 연봉을 구하시오*/
SELECT AVG(salary) AS Daegu FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
GROUP BY d.deptname = '대구'



/*4. 홍영자 직원와 같은 부서 직원들의 
근무 월수를 구하시오 (P245 PERIOD_DIFF()) */
SELECT *, PERIOD_DIFF(DATE_FORMAT(CURDATE(), '%Y%m'),DATE_FORMAT(hdate, '%Y%m')) FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE empname = '홍영자')
AND empname NOT IN ('홍영자');



/*5. 입사 년수가 가장 많은 직원 순으로 
정렬 하여 순위를 정한다.
이름, 부서명, 직위, 년수*/
SELECT e.empname, d.deptname, t.titlename, DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(hdate, '%Y') AS wy  
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno
INNER JOIN title t
ON e.titleno = t.titleno
ORDER BY wy DESC;
