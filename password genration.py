import random
import string
password_length = int(input("Enter the desired password length: "))
all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for _ in range(password_length))
print(f"Generated password: {password}")
