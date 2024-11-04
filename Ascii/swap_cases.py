#swap
#upper->lower
#lower->upper
def char_change(my_string:str):
    result=""
    for ch in my_string:
        ascii_code = ord(ch)
        if ascii_code >=ord("a") and ascii_code <=ord("z"):
            ascii_code -=32
            result =result+chr(ascii_code)
        elif ascii_code >=ord('A') and ascii_code <=('Z'):
            ascii_code+=32
            result =result +chr(ascii_code)
        else:
            result =result + chr
    print(result)
    
my_string=input("enter your string :")
char_change(my_string)