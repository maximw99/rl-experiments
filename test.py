import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import random


print(torch.__version__)
print(torch.version.cuda)
x = torch.randn(1).cuda()
print(x)