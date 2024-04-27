create database EntregaPyhton

use EntregaPyhton

create table usuarios(
idUsuario INT PRIMARY KEY IDENTITY(1,1),
nombreUsuario varchar(50),
contraseñaUsuario varchar(50)
)

insert into usuarios values ('admin','admin')

select * from usuarios 

delete from usuarios
