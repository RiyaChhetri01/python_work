def count_char(user_string :str):
    alphabets=0
    digit=0
    spaces=0
    symbols=0
    for ch in user_string:
        ascii_code =ord(ch)
        if 97<= ascii_code <=122 or  65<=ascii_code<=90:
            alphabets += 1
        elif ascii_code >=48 and ascii_code<=57:
            digit += 1
        elif ascii_code == 32:
            spaces+=1
        else:
            symbols+=1
        print(f"Alphabets={alphabets},digits ={digit},spaces={spaces},symmbols={symbols}")

user_string="hgj"
count_char(user_string)
