import unittest
import os
import numpy as np
import pandas as pd
import torch
from torchvision import transforms
from PIL import Image
from torchvision import datasets, models, transforms
from classifier import classify_image

PATH = "test_images"
test_images = {}
for dir in os.listdir(PATH):
    for file in os.listdir(os.path.join(PATH, dir)):
        full_path = os.path.join(os.path.join(PATH, dir), file)
        key = file.split(".")[0]
        test_images[key] = full_path

test_images_keys = test_images.keys()

label_dict = {
    'gl' : 'glioma',
    'me' : 'meningioma',
    'no' : 'notumor',
    'pi' : 'pituitary'
}


class Tester(unittest.TestCase):
    
    def test1(self):        
        index = 0
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test2(self):        
        index = 1
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test3(self):        
        index = 2
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test4(self):        
        index = 3
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test5(self):        
        index = 4
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test6(self):        
        index = 5
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test7(self):        
        index = 6
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test8(self):        
        index = 7
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test9(self):        
        index = 8
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test10(self):        
        index = 9
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test11(self):        
        index = 10
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test12(self):        
        index = 11
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test13(self):        
        index = 12
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test14(self):        
        index = 13
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test15(self):        
        index = 14
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test16(self):        
        index = 15
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test17(self):        
        index = 16
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test18(self):        
        index = 17
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test19(self):        
        index = 18
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test20(self):        
        index = 19
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test21(self):        
        index = 20
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test22(self):        
        index = 21
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test23(self):        
        index = 22
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test24(self):        
        index = 23
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test25(self):        
        index = 24
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test26(self):        
        index = 25
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test27(self):        
        index = 26
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test28(self):        
        index = 27
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test29(self):        
        index = 28
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test30(self):        
        index = 29
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test31(self):        
        index = 30
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])
    
    def test32(self):        
        index = 31
        result = classify_image(test_images[test_images_keys[index]])
        if result == 'No tumor was detected':
            result = 'notumor'
        else:
            result = result.split(": ")[1]
        print("Image: "+test_images_keys[index]+" --> Predicted tumor type: "+result+"   Actual type: "+label_dict[test_images_keys[index].split("_")[0].split("-")[1]]+"   Result: "+("SUCCESS" if (result == label_dict[test_images_keys[index].split("_")[0].split("-")[1]]) else "FAILURE"))
        self.assertEqual(result, label_dict[test_images_keys[index].split("_")[0].split("-")[1]])


if __name__ =="__main__":
    unittest.main()
