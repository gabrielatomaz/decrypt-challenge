import base64

def base64_to_hex(base64_string):
    decoded_bytes = base64.b64decode(base64_string, validate=True)
    hex_string = decoded_bytes.hex()
    return hex_string

base64_input = "TcIHoIbSS80pEl05rbsXGQRk8Kolm8al98NnzTZZTfE="
hex_output = base64_to_hex(base64_input)

if hex_output:
    print("hex:", hex_output)
