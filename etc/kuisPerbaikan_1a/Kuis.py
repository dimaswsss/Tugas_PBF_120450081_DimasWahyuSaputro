# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 04 March 2022
# Program Description : Program to solve simple encryption password problem

# simple password encryption
password = input("Masukkan password (maksimal 100 karakter): ")
if len(password) > 100:
    print("Password terlalu panjang, masukkan password yang lebih pendek")
    password = input("Masukkan password (maksimal 100 karakter): ")
else:
    pass

# convert string to list
password_list = list(password)
password_list_ord = [ord(x) for x in password_list]
print(password_list)
print(password_list_ord)

temp_password = []
a = [] # menyimpan hasil bagi
b = [] # menyimpan hasil sisa
for i in range(len(password_list_ord)):
    val1 = (password_list_ord[i] // 26 + 80)
    temp_password.append(chr((password_list_ord[i] // 26 + 80)))
    temp_password.append(chr((password_list_ord[i] % 26 + 80)))
    if i == 0:
        if temp_password[i] >= temp_password[i+1]:
            temp_password.append('-')
        else:
            temp_password.append('+')
    else:
        m, n = 3, i
        if temp_password[m*n] > temp_password[m*n+1]:
            temp_password.append('-')
        else:
            temp_password.append('+')     

# create dictionary for save result
temp = {}
temp = {'a':temp_password[0:len(temp_password)//2], 'b':temp_password[len(temp_password)//2:len(temp_password)]}


# convert list to string
password_final = ''.join(temp_password)
print(password_final)

# check ord password final
password_final_ord = [ord(x) for x in password_final]
print(password_final_ord)