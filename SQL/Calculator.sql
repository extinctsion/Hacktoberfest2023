-- main table for get every values 
create table calculator(
cid int identity(1,1),
val1 int,
val2 int,
sum1 int,
sub1 int,
multi1 int,
div1 decimal,
allSum decimal,
constraint pk_calculator primary key(cid))


-- trigger table 
create table calculatorLog(
logId int identity(1,1),
value1 int,
value2 int,
changed datetime,
operation varchar(20),
changedby SYSNAME
)

-- create trigger for insert

create trigger trd_calInsert
on calculator
FOR INSERT
as
begin
insert into calculatorLog (value1,value2,changed,operation,changedby)
select val1,val2,GETDATE(),'INSERTED',user from INSERTED
end

-- create trigger for update

create trigger trd_calUpdate
on calculator
AFTER UPDATE
as
begin
insert into calculatorLog (value1,value2,changed,operation,changedby)
select val1,val2,GETDATE(),'UPDATED',user from INSERTED
end

-- create trigger for Delete

create trigger trd_calDelete
on calculator
INSTEAD OF DELETE
as
begin
insert into calculatorLog (value1,value2,changed,operation,changedby)
select val1,val2,GETDATE(),'DELETED',user from DELETED
begin
print 'Values will not be deleted...!'
end
end

-- Create view for table 
create view view_calculatorLog
as 
select * from calculatorLog

-- create procedure for print all table
CREATE PROCEDURE view_table
AS
BEGIN
    PRINT 'Calculator Table';
    SELECT * FROM calculator;
    
    PRINT 'Log Table';
    SELECT * FROM calculatorLog;
END;

exec view_table

-- function for sum

create function sumValue(@a int, @b int)
returns int
as
begin
declare @c int = 0
set @c = @a + @b
return @c
end

-- function for sub

create function subValue(@a int, @b int)
returns int
as
begin
declare @c int = 0
set @c = @a - @b
return @c
end


-- function for multiplication

create function multiValue(@a int, @b int)
returns int
as
begin
declare @c int = 0
set @c = @a * @b
return @c
end


-- function for div

alter function divValue(@a int, @b int)
returns decimal
as
begin
declare @c decimal = 0
set @c = @a/@b
return @c
end

-- create procedure for sum of all function
create procedure pr_calc
(@val1 int,
@val2 int )
as 
begin
declare @a int=0,@b  int=0,@c int=0,@d int=0,@e int=0
set @a=dbo.sumValue(@val1,@val2)
set @b=dbo.subValue(@val1,@val2)
set @c=dbo.multiValue(@val1,@val2)
begin try
set @d=dbo.divValue(@val1,@val2)
end try
begin catch
print 'ALU error'
end catch
set @e=@a+@b+@c+@d
insert into calculator(
val1 ,
val2 ,
sum1 ,
sub1,
multi1 ,
div1 ,allsum)
 values(@val1,@val2,@a,@b,@c,@d,@e)
end

exec pr_calc @val1=23,@val2=4;

delete from calculator where cid = 1;
update calculator set div1 = 6;
exec view_table
