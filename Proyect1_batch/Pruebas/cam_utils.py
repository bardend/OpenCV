# From http://www.pyimagesearch.com/2015/12/21/increasing-webcam-fps-with-python-and-opencv/
import cv2
import datetime
from threading import Thread
from multiprocessing import Process, Queue
from queue import Empty

from pkg_resources import parse_version
OPCV3 = parse_version(cv2.__version__) >= parse_version('3')

def capPropId(prop):
  return getattr(cv2 if OPCV3 else cv2.cv,
    ("" if OPCV3 else "CV_") + "CAP_PROP_" + prop)

class WebcamVideoStream:
    def __init__(self, src, width, height):
        # Inicializar la transmisión de la cámara de video y leer el primer fotograma
        self.stream = cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        (self.grabbed, self.frame) = self.stream.read()

        # Inicializar la cola para comunicación entre procesos
        self.queue = Queue()
        self.num_frame = 0

    def start(self):
        # Iniciar el proceso para leer fotogramas de la transmisión de video
        Process(target=self.update, args=()).start()
        return self

    def update(self):
        # Mantenerse en un bucle infinito para leer continuamente fotogramas de la transmisión de video
        while True:
            # Leer el siguiente fotograma de la transmisión de video
            (grabbed, frame) = self.stream.read()

            if not grabbed:
                break

            # Poner el fotograma en la cola
            self.queue.put((frame, self.num_frame))

            self.num_frame += 1

            # Si no se pudo leer un fotograma, salir del bucle
    def read(self):
        # Devolver el fotograma más recientemente leído de la cola
        try:
            return self.queue.get()
        except Empty:
            print("Thread to read images so slow")


    def stop(self):
        # Detener la transmisión de video liberando los recursos
        self.stream.release()

