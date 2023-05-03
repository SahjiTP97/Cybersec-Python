import sympy
from Crypto.Util.number import inverse,long_to_bytes
n = 742449129124467073921545687640895127535705902454369756401331
p = 752708788837165590355094155871
q = 986369682585281993933185289261
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(ct,d,n)

print(long_to_bytes(m))