from os import listdir
import random

import torch
from torch.nn.functional import log_softmax
import torch.optim as optim
import torchvision
from PIL import Image
from torch import tensor
from torch.tensor import Tensor
from torchvision import transforms
import torch.nn.functional as F
import torch.nn as nn
from torch.autograd import Variable

normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

transform = transforms.Compose([
	transforms.Resize(256),
	transforms.CenterCrop(256),
	transforms.ToTensor(),
	normalize])

trainDataList = []
targetList = []
trainData = []
files = listdir('catDog/train/')
for f in range(len(listdir('catDog/train/'))):
	f = random.choice(files)
	files.remove(f)
	img = Image.open("catDog/train/" + f)
	img_tensor = transform(img)
	trainDataList.append(img_tensor)
	isCat = 1 if 'cat'in f else 0
	isDog = 1 if 'dog'in f else 0
	target = [isCat, isDog]
	targetList.append(target)
	if len(trainDataList) >= 64:
		trainData.append((torch.stack(trainDataList), targetList))
		trainDataList = []
	break

class Netz(nn.Module):
	def __init__(self):
		super(Netz, self).__init__()
		self.conf1 = nn.Conv2d(3, 6, kernel_size=5)
		self.conf2 = nn.Conv2d(6, 12, kernel_size=5)
		self.conf3 = nn.Conv2d(12, 18, kernel_size=5)
		self.fc1 = nn.Linear(14112, 1000)
		self.fc2 = nn.Linear(1000, 2)

	def forward(self, x):
		x = self.conf1(x)
		x = F.max_pool2d(x, 2)
		x = F.relu(x)
		x = self.conf2(x)
		x = F.max_pool2d(x, 2)
		x = F.relu(x)
		x = F.max_pool2d(x, 2)
		x = F.relu(x)
		x = x.view(-1,14112)
		x = F.relu(self.fc1(x))
		x = self.fc2(x)
		return log_softmax(x)

model = Netz()


optimizer = optim.Adam(model.parameters(), lr=0.01)
def train(epoch):
	model.train()
	batch_id= 0
	for data, target in trainData:
		target = torch.LongTensor(target)
		data = Variable(data)
		target = Variable(target)
		optimizer.zero_grad()
		out = model(data)
		criterion = F.nll_loss
		loss = criterion(out, target)
		loss.backward()
		optimizer.step()
		print('epoche: ', epoch,f' [{batch_id * len(data)}/{len(trainData)}] ({100. * batch_id / len(trainData):.0f}%)',  f' \tLoss: {loss.data}')
		batch_id = batch_id + 1

for epoch in range(1,30):
	train(epoch)