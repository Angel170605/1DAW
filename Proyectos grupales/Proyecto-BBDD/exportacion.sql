PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE Profesor (
ID_Profesor text primary key,
Nombre text
);
CREATE TABLE Departamento (
ID_Departamento text primary key,
Nombre text
);
CREATE TABLE Estudiante (
DNI text primary key,
Nombre text,
Apellido text,
Direccion_Postal text,
ID_Profesor text references Profesor (ID_Profesor)
);
CREATE TABLE Programa (
ID_Programa text primary key,
Nombre text,
ID_Departamento text references Departamento(ID_Departamento)
);
CREATE TABLE Curso (
ID_Curso text primary key,
Nombre text,
ID_Programa text references Programa(ID_Programa)
);
CREATE TABLE Matricula (
ID_Matricula integer primary key,
DNI text references Estudiantes(DNI),
ID_Curso text references Curso(ID_Curso)
);
CREATE TABLE Curso_Profesor (
ID_Curso text references Curso(ID_Curso),
ID_Profesor text references Profesor(ID_Profesor),
primary key(ID_Curso,ID_Profesor)
);
CREATE TABLE Asignatura (
ID_Asignatura text primary key,
Nombre text
);
CREATE TABLE Curso_Asignatura (
ID_Curso text references Curso(ID_Curso),
ID_Asignatura text references Asignatura(ID_Asignatura),
primary key(ID_Curso,ID_Asignatura)
);
CREATE TABLE Prerequisito (
ID_Prerequisito text primary key,
Nombre text
);
CREATE TABLE Asignatura_Prerequisito (
ID_Asignatura text references Asignatura(ID_Asignatura),
ID_Prerequisito text references Prerequisito(ID_Prerequisito),
primary key(ID_Asignatura,ID_Prerequisito)
);
CREATE TABLE Aula (
ID_Aula text primary key,
Nombre integer
);
CREATE TABLE Curso_Aula (
ID_Curso text references Curso(ID_Curso),
ID_Aula text references Aula(ID_Curso),
primary key(ID_Curso,ID_Aula)
);
CREATE TABLE Programa_Departamento (
ID_Programa text references Programa(ID_Programa),
ID_Departamento text references Departamento(ID_Departamento),
primary key (ID_Programa,ID_Departamento)
);
CREATE TABLE Instalacion (
ID_Instalacion text primary key,
Nombre text
);
CREATE TABLE Evento (
ID_Evento text primary key,
Nombre text
);
CREATE TABLE Instalacion_Deportiva (
ID_Instalacion text primary key,
Nombre text
);
CREATE TABLE Evento_Deportivo (
ID_Evento_Deportivo integer primary key,
ID_Evento text references Evento(ID_Evento),
ID_Instalacion text references Instalacion_Deportiva(ID_Instalacion)
);
CREATE TABLE Empleado_Administrativo (
ID_EmpleadoAd integer primary key,
DNI text,
Nombre text,
Apellido text,
ID_Departamento text references Departamento(ID_Departamento)
);
COMMIT;
