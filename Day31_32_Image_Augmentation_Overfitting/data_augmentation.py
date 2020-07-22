train_datagen = ImageDataGenerator(rescale=1./255)  # rescaling on the fly

# Updated to do image augmentation

train_datagen = ImageDataGenerator(
    rescale = 1./255,  # recaling
    rotation_range = 40,  # randomly rotate b/w 0 and 40 degrees
    width_shift_range = 0.2,  # shifting the images
    height_shift_range = 0.2, # Randomly shift b/w 0 to 20 %
    shear_range = 0.2,  # It will shear the image by specified amounts upto the specified portion of the image  
    zoom_range = 0.2, # Zoom the image by 20% of random amounts of the image
    horizontal_flip = True,  # Flip the image/ Mirror image at random
    fill_mode = 'nearest'  # Fills the pixels that might have been lost in the operations
)

