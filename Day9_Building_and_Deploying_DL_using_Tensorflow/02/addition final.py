import os
import tensorflow as tf

# Turn off TensorFlow warning messages in program output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define computational graph
X = tf.placeholder(tf.float32, name="X")
Y = tf.placeholder(tf.float32, name="Y")

addition = tf.add(X, Y, name="addition")


# Create the session
with tf.Session() as session:

    result = session.run(addition, feed_dict={X: [1, 2, 10], Y: [4, 2, 10]})

    print(result)
