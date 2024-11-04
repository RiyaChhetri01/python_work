#removing all the symbols ,spaces and digits from a string
def removing_from_string(my_string:str):
    result=""
    for ch in my_string:
        if "a"<= ch <= "z":
            result +=ch
    print(result)

my_string=input("enter :")
removing_from_string(my_string)