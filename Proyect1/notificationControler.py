import requests
import base64

def sent_notification(bash_encode, y='localhost', x = 5000):

    url = f'http://{y}:{x}/api/v1/sendNotification'

    payload = {
        'data': {
            'recipients': [
                'a.printcat@gmail.com'
                # 'mikoiino0905@gmail.com'
            ],
            'subject': 'Reporte de ataque en peaje 2 (TESTEO-DOCKER-NO-REAL)',
            'body': 'La camara 8 detectó un intruso. \nProceder a atender la situación.\nImagen adjunta del intruso:',
            # Aquí debes colocar la imagen en base64
            'image': 'base64_encoded_image_here'
        }
    }

  #File "/home/bardend/Documents/Python/The_Boys/Proyect1/notificationControler.py", line 23, in sent_notification
  #  encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
#ValueError: read of closed file

    payload['data']['image'] = bash_encode

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Notificación enviada correctamente")
    else:
        print("Error al enviar la notificación:", response.text)
