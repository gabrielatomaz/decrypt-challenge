import gmpy2
from Crypto.PublicKey import RSA

f = open("key_public.txt", "r")
key = RSA.importKey(f.read())
print("n:", key.n)
print("e:", key.e)

n = key.n # 26179751854087331402331071604988485626982836276798177195222446151071273439780592994270737435017138406631242790569709
e = key.e # 65537
p = 5146951772184269300025961189405010212772342675599485312661 # factor N using cado nfs
q =  5086457579721431558131968975470302984140630429995118930169 # factor N using cado nfs
phi = (p - 1) * (q - 1)

print("p:", p)
print("q:", q)

d = gmpy2.invert(e, phi)
print("d:", d)
