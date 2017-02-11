#Author: Curtis Turner
#Email: cjturner@csu.fullerton.edu
#Description: The file contains the class with the Lehmer's Algorithm random number generator

class PRNG:
    def __init__(self):
        return None

    def next_prn(prevPRNG, _n, _m):
        newNextRand = int((16807*prevPRNG) % (2**31 - 1))
        x = _m - _n + 1
        j = newNextRand % x
        newRand = _n + j
        return newRand
    
    def seed (self, rseed):
        self.seed = rseed

    def newRandom(self, _min, _max):

        newRand = int(((7**5) * self.seed ) % ((2**31) -1))

        n = _max - _min + 1

        i = newRand % n

        randomNumber = _min + i

        return randomNumber
