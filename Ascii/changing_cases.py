def changing_cases(my_string:str):
    result=""
    for ch in my_string:
        ascii_code=ord(ch)
        if ord(ch)>=ord("a")and ord(ch)<=ord("z"):
            ascii_code -=32
            result += chr(ascii_code)
        else:
            result = result+ch
    print(result)

my_string=input("enter ")
changing_cases(my_string)


