# coding=utf-8

import time
from flask import Flask, request
import numpy.random as rand

app = Flask(__name__)

@app.route("/livetest")
def livetest():
    return "TEST OK"

@app.route('/')
def calculate_fact():
    n = rand.randint(low=1000, high=20000)
    if n == 0:
        return 1
    elif n<0:
        return ValueError
    else:
        x = 1
        for i in range(1, n):
            x = x * n

        return '{0} != {1}'.format(n, x)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
