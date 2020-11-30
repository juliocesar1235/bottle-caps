from django.test import TestCase
from datetime import datetime
from ..models import User, Category, Title, Review
from django.db.utils import IntegrityError

class CategoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='FPS')
        cls.title1 = Title.objects.create(
            name='Cyberpunk 2077',
            synopsis='First person open world sandbox set in the year 2077',
            cover_image_path='https://i.redd.it/9e0miqiv9f331.jpg',
            featured=True,
            user_score=4.5,
            user_review_count=129,
        )
        cls.title2 = Title.objects.create(
            name='Dark souls 3',
            synopsis='Self explanatory, souls like game',
            cover_image_path='https://cdn-prod.scalefast.com/public/assets/user/122595/image/5243deb55a7ee9587ad2db9298e96ca5.jpg',
            featured=False,
            user_score=4,
            user_review_count=367,
        )        

    def test_if_category_has_info_fields(self):
        self.assertIsInstance(self.category.name, str)
        self.assertIsInstance(self.category.created_at, datetime)

    def test_it_can_have_multiple_titles(self):
        self.title1.category.add(self.category)
        self.title2.category.add(self.category)

        self.assertEquals(len(self.category.titles.all()), 2)
    
    def test_its_string_representation(self):
        catStr = f'<Category "{self.category.name}">'
        self.assertEquals(str(self.category), catStr)

class TitleTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.title = Title.objects.create(
            name='BO3',
            synopsis='Action first person shooter',
            cover_image_path='https://images-na.ssl-images-amazon.com/images/I/81GN6gepa5L._AC_UL600_SR489,600_.jpg',
            featured=True,
            user_score=3.2,
            user_review_count=35,
        )     

    def test_if_title_has_info_fields(self):
        self.assertIsInstance(self.title.name, str)
        self.assertIsInstance(self.title.synopsis, str)
        self.assertIsInstance(self.title.cover_image_path, str)
        self.assertIsInstance(self.title.user_score, float)
        self.assertIsInstance(self.title.featured, bool)
        self.assertIsInstance(self.title.user_review_count, int)
        self.assertIsInstance(self.title.created_at, datetime)
    
    def test_it_can_have_multiple_categories(self):
        categories = [Category.objects.create() for _ in range(3)]
        for category in categories:
            self.title.category.add(category)
        
        self.assertEquals(len(categories), self.title.category.count())
        for category in categories:
            self.assertIn(category, self.title.category.all())
        
    def test_its_string_representation(self):
        titleStr = f'<Title "{self.title.name}">'
        self.assertEquals(str(self.title), titleStr)

class ReviewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='capper', password='12345')
        cls.title = Title.objects.create(
            name='Cyberpunk 2077',
            synopsis='First person open world sandbox set in the year 2077',
            cover_image_path='https://i.redd.it/9e0miqiv9f331.jpg',
            featured=True,
            user_score=4.5,
            user_review_count=129,
        )
        cls.review = Review.objects.create(
            heading='The best game ever',
            comment='This is the best game ive ever played in while',
            rating=5,
            user=cls.user,
            title=cls.title
        )

    def test_if_review_has_info_fields(self):
        self.assertIsInstance(self.review.heading, str)
        self.assertIsInstance(self.review.comment, str)
        self.assertIsInstance(self.review.rating, int)
        self.assertIsInstance(self.review.user, User)
        self.assertIsInstance(self.review.title, Title)
        self.assertIsInstance(self.review.created_at, datetime)

    def test_its_string_representation(self):
        reviewStr = f'<Review {self.review.id}>'
        self.assertEquals(str(self.review), reviewStr)

    def test_when_user_is_not_unique(self):
        with self.assertRaises(IntegrityError):
            Review.objects.create(
                heading='This game is trash',
                comment='The worst game ive played in a while, buggy as fallout 76',
                rating=1,
                user=self.user,
                title=self.title
            )
            