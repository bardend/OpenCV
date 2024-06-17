import cv2
import json
import numpy as np
import requests

# URL del servidor HTTP al que enviarás el JSON
server_url = "http://localhost:5000/update_frame"

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

id_camera = 1

while True:
    # Capturar un fotograma
    ret, frame = cap.read()

    # Aquí puedes realizar el procesamiento de imagen que necesites en el fotograma
    # Por ejemplo, podrías convertir la imagen a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray_frame = cv2.resize(gray_frame, (10, 10))

    # Convertir el fotograma procesado a una lista de Python
    frame_list = gray_frame.tolist()

    # Crear un diccionario para almacenar los datos del fotograma
    frame_data = {
        "width": gray_frame.shape[1],
        "height": gray_frame.shape[0],
        "data": frame_list
    }

    # Serializar el diccionario en formato JSON
    frame_json = json.dumps(frame_data)

    # Enviar el diccionario directamente sin convertirlo en una cadena JSON
    try:
        response = requests.post(server_url, json=frame_data)
        print("JSON enviado correctamente.")

        # Manejar la respuesta del servidor
        if response.status_code == 200:
            numero_recibido = response.json().get("numero", None)
            if numero_recibido is not None:
                print(f"Número recibido del servidor: {numero_recibido}")
            else:
                print("El servidor no devolvió ningún número.")
        else:
            print(f"Error al recibir respuesta del servidor: {response.text}")

    except Exception as e:
        print(f"Error al enviar JSON: {e}")

    # Mostrar el fotograma original
    cv2.imshow('Frame', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar la ventana
cap.release()
cv2.destroyAllWindows()

