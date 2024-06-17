import os
import cv2

# Crear la carpeta "imagenes" si no existe
if not os.path.exists('imagenes'):
    os.makedirs('imagenes')

# Inicializar el objeto de captura de video desde la cámara (dispositivo 0)
video = cv2.VideoCapture(0)

# Inicializar contador de frames
frame_count = 0

# Inicializar contador de imágenes guardadas
saved_image_count = 0

# Lista para guardar los paths de las imágenes
path_images = []

# Número total de imágenes que se desean guardar
total_images = 100

# Número de imágenes a guardar por grupo (batch)
batch = 10

# Leer frames de la cámara
while True:
    # Leer un frame de la cámara
    ret, frame = video.read()
    
    # Verificar si se pudo leer el frame
    if not ret:
        break
    
    # Incrementar contador de frames
    frame_count += 1
    
    # Guardar el frame en la carpeta "imagenes" con nombre 'image_{frame_count}.jpg'
    cv2.imwrite(f'imagenes/image_{frame_count}.jpg', frame)  # Guarda cada frame en la carpeta "imagenes"
    
    # Incrementar contador de imágenes guardadas
    saved_image_count += 1
    
    # Guardar el path de la imagen en la lista
    path_images.append(f'imagenes/image_{frame_count}.jpg')
    
    # Verificar si se han guardado suficientes imágenes para formar un batch
    if len(path_images) == batch:
        # Mostrar las imágenes guardadas
        print("Imágenes guardadas:")
        for path in path_images:
            print(path)
        
        # Limpiar la lista para guardar los siguientes paths de las imágenes
        path_images = []
    
    # Salir del bucle si se han guardado todas las imágenes deseadas
    if saved_image_count >= total_images:
        break

# Liberar el objeto de captura y cerrar las ventanas
video.release()
cv2.destroyAllWindows()

