from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'


def create_db(db_path: str) -> None:
    """Crea la base de datos y la siguiente tabla:
    - tasks (id, name, done)
        └ id es la clave primaria identificador numérico
        └ name es el nombre/descripción de la tarea
        └ done indica si la tarea está hecha o no"""

    table_creation = """CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    name TEXT INTEGER,
    done TEXT
    )"""
    Task.cur.execute(table_creation)


class Task:
    """Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como "filas".
    - cur: para el cursor de manejo."""

    con = sqlite3.connect('todo.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    pass

    def __init__(self, name: str, done: bool = False, id: int = -1):
        self.name = name
        self.done = done
        self.id = id
        pass

    def save(self):
        info_insertion = 'INSERT INTO tasks VALUES(:name, :done)'
        Task.cur.execute(info_insertion, dict(name=self.name, done=self.done))
        Task.con.commit()
        pass

    def update(self):
        info_update = 'UPDATE tasks SET name=:name, done=:done'
        Task.cur.execute(info_update, dict(name=self.name, done=self.done))
        Task.con.commit()
        pass

    def check(self):
        """Marca la tarea como completada. Haz uso también de .update()"""
        check_task = 'UPDATE tasks SET done=:done'
        Task.cur.execute(check_task, dict(done=TASK_DONE_SYMBOL))
        Task.con.commit()
        pass

    def uncheck(self):
        """Marca la tarea como no completada. Haz uso también de .update()"""
        check_task = 'UPDATE tasks SET done=:done'
        Task.cur.execute(check_task, dict(done=TASK_PENDING_SYMBOL))
        Task.con.commit()
        pass

    def __repr__(self):
        """Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)"""
        info_query = 'SELECT done, name, id FROM tasks'
        Task.cur.execute(info_query)
        pass

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        """Construye una nueva tarea a partir de una fila de consulta devuelta por execute()"""
        name, done, id = row
        return Task(name, done, id)

    @classmethod
    def get(cls, task_id: int) -> Task:
        """Devuelve un objeto Task desde la consulta a la base de datos"""
        task_query_by_id = Task.cur.execute('SELECT * FROM tasks WHERE id={task_id}')
        name, done, id = task_query_by_id.fetchone()
        return Task(name, done, id)


class ToDo:
    """Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como "filas".
    - cur: para el cursor de manejo."""

    con = sqlite3.connect('todo.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    pass

    def get_tasks(self, *, done: int = -1):
        """Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora."""
        get_task = (
            ToDo.cur.execute('SELECT * tasks WHERE done={TASK_DONE_SYMBOL}')
            if done == 1
            else ToDo.cur.execute('SELECT * tasks WHERE done={TASK_PENDING_SYMBOL}')
        )
        pass

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        ToDo.cur.execute('INSERT INTO tasks(name) VALUES({self.name})')
        ToDo.con.commit()
        pass

    def complete_task(self, task_id: int):
        """Marca la tarea con identificador "task_id" como completada"""
        ToDo.cur.execute('INSERT INTO tasks(done) VALUES({TASK_DONE_SYMBOL}) where name={name.id}')
        ToDo.con.commit()
        pass

    def reopen_task(self, task_id: int):
        """Marca la tarea con identificador "task_id" como pendiente"""
        ToDo.cur.execute(
            'INSERT INTO tasks(done) VALUES({TASK_PENDING_SYMBOL}) where name={name.id}'
        )
        ToDo.con.commit()
        pass
