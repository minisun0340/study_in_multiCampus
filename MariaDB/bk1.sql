-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.3.34-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 테이블 company.dept 구조 내보내기
CREATE TABLE IF NOT EXISTS `dept` (
  `deptno` char(2) NOT NULL,
  `deptname` varchar(20) DEFAULT NULL,
  `deptloc` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`deptno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 company.dept:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `dept` DISABLE KEYS */;
INSERT INTO `dept` (`deptno`, `deptname`, `deptloc`) VALUES
	('10', '관리부', '서울'),
	('20', '생산부', '부산'),
	('30', '영업부', '대구'),
	('40', '기술부', '대전');
/*!40000 ALTER TABLE `dept` ENABLE KEYS */;

-- 테이블 company.emp 구조 내보내기
CREATE TABLE IF NOT EXISTS `emp` (
  `empno` char(4) NOT NULL,
  `titleno` char(2) DEFAULT NULL,
  `deptno` char(2) DEFAULT NULL,
  `empname` varchar(10) DEFAULT NULL,
  `manager` char(4) DEFAULT NULL,
  `salary` int(5) DEFAULT NULL,
  `hdate` date DEFAULT NULL,
  PRIMARY KEY (`empno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 company.emp:~10 rows (대략적) 내보내기
/*!40000 ALTER TABLE `emp` DISABLE KEYS */;
INSERT INTO `emp` (`empno`, `titleno`, `deptno`, `empname`, `manager`, `salary`, `hdate`) VALUES
	('1001', '40', '10', '킹', NULL, 5000, '1997-01-01'),
	('1002', '30', '20', '이영업', '1001', 4300, '1998-01-01'),
	('1003', '30', '30', '김생산', '1001', 4800, '1999-01-01'),
	('1004', '30', '40', '홍연구', '1001', 4500, '1999-12-01'),
	('1005', '20', '20', '이말숙', '1002', 3300, '2000-01-01'),
	('1006', '10', '20', '김말숫', '1002', 2800, '2001-01-01'),
	('1007', '20', '30', '홍영자', '1003', 3500, '2000-12-01'),
	('1008', '10', '30', '이영자', '1003', 2300, '2002-05-01'),
	('1009', '20', '40', '김강국', '1004', 3800, '2001-01-01'),
	('1010', '10', '40', '홍정국', '1004', 2500, '2002-12-01');
/*!40000 ALTER TABLE `emp` ENABLE KEYS */;

-- 테이블 company.title 구조 내보내기
CREATE TABLE IF NOT EXISTS `title` (
  `titleno` char(2) NOT NULL,
  `titlename` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`titleno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 company.title:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `title` DISABLE KEYS */;
INSERT INTO `title` (`titleno`, `titlename`) VALUES
	('10', '사원'),
	('20', '대리'),
	('30', '팀장'),
	('40', '대표');
/*!40000 ALTER TABLE `title` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
