# Contains business logic (validation, processing, rules)
# Does NOT know about HTTP — only works with Python data

from database.queries import (
    db_get_all
)

def service_get_all():
    return db_get_all()