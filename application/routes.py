from application import app, db
from flask.templating import render_template
from application.models import Book, Review
from flask import redirect, url_for, request
from .models import Book, Review, BookForm, ReviewForm

#Home page url created for reroutes
@app.route('/', methods=['GET', 'POST'])
def home1():
    return render_template('homepage.html')


@app.route('/home', methods=['GET', 'POST'])
def homereroute():
    return render_template('homepage.html')

#All create routes with form validation
@app.route('/createbook', methods=['GET', 'POST'])
def createbook(): 
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data, genre=form.genre.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('createbook'))
    return render_template('createbook.html', form=form)

@app.route('/createreview', methods=['GET', 'POST'])
def createreview():
    form = ReviewForm()
    if form.validate_on_submit():
        new_review = Review(name=form.name.data, content=form.content.data, book_id=form.book_id.data)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('createreview'))
    else:
        return render_template('createreview.html', form=form)

#View and read routes
@app.route('/viewbook')
def viewbook():
    all_books = Book.query.all()
    return render_template('viewbook.html', all_books=all_books)

@app.route('/readreview')
def readreview():
    all_reviews = Review.query.all()
    return render_template('readreview.html', all_reviews=all_reviews)

#update routes
@app.route('/updatebook/<int:id>', methods = ['GET','POST'])
def updatebook(id):
    all_books = Book.query.all()
    form = BookForm()
    if request.method == 'POST':
        updatebook = Book.query.filter_by(id=id).first()
        if updatebook: 
            updatebook.title = request.form['title']
            updatebook.genre = request.form['genre']
            updatebook.author = request.form['author']
            db.session.commit()
            return render_template('viewbook.html', all_books=all_books)
        return f"book with id = {id} Does not exist"
    else:
        return render_template('updatebook.html', form=form, id=id)
           
@app.route('/updatereview/<int:id>',methods = ['GET','POST'])
def updatereview(id):
    form = ReviewForm()
    if request.method == 'POST':
        update_review = Review.query.filter_by(id=id).first()
        if update_review: 
            update_review.name = request.form['name']
            update_review.content = request.form['content']
            update_review.game_id = request.form['book_id']
            db.session.commit()
            return redirect(url_for('readreview'))
    else:
        return render_template('createreview.html', form=form, id=id)


#delete routes
@app.route('/deletebook/<int:id>', methods=['GET', 'POST'])
def deletebook(id):
    book = Book.query.filter_by(id=id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return render_template('viewbook.html', all_books=Book.query.all())
    return render_template ('viewbook.html', all_books=Book.query.all())
        
@app.route('/deletereview/<int:id>', methods=['GET', 'POST'])
def deletereview(id):
    review = Review.query.filter_by(id=id).first()
    if review:
        db.session.delete(review)
        db.session.commit()
        return redirect(url_for('readreview'))
    else:
        return render_template('readreview.html', id=id)
