# Recursive approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

#character count program
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

#Palindrome Program
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

print('factorial using recursive',factorial_recursive(6))
print('factorial using iterative',factorial_iterative(7))
print('dictonary of count of charchters: ',count_characters("hello"))
print('madam is palindrome: ',is_palindrome('madam'))