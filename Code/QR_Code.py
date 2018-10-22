import qrcode, random

cijfer = random.randint(1,999999)
img = qrcode.run_example(cijfer)

print('\033[34mBewaar deze foto om je fiets weer op te halen.\033[0m')
ans = input('Voer cijfer in: ')

while not ans == str(cijfer):
    print('Dit cijfer is incorrect.')
    ans = input('Voer cijfer in: ')
else:
    print('Juiste invoer.')
