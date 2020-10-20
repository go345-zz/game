import torch
import torchvision
from torchvision import transforms
from PIL import Image

normalize = transforms.Normalize(mean= [0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

transform = transforms.Compose([
	transforms.Resize(256),
	transforms.CenterCrop(256),
	transforms.ToTensor(),
	normalize])

img=Image.open("catDog/train/cat.0.jpg")
img_tensor = transform(img)
img_tensor.unsqueeze_(0)
print(img_tensor)
