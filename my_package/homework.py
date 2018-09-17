__all__ = (
    'is_english_letter',
    'factorial',
    'multiple_table'
)


# task 1
def is_english_letter(letter):
    letter = letter.lower()
    return 'a' <= letter <= 'z'


# task 2
def factorial(n):
    return n * factorial(n-1) if n else 1


# task 3
def multiple_table(n):
    for i in range(1, n, 1):
        for j in range(1, n, 1):
            print("%s x %s = %s".rjust(20, " ") % (i, j, i * j), end='')
        print()

if __name__ == '__main__':
    print(is_english_letter('a'))
    print(factorial(5))
    print(multiple_table(10))
