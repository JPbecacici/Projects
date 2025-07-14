#Email Slicer
# Email Slicer is a simple program that takes an email address as input and slices it to extract the username and domain.

email = input('Enter your email: ')

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f'Your username is {username} and your domain is {domain}')