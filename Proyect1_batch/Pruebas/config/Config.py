import yaml
import random
class Config():
    def __init__(self,path_yaml) -> None:
        with open(path_yaml, 'r') as f:
            data = yaml.safe_load(f)
        self.labels = data["labels"]
        self.cuda = data["cuda"]
        self.weight_dir = data["weight_dir"]
        self.colors = {name:[random.randint(0, 255) for _ in range(3)] for i,name in enumerate(self.labels)}
