# Contains business logic (validation, processing, rules)
# Does NOT know about HTTP — only works with Python data

from database.queries import (
    db_get_all
    , db_get_one
    , db_create
    , db_update
    , db_delete
)

def service_get_all():
    return db_get_all()

def service_get_one(student_id):
    return db_get_one(student_id)

def service_create(data):
    return db_create(data)

def service_update(student_id, data):
    return db_update(student_id, data)

def service_delete(student_id):
<<<<<<< HEAD
    return db_delete(student_id)
=======
    return db_delete(student_id)
>>>>>>> 3a05da450b2fabcb3f28719b7afae6d772ac5c9d
