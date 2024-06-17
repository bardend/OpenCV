
from queue import Empty

def reader(output_q, video_capture):
    while True:
        frame, num_frame = video_capture.read()
        #print("reader num_frame :", num_frame)
        if num_frame % 20 == 0:
            output_q.put((frame, num_frame))

def batcher(input_q, output_q, batch_size):
    batch = []
    while True:
        try:
            frame, num_frame = input_q.get(block = False)
            batch.append((frame, num_frame))
            print("add_ frame :", num_frame//20)

        except Empty:
            #print("More fast processing read the images")
            continue

        if len(batch) == batch_size:
            output_q.put(batch)
            batch = []

