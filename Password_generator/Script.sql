drop database if exists password_generator;
create database if not exists password_generator;
use password_generator;

create table Password_table (

	Password_id				int				not null auto_increment,
    Account_name			varchar(32)		not null,
    User_password 	        varchar(64)		not null,
    
    primary key(Password_id)
    );

use password_generator;
select * from Password_table;