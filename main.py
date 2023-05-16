import RSA as rsa
import DSA as dsa

def rsa_test():
    r = rsa.RSA(463, 547)
    m = 20

    enc = r.encrypt(m)
    dec = r.decrypt(enc)

    print('p: ',r.p)
    print('q: ',r.q)
    print('message: ', m)
    r.print_public_key()
    r.print_private_key()
    print('encrypted message: ', enc)
    print('decrypted message: ', dec)


def dsa_test():
    d = dsa.DSA(1024)
    message = b"asd"
    signature = d.sign(message)
    print(d.validate(message))
    print(d.validate(b"add"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rsa_test()
    #dsa_test()

