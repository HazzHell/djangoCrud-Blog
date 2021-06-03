from django.test import TestCase
from .models import Post

#permet de vérifier si ecriture et lecture fonctionne
#au niveau du modele
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='juste un test')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        ce_quon_attend = 'juste un test'
        contenu_post =str(post.text)
        self.assertEqual(ce_quon_attend, contenu_post)

#Verifier si l'affichage templates+modele fonctionne 
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='cest un post num 1')
        Post.objects.create(text='cest un post num 2')

    def test_status_ok(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    #affiche t on au moins un post
    def test_lire_un_post(self):
        resp =self.client.get('/')
        self.assertContains(resp, text='cest un post num')

    #affiche t on plusieurs posts (list)
    def test_affiche_list_post(self):
        resp = self.client.get('/')
        self.assertContains(resp, text='cest un post num', count=2)

# Create your tests here.
