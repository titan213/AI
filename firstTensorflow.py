#python3

import tensorflow as tf
hello = tf.constant('Hello tensorflow')
sess=tf.Session()
print(sess.run(hello))

print('Hello')