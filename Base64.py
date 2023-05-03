import base64

result = bytearray.fromhex('72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf')
base64res = base64.b64encode(result)
print(base64res)