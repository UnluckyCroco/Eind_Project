import random
from time import*


def times():
    ''
    localtime(time())
    ''
    return(asctime(localtime(time())))

# naam = input("Wat zijn de laatste 4 cijfers van uw OV kaart?: ")
#
# def fiets_stallen():
#     read = open('Gegevens', 'r')
#     write = open('Stallen.txt', 'a')
#     infile = read.readlines()
#     outfile = write.write
#
#     for infiles in infile:
#         zin = infiles.split(';')
#         info = zin[4]
#
#         if info == naam:
#
#
#             for x in range(1):
#                 rnummer = random.randint(1,701)
#                 infile = open('Stallen.txt', 'r')
#                 regels = infile.readlines()
#                 for regel in regels:
#                     zin = regel.split(';')
#                     nummer = zin[0]
#                     if nummer == rnummer :
#                      Random = True
#                     else:
#                      Random = False
#                     if Random:
#                      fiets_stallen()
#             outfile('\n' + naam + '; ' + str(times()) + '; ' + str(rnummer))
#
#             return 'Alstublieft, u kunt uw fiets nu veilig stallen op stallingplek: ' + str(rnummer)
#     return 'Dit nummer is niet geregistreerd'
#
#


def fiets_stallen(self):
        read = open('Ingelogd', 'r')
        read1 = open('Stallen.txt', 'r')
        write = open('Stallen.txt', 'a')
        infile = read.readlines()
        infile1 = read1.readlines()
        outfile = write.write

        for infiles1 in infile1:
            zin1 = infiles1.split(';')
            self.info1 = zin1[1]

        for infiles in infile:
            zin = infiles.split(';')
            self.info = zin[4]

            if self.info  == self.info1:
                return self.warning()


            #if info == naam:
            for x in range(1):
                    self.rnummer = random.randint(1, 701)
                    infile = open('Stallen.txt', 'r')
                    regels = infile.readlines()
                    for regel in regels:
                        zin = regel.split(';')
                        nummer = zin[2]
                        ov = zin[1]
                        if nummer == self.rnummer:
                            self.fiets_stallen()
                        if ov == self.info:
                            self.warning()
                    self.stallen = (str(self.times()) + '; ' + self.info + '; ' + str(self.rnummer) + '\n')
                    outfile(self.stallen)
        return self.toonStallen()