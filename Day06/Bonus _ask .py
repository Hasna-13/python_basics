print("Password Generator")
length = int(input("Length: "))
N = input("Include numbers? (y/n): ").strip().lower() == 'y'
S = input("Include symbols? (y/n): ").strip().lower() == 'y'

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+:?"

seed = ord(letters[0]) 

def generate_password(length, include_numbers=True, include_symbols=True):

    pool = letters
    if include_numbers:
        pool += numbers
    if include_symbols:
        pool += symbols

    password = ""
    local_seed = seed

    for i in range(length):
        index = (local_seed * 7 + i * 3 + 5) % len(pool)
        password += pool[index]
        local_seed = index + 1  

    return password

p = generate_password(length, N, S)
print("Generated password:", p)
