from application import app, db 
from flask import url_for
from flask_testing import TestCase
from application.models import Book, Review, BookForm, ReviewForm


#Testing if routes and response codes are correctly working and then follow on to testing on routes

class TestViewPages(TestApps):

    def test_home_page(self):
        response = self.client.get(url_for('home1'))
        self.assertEqual(response.status_code, 200)

    def test_home_page1(self):
        response = self.client.get(url_for('homereroute'))
        self.assertEqual(response.status_code, 200)

    def test_create_game(self):
        response = self.client.get(url_for('createbook'))
        self.assertEqual(response.status_code, 200)
      
    def test_update_game(self):
        response = self.client.get(url_for('updatebook', id=1))
        self.assertEqual(response.status_code, 200)

    def test_create_review(self):
        response = self.client.get(url_for('createreview', id=1))
        self.assertEqual(response.status_code, 200)
        
    def test_read_review(self):
        response = self.client.get(url_for('readreview', id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_review(self):
        response = self.client.get(url_for('updatebook', id=1))
        self.assertEqual(response.status_code, 200)


class TestApps(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///:test.db',DEBUG =True, WTF_CSRF_ENABLED =False)
        return app

    def setUp(self):
        db.create_all()
        testbook = Book(title='test_book', author='test_author', genre = 'test_genre')
        db.session.add(testbook)
        testreview = Review(name= "test_name", content= "test_content", book_id=1)
        db.session.add(testreview)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

#testing assert details into reading pages

class TestRead(TestApps):
    def test_viewbook(self):
        response = self.client.get(url_for('viewbook'))
        assert 'test_book'in response.data.decode()
        assert 'test_author'in response.data.decode()
        assert 'test_genre'in response.data.decode()


class TestReadReview(TestApps):
    def test_read_review(self):
        response = self.client.get(url_for('readreview'))
        assert 'test_name'in response.data.decode()
        assert 'test_content'in response.data.decode()
        assert '1'in response.data.decode()

#testing create functionality

class TestCreate(TestApps):
    def test_create_book(self):
        response = self.client.post(url_for('createbook'), data=dict(title="test_book", author="test_author", genre="test_genre"), follow_redirects=True)
        assert 'Please Enter Your Book Details'in response.data.decode()

#testing the update methids
class TestCreateReview(TestApps):
    def test_create_review(self):
        response = self.client.post(url_for('createreview'), data=dict(name="test_name", content="test_content", book_id=1), follow_redirects=True)
        assert 'Please Enter Your Review and BookID'in response.data.decode()


class TestUpdate(TestApps):
    def test_update_book(self):
        response = self.client.post(url_for('updatebook', id=1), data=dict(title="test_book", author="test_author", genre="test_genre"), follow_redirects=True)
        assert 'test_book'in response.data.decode()
        assert 'test_author'in response.data.decode()
        assert 'test_genre'in response.data.decode()


class TestUpdateReview(TestApps):
    def test_update_review(self):
        response = self.client.post(url_for('updatereview', id=1), data=dict(name="test_name", content="test_content", book_id=1), follow_redirects=True)
        assert 'test_name'in response.data.decode()
        assert 'test_content'in response.data.decode()
        assert '1'in response.data.decode()
