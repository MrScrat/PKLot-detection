import cv2
from keras import models
import numpy as np
import pdb


# demo_img = cv2.imread('/Users/ludwig/Documents/College/Semester5/ai2/project2/PKLot/PKLotSegmented_resized/PUC/Rainy/2012-10-23/Occupied/2012-10-23_08_15_50#006.jpg')
demo_img = cv2.imread('./PKLot/PKLotSegmented_resized/UFPR05/Cloudy/2013-03-09/Empty/2013-03-09_18_35_14#008.jpg')

model = models.load_model('./simple_nn/simple_nn_weights')
demo_img = cv2.resize(demo_img, (100, 100))
print(demo_img.shape)

noise = np.random.normal(size=demo_img.shape)

# pdb.set_trace()
# print(model.predict(demo_img.reshape((1, *demo_img.shape))))
print(model.predict(demo_img.reshape((1, *demo_img.shape))))
cv2.imshow('', demo_img)
cv2.waitKey()