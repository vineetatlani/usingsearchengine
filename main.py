from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import secrets
from algoliasearch.search_client import SearchClient
import json
import pandas as pd
import requests
data = pd.read_csv('/home/user/Downloads/Compressed/WinnersInterviewBlogPosts.csv')

client = SearchClient.create('FOL57BHXOW', '045e466101d4cf13e7ee4b16c889d2f6')
index = client.init_index('demo_myblog')

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(25)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __init__(self, id=None, title=None, content=None):
        self.id = id
        self.title = title
        self.content = content
    
    def to_dict(self):
        return {
            "objectID": self.id,
            "title": self.title,
            "content": self.content
        }
    
    def __str__(self):
        return str([self.title, self.content, self.id])

db.create_all()

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/show/<title>/")
def show(title):
    print(title)
    blog = Blog.query.filter_by(title=title).first()
    print(blog)
    if blog!= None:
        return "<h1>"+blog.title+"</h1>"+"<p>"+blog.content+"</p>"
    return title

@app.route("/add/", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        blog = Blog(title=request.form['title'], content=request.form['content'])
        result = db.session.add(blog)
        db.session.commit()
        response = requests.post("http://0.0.0.0:5000/add/ZTEsBf6qf7Ekog/myblog", json=blog.to_dict())
        print(response.json)
        index.save_object(blog.to_dict())
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
