def askhchars()->str:
    my_string= ""
    while True:
        char = input("enter a char=")
        if char == "q" or char =="Q":
            break
        my_string +=char

    return my_string
           

askhchars()