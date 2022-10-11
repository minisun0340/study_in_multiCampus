/*1. emp 정보를 조회 한다. 
emp 직원들의 모든 정보와 사원의 Manager 정보 까지 조회 한다.
출력 정보 
empno, empname, titlename, mgrname*/
SELECT * FROM emp e
LEFT JOIN title t ON e.titleno = t.titleno
LEFT JOIN emp e2 ON e.manager = e2.empno

/*2. emp 정보를 조회 한다. 
모든 emp 직원들의 모든 정보와 사원의 Manager명 정보 까지 조회 한다.
추가 적으로 의 부서명,타이틀명 까지 출력 한다.*/
SELECT * FROM emp e
LEFT JOIN dept d ON e.deptno = d.deptno
LEFT JOIN title t ON e.titleno = t.titleno
LEFT JOIN emp e2 ON e.manager = e2.empno