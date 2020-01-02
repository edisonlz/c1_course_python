#coding=utf-8
import matplotlib.pyplot as plt
import tensorflow as tf
import input_data
import os,sys
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
log_path = os.path.join(PROJECT_ROOT ,'log')
mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)



def draw_images():
    images = mnist.train.images
    labels = mnist.train.labels
    print("[image 0]归一化")
    print(len(images[0]))
    print(images[0])

    print("[image 0]")
    print(labels[0])
    
    fig, ax = plt.subplots(nrows=10, ncols=10, sharex='all', sharey='all')
    ax = ax.flatten()
    for i in range(100):
        img = images[i].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()



def draw_test_images():
    images = mnist.test.images
    labels = mnist.test.labels
    print("[image 0]归一化")
    print(len(images[0]))
    print(images[0])

    print("[image 0]")
    print(labels[0])
    
    fig, ax = plt.subplots(nrows=10, ncols=10, sharex='all', sharey='all')
    ax = ax.flatten()
    for i in range(100):
        img = images[i].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()



def build_net():
    x = tf.placeholder("float", [None, 784])
    W = tf.Variable(tf.zeros([784,10]))
    b = tf.Variable(tf.zeros([10]))

    with tf.name_scope('inputs'):
        y = tf.nn.softmax(tf.matmul(x,W) + b)
        y_ = tf.placeholder("float", [None,10])

    cross_entropy = -tf.reduce_sum(y_*tf.log(y))
    with tf.name_scope('loss'):
        cross_entropy = -tf.reduce_sum(y_*tf.log(y))
        tf.summary.scalar('loss', cross_entropy)

    with tf.name_scope('train'):
        train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    init = tf.initialize_all_variables()

    sess = tf.Session()
    sess.run(init)


    merged = tf.summary.merge_all()

    writer = tf.summary.FileWriter(log_path, sess.graph)

    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

        if i % 10 == 0:  
            result = sess.run(merged,  
                                feed_dict={x: batch_xs, y_: batch_ys})
            writer.add_summary(result, i)


    correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))


    #验证准确度
    a = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})
    print(a)



if __name__ == "__main__":
    #draw_images()
    draw_test_images()
    #build_net()

