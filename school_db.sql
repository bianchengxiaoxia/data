/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 80037
 Source Host           : localhost:3306
 Source Schema         : school_db

 Target Server Type    : MySQL
 Target Server Version : 80037
 File Encoding         : 65001

 Date: 03/06/2024 17:20:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `cno` char(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `cname` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `credit` tinyint NOT NULL,
  PRIMARY KEY (`cno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of course
-- ----------------------------
INSERT INTO `course` VALUES ('101', '水之呼吸', 3);
INSERT INTO `course` VALUES ('102', '雷之呼吸', 3);
INSERT INTO `course` VALUES ('103', '炎之呼吸', 3);
INSERT INTO `course` VALUES ('104', '风之呼吸', 3);
INSERT INTO `course` VALUES ('105', '八分光轮', 2);
INSERT INTO `course` VALUES ('106', '断头刀', 3);
INSERT INTO `course` VALUES ('107', '蛇之呼吸', 3);
INSERT INTO `course` VALUES ('108', '花之呼吸', 3);
INSERT INTO `course` VALUES ('109', '音之呼吸', 3);
INSERT INTO `course` VALUES ('110', '日之呼吸', 3);
INSERT INTO `course` VALUES ('112', '岩之呼吸', 3);
INSERT INTO `course` VALUES ('220', '火之神神乐1', 4);
INSERT INTO `course` VALUES ('221', '碧罗之天', 2);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `sno` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sname` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `birthday` date NULL DEFAULT NULL,
  `tel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`sno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('2102041', '炭治郎', 'M', '2000-01-01', '1234567890');
INSERT INTO `student` VALUES ('2102042', '祢豆子', 'F', '2000-02-02', '2345678901');
INSERT INTO `student` VALUES ('2102043', '善逸', 'M', '2000-03-03', '3456789012');
INSERT INTO `student` VALUES ('2102044', '伊之助', 'M', '2000-04-04', '4567890123');
INSERT INTO `student` VALUES ('2102046', '天音', 'F', '2000-06-06', '6789012345');
INSERT INTO `student` VALUES ('2102047', '时透', 'M', '2000-07-07', '7890123456');
INSERT INTO `student` VALUES ('2102048', '煉獄', 'M', '2000-08-08', '8901234567');
INSERT INTO `student` VALUES ('2102049', '无惨', 'M', '2000-09-09', '9012345678');
INSERT INTO `student` VALUES ('2102050', '光太郎', 'M', '2000-10-10', '0123456789');
INSERT INTO `student` VALUES ('2210204', '大古', '男', '1990-06-01', '123-456-7890');
INSERT INTO `student` VALUES ('22102041', '炭治郎', 'M', '2000-01-01', '1234567890');
INSERT INTO `student` VALUES ('22102042', '祢豆子', 'F', '2000-02-02', '2345678901');
INSERT INTO `student` VALUES ('22102043', '善逸', 'M', '2000-03-03', '3456789012');
INSERT INTO `student` VALUES ('22102045', '义勇', 'M', '2000-05-05', '5678901234');
INSERT INTO `student` VALUES ('22102046', '天音', 'F', '2000-06-06', '6789012345');
INSERT INTO `student` VALUES ('22102047', '时透', 'M', '2000-07-07', '7890123456');
INSERT INTO `student` VALUES ('22102048', '煉獄', 'M', '2000-08-08', '8901234567');
INSERT INTO `student` VALUES ('22102049', '无惨', 'M', '2000-09-09', '9012345678');
INSERT INTO `student` VALUES ('22102050', '光太郎', 'M', '2000-10-10', '0123456789');
INSERT INTO `student` VALUES ('2210456', '崛井', '男', '1991-08-22', '123-456-7892');
INSERT INTO `student` VALUES ('2211111', '夏雨鍩', '男', '2004-10-25', '15122107010');
INSERT INTO `student` VALUES ('2212437', '丽娜', '女', '1992-07-15', '123-456-7891');
INSERT INTO `student` VALUES ('2213478', '宗方', '男', '1989-05-30', '123-456-7893');

-- ----------------------------
-- Table structure for student_course
-- ----------------------------
DROP TABLE IF EXISTS `student_course`;
CREATE TABLE `student_course`  (
  `sno` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tcid` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `score` tinyint NULL DEFAULT NULL,
  PRIMARY KEY (`sno`, `tcid`) USING BTREE,
  INDEX `student_course_ibfk_2`(`tcid` ASC) USING BTREE,
  CONSTRAINT `student_course_ibfk_1` FOREIGN KEY (`sno`) REFERENCES `student` (`sno`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `student_course_ibfk_2` FOREIGN KEY (`tcid`) REFERENCES `course` (`cno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_course
-- ----------------------------
INSERT INTO `student_course` VALUES ('2102041', '101', 85);
INSERT INTO `student_course` VALUES ('2102041', '102', 90);
INSERT INTO `student_course` VALUES ('2102042', '101', 88);
INSERT INTO `student_course` VALUES ('2102042', '103', 92);
INSERT INTO `student_course` VALUES ('2102043', '104', 75);
INSERT INTO `student_course` VALUES ('2102043', '105', 80);
INSERT INTO `student_course` VALUES ('2102043', '106', 99);
INSERT INTO `student_course` VALUES ('2102044', '102', 85);
INSERT INTO `student_course` VALUES ('2102044', '106', 78);
INSERT INTO `student_course` VALUES ('2102046', '104', 77);
INSERT INTO `student_course` VALUES ('2102046', '108', 83);
INSERT INTO `student_course` VALUES ('2102047', '105', 92);
INSERT INTO `student_course` VALUES ('2102047', '109', 87);
INSERT INTO `student_course` VALUES ('2102048', '106', 91);
INSERT INTO `student_course` VALUES ('2102048', '110', 85);
INSERT INTO `student_course` VALUES ('2102049', '101', 88);
INSERT INTO `student_course` VALUES ('2102049', '107', 79);
INSERT INTO `student_course` VALUES ('2102050', '102', 90);
INSERT INTO `student_course` VALUES ('2102050', '108', 93);
INSERT INTO `student_course` VALUES ('2210204', '101', 88);
INSERT INTO `student_course` VALUES ('22102041', '101', 85);
INSERT INTO `student_course` VALUES ('22102041', '102', 90);
INSERT INTO `student_course` VALUES ('22102042', '101', 88);
INSERT INTO `student_course` VALUES ('22102042', '103', 92);
INSERT INTO `student_course` VALUES ('22102043', '104', 75);
INSERT INTO `student_course` VALUES ('22102043', '105', 80);
INSERT INTO `student_course` VALUES ('22102045', '103', 95);
INSERT INTO `student_course` VALUES ('22102045', '107', 89);
INSERT INTO `student_course` VALUES ('22102046', '104', 77);
INSERT INTO `student_course` VALUES ('22102046', '108', 83);
INSERT INTO `student_course` VALUES ('22102047', '105', 100);
INSERT INTO `student_course` VALUES ('22102047', '109', 87);
INSERT INTO `student_course` VALUES ('22102048', '106', 91);
INSERT INTO `student_course` VALUES ('22102048', '110', 85);
INSERT INTO `student_course` VALUES ('22102049', '101', 88);
INSERT INTO `student_course` VALUES ('22102049', '107', 79);
INSERT INTO `student_course` VALUES ('22102050', '102', 90);
INSERT INTO `student_course` VALUES ('22102050', '108', 95);
INSERT INTO `student_course` VALUES ('2210456', '102', 92);
INSERT INTO `student_course` VALUES ('2211111', '112', 100);
INSERT INTO `student_course` VALUES ('2211111', '220', 100);
INSERT INTO `student_course` VALUES ('2211111', '221', 100);
INSERT INTO `student_course` VALUES ('2212437', '101', 85);
INSERT INTO `student_course` VALUES ('2213478', '103', 90);

-- ----------------------------
-- Table structure for student_pwd
-- ----------------------------
DROP TABLE IF EXISTS `student_pwd`;
CREATE TABLE `student_pwd`  (
  `user` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pwd` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user`) USING BTREE,
  CONSTRAINT `student_pwd_ibfk_1` FOREIGN KEY (`user`) REFERENCES `student` (`sno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_pwd
-- ----------------------------
INSERT INTO `student_pwd` VALUES ('2102041', '2102041');
INSERT INTO `student_pwd` VALUES ('2102042', '2102042');
INSERT INTO `student_pwd` VALUES ('2102043', '2102043');
INSERT INTO `student_pwd` VALUES ('2102044', '2102044');
INSERT INTO `student_pwd` VALUES ('2102046', '2102046');
INSERT INTO `student_pwd` VALUES ('2102047', '2102047');
INSERT INTO `student_pwd` VALUES ('2102048', '2102048');
INSERT INTO `student_pwd` VALUES ('2102049', '2102049');
INSERT INTO `student_pwd` VALUES ('2102050', '2102050');
INSERT INTO `student_pwd` VALUES ('2210204', '2210204');
INSERT INTO `student_pwd` VALUES ('22102041', '22102041');
INSERT INTO `student_pwd` VALUES ('22102042', '22102042');
INSERT INTO `student_pwd` VALUES ('22102043', '22102043');
INSERT INTO `student_pwd` VALUES ('22102045', '22102045');
INSERT INTO `student_pwd` VALUES ('22102046', '22102046');
INSERT INTO `student_pwd` VALUES ('22102047', '22102047');
INSERT INTO `student_pwd` VALUES ('22102048', '22102048');
INSERT INTO `student_pwd` VALUES ('22102049', '22102049');
INSERT INTO `student_pwd` VALUES ('22102050', '22102050');
INSERT INTO `student_pwd` VALUES ('2210456', '2210456');
INSERT INTO `student_pwd` VALUES ('2211111', '2211111');
INSERT INTO `student_pwd` VALUES ('2212437', '2212437');
INSERT INTO `student_pwd` VALUES ('2213478', '2213478');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `tno` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `tname` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sex` char(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `birthday` date NULL DEFAULT NULL,
  `tel` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tno`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('2102051', '赛文', '男', '1970-01-01', '1111111111');
INSERT INTO `teacher` VALUES ('2102052', '艾斯', '男', '1970-02-02', '2222222222');
INSERT INTO `teacher` VALUES ('2102053', '泰罗', '男', '1970-03-03', '3333333333');
INSERT INTO `teacher` VALUES ('2102054', '杰克', '男', '1970-04-04', '4444444444');
INSERT INTO `teacher` VALUES ('2102055', '雷欧', '男', '1970-05-05', '5555555555');
INSERT INTO `teacher` VALUES ('2102056', '阿斯特拉', '男', '1970-06-06', '6666666666');
INSERT INTO `teacher` VALUES ('2102057', '迪迦', '男', '1970-07-07', '7777777777');
INSERT INTO `teacher` VALUES ('2102058', '戴拿', '男', '1970-08-08', '8888888888');
INSERT INTO `teacher` VALUES ('2102059', '盖亚', '男', '1970-09-09', '9999999999');
INSERT INTO `teacher` VALUES ('2102060', '阿古茹', '男', '1970-10-10', '0000000000');
INSERT INTO `teacher` VALUES ('2210208', '入间', '女', '1965-04-11', '123-456-8000');
INSERT INTO `teacher` VALUES ('2210209', '真崎', '男', '1967-09-19', '123-456-8001');
INSERT INTO `teacher` VALUES ('2210210', '花泽', '女', '1970-01-01', '123-456-8002');

-- ----------------------------
-- Table structure for teacher_pwd
-- ----------------------------
DROP TABLE IF EXISTS `teacher_pwd`;
CREATE TABLE `teacher_pwd`  (
  `user` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pwd` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user`) USING BTREE,
  CONSTRAINT `teacher_pwd_ibfk_1` FOREIGN KEY (`user`) REFERENCES `teacher` (`tno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher_pwd
-- ----------------------------
INSERT INTO `teacher_pwd` VALUES ('2102051', '2102051');
INSERT INTO `teacher_pwd` VALUES ('2102052', '2102052');
INSERT INTO `teacher_pwd` VALUES ('2102053', '2102053');
INSERT INTO `teacher_pwd` VALUES ('2102054', '2102054');
INSERT INTO `teacher_pwd` VALUES ('2102055', '2102055');
INSERT INTO `teacher_pwd` VALUES ('2102056', '2102056');
INSERT INTO `teacher_pwd` VALUES ('2102057', '2102057');
INSERT INTO `teacher_pwd` VALUES ('2102058', '2102058');
INSERT INTO `teacher_pwd` VALUES ('2102059', '2102059');
INSERT INTO `teacher_pwd` VALUES ('2102060', '2102060');
INSERT INTO `teacher_pwd` VALUES ('2210208', '2210208');
INSERT INTO `teacher_pwd` VALUES ('2210209', '2210209');
INSERT INTO `teacher_pwd` VALUES ('2210210', '2210210');

-- ----------------------------
-- View structure for course_student_view
-- ----------------------------
DROP VIEW IF EXISTS `course_student_view`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `course_student_view` AS select `c`.`cno` AS `cno`,`c`.`cname` AS `cname`,`s`.`sno` AS `sno`,`s`.`sname` AS `sname`,`sc`.`score` AS `score` from ((`course` `c` join `student_course` `sc` on((`c`.`cno` = `sc`.`tcid`))) join `student` `s` on((`sc`.`sno` = `s`.`sno`)));

-- ----------------------------
-- View structure for student_scores_view
-- ----------------------------
DROP VIEW IF EXISTS `student_scores_view`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `student_scores_view` AS select `s`.`sno` AS `sno`,`s`.`sname` AS `sname`,`sc`.`tcid` AS `tcid`,`sc`.`score` AS `score` from (`student` `s` join `student_course` `sc` on((`s`.`sno` = `sc`.`sno`)));

-- ----------------------------
-- Procedure structure for update_course_and_student_course
-- ----------------------------
DROP PROCEDURE IF EXISTS `update_course_and_student_course`;
delimiter ;;
CREATE PROCEDURE `update_course_and_student_course`(IN course_no CHAR(10),
    IN new_course_name CHAR(20))
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '存储过程执行失败';
    END;

    START TRANSACTION;

    -- 更新课程表中的课程名称
    UPDATE course
    SET cname = new_course_name
    WHERE cno = course_no;

    -- 更新学生课程表中的课程名称
    UPDATE student_course sc
    JOIN course c ON sc.tcid = c.cno
    SET sc.tcid = c.cno
    WHERE c.cno = course_no;

    COMMIT;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table student
-- ----------------------------
DROP TRIGGER IF EXISTS `check_sno_length`;
delimiter ;;
CREATE TRIGGER `check_sno_length` BEFORE INSERT ON `student` FOR EACH ROW BEGIN
    IF CHAR_LENGTH(NEW.sno) != 7 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '学号长度必须为7位';
    END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
