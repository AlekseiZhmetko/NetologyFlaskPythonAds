import requests

# POST
response = requests.post('http://127.0.0.1:5000/ads', json=
{
    'title': 'car',
    'text': 'Best car ever',
    'user': 'Ivan'})
print(response.status_code)
print(response.text)

# GET
response = requests.get('http://127.0.0.1:5000/ads/7')

print(response.status_code)
print(response.text)

# DELETE
response = requests.delete('http://127.0.0.1:5000/ads/5')

print(response.status_code)
print(response.text)