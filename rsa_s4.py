import sympy

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

N_totient = (p-1) * (q-1)
result = sympy.mod_inverse(e, N_totient)
print (result)