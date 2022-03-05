# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 04 March 2022
# Program Description : Program to solve simple encryption password problem

def enc(password):
    password_list = list(password)
    temp_password = []
    for i in range(len(password_list)):
        temp_password.append(chr(((ord(password_list[i]))//26) + 80))
        temp_password.append(chr(((ord(password_list[i]))%26) + 80))
        if temp_password[i] >= temp_password[i+1]:
            temp_password.append('-')
        else:
            temp_password.append('+')
    password_final = ''.join(temp_password)
    return password_final    

def dec(password):
    # convert string to list
    password_list = list(password)
    splitpass = [password_list[i:i+3] for i in range(0, len(password_list), 3)]
    temp_password = []
    for word in splitpass:
        a = ord(word[0]) - 80
        b = ord(word[1]) - 80
        desc = a * 26 + b
        temp_password.append(chr(desc))
    decrypt_final = ''.join(temp_password)
    return decrypt_final