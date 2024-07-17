
## 🕵️‍♂️ Challenge Overview 

As a cryptanalyst in the Biuro Szyfrów, you have intercepted an encrypted message. The message was encrypted using AES 256-bit encryption, and its key (stored in `key_for_message.en`) was encrypted with an RSA public key. However, the RSA public key itself is encrypted with AES 256-bit encryption, and you only have the first two characters of the 12-character password: "an". Additionally, you have received the hash of the password used to encrypt the RSA public key (stored in `key_for_rsa_public.hash`). 

Your mission, should you choose to accept it, is to decrypt the encrypted message by finding the missing password, decrypting the RSA public key, and then using it to decrypt the AES key, which will finally allow you to decrypt the message.

## 📂 Files Provided 

- `message.en`: The encrypted message
- `key_for_message.en`: The AES key for the message, encrypted with the RSA public key
- `key_public.en`: The RSA public key, encrypted with a 12-character password
- `key_for_rsa_public.hash`: The hash of the password used to encrypt the RSA public key

## 🛠️ Steps to Solve the Challenge 

### 🔓 Step 1: Brute-forcing the Password 

1. Convert the `key_for_rsa_public.hash` from base64 to hex using a Python script (`base64_to_hex.py`) 
2. Use Hashcat to brute-force the password using the known first two characters "an"

```bash
hashcat -m 1400 -a 3 4dc207a086d24bcd29125d39adbb17190464f0aa259bc6a5f7c367cd36594df1 an?!?!?!?!?!?!?!?!?!?! -o decrypted_password.txt -O
```

**Explanation:**
- `hashcat`: A password recovery tool.
- `-m 1400`: Specifies the hash type (SHA-256).
- `-a 3`: Specifies the attack mode (brute-force).
- `4dc207a086d24bcd29125d39adbb17190464f0aa259bc6a5f7c367cd36594df1`: The hex-encoded hash.
- `an?!?!?!?!?!?!?!?!?!?!`: The mask indicating the known and unknown parts of the password.
- `-o decrypted_password.txt`: Output file for the found password.
- `-O`: Optimized kernel.

### 🔑 Step 2: Decrypting the RSA Public Key 

After obtaining the password from Hashcat (this took 6 days and 10 hours on an 8GB RAM server 🖥️💻), use it to decrypt the RSA public key.

```bash
openssl aes-256-cbc -a -nosalt -d -in key_public.en -out key_public.txt
```

**Explanation:**
- `openssl aes-256-cbc`: Uses the AES 256-bit encryption in CBC mode.
- `-a`: Base64 decode.
- `-nosalt`: Do not use a salt.
- `-d`: Decrypt mode.
- `-in key_public.en`: Input encrypted file.
- `-out key_public.txt`: Output decrypted file.

### 🧩 Step 3: Extracting RSA Components 

Use Python's `pycryptodome` library to extract the RSA components (N and E) from the decrypted public key.

### 🔢 Step 4: Factoring N 

Use `cado-nfs` to factor N into its prime components (p and q).

```bash
./cado-nfs.py N
```

### 🔐 Step 5: Calculating the Private Key 

Calculate φ(N) and d using the prime factors p and q. Generate the private key using the `cryptography` library in Python (`pem_generator.py`).

### 🔓 Step 6: Decrypting the AES Key 

With the private key, decrypt the AES key for the message.

```bash
openssl pkeyutl -decrypt -inkey private_key.pem -in key_for_message.en -out new_file_decrypt.txt
```

**Explanation:**
- `openssl pkeyutl`: Utility for public key operations.
- `-decrypt`: Decrypt mode.
- `-inkey private_key.pem`: Input private key file.
- `-in key_for_message.en`: Input encrypted AES key file.
- `-out new_file_decrypt.txt`: Output decrypted AES key file.

### 📜 Step 7: Decrypting the Message 

Finally, use the decrypted AES key to decrypt the message.

```bash
openssl aes-256-cbc -nosalt -a -d -in message.en -out final_text.txt
```

**Explanation:**
- `openssl aes-256-cbc`: Uses the AES 256-bit encryption in CBC mode.
- `-a`: Base64 decode.
- `-nosalt`: Do not use a salt.
- `-d`: Decrypt mode.
- `-in message.en`: Input encrypted message file.
- `-out final_text.txt`: Output decrypted message file.

🎉🔓📜 By following these steps, you will successfully decrypt the intercepted message. 