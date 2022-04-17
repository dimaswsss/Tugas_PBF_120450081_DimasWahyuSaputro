# the big number addition
bilangan_pertama = open('bilangan_pertama.txt').read()
bilangan_kedua = open('bilangan_kedua.txt').read()

print((lambda x,y: int(x) + int(y))(bilangan_pertama, bilangan_kedua))
