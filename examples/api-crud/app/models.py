from app import app,db
from sqlalchemy.exc import IntegrityError

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


def insert_data():
    users = [
        {'email': 'user1@example.com', 'username': 'user1', 'password': 'user1'},
        {'email': 'user2@example.com', 'username': 'user2', 'password': 'user2'}
    ]

    for i in range(len(users)):
        db.session.add(Users(email=users[i]['email'], username=users[i]['username'], password=users[i]['password']))

    db.session.commit()


with app.app_context():
    db.create_all()
    try:
        insert_data()
    except IntegrityError:
        pass
