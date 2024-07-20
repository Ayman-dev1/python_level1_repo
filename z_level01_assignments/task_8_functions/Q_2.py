def check_palindrome(string):
    is_palindrome = string == string[::-1]
    return string + " is a palindrome? " + str(is_palindrome)


result = check_palindrome("radar")
print(result)
