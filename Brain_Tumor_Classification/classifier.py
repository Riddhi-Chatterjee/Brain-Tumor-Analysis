import numpy as np
import pandas as pd
import torch
from torchvision import transforms
from PIL import Image
from torchvision import datasets, models, transforms

classes = ['Predicted tumor type: glioma', 'Predicted tumor type: meningioma', 'No tumor was detected', 'Predicted tumor type: pituitary']

def base_model_build():
    #Load the pretrained model from pytorch
    vgg16 = models.vgg16(pretrained=True)

    # print out the model structure
    #print(vgg16)
    
    # Freeze training for all "features" layers
    for param in vgg16.features.parameters():
        param.requires_grad = False
        
    import torch.nn as nn

    n_inputs = vgg16.classifier[6].in_features

    # add last linear layer (n_inputs -> 5 flower classes)
    # new layers automatically have requires_grad = True
    last_layer = nn.Linear(n_inputs, len(classes))

    vgg16.classifier[6] = last_layer

    # if GPU is available, move the model to GPU
    train_on_gpu = torch.cuda.is_available()
    if train_on_gpu:
        print("training on gpu...")
        vgg16.cuda()
    else:
        print("no gpu found.")

    # check to see that your last layer produces the expected number of outputs
    #print(vgg16.classifier[6].out_features)
    #print(vgg16)
    
    return vgg16

model = base_model_build()
model.load_state_dict(torch.load("./vgg16.pth", map_location=torch.device('cpu')))

data_transform = transforms.Compose([transforms.ToTensor(),
                                     transforms.Resize((224,224))])

def classify_image(img_path):
    img = Image.open(img_path).convert('RGB')
    img = data_transform(img)
    img = img.reshape(1, img.shape[0], img.shape[1], img.shape[2])
    if torch.cuda.is_available():
        img = img.cuda()
    
    pred=''
    with torch.no_grad():
        # Set to evaluation mode:
        model.eval()
        #Get the prediction:
        pred = model(img)
    return classes[np.argmax(pred[0], axis=-1)]
