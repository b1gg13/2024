def raise_to (base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result

print (raise_to(2, 9))
print (raise_to(4, 4))
print (raise_to(12, 2))
