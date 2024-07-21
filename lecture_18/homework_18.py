import requests

# Начальные данные
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

# Получение данных с API
response = requests.get(url, params=params)
data = response.json()

# Проверка, есть ли данные в ответе
if 'photos' in data:
    photos = data['photos']

    # Сохранение фото локально
    for i, photo in enumerate(photos):
        img_url = photo['img_src']
        img_data = requests.get(img_url).content

        # Определение имени файла
        file_name = f"mars_photo{i + 1}.jpg"

        # Запись фото в файл
        with open(file_name, 'wb') as file:
            file.write(img_data)

        print(f"Photo {file_name} is saved successfully.")
else:
    print("No photos found.")