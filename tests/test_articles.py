import requests


class TestArticles:

    def test_articles(self, config):
        url = config['localhost']['url'] + '/articles'
        response = requests.get(
            url=url
        )
        print(response.text)
        assert response.status_code == 200


# def test_hello_world():
#     response = requests.get(
#         'http://localhost:12345/hello_world'
#     )
#     assert response.status_code == 200
#     assert response.text == 'hello world.'
#
#
# def test_signup():
#     body = {
#         "login": "hello",
#         "password": "test"
#     }
#     response = requests.post(
#         'http://localhost:12345/auth/signup',
#         json=body
#
#     )
#     assert response.status_code == 200, response.text
#
#
# def test_login():
#     body = {
#         "login": "hello",
#         "password": "test"
#     }
#     response = requests.post(
#         'http://localhost:12345/auth/login',
#         json=body
#
#     )
#     assert response.status_code == 200, response.text
