import numpy as np
import cv2 
import time

def letterbox(im, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleup=True, stride=32):
    shape = im.shape[:2]
    if isinstance(new_shape, int):
        new_shape = (new_shape, new_shape)

    r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
    if not scaleup:
        r = min(r, 1.0)

    new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
    dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]

    if auto: 
        dw, dh = np.mod(dw, stride), np.mod(dh, stride) 

    dw /= 2
    dh /= 2

    if shape[::-1] != new_unpad:  
        im = cv2.resize(im, new_unpad, interpolation=cv2.INTER_LINEAR)
    top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
    left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
    im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color) 
    return im, r, (dw, dh)


def transform_img(img, outputs, labels, dwdh, ratio, colors):
    ori_images = [img.copy()]
    for _, (batch_id,x0,y0,x1,y1,cls_id,score) in enumerate(outputs):
        image = ori_images[int(batch_id)]
        box = np.array([x0,y0,x1,y1])
        box -= np.array(dwdh*2)
        box /= ratio
        box = box.round().astype(np.int32).tolist()
        cls_id = int(cls_id)
        score = round(float(score),3)
        name = labels[cls_id]
        color = colors[name]
        name += ' '+str(score)
        cv2.rectangle(image,box[:2],box[2:],color,2)
        cv2.putText(image,name,(box[0], box[1] - 2),cv2.FONT_HERSHEY_SIMPLEX,0.75,[225, 255, 255],thickness=2)

        return ori_images[0]



def inference_multiple_img(session, images: list):
    processs_imgs = [preprocess_img(img) for img in images]
    
    images_batch = [pi[0] for pi in processs_imgs]
    #[print(img.shape) for img in images_batch]
    images_np = np.vstack(images_batch)
    images_np = np.ascontiguousarray(images_np)
    outname = [i.name for i in session.get_outputs()]
    outname

    inname = [i.name for i in session.get_inputs()]
    #print(inname,images_np.shape)
    inp = {inname[0]:images_np}
    outputs = session.run(outname, inp)
    
    return outputs

def preprocess_img(img):
    image = img.copy()
    image, ratio, dwdh = letterbox(np.array(image), auto=False)
    image = image.transpose((2, 0, 1))
    image = np.expand_dims(image, 0)
    #image = np.ascontiguousarray(image)

    im = image.astype(np.float32)
    im /= 255
    im.shape
    return im,ratio, dwdh

def inference(session, img):
    image = img.copy()
    image, ratio, dwdh = letterbox(image, auto=False)
    image = image.transpose((2, 0, 1))
    image = np.expand_dims(image, 0)
    image = np.ascontiguousarray(image)

    im = image.astype(np.float32)
    im /= 255
    im.shape

    outname = [i.name for i in session.get_outputs()]
    outname

    inname = [i.name for i in session.get_inputs()]
    inname
    print(inname,im.shape)
    inp = {inname[0]:im}
    inicio = time.time()
    outputs = session.run(outname, inp)[0]
    fin = time.time()
    print(fin-inicio)
    return outputs, ratio, dwdh
