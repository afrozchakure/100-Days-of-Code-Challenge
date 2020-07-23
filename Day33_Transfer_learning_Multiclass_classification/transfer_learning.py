import os

from tensorflow.keras import layers
from tensorflow.keras import Model

from tensorflow.keras.application.inception_v3 import InceptionV3

local_weights_file = '/tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

pre_trained_model = InceptionV3(input_shape = (150, 150, 3),
                                include_top = False,  # Ignore build-in weights and get straight to the convolutions
                                weights = None)

pre_trained_model.load_weights(local_weights_file)


for layer in pre_trained_model.layers:
    layer.trainable = False  # Lock the layers to say they will not be trainable with this code
    
pre_trained_model.summary()

last_layer = pre_trained_model.get_layer('mixed7')  # Output of the model that are 7 * 7 
last_output = last_layer.output  # Grab that layer from inception and take its output

from tensorflow.keras.optimizers import RMSprop

x = layers.Flatten()(last_output) # Takes the output from the inception model mixed7 layer (We flatten the input)
x = layers.Dense(1024, activation = 'relu')(x)  # Dense hidden layer
x = layers.Dropout(0.2)(x)  # Adding dropouts, removing 20% of our neurons
x = layers.Dense(1, activation = 'sigmoid')(x)  

model = Model(pre_trained_model.input, x)  # Create a model by passing the input and the layers definition

# Compilting the model
model.compile(optimizer = RMSprop(lr = 0.0001,  
                        loss = 'binary_crossentropy', 
                        metrics = ['acc'])
                        
# Add our data-augmentation parameters to ImageDataGenerator (We are augmenting the images)
train_datagen = ImageDataGenerator(rescale = 1./255., 
                                rotation_range = 40,
                                width_shift_range = 0.2,
                                height_shift_range = 0.2, 
                                shear_range = 0.2, 
                                zoom_range = 0.2, 
                                horizontal_flip = True)

# Getting the training data from the generator by going through the augmentations
train_generator = train_datagen.flow_from_directory(
                            train_dir, 
                            batch_size = 20,
                            class_mode = 'binary',
                            target_size = (150, 150))
