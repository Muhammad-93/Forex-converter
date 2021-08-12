from app import app
from flask import session
from unittest import TestCase


app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class ColorViewsTestCase(TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print("INSIDE SET UP CLASS")

    # @classmethod
    # def tearDownClass(cls):
    #     print("INSIDE TEAR DOWN CLASS")

    # def setUp(self):
    #     print("INSIDE SET UP")

    # def tearDown(self):
    #     print("INSIDE TEAR DOWN")

    def test_currency_form(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Currency Coverter</h1>', html)

    def test_currency_conversion(self):
        with app.test_client() as client:
            res = client.post('/result', data={'Currency': 'USD', 'Currency2': 'USD', 'Amount': 1})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>The result is US$ 1.0</h1>',  html)

    def test_first_currency_code_check(self):
        with app.test_client() as client:
            res = client.post('/result', data={'Currency': 'AAA', 'Currency2': 'USD', 'Amount': 1})
            html = res.get_data(as_text=True)

            self.assertIn('<p>Invalid currency code: AAA</p>',  html)
    
    def test_second_currency_code_check(self):
        with app.test_client() as client:
            res = client.post('/result', data={'Currency': 'USD', 'Currency2': 'BBB', 'Amount': 1})
            html = res.get_data(as_text=True)

            self.assertIn('<p>Invalid currency code: BBB</p>',  html)

    def test_amount(self):
        with app.test_client() as client:
            res = client.post('/result', data={'Currency': 'IND', 'Currency2': 'USD', 'Amount': 'abc'})
            html = res.get_data(as_text=True)

            self.assertIn('<p>Please enter a valid amount!</p>',  html)