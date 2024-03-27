from django.test import TestCase, Client
from django.urls import reverse


class FindRouteViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_find_route_page(self):
        response = self.client.get(reverse('find_route'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'find_route.html')

    def test_find_route(self):
        response = self.client.post(
            reverse('find_route'),
            data={'startPoint': 'Москва', 'endPoint': 'Ахалцихе'},
        )


#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Расстояние:')
#         self.assertContains(response, 'Время в пути:')
