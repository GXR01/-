import torch
import torchvision.datasets
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset =torchvision.datasets.CIFAR10("../data",train=False,download=True,
                                      transform=torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset,batch_size=64)


class MyNN(nn.Module):
    def __init__(self):
        super(MyNN,self).__init__()
        self.maxpool = MaxPool2d(kernel_size=3,ceil_mode=True)
    def forward(self,input):
        output = self.maxpool(input)
        return output

mynn = MyNN()

writer = SummaryWriter("logs_maxpool")

step=0
for data in dataloader:
    imgs,targets = data
    writer.add_images("input",imgs,step)
    output = mynn(imgs)
    writer.add_images("output",output,step)
    step=step+1