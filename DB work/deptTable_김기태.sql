drop table dept;

create table dept (
deptno number(3) constraint dept_dept_no_uq unique,
dname VARCHAR2(10),
loc VARCHAR2(20));
insert into dept values(10,'총무부','서울');
insert into dept values(20,'영업부','대전');
insert into dept values(30,'전산부','부산');
insert into dept values(40,'관리부','광주');

select * from tab;
