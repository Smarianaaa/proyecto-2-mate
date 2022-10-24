def mcd(n1, n2):
    mcd = 1

    if n1 % n2 == 0:
        return n2
    
    for k in range(int(n2/2), 0, -1):
        if n1 % k == 0 and n2 % k == 0:
            mcd = k 
            break

    return mcd

print(mcd(150, 39))
print("ingrese los digitos:",mcd)
