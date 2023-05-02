UNLOCK TABLES;
DROP DATABASE IF EXISTS `truonghoc`;
CREATE DATABASE `truonghoc`;
USE `truonghoc`;

-- DROP TABLE IF EXISTS `truong`;
DROP TABLE IF EXISTS `LOAIHINH`;
CREATE TABLE `LOAIHINH` (
  `MaLH` varchar(50) NOT NULL,
  `TenLH` varchar(45) NOT NULL,
  PRIMARY KEY (`MaLH`)
) DEFAULT CHARSET=utf8;


INSERT INTO `LOAIHINH`
VALUES ('CL', 'Công lập'),
		('TT', 'Tư thục'),
    ('DL', 'Dân lập');

DROP TABLE IF EXISTS `PHONGGDDT`;
CREATE TABLE `PHONGGDDT` (
  `MaPGD` varchar(45) NOT NULL,
  `TenPGD` varchar(100),
  `TenSGD` varchar(100) NOT NULL,
  PRIMARY KEY (`MaPGD`)
) DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `LOAITRUONG`;
CREATE TABLE `LOAITRUONG` (
  `MaLT` varchar(50) NOT NULL,
  `TenLTrg` varchar(100) NOT NULL,
  PRIMARY KEY (`MaLT`)
) DEFAULT CHARSET=utf8;

INSERT INTO `LOAITRUONG`
VALUES ('PT', 'Trường phổ thông'),
		    ('GDTX', 'TT GDTX'),
        ('DTBT', 'Dân tộc bán trú'),
        ('NKTT', 'Năng khiếu thể dục thể thao'),
        ('GDNN', 'TT GDNN - GDTX (Sát nhập theo TTLT số 39/2015)');

DROP TABLE IF EXISTS CAP;
CREATE TABLE CAP(
    `MaCap` CHAR(10) NOT NULL,
    `TenCap` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`MaCap`)
)DEFAULT CHARSET=utf8;

INSERT INTO `CAP`
VALUES ('TX', 'Giáo dục thường xuyên'),
		('MN', 'Mầm non'),
        ('TH', 'Tiểu học'),
        ('THCS', 'Trung học cơ sở'),
        ('THPT', 'Trung học phổ thông');

CREATE TABLE `truong` (
  `MaTrg` varchar(50) NOT NULL,
  `TenTrg` varchar(200) NOT NULL,
  -- `SoGD` tinyint(2) DEFAULT 0,
  `PhongGD` varchar(100) DEFAULT NULL,
  `DiaChi` varchar(300) DEFAULT NULL,
  `LoaiHinh` varchar(50) DEFAULT 0,
  `LoaiTruong` varchar(50) DEFAULT 0,
  `CapHoc` varchar(50) DEFAULT 0, 
  PRIMARY KEY (`MaTrg`, `CapHoc`),
  CONSTRAINT FOREIGN KEY (`LoaiHinh`) REFERENCES `LOAIHINH` (`MaLH`) ,
  CONSTRAINT FOREIGN KEY (`LoaiTruong`) REFERENCES `LOAITRUONG` (`MaLT`),
  CONSTRAINT FOREIGN KEY (`PhongGD`) REFERENCES `PHONGGDDT` (`MaPGD`),
  CONSTRAINT FOREIGN KEY (`CapHoc`) REFERENCES `CAP` (`MaCap`)
  /* CONSTRAINT FOREIGN KEY (`BacHoc`) REFERENCES `BACHOC` (`stt`) */
) DEFAULT CHARSET=utf8;


