def mapped():
    string_original = 'abcdefghijklmnopqrstuvwxyz'
    string_list = list(string_original)
    string_mapped = list(range(1, 27))
    reverse = string_mapped[::-1]
    string_dict = dict(zip(string_list, reverse))
    return string_dict

def inputMap(password, string_dict):
    password_list = list(password)
    password_mapped = []
    for i in range(len(password_list)):
        password_mapped.append(string_dict[password_list[i]])
    
    temp_password = []
    for i in range(len(password_mapped)):
        temp_password.append(chr(password_mapped[i] + 90))
        temp_password.append(chr(abs(password_mapped[i] - 100)))

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

password = input("Masukkan password (maksimal 100 karakter): ")
print(inputMap(password, mapped()))