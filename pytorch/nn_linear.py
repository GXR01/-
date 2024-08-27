import torch
import torchvision
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("dataset",train=False,transform=torchvision.transforms.ToTensor())
dataloader = DataLoader(dataset,batch_size=64)

class MyNN():
    def __init__(self):
        super(MyNN,self).__init__()
        self.linear1 = Linear(199608,10)

mynn=MyNN()

for data in dataloader:
    imgs, targets = data
    output = torch.flatten(imgs)
    ouput=mynn(output)
