sqlite> create table Profesor (
   ...> ID_Profesor text primary key,
   ...> Nombre text
   ...> );


sqlite> create table Departamento (
   ...> ID_Departamento text,
   ...> Nombre text,
   ...> );

sqlite> create table Estudiante (
   ...> DNI text primary key,
   ...> Nombre text,
   ...> Apellido text,
   ...> Direccion_Postal text,
   ...> ID_Profesor text references Profesor (ID_Profesor)
   ...> );

sqlite> create table Programa (
   ...> ID_Programa text primary key,
   ...> Nombre text,
   ...> ID_Departamento text references Departamento(ID_Departamento)
   ...> );

sqlite> create table Curso (
   ...> ID_Curso text primary key,
   ...> Nombre text,
   ...> ID_Programa text references Programa(ID_Programa)
   ...> );

sqlite> create table Matricula (
   ...> ID_Matricula integer primary key,
   ...> DNI text references Estudiantes(DNI),
   ...> ID_Curso text references Curso(ID_Curso)
   ...> );
sqlite> create table Asignatura (
   ...> ID_Asignatura text primary key,
   ...> Nombre text
   ...> );
sqlite> create table Curso_Asignatura (
   ...> ID_Curso text references Curso(ID_Curso),
   ...> ID_Asignatura text references Asignatura(ID_Asignatura),
   ...> primary key(ID_Curso,ID_Asignatura)
   ...> );

sqlite> create table Asignatura_Prerequisito (
   ...> ID_Asignatura text references Asignatura(ID_Asignatura),
   ...> ID_Prerequisito text references Prerequisito(ID_Prerequisito),
   ...> primary key(ID_Asignatura,ID_Prerequisito)
   ...> );
sqlite> create table Aula (
   ...> ID_Aula text primary key,
   ...> Nombre integer
   ...> );

sqlite> create table Programa_Departamento (
   ...> ID_Programa text references Programa(ID_Programa),
   ...> ID_Departamento text references Departamento(ID_Departamento),
   ...> primary key (ID_Programa,ID_Departamento)
   ...> );

sqlite> create table Evento_Deportivo (
   ...> ID_Evento_Deportivo integer primary key,
   ...> ID_Evento text references Evento(ID_Evento),
   ...> ID_Instalacion text references Instalacion_Deportiva(ID_Instalacion)
   ...> );
sqlite> 

sqlite> create table Empleado_Administrativo (
   ...> ID_EmpleadoAd integer primary key,
   ...> DNI text,
   ...> Nombre text,
   ...> Apellido text,
   ...> ID_Departamento text references Departamento(ID_Departamento)
   ...> );
   sqlite> create table Empleado_Administrativo (
   ...> ID_EmpleadoAd integer primary key,
   ...> DNI text,
   ...> Nombre text,
   ...> Apellido text,
   ...> ID_Departamento text references Departamento(ID_Departamento)
   ...> );

   sqlite> create table Estudiante_Programa (
   ...> DNI_Estudiante text primary key,
   ...> ID_Programa text references Programa(ID_Programa)
   ...> );

   