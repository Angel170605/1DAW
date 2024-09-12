sqlite> insert into Profesor (ID_Profesor,Nombre) values ('ID_Profesor1','Johatam');
sqlite> insert into Profesor (ID_Profesor,Nombre) values ('ID_Profesor2','Sergio');


sqlite> insert into Departamento (ID_Departamento,Nombre) values ('ID_Departamento','
BAE');
sqlite> insert into Departamento (ID_Departamento,Nombre) values ('ID_Departamento2',
'PRO');

sqlite> insert into Estudiante (DNI,Nombre,Apellido,Direccion_Postal,ID_Profesor) values ('1111D','Ricardo','Zamora','Avenida La Gallega 3','ID_Profesor1');
sqlite> insert into Estudiante (DNI,Nombre,Apellido,Direccion_Postal,ID_Profesor) values ('2222D','Omar','Perez','Calle San Agustin 30','ID_Profesor2');
sqlite> insert into Estudiante (DNI,Nombre,Apellido,Direccion_Postal,ID_Profesor) values ('3333H','Laura','Rodriguez','Paseo Fermin Rodriguez 2A','ID_Profesor2');

sqlite> insert into Programa (ID_Programa,Nombre,ID_Departamento) values ('ID_Programa1','Programa1','ID_Departamento1');
sqlite> insert into Programa (ID_Programa,Nombre,ID_Departamento) values ('ID_Programa2','Pro
grama2','ID_Departamento2');

sqlite> insert into Curso (ID_Curso,Nombre,ID_Programa) values ('ID_Curso1','1 Bach','ID_Programa1');
sqlite> insert into Curso (ID_Curso,Nombre,ID_Programa) values ('ID_Curso2','2 Bach','ID_Prog
rama2');

sqlite> insert into Matricula (ID_Matricula,DNI,ID_Curso) values (1,'1111D','ID_Curso1');
sqlite> insert into Matricula (ID_Matricula,DNI,ID_Curso) values (2,'2222D','ID_Curso2');
sqlite> insert into Matricula (ID_Matricula,DNI,ID_Curso) values (3,'3333H','ID_Curso2');

sqlite> insert into Asignatura (ID_Asignatura, Nombre) values ('ID_Asignatura1','BAE');
sqlite> insert into Asignatura (ID_Asignatura, Nombre) values ('ID_Asignatura2','PRO');

sqlite> insert into Curso_Asignatura (ID_Curso,ID_Asignatura) values ('ID_Curso1','ID_Asignat
ura1');
sqlite> insert into Curso_Asignatura (ID_Curso,ID_Asignatura) values ('ID_Curso2','ID_Asignat
ura2');

sqlite> insert into Asignatura_Prerequisito (ID_Asignatura,ID_Prerequisito) values ('ID_Asign
atura1','ID_Prerequisito1');
sqlite> insert into Asignatura_Prerequisito (ID_Asignatura,ID_Prerequisito) values ('ID_Asign
atura2','ID_Prerequisito2');

sqlite> insert into Aula (ID_Aula,Nombre) values ('ID_Aula1',102);
sqlite> insert into Aula (ID_Aula,Nombre) values ('ID_Aula2',103);

sqlite> insert into Estudiante_Programa (DNI_Estudiante,ID_Programa) values ('1111D','ID_Prog
rama1');
sqlite> insert into Estudiante_Programa (DNI_Estudiante,ID_Programa) values ('2222D','ID_Prog
rama2');

sqlite> insert into Empleado_Administrativo (ID_EmpleadoAd,DNI,Nombre,Apellido,ID_Departament
o) values (1,'DNI1','Daniel','Zamora','ID_Departamento1');
sqlite> insert into Empleado_Administrativo (ID_EmpleadoAd,DNI,Nombre,Apellido,ID_Departamento) values (2,'DNI2','Adrian','Zapata','ID_Departamento2');

sqlite> insert into Instalacion_Deportiva (ID_Instalacion,Nombre) values ('ID_Instacion1','Cancha1');
sqlite> insert into Instalacion_Deportiva (ID_Instalacion,Nombre) values ('ID_Instacion2','Ca
ncha2');






