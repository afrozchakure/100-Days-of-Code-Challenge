train_datagen = ImageDataGenerator(rescale = 1./255)

train_generator = train_datagen.flow_from_directory(
                        train_dir, 
                        target_size = (300, 300),
                        batch_size = 128,
                        class_mode = 'categorical')  # For 2 classes set to 'binary'

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation = 'relu', input_shape = (300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2,2),    
    tf.keras.layers.Conv2D(16, (3, 3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(16, (3, 3), activation = 'relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation = 'relu'),
#    tf.keras.layers.Dense(1, activation = 'sigmoid') # for single prediction
    tf.keras.layers.Dense(3, activation = 'sigmoid') # for multi-class classification
])
                        
# Compiling neural network

from tensorflow.keras.optimizers import RMSprop

model.compile(loss='categorical_crossentropy', # binary_crossentropy for single classification
              optimizer = RMSprop(lr=0.001), 
              metrics = ['acc'])
              

