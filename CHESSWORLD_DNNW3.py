from decimal import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

"""y_ is the appended list of J values as we step through the train method and decrease the Error """
y_ = []
# """X_ is the list of epoch numbers relative to y_ item."""
X_ = []


class CWNetwork:

    def __init__(self):
        self.target = []
        self.data = []
        self.targetN = []
        self.dataN = []
        self.dataW1 = []
        self.dataW2 = []
        self.dataW3 = []
        self.best_J = []
        self.start64 = []

    def tanh(self, z):
        return np.tanh(z)

    def tanhprime(self, z):
        return 1.0 - np.tanh(z) ** 2


    def ReLU(self, z):
        return z * (z > 0)

    def ReLUPrime(self, z):
        return 1. * (z > 0)

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoidprime(self, z):
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def data_sets(self):


        self.data64 = np.array([[-5.0], [-3.0], [-4.0], [-8.0], [-1.0], [-4.0], [-3.0], [-5.0],
                                [-2.0], [-2.0], [-2.0], [-2.0], [-2.0], [-2.0], [-2.0], [-2.0],
                                [9.0],  [9.0],  [9.0],  [9.0],  [9.0],  [9.0],  [9.0],  [9.0],
                                [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0],
                                [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0],
                                [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0],
                                [2.0], [2.0], [2.0], [2.0], [2.0], [2.0], [2.0], [2.0],
                                [5.0], [3.0], [4.0], [8.0], [1.0], [4.0], [3.0], [5.0]])

        self.start64 = np.array([[-5.0], [-3.0], [-4.0], [-8.0], [-1.0], [-4.0], [-3.0], [-5.0],
                                [-2.0], [-2.0], [-2.0], [-2.0], [-2.0], [-2.0], [-2.0], [-2.0],
                                [9.0],  [9.0],  [9.0],  [9.0],  [9.0],  [9.0],  [9.0],  [9.0],
                                [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0],
                                [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0],
                                [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0], [9.0],
                                [2.0], [2.0], [2.0], [2.0], [2.0], [2.0], [2.0], [2.0],
                                [5.0], [3.0], [4.0], [8.0], [1.0], [4.0], [3.0], [5.0]])

        """Normalize DATA"""
        self.data64N = self.data64 / np.amax(self.data64)
        self.start64N = self.start64 / np.amax(self.start64)

        """Get weights/ W1 = row vector, W2 = square matrix, W3 = column vector"""
        #self.dataW1 = np.random.normal(0, 1, (1, 64))
        #self.dataW2 = np.random.normal(0, 1, (64, 64))
        #self.dataW3 = np.random.normal(0, 1, (64, 1))
        self.dataW1 = np.load('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/W1_update.npy')
        self.dataW2 = np.load('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/W2_update.npy')
        self.dataW3 = np.load('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/W3_update.npy')


    def train(self):


        best_J = np.load('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/best_J.npy')
        #best_J = 20
        J = 1
        total_accuracy = 0
        self.data_sets()
        epoch = 100000
        theta = 0.0016
        b = 1.74

        #b =2.9

        for i in range(2, epoch):
            z2 = (np.dot(self.data64N, self.dataW1) + b)
            a2 = self.tanh(z2)
            z3 = (np.dot(a2, self.dataW2) + b)
            a3 = self.tanh(z3)
            z4 = (np.dot(a3, self.dataW3) + b)
            yHat = self.tanh(z4)
            J = 0.5 * sum((self.start64N - yHat) ** 2)
            delta4 = np.multiply(-(self.data64N - yHat), self.tanhprime(z4))
            dJdW3 = np.dot(a3.T, delta4)
            delta3 = np.dot(delta4, self.dataW3.T) * self.tanhprime(z3)
            dJdW2 = np.dot(delta3, a2)
            delta2 = np.dot(delta3, self.dataW2)
            dJdW1 =  np.dot(self.data64N.T, delta2)
            W1_grad_applied = np.dot(theta, dJdW1)
            W2_grad_applied = np.dot(theta, dJdW2)
            W3_grad_applied = np.dot(theta, dJdW3)
            self.dataW1 = self.dataW1 - W1_grad_applied
            self.dataW2 = self.dataW2 - W2_grad_applied
            self.dataW3 = self.dataW3 - W3_grad_applied
            print('Epoch : {0}, Error = {1}'.format(i, J))
            if best_J > J:
                best_J = J
                np.save('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/W1_update', self.dataW1)
                np.save('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/W2_update', self.dataW2)
                np.save('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/W3_update', self.dataW3)
                np.save('C:/Users/user/PycharmProjects/CHESS/CHESSWORLD_DNNW3/best_J', best_J)
                print('best_J = {}'.format(best_J))
        print('current best_J = {}'.format(best_J))
        #for i in range(0, 130):
         #   accuracy = ((yHat[i] * 9) / self.data64[i] * 100)
          #  print('%0.1f, %0.1f, %0.1f ' % ((self.data64[i]), yHat[i] * 9, accuracy))
           # total_accuracy = total_accuracy + accuracy
            #ave_accuracy = total_accuracy/130
       # print('Ave Accuracy =', ave_accuracy)

data = CWNetwork()
#data.data_sets()
data.train()

#plt.scatter(X_[50 :], y_[50 :], s=25, c="blue")
#plt.xlabel('Epochs # training cycles')
#plt.ylabel('Error (Cost function J')
#plt.show()