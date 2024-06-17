import onnxruntime as ort
from config.Config import Config

class ManageModel:
    def __init__(self,config:Config) -> None:
        self.providers = ['CUDAExecutionProvider', 'CPUExecutionProvider'] if config.cuda else ['CPUExecutionProvider']
        self.session = ort.InferenceSession(config.weight_dir, providers=self.providers)
    