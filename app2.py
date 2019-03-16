import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import io
from flask import Flask, render_template

app2 = Flask(__name__)


@app2.route('/')
def hello_world():
    X = [1., 2., 3, ]
    Y = [1., 2., 3, ]
    m = n_samples = len(X)
    W = tf.placeholder(tf.float32)
    hypothesis = tf.multiply(X, W)
    cost = tf.reduce_mean(tf.pow(hypothesis - Y, 2)) / m
    W_val = []
    cost_val = []
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(-30, 50):
        W_val.append(i * 0.1)
        cost_val.append(sess.run(cost, feed_dict={W: i * 0.1}))

    plt.plot(W_val, cost_val, 'ro')
    plt.ylabel('COST')
    plt.xlabel('W')

    return render_template('index.html', name='LINEAR REGRESSION2')


if __name__ == '__main__':
    app2.run()
