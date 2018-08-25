from decimal import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

"""y_ is the appended list of J values as we step through the train method and decrease the Error """
y_ = []
# """X_ is the list of epoch numbers relative to y_ item."""
X_ = []

class SWNetwork:

    def __init__(self):
        self.targetchess64 = []
        self.datachess64 = []
        self.targetchess64N = []
        self.datachess64N = []
        self.datachess64W1 = []
        self.datachess64W2 = []
        self.datachess64W3 = []
        self.datachess64W4 = []
        self.datachess64W5 = []
        self.best_J = []

    def tanh(self, z):
        return np.tanh(z)

    def tanhprime(self, z):
        return 1.0 - np.tanh(z) ** 2

    def data_sets(self):

        self.targetchess64 = np.array([[5], [3], [3], [8], [4], [3], [3], [5], [2], [2], [2], [2], [2], [2], [2], [2],
                                       [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9],
                                       [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9],
                                       [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-5], [-3], [-3], [-8], [-4],
                                       [-3], [-3], [-5]])

        self.datachess64 =np.array([[5], [3], [3], [8], [4], [3], [3], [5], [2], [2], [2], [2], [2], [2], [2], [2],
                                       [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9],
                                       [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9], [9],
                                       [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-2], [-5], [-3], [-3], [-8], [-4],
                                       [-3], [-3], [-5]])

        # print(self.datachess64)


        """Normalize DATA"""
        self.datachess64N = self.datachess64 / np.amax(self.datachess64)


        """Get weights/ W1 = row vector, W2 = square matrix, W3 = column vector"""
        #self.datachess64W1 = np.random.normal(0, 1, (1, 64))
        #self.datachess64W2 = np.random.normal(0, 1, (64, 64))
        #self.datachess64W3 = np.random.normal(0, 1, (64, 64))
        #self.datachess64W4 = np.random.normal(0, 1, (64, 64))
        #self.datachess64W5 = np.random.normal(0, 1, (64, 1))
        self.datachess64W1 = np.load('C:/Users/user/PycharmProjects/CHESS/W641_update.npy')
        self.datachess64W2 = np.load('C:/Users/user/PycharmProjects/CHESS/W642_update.npy')
        self.datachess64W3 = np.load('C:/Users/user/PycharmProjects/CHESS/W643_update.npy')
        self.datachess64W4 = np.load('C:/Users/user/PycharmProjects/CHESS/W644_update.npy')
        self.datachess64W5 = np.load('C:/Users/user/PycharmProjects/CHESS/W645_update.npy')

    def train(self):

        best_J = np.load('C:/Users/user/PycharmProjects/CHESS/best_J.npy')
        #best_J = 10
        total_accuracy = 0
        self.data_sets()
        epoch =100000
        theta = 0.004301
        b = 1
        for i in range(2, epoch):
            """3 hidden layer network forward pass"""
            z2 = (np.dot(self.datachess64N, self.datachess64W1) + b)
            a2 = self.tanh(z2)
            z3 = (np.dot(a2, self.datachess64W2) + b)
            a3 = self.tanh(z3)
            z4 = (np.dot(a3, self.datachess64W3) + b)
            a4 = self.tanh(z4)
            z5 = (np.dot(a4, self.datachess64W4) + b)
            a5 = self.tanh(z5)
            z6 = (np.dot(a5, self.datachess64W5) + b)
            yHat = self.tanh(z6)
            J = 0.5 * sum((self.datachess64N - yHat) ** 2)
            X_.append(i)
            y_.append(J)
            """back propogation algorithm"""
            delta6 = np.multiply(-(self.datachess64N - yHat), self.tanhprime(z6))
            dJdW5 = np.dot(a5.T, delta6)
            delta5 = np.dot(delta6, self.datachess64W5.T) * self.tanhprime(z5)
            dJdW4 = np.dot(delta5, a4)
            delta4 = np.dot(delta5, self.datachess64W4.T) * self.tanhprime(z4)
            dJdW3 = np.dot(delta4, a3)
            delta3 = np.dot(delta4, self.datachess64W3.T) * self.tanhprime(z3)
            dJdW2 = np.dot(delta3, a2)
            delta2 = np.dot(delta3, self.datachess64W2)
            dJdW1 =  np.dot(self.datachess64N.T, delta2)
            """applied weight adjustment 'theta dependent'"""
            W1_grad_applied = np.dot(theta, dJdW1)
            W2_grad_applied = np.dot(theta, dJdW2)
            W3_grad_applied = np.dot(theta, dJdW3)
            W4_grad_applied = np.dot(theta, dJdW4)
            W5_grad_applied = np.dot(theta, dJdW5)
            """updating weights"""
            self.datachess64W1 = self.datachess64W1 - W1_grad_applied
            self.datachess64W2 = self.datachess64W2 - W2_grad_applied
            self.datachess64W3 = self.datachess64W3 - W3_grad_applied
            self.datachess64W4 = self.datachess64W4 - W4_grad_applied
            self.datachess64W5 = self.datachess64W5 - W5_grad_applied

            print('Epoch : {0}, Error = {1},'.format(i, J))
        if best_J > J:
            best_J = J

            np.save('C:/Users/user/PycharmProjects/CHESS/W641_update', self.datachess64W1)
            np.save('C:/Users/user/PycharmProjects/CHESS/W642_update', self.datachess64W2)
            np.save('C:/Users/user/PycharmProjects/CHESS/W643_update', self.datachess64W3)
            np.save('C:/Users/user/PycharmProjects/CHESS/W644_update', self.datachess64W4)
            np.save('C:/Users/user/PycharmProjects/CHESS/W645_update', self.datachess64W5)

            np.save('C:/Users/user/PycharmProjects/CHESS/best_J', best_J)
            print('best_J = {}'.format(best_J))
        print('current best_J = {}'.format(best_J))

        for i in range(0, 64):
            accuracy = ((yHat[i] * 9) / self.datachess64[i]) * 100
            print('%0.1f, %0.1f, %0.1f ' % ((self.datachess64[i]), yHat[i] * 9, accuracy))
            total_accuracy = total_accuracy + accuracy
            ave_accuracy = total_accuracy/64
        print('Ave Accuracy =', ave_accuracy)

data = SWNetwork()
# data.data_sets()
data.train()

plt.scatter(X_[50 :], y_[50 :], s=25, c="blue")
plt.xlabel('Epochs # training cycles')
plt.ylabel('Error (Cost function J')
plt.show()
