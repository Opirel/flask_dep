import json
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# Set your configuration before initializing SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

# Initialize your database
with app.app_context():
    db.create_all()

ar = [{"name": "betty", "age": 20}, {"name": "alex", "age": 21}, {"name": "shadi", "age": 15}]

@app.route('/')
def hello():
    return json.dumps(ar)
 
if __name__ == '__main__':
    app.run(debug=True)
