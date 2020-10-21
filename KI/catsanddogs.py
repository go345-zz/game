from typing import List
import torch
import torchvision
from torchvision import transforms
from PIL import Image
from os import listdir
from random import random
import torch.optim as optim

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

optimizer = optim.Adam(model.parameters(), lr=0.01)
def train(epoch):
	model.train()
	for 