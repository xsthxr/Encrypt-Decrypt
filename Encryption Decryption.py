def dessubtable(sixbit):
    row = sixbit[0] + sixbit[-1]
    col = sixbit[1:-1]

    row_dec = int(row,2)
    col_dec = int(col,2)

    print("Row:",row_dec)
    print("Column:",col_dec)

    table_result = int(input("Put the result, based on table: "))
    table_result_bin = bin(table_result)[2:].zfill(4)

    print("4-bit output: ", table_result_bin)

def vernamDecryption(ciphertext,key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = alpha.lower()

    #Extend key to match len of ciphertext
    if len(key) < len(ciphertext):
        difference = len(ciphertext) - len(key)
        key += key[0:difference]

    decrypted = []
    ciphertext_nums = []
    key_nums = []

    #Find the alphabetical position of each letter of both ciphertext and key
    #Find the difference of the alphabetical position of the ciphertext and key, then % 26
    #Append the result_letter to decrypted
    for index,letter in enumerate(key):
        numInAlpha = alpha.index(letter) #convert letter to num
        key_nums.append(numInAlpha)
        letterInCipher = ciphertext[index]
        numInCipher = alpha.index(letterInCipher)
        ciphertext_nums.append(numInCipher)
        result_num = ((int(numInCipher) - int(numInAlpha))%26)
        result_letter = alpha[result_num]
        decrypted.append(result_letter)

    decrypted = "".join(decrypted)
    print(ciphertext)
    print("cipher numeric:", ciphertext_nums)
    print(key)
    print("key numeric:",key_nums)
    return decrypted

def columnartranspositionDecryption(ciphertext,key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = alpha.lower()
    key_list = []

    for letter in key:
        key_list.append(letter)

    sorted_key = sorted(key)
    key_alpha_pos = []
    key_alpha_pos_str = []

    for letter in key:
        key_num = sorted_key.index(letter) #letter's position in sorted.key
        sorted_key[key_num] = ""
        key_alpha_pos.append(key_num+1)

    print(key_list)


    for num in key_alpha_pos:
        key_alpha_pos_str.append(str(num))

    print("Key numeric: ")
    print(key_alpha_pos_str)
    print()

    rows_w_ele = len(ciphertext)//len(key)
    lastrow_w_ele = len(ciphertext)%len(key)
    empty_lastrow = [""]*lastrow_w_ele
    grid = []
    for i in range(rows_w_ele):
        empty_row = [""] * len(key)
        grid.append(empty_row)
    grid.append(empty_lastrow)

    row = 0
    col_num = 1
    for letter in ciphertext:
        col = key_alpha_pos.index(col_num)
        if row == len(grid)-1:
            if col >= len(grid[row]):
                row = 0
                col_num += 1
                col = key_alpha_pos.index(col_num)
        grid[row][col] = letter #add letter to grid
        row += 1
        if row == len(grid):
            row = 0
            col_num += 1

    for row in grid:
        print(row)

    result = ""
    for i in grid:
        row_result = ""
        for j in i:
            row_result += j
        result += row_result

    return result

def ceasarcipherDecryption(ciphertext,key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = alpha.lower()

    result = ""
    cipher_numeric = []
    shifted_numeric = []

    for letter in ciphertext:
        numInAlpha = int(alpha.index(letter))
        cipher_numeric.append(numInAlpha)
        shifted_index = (numInAlpha - int(key))%26
        shifted_numeric.append(shifted_index)
        shifted_letter = alpha[shifted_index]
        result += shifted_letter

    print("cipher_numeric: ",cipher_numeric)
    print(f"-{key} shift numeric: ",shifted_numeric)
    return result

def vernamEncryption(plaintext, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = alpha.lower()

    # Extend key to match len of ciphertext
    if len(key) < len(plaintext):
        difference = len(plaintext) - len(key)
        key += key[0:difference]

    encrypted = []
    plaintext_nums = []
    key_nums = []

    # Find the alphabetical position of each letter of both ciphertext and key
    # Find the difference of the alphabetical position of the ciphertext and key, then % 26
    # Append the result_letter to decrypted
    for index, letter in enumerate(key):
        numInAlpha = alpha.index(letter)  # convert letter to num
        key_nums.append(numInAlpha)
        letterInCipher = plaintext[index]
        numInCipher = alpha.index(letterInCipher)
        plaintext_nums.append(numInCipher)
        result_num = ((int(numInCipher) + int(numInAlpha)) % 26)
        result_letter = alpha[result_num]
        encrypted.append(result_letter)

    encrypted = "".join(encrypted)
    print(plaintext)
    print("plaintext numeric:", plaintext_nums)
    print(key)
    print("key numeric:", key_nums)
    return encrypted

def columnartranspositionEncryption(plaintext, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = alpha.lower()
    key_list = []

    for letter in key:
        key_list.append(letter)

    sorted_key = sorted(key)
    key_alpha_pos = []
    key_alpha_pos_str = []

    for letter in key:
        key_num = sorted_key.index(letter)  # letter's position in sorted.key
        sorted_key[key_num] = ""
        key_alpha_pos.append(key_num + 1)

    print(key_list)

    for num in key_alpha_pos:
        key_alpha_pos_str.append(str(num))

    print("Key numeric: ")
    print(key_alpha_pos_str)
    print()

    #grid
    rows_w_ele = len(plaintext) // len(key)
    lastrow_w_ele = len(plaintext) % len(key)
    empty_lastrow = [""] * lastrow_w_ele
    grid = []
    for i in range(rows_w_ele):
        empty_row = [""] * len(key)
        grid.append(empty_row)
    grid.append(empty_lastrow)

    #row & column
    index = 0
    for r_index,row in enumerate(grid):
        for c_index, col in enumerate(row):
            grid[r_index][c_index] = plaintext[index]
            index += 1

    for row in grid:
        print(row)

    result = ""
    col = 1
    for i in range(len(key_alpha_pos)):
        col_index = key_alpha_pos.index(col)
        for row in grid:
            if col_index < len(row):
                result += row[col_index]
        col += 1

    return result

def ceasarcipherEncryption(plaintext,key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = alpha.lower()

    result = ""
    plaintext_numeric = []
    shifted_numeric = []

    for letter in plaintext:
        numInAlpha = int(alpha.index(letter))
        plaintext_numeric.append(numInAlpha)
        shifted_index = (numInAlpha + int(key)) % 26
        shifted_numeric.append(shifted_index)
        shifted_letter = alpha[shifted_index]
        result += shifted_letter

    print("plaintext_numeric: ", plaintext_numeric)
    print(f"+{key} shift numeric: ", shifted_numeric)
    return result


def main():
    print("""0. Quit
1. DES Substitution Table (S-Box1)
Decryption: 2. Vernam Decryption, 3. Columnar Transposition Decryption, 4. Caesar Cipher Decryption
Encryption: 5. Vernam Encryption 6. Columnar Transposition Encryption 7. Caesar Cipher Encryption """)
    while True:
        choice = int(input("Enter choice: "))
        if choice == 0:
            break
        if choice == 1:
            sixbit = input("Enter 1st block of 6-bit: ")
            des_sub = dessubtable(sixbit)
            continue
        if choice == 2 or choice == 3 or choice == 4:
            ciphertext = input("Enter ciphertext: ").lower()
            key = input("Enter key: ").lower()
            if choice == 2:
                vernam = vernamDecryption(ciphertext,key)
                print("Plaintext: ",vernam)
            elif choice == 3:
                columnar = columnartranspositionDecryption(ciphertext,key)
                print("Plaintext: ",columnar)
            elif choice == 4:
                caesar = ceasarcipherDecryption(ciphertext,key)
                print("Plaintext: ",caesar)
        else:
            plaintext = input("Enter plaintext: ").lower()
            key_encrypt = input("Enter key: ").lower()
            if choice == 5:
                vernam_encrypt = vernamEncryption(plaintext, key_encrypt)
                print("Ciphertext: ",vernam_encrypt)
            elif choice == 6:
                columnar_encrypt = columnartranspositionEncryption(plaintext, key_encrypt)
                print("Ciphertext: ",columnar_encrypt)
            elif choice == 7:
                caesarencrypt = ceasarcipherEncryption(plaintext,key_encrypt)
                print("Ciphertext: ",caesarencrypt)
main()
