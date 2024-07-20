def check_prime_num(num):
    if num % 1 == 0 and num % num == 0:
        return str(num) + " is a prime number? "
    else:
        return False


m = check_prime_num(1)
print(m)
