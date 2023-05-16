import math
import util as u
from Crypto.Math import Primality as prm

class RSA:
    def __init__(self, prime1, prime2, e = None):
        if not (prm.test_probable_prime(prime1) or prm.test_probable_prime(prime2)):
            print("A megadott számok nem prímek!")
            return

        # initialize the two primes
        self.p = prime1
        self.q = prime2

        # calculate n and phi(n)
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)

        # find an optimal number for e
        if e is None or math.gcd(e,self.phi_n) != 1:
            self.e = 2 # legkisebb prim
            while self.e < self.phi_n:
                if (math.gcd(self.e, self.phi_n) == 1):
                    break
                else:
                    self.e += 1
        else:
            self.e = e

        # multiplikatív inverz
        self.d = u.modinv(self.e,self.phi_n)

    def encrypt(self,message):
        return u.mod_power(message,self.e,self.n)

    def decrypt(self,dec_message):
        return u.mod_power(dec_message,self.d,self.n)

    def print_public_key(self):
        print(f'public_key: {self.e,self.n}')

    def print_private_key(self):
        print(f'private_key: {self.d,self.n}')
