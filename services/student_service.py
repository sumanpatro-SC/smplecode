# Contains business logic (validation, processing, rules)
# Does NOT know about HTTP — only works with Python data

from database.queries import (
    db_get_all
)

def service_get_one(student_id):
     return db_get_one(student_id)

def service_create(data):
     return db_create(data)
def service_get_all():
    return db_get_all()
