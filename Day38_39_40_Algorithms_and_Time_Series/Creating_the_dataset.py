import tensorflow as tf


# Create dataset from 0 to 9
dataset = tf.data.Dataset.range(10)
# Expand our dataset using windowing (Size of window and how much we want to shift by each time)
dataset = dataset.window(5, shift=1, drop_remainder=True) 
# drop_remainder removes all the value which are less than 5 digits
for window_dataset in dataset:
    for val in window_dataset:
        print(val.numpy(), end='')
    print()

#print("Window:\n", dataset)
"""
for val in dataset:
    print(val.numpy())
"""

### Converting the above into a numpy list
print("\nConverted Numpy list form:\n")
dataset = dataset.flat_map(lambda window: window.batch(5))
for window in dataset:
    print(window.numpy())
    
# Splt the data into features and labels
print("\nSplitting the data in features and labels\n")
dataset = dataset.map(lambda window : (window[:-1], window[-1:]))
for x,y in dataset:
    print(x.numpy(), y.numpy())
    
# Suffle the data before training
print("\nSuffled output\n")
dataset = dataset.shuffle(buffer_size = 10) # 10 is amount of data items we have (0 - 9)
for x, y in dataset:
    print(x.numpy(), y.numpy())
    
# Batching the data
print("\nBatching the data\n")
dataset = dataset.batch(2).prefetch(1)  # Batching the data into sets of 2
for x,y in dataset:
    print("x = ", x.numpy())
    print("y = ", y.numpy())
    

