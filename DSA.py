from Crypto.PublicKey import DSA as dsa
from Crypto.Signature import DSS as dss
from Crypto.Hash import SHA256

class DSA:
    def __init__(self,bits):
        self.sk = dsa.generate(bits)
        self.pk = self.sk.publickey()

        self._signer = dss.new(self.sk,'fips-186-3')
        self._validator = dss.new(self.pk,'fips-186-3')

    def sign(self,message):
        self.hash_obj = SHA256.new(message)
        self._signature = self._signer.sign(self.hash_obj)
        return self._signature

    def validate(self,message) -> bool:
        try:
            self._validator.verify(self.hash_obj,self.sign(message))
            return True
        except ValueError:
            return False