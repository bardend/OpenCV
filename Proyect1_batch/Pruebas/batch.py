import multiprocessing
from multiprocessing import Queue
from cam_utils import WebcamVideoStream
import cv2
from queue import Empty
import datetime
from functions import *
from settings import * 
from test_multiple_inference import *
from time import perf_counter

import time



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

    while True:
        try:
            batch = output_q.get()  # Obtener un lote de fotogramas
        except Empty:
            print("Waiting to build the batch")
            continue
        
        path_images = []

        print("=================================================")
        for frame, num_frame in batch:

            cv2.imwrite(f'imagenes/image_{num_frame}.jpg', frame)  # Guarda cada frame en la carpeta 
            path_images.append(f'imagenes/image_{num_frame}.jpg')

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        s2_time = perf_counter()
        s_time = time.time()


        predict(path_images)

        f2_time = perf_counter()
        f_time = time.time()

        print("Time_predict :", f_time - s_time)
        print("Time2_predict : ", f2_time - s2_time)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # Esperar a que los procesos terminen
    reader_process.join()
    batcher_process.join()
    video_capture.stop()
    cv2.destroyAllWindows()
