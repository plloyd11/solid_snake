username = input('Enter your username ')
password = input('Please enter your password ')

password_length = len(password)
password_secret = '*' * password_length

print(f'{username}, your password {password_secret} is {password_length} letters long!')
