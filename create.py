from time import sleep
from application import db

# db.drop_all()
db.create_all()

while tries > 0:
    try:        
        db.create_all()
        tries = 0
    except Exception as ex:
        tries-= 1
        sleep(5)