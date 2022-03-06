email = input("Email: ").strip()

username = email[:email.index("@")]  # It gets the reference from the email variable.

domain = email[email.index("@") + 1:]

print(f'Your Username: {username}')
print(f'Your Domain: {domain}')
