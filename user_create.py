"""Create a new admin user able to view the /reports endpoint."""
from sqlalchemy import create_engine
import sys
from flask.ext.bcrypt import Bcrypt
from application import *
from application.models import AdminUser

bcrypt = Bcrypt(app)

#admin
password = 'j1f@WskjeU6)(wij'
hashed = bcrypt.generate_password_hash(password)
ins = AdminUser(username='admin', email='lavin@pitt.edu', password=hashed)

try:
    db.session.add(ins)
    db.session.commit()

except:
    db.session.rollback()
