# author : Dimas Wahyu Saputro
# NIM : 120450081
# Affiliation : Sains Data ITERA
# Date : 04 March 2022
# Program Description : Program to solve simple encryption password problem

def checkLen(password):
    if len(password) > 100 or len(password) <= 0:
        return False
    else:
        return True

def mapped(password):
    string_original = 'abcdefghijklmnopqrstuvwxyz'
    string_list = list(string_original)
    string_mapped = list(range(1, 27))
    reverse = string_mapped[::-1]
    string_dict = dict(zip(string_list, reverse))

    # map from input to mapped
    password_list = list(password)
    password_mapped = []
    for i in range(len(password_list)):
        password_mapped.append(string_dict[password_list[i]])

    # transform
    temp_password = []
    for i in range(len(password_mapped)):
        temp_password.append(chr(password_mapped[i] + 90))
        temp_password.append(chr(abs(password_mapped[i] - 100)))
    return temp_password

def change(temp_password):
    temp_password_len = len(temp_password)
    mid = len(temp_password) // 2
    x1 = list(temp_password[:mid])
    x2 = list(temp_password[mid:temp_password_len])

    if mid % 2 == 0:
        midd = mid
    else:
        midd = mid - 1

    for i in range(0, midd, 2):
        temp = x1[i]
        x1[i] = x1[i+1]
        x1[i+1] = temp

        temp2 = x2[i]
        x2[i] = x2[i+1]
        x2[i+1] = temp2
    
    return ''.join(x2 + x1)

def enkrip(password):
    return change(mapped(password))

# decryption
def dec(password):
    tukarKembali = change(password)
    temp_password = []
    for i in range(0, len(password), 2):
        temp_password.append((ord(tukarKembali[i]) - 90))
    return temp_password

def convertMaptoOriginal(temp_password):
    string_mapped = list(range(1, 27))
    string_original = 'abcdefghijklmnopqrstuvwxyz'
    string_list = list(string_original)
    reverse = string_mapped[::-1]
    string_dict = dict(zip(reverse, string_list))

    password_original = []
    for i in range(len(temp_password)):
        password_original.append(string_dict[temp_password[i]])
    return ''.join(password_original)

def dekrip(password):
    return convertMaptoOriginal(dec(password))