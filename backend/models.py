from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_security import UserMixin, RoleMixin,Security,SQLAlchemyUserDatastore
#from security import user_datastore, sec
from flask_security import hash_password

#create a Flask Instance
app=Flask(__name__)
CORS(app)

# Add Database
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'
app.config['SECRET_KEY'] = "thisissecret"
app.config['SECURITY_PASSWORD_SALT'] = 'salt'
app.config['WTF_CSRF_ENABLED'] = False
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = "Authentication-Token"
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'




#Initialize the database
db=SQLAlchemy()
db.init_app(app)



app.app_context().push()

#create Model

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('user.uid')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))


class cards(db.Model):
    cid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    obverse=db.Column(db.String(100), nullable=False)
    reverse=db.Column(db.String(100), nullable=False)
    score=db.Column(db.Integer,default=1)

class decks(db.Model):
	did=db.Column(db.Integer,primary_key=True,autoincrement=True)
	deck_name=db.Column(db.String(100), nullable=False, unique=True)
	cid=db.Column(db.String(100), nullable=True)
	deck_score=db.Column(db.Integer)
	deck_description=db.Column(db.String(100))
	last_reviewed=db.Column(db.String(10))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=False, nullable=False)
    name=db.Column(db.String(100))
    decks_owned=db.Column(db.Integer, db.ForeignKey('decks.did'),nullable=True)
    
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


# class users(db.Model):
#     uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
#     decks_owned=db.Column(db.Integer, db.ForeignKey('decks.did'),nullable=True)
#     username=db.Column(db.String(10),nullable=False)
#     name=db.Column(db.String(100))
    

#db.create_all()


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
sec = Security()
sec.init_app(app, user_datastore)

# db.create_all()

# if not user_datastore.find_user(email="user1@demo.com"):
#     user_datastore.create_user(
#         username="user1", email="user1@demo.com", password=hash_password("user1"))
#     db.session.commit()

# if not user_datastore.find_role('admin'):
#     user_datastore.create_role(
#         name='Admin', description='Admin Related Role')

#     db.session.commit()

# user_datastore.create_user(
#     username="user2", email="user2@demo.com", password=hash_password("user2"))
# db.session.commit()

# user_datastore.create_user(
#     username="user3", email="user3@demo.com", password=hash_password("user3"))
# db.session.commit()