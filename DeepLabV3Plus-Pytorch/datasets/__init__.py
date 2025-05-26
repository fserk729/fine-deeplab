from .voc import VOCSegmentation
from .cityscapes import Cityscapes
from .my_FINE_dataset import MyDataset

def get_dataset(name):
    if name == 'voc':
        return VOCSegmentation
    elif name == 'cityscapes':
        return Cityscapes
    elif name == 'mydataset':  # Replace with the CLI name you want
        return MyDataset
    else:
        raise ValueError(f"Dataset {name} not supported")
