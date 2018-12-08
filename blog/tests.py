from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from .views import post_delete
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser

class PostTestCase(TestCase):
    
    def setUp(self):
    	me = User.objects.create(username='tester')
    	Post.objects.create(author=me, title="test", text="test")
    	Post.objects.create(author=me, title="test2", text="test2")

    def test_delete_post_count_itmes(self):
    	countBefore = Post.objects.all()
    	post = Post.objects.get(title="test")
    	user = AnonymousUser()
    	post_delete(user,post.pk)
    	countAfter = Post.objects.all()
    	self.assertNotEqual(countBefore,countAfter)

    def test_delete_exactly_item(self):
    	post = Post.objects.get(title="test2")
    	user = AnonymousUser()
    	post_delete(user,post.pk)
    	check_post = Post.objects.get(pk=post.pk)
    	self.assertNotEqual()