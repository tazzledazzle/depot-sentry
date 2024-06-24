from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

from backend.src.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/dbname'
db = SQLAlchemy(app)


class Repository(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Repository {self.name}>'


@app.route('/api/repos', methods=['POST'])
def add_repo():
    data = request.get_json()
    new_repo = Repository(name=data['name'], url=data['url'])
    db.session.add(new_repo)
    db.session.commit()
    return jsonify({"message": "Repository added"}), 201
