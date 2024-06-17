import multiprocessing
from multiprocessing import Queue
from cam_utils import WebcamVideoStream
import cv2
from queue import Empty
import datetime
from functions import *
from settings import * 


if __name__ == '__main__':
    # Definir colas para la comunicación entre procesos
    input_q = Queue()
    output_q = Queue()

    # Definir el tamaño del lote

    video_capture =  WebcamVideoStream(0,640,640).start()

    # Crear procesos
    #reader_process = multiprocessing.Process(target=reader, args=(input_q, intermediate_q))
    reader_process = multiprocessing.Process(target=reader, args= (input_q, video_capture))
    batcher_process = multiprocessing.Process(target=batcher, args=(input_q, output_q, batch_size))

    # Iniciar procesos
    reader_process.start()
    batcher_process.start()

    # Mostrar los fotogramas en tiempo real
    while True:
        try:
            batch = output_q.get()  # Obtener un lote de fotogramas
        except Empty:
            print("Waiting to build the batch")
            continue
        
        #_, imagen_codificada = cv2.imencode('.jpg', frame)
        #bytes_imagen = imagen_codificada.tobytes()

        #bytes_batch = b''.join([cv2.imencode('.jpg', frame)[1].tobytes() for frame in batch])
        #print(bytes_batch)

        #result = 

        for frame in batch:

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Esperar a que los procesos terminen
    reader_process.join()
    batcher_process.join()
    video_capture.stop()
    cv2.destroyAllWindows()
