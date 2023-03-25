from flask import render_template
from app import app, db
from faker import Faker
from app.models.user_model import User

@app.route('/users')
def users():
    # users = User.query.all()
    fake = Faker()
    users = []
    for i in range(10):
        users.append({
            'name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number()
        })
    return render_template('user/index.html', users=users)
