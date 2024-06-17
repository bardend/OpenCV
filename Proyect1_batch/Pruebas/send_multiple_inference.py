import requests

# Define la URL del servidor FastAPI

#def predict(files,  url = 'http://localhost:8000/process-images/'):
def predict(url = 'http://192.168.37.105:5000/process-images/'):
    #url = 'http://localhost:8000/process-images/'
    # Crea una lista de archivos a enviar

    files = [
        ('images', ('imagen1.jpg', open('./imagenes/image_0.jpg', 'rb'), 'image/jpeg')),
        ('images', ('imagen2.jpg', open('./imagenes/image_1.jpg', 'rb'), 'image/jpg'))
    ]

    # Envía la solicitud POST con la lista de archivos
    response = requests.post(url, files=files)

    # Imprime la respuesta del servidor
    print(response.json())

predict()
