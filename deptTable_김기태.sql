drop table dept;

create table dept (
deptno number(3) constraint dept_dept_no_uq unique,
dname VARCHAR2(10),
loc VARCHAR2(20));
insert into dept values(10,'�ѹ���','����');
insert into dept values(20,'������','����');
insert into dept values(30,'�����','�λ�');
insert into dept values(40,'������','����');

select * from tab;