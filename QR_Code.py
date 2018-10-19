import qrcode, random

cijfer = random.randint(1,999999)
img = qrcode.run_example(cijfer)

ans = input('Voer cijfer in: ')
while not ans == str(cijfer):
    print('DIt cijfer is incorrect.')
    ans = input('Voer cijfer in: ')
else:
    print('Juiste invoer.')
