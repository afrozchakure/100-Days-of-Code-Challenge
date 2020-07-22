from tensorflow.keras.preprocessing.image
import ImageDataGenerator 

train_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory(  # load images from directory and its sub-directory(point to the directory that point to the sub-directory)
    train_dir, 
    target_size = (300, 300), 
    batch_size = 128, 
    class_mode = 'binary')

# directory --> subdirectory ---> (contain various classes)

test_datagen = ImageDataGenerator(rescale = 1./255)
validation_generator = test_datagen.flow_from_directory(
    validation_dir, 
    target_size = (300, 300), 
    batch_size = 32, 
    class_mode = 'binary')


##  For 300 * 300 input image with 3 color channels 
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation = 'relu', input_shape = (300, 300, 3)),  
    tf.keras.layers.MaxPooling2D(2, 2), 
    tf.keras.layers.Conv2D(32, (3, 3), activation = 'relu'), 
    tf.keras.layers.MaxPooling2D(2,2), 
    tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2), 
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation = 'relu'),
    tf.keras.layers.Dense(1, activation = 'sigmoid')    
])    

## Training the ConvNet with fit_generator
from tensorflow.keras.optimizers import RMSprop

model.compile(loss = 'binary_cross_entropy', 
    optimizers = RMS(lr=0.001), 
    metrics=['acc'])
    
## Streams the images from the training directory
history = model.fit_generator(
        train_generator, 
        steps_per_epoch=8, # Doing 8 batches
        epochs = 15,  # No. of epochs to train for
        validation_data = validation_generator,  
        validation_steps = 8,  # Doing it in steps (batches of 32)
        verbose = 2)  # A little less animation, hiding the epoch progress
  



