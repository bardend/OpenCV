import requests

#def get_prediction(archivo, url = "http://0.0.0.0:5080/process-image/"):
def get_prediction(url = "http://0.0.0.0:50051/process-image/"):
#def get_prediction(url = "http://172.21.0.2:3080/process-image/"):
#def get_prediction(url = "http://172.0.0.0:80/process-image/"):
#def get_prediction( url = "http://0.0.0.0:5080/process-image/"): #????????????????IPv6???????????????????

  archivo = 'im3.jpg'

  payload = {'flag': 'false'}

#  files=[
#      ('file',('1eef6228-2ceb-4590-89bf-f1d6f4eba770', archivo,'application/octet-stream'))
#  ]

  files=[
    ('file',('1eef6228-2ceb-4590-89bf-f1d6f4eba770',open('./im3.jpg','rb'),'application/octet-stream'))
  ]

  headers = {}

  print(" send ")
  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  print(response)
  return response

get_prediction()

