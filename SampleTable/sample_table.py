from unicodedata import name
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class LogicalDevice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    location = db.Column(db.Integer, index=True)
    last_seen = db.Column(db.String(256))
    physical_device = db.Column(db.String(30))
    time_of_mapping = db.Column(db.String(120), index=True)

db.create_all()

@app.route('/')
def index():
    logicalDevices = LogicalDevice.query
    return render_template('sample_table.html', title='ITC303 Sample Table',logicalDevices=logicalDevices)

if __name__ == '__main__':
    app.run()

