from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from sqlalchemy import Integer

#Classes related to Review
#ForgeinKey used
#import and install flask forms to use forms 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    reviews = db.relationship('Review', backref='book')

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

class BookForm(FlaskForm):
    title = StringField('Enter the book title')
    genre = StringField('Enter the book genre')
    author = StringField('Enter the book author')
    submit = SubmitField('submit')

class ReviewForm(FlaskForm):
    name = StringField('Please enter your full name')
    content = StringField('Please enter your review')
    book_id = IntegerField('Please enter the book id')
    submit = SubmitField('submit')