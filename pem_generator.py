from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

d = 9772916506862483219525301231610285805943743068981909533253990642326690750762735154849167902258751777335016599455073
n = 26179751854087331402331071604988485626982836276798177195222446151071273439780592994270737435017138406631242790569709
e = 65537

p = 5146951772184269300025961189405010212772342675599485312661  
q = 5086457579721431558131968975470302984140630429995118930169 

dmp1 = d % (p - 1)
dmq1 = d % (q - 1)
iqmp = pow(q, -1, p)

private_key = rsa.RSAPrivateNumbers(p, q, d, dmp1, dmq1, iqmp, rsa.RSAPublicNumbers(e, n)).private_key()

private_pem = private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption())

with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(private_pem)

