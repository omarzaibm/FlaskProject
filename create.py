from application import db
from application.models import Book, Review
from os import getenv
from datetime import datetime

db.drop_all()
db.create_all()

#new_book = Book(title="QA")
#db.session.add(new_book)
#db.session.commit()

#new_book = Book(title="Harry Potter: Philosphers Stone")
#db.session.add(new_book)
#db.session.commit()

#new_book = Book(title=" Art of War")
#db.session.add(new_book)
#db.session.commit()

#list_of_books = Book.query.all()
#print(Book.query.order_by(book.id))
