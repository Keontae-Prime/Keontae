CREATE TABLE SECTION
(
    deptCode char(6) NOT NULL,
    courseNum char(4) NOT NULL,
    semester char(8) NOT NULL,
    sectNum char(4) primary key NOT NULL,
    oer char(1) default 'N',
    instructorName char(30),
);

INSERT INTO SECTION(deptCode,courseNum,semester,sectNum)
VALUES(ENG,1000,SP2021,A1);
INSERT INTO SECTION(deptCode,courseNum,semester,sectNum)
VALUES(ENG,1000,SP2021,A2);
INSERT INTO SECTION(deptCode,courseNum,semester,sectNum)
VALUES(ENG,1000,SP2021,A3);

SELECT sectNum,deptCode,courseNum FROM SECTION 
WHERE semester='SP2021';