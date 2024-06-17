from gameControler import GameControler
from notificationControler import *
from test_send import *
import time
import cv2
import logging
from time import perf_counter
from Pruebas import client

#with open("img2.jpg", "rb") as image_file:
#    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

class FrameProcessor:

    def __init__(self, video_path, stack_size=5):
        self.control = GameControler()
        self.cap = cv2.VideoCapture(video_path)

    def read_frame(self):
        while True:
            start_time = perf_counter()

            ret, frame = self.cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (640, 640))

            _, imagen_codificada = cv2.imencode('.jpg', frame)
            bytes_imagen = imagen_codificada.tobytes()
            s2_time = perf_counter()
            s_time = time.time()

            son = process_image(bytes_imagen, False)
            #son =  get_prediction(bytes_imagen)

            f2_time = perf_counter()
            f_time = time.time()

            print("Time_predict :", f_time - s_time)
            print("Time2_predict : ", f2_time - s2_time)

                        #logging.info("Time_predict : ", f_time - s_time)

            cv2.imshow("title", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


            #if flag:
            #    print("Send")
                #sent_notification(encoded_string, "172.21.0.2")

            end_time = perf_counter();
            print("Total time :", end_time - start_time)
            print("=======================================")

            fps = 1/30 - (end_time - start_time)
            time.sleep(max(0, fps))

if __name__ == "__main__":
    processor = FrameProcessor(0)
    processor.read_frame()

