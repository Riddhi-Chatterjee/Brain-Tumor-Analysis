import gdown

file_id = '1bhxOexfwqxOX4CbjSXtQ1Gu3PApR2Csq'
url = f'https://drive.google.com/uc?id={file_id}'
output = "Brain_Tumor_Classification/vgg16.pth"  # Specify the output file name

gdown.download(url, output, quiet=False)
