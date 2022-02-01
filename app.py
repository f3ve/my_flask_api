import os
from flask import Flask
from flask_migrate import Migrate
from data.Models import db, UserModel

app = Flask(__name__)

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME')
db_server = 'localhost'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_server}:5432/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Index page'


@app.route('/hello')
def hello():
    return 'Hello, Word!'


@app.route('/users/<int:user_id>')
def get_user(user_id):
    return f'User: {user_id}'


if __name__ == '__main__':
    app.run(debug=True)

