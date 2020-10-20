import os

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

kwargs = {}
trainData = torch.utils.data.DataLoader(datasets.MNIST('data',train=True, download=True, transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307,),(0.3081,))])), batch_size=64, shuffle=True, **kwargs)

testData = torch.utils.data.DataLoader(datasets.MNIST('data',train=False, transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.1307,),(0.3081,))])), batch_size=64, shuffle=True, **kwargs)



class Netz (nn.Module):
	def __init__(self):
		super(Netz, self).__init__()
		self.conf1 = nn.Conv2d(1, 10, kernel_size=5)
		self.conf2 = nn.Conv2d(10, 20, kernel_size=5)
		self.conf_dropout = nn.Dropout2d()
		self.fc1 = nn.Linear(320, 60)
		self.fc2 = nn.Linear(60, 10)

	def forward(self, x):
		x = self.conf1(x)
		x = F.max_pool2d(x, 2)
		x = F.relu(x)
		x = self.conf2(x)
		x = self.conf_dropout(x)
		x = F.max_pool2d(x, 2)
		x = F.relu(x)
		x = x.view(-1, 320)
		x = F.relu(self.fc1(x))
		x = self.fc2(x)
		return F.log_softmax(x)

model = Netz()

optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.8)

if os.path.isfile('MNIST.pt'):
    model = torch.load('MNIST.pt')

def train(epoch):
	model.train()
	for batch_id, (data, target) in enumerate(trainData):
		data = Variable(data)
		target = Variable(target)
		optimizer.zero_grad()
		out = model(data)
		criterion = F.nll_loss
		loss = criterion(out, target)
		loss.backward()
		optimizer.step()
		print('epoche: ', epoch,f' [{batch_id * len(data)}/{len(trainData.dataset)}] ({100. * batch_id / len(trainData):.0f}%)',  f' \tLoss: {loss.data}')

def test():
	model.eval()
	loss = 0
	correct = 0
	for data, target in testData:
		data = Variable(data)
		target = Variable(target)
		out = model(data)
		loss += F.nll_loss(out, target, size_average=False).data
		prediction = out.data.max(1, keepdim=True)[1]
		correct += prediction.eq(target.data.view_as(prediction)).cpu().sum()
	loss = loss / len(testData.dataset)
	print('Loss: ', loss)
	print('Genauigkeit : ', 100. * correct/len(testData.dataset),'%')

for epoch in range(1, 1):
	train(epoch)
	test()

torch.save(model, 'MNIST.pt')