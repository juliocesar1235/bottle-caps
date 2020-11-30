import json
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate
from ..models import User, Category, Title, Review

class UserTests(APITestCase):
    
    def test_create_user(self):
        url = reverse('sign_up')
        data = {'username': 'bottlecapper','email': 'capper@bottlecaps.com','password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'bottlecapper')

class CategoryTests(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='bottlecapper',email='capper@bottlecaps.com', password='12345')
        cls.category1 = Category.objects.create(name='Platformer')
        cls.category2 = Category.objects.create(name='Survival horror')
        cls.category3 = Category.objects.create(name='Sports')
    
    def test_get_all_categories(self):
        url = reverse('categories')
        token = Token.objects.get(user__username='bottlecapper')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(url,format='json')
        self.assertEqual(len(response.data), 3)

class TitleTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='rigo',email='rigo@bottlecaps.com', password='12345')
        cls.token = Token.objects.get(user__username='rigo')
        cls.category1 = Category.objects.create(name='FPS')
        cls.category2 = Category.objects.create(name='Adventure')
        cls.title1 = Title.objects.create(
            name='Call of duty black ops 2',
            synopsis='Action first person shooter',
            cover_image_path='https://images-na.ssl-images-amazon.com/images/I/81GN6gepa5L._AC_UL600_SR489,600_.jpg',
            featured=True,
            user_score=4.7,
            user_review_count=167,
        )
        cls.title2 = Title.objects.create(
            name='GTA 5',
            synopsis='Action-adventure open world sandbox',
            cover_image_path='https://cdn.cdkeys.com/500x706/media/catalog/product/g/r/grand_theft_auto_v_5_gta_5_pc_3.jpg',
            featured=True,
            user_score=4.5,
            user_review_count=289,
        )
        cls.title1.category.add(cls.category1)
        cls.title2.category.add(cls.category2)
    
    def test_get_title(self):
        url = f'/title/{self.title2.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['name'], 'GTA 5')

    
    def test_get_all_titles(self):
        url = reverse('titles')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 2)
    
    def test_get_filtered_titles(self):
        url = reverse('titles_filter')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {'categories': [str(self.category1.id)]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(len(response.data), 1)

    
    def test_create_new_title(self):
        url = reverse('titles')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            'name': 'The last of us part 2',
            'synopsis': 'Action-adventure survival horror game',
            'cover_image_path': 'https://cdn.cdkeys.com/500x706/media/catalog/product/g/r/grand_theft_auto_v_5_gta_5_pc_3.jpg',
            'featured':'True',
            'user_score': '3.8',
            'category': 'Adventure',
            'user_review_count': '183',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Title.objects.count(), 3)
    
    def test_delete_title(self):
        url = f'/title/{self.title1.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Title.objects.count(), 1)

class ReviewTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='sergio',email='s@bottlecaps.com',password='12345')
        cls.user2 = User.objects.create_user(username='julio',email='j@bottlecaps.com',password='12344')
        cls.token = Token.objects.get(user__username='sergio')
        cls.title1 = Title.objects.create(
            name='Cyberpunk 2077',
            synopsis='First person open world sandbox set in the year 2077',
            cover_image_path='https://i.redd.it/9e0miqiv9f331.jpg',
            featured=True,
            user_score=4.5,
            user_review_count=129,
        )
        cls.title2 = Title.objects.create(
            name='Zelda breath of the wild',
            synopsis='Adventure open world fantasy videogame',
            cover_image_path='https://i.redd.it/9e0miqiv9f3131.jpg',
            featured=False,
            user_score=4.9,
            user_review_count=84,
        )
        cls.review1 = Review.objects.create(
            heading='The best game ever',
            comment='This is the best game ive ever played in while',
            rating=5,
            user=cls.user,
            title=cls.title1
        )
        cls.review2 = Review.objects.create(
            heading='Average game',
            comment='The combat is kind of stiff it needs some work',
            rating=3.2,
            user=cls.user2,
            title=cls.title2
        )
    
    def test_get_review(self):
        url = f'/review/{self.review2.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['heading'], 'Average game')

    def test_get_all_reviews(self):
        url = reverse('reviews')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url, format='json')
        self.assertEqual(len(response.data), 2)
    
    def test_create_new_review(self):
        url = reverse('reviews')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            'heading': 'GOTY for my',
            'comment': 'This game is the absolute best ive played in ages',
            'rating': '5',
            'user': f'{self.user.id}',
            'title': f'{self.title2.id}',
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 3)

    def test_delete_review(self):
        url = f'/review/{self.review1.id}/'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Review.objects.count(), 1)
