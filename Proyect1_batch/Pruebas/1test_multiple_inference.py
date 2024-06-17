from PIL import Image
from io import BytesIO
from utils import inference_multiple_img,inference
from config.Config import Config
from model import ManageModel
import numpy as np


def predict(path_images):
    #path_images = [
    #    "im1.jpg",
    #    "im2.jpg",
    #    "im3.jpg"
    #]
    path_yml = "weights/config.yaml"
    CFG = Config(path_yml)
    manage = ManageModel(CFG)
    images = []
    for path_image in path_images:
        with open(path_image,"rb") as file:
            images.append(file.read())

    images = [Image.open(BytesIO(content)) for content in images]


    out,ds,r = inference(manage.session,np.array(images[0]))
    #print(out,len(images))
    outputs = inference_multiple_img(manage.session,images)
    #print(outputs,len(outputs))
    num_perons = [0 for _ in range(len(images))]
    #print(outputs,len(outputs))
    for index,out in enumerate(outputs[0]):
    #    print(out,int(out[0]))
        index_person = int(out[0])
        num_perons[index_person]+=1
    response = {
        "response":[{"num_person": out} for out in num_perons]
    }
    print(response)
