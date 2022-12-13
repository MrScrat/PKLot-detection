  <h1>Parking Spot detection with PKLot dataset</h1>

  <p>
    This was a project from CSC 3520 at Florida Southern College. We used the the publicly available PKLot dataset and tried some different simple neural network architectures to decide whether a given image segment is an occupied or an empty parking spot.
    <br>
  </p>

  ## Table of contents

- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Neural Networks Used](#neural-networks-used)
- [Heatmaps](#heatmaps)
- [Miscellaneous](#miscellaneous)

## Dataset
We used the publicly available PKLot dataset.
This is the original paper:
<p>
    Almeida, Paulo & Soares de Oliveira, Luiz & Jr, Alceu & Jr, Eunelson & Koerich, Alessandro. (2015). PKLot - A Robust Dataset for Parking Lot Classification. Expert Systems with Applications. 42. 10.1016/j.eswa.2015.02.009.
</p>
<p>
    The version we used includes segmented parking spots. Here is the link to the version we used: <a href='https://www.kaggle.com/datasets/blanderbuss/parking-lot-dataset'>https://www.kaggle.com/datasets/blanderbuss/parking-lot-dataset</a>
</p>
<p>
    To get a validation, a test, and a training dataset, we split the original dataset into three different parts. As the paper suggests, we didn't use images from the same days for the different sets. This means that none of the pictures in the training set were taken on the same day as the images in the test or the validation sets.
</p>
<p>
    Our Training dataset contained 489852 images. Our validation dataset contained 57115 images. And our test dataset contained 148884 images.
</p>

## Preprocessing
<p>
    Since the dataset already contained segmented images, we only had to resize the images for our purpose. The script <a href='./resize_images.py'> resize_images.py </a> uses opencv to resize all images to 90x90.
</p>

## Neural Networks Used
<p>
    We used two different architectures. First, we tried a network with one hidden layer. Originally we did this to see if everything else like the datagenerator works. We were surprised by its performance which is why we kept it. The other architecture we tried is a convulutional neural network with multiple max pooling and convolutional layers. The performance of the networks on our validation dataset turned out to be very similar and was around 98%.
    <br>
    The models are in the directories 'simple_nn' and 'simple_conv'. Both folders contain a jupyter notebook which was used to train the models and some different version of the models that we experimented with.
</p>

## Heatmaps
<p>
    <a href=./heatmap.ipynb>heatmap.ipynb</a> is a jupyter notebook that creates two heatmaps for empty and occupied by using a very simple sliding window approach. The input image path is defined at the top of the notebook. The size of the sliding window and the step in which the window moves can be adjusted further down. Currently the input image is resized to 1350x720 which is divisible by 90 to prevent having to deal with the edges. This means step and window size should be chosen so 90 is divisible by them.
</p>

## Miscellaneous
<p>
    <a href=./test_model.py>test_model.py</a> was used to see a model's predictions and validate that our code was doing what we intended. <a href=./find_img_sizes.py>find_img_sizes.py</a> was used once to find the sizes of all the original image segments. <a href=./visualize_bbox.py>visualize_bbox.py</a> uses the annotations and the full parking lot images to visualize the annotated bounding boxes. Press any key to cycle through the input images.
</p>
