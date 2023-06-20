import random
import string

def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

random_string = generate_random_string(10)
print(random_string)
