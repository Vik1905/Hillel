import requests

# Завантаження зображення
url = 'http://127.0.0.1:8080/upload'
files = {'image': open('C:/Users/Viktor/Pictures/Ford_mustang.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())

# Отримання URL зображення
image_url = response.json().get('image_url')
filename = image_url.split('/')[-1]
get_url = f'http://127.0.0.1:8080/image/{filename}'
headers = {'Content-Type': 'text'}
response = requests.get(get_url, headers=headers)
print(response.json())

# Видалення зображення
delete_url = f'http://127.0.0.1:8080/delete/{filename}'
response = requests.delete(delete_url)
print(response.json())
