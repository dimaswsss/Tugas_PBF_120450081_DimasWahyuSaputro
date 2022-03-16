# the big number addition
bilangan_pertama = open('bilangan_pertama.txt', 'r')
bilangan_kedua = open('bilangan_kedua.txt', 'r')

# reading from the file
bilangan_pertama = bilangan_pertama.read()
bilangan_kedua = bilangan_kedua.read()

add = (lambda bilangan_pertama, bilangan_kedua: bilangan_pertama + bilangan_kedua)(bilangan_pertama, bilangan_kedua)

# the big number addition
