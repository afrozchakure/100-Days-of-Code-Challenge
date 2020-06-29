import os
import tensorflow as tf

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Turn off log messages to the console

# Define computational graph
X = tf.compat.v1.placeholder(dtype = tf.float32, name = 'X')
Y = tf.compat.v1.placeholder(dtype = tf.float32, name = 'Y')

addition = tf.add(X, Y, name = 'addition')


# Create the session
with tf.compat.v1.Session() as session:

    result = session.run(addition, feed_dict = {X : [1, 2, 3], Y : [4, 5, 6]})

    print(result)
