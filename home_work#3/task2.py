n = int(input('Write an enteger: '))

def is_prime(n):
    if n < 2:
        return 'False'

    for k in range(2, int(n / 2 + 1)):
        if n % k == 0:
            return 'False'
    else:
        return 'True'

print(is_prime(n))