create database EntregaPyhton

use EntregaPyhton

create table usuarios(
idUsuario INT PRIMARY KEY IDENTITY(1,1),
nombreUsuario varchar(50),
contraseñaUsuario varchar(50)
)

create table moto(
idMoto int primary key identity(1,1),
placa varchar(50),
nombre varchar(50))

create table carro(
idCarro int primary key identity(1,1),
placa varchar(50),
nombre varchar(50))

create table placasVetadas(
idVetada int primary key identity(1,1),
placa varchar(50))

insert into usuarios values ('admin','admin')

update usuarios set contraseñaUsuario = 'hola' where nombreUsuario = 'juancho'

delete from moto where placa = 'hhh-333'

select * from usuarios 
select * from moto
select * from carro
select placa from placasVetadas 

delete from usuarios
delete from moto
delete from carro
