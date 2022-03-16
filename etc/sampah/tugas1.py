# simple password encryption
password = input("Masukkan password (maksimal 100 karakter): ")
if len(password) > 100:
    print("Password terlalu panjang, masukkan password yang lebih pendek")
    password = input("Masukkan password (maksimal 100 karakter): ")
else:
    pass

# convert string to list
password_list = list(password)
print(password_list)
password_list1 = password_list[::3]
print(password_list1)
password_list2 = password_list[1::3]
print(password_list2)
password_list3 = password_list[2::3]
print(password_list3)

# value 1
temp_password1 = []
for i in range(len(password_list1)):
    temp_password1.append(chr(((ord(password_list1[i]))//26) + 80))

# value 2
temp_password2 = []
for i in range(len(password_list2)):
    temp_password2.append(chr((ord(password_list2[i]))%26 + 80))

# value 3
temp_password3 = []
for i in range(len(password_list3)):
    if temp_password1[i] > temp_password2[i]:
        temp_password3.append('+')
    else:
        temp_password3.append('-')

print(temp_password1)
print(temp_password2)
print(temp_password3)

# merge value 1, 2, 3
temp_password_final = []
for i in range(len(password_list)):
    if i%3 == 0:
        temp_password_final.append(temp_password1[i//3])
    elif i%3 == 1:
        temp_password_final.append(temp_password2[i//3])
    else:
        temp_password_final.append(temp_password3[i//3])

# convert list to string
password_final = ''.join(temp_password_final)
print(password_final)