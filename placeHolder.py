jump = "something"
for char in jump:
    rtrnString = ""
    if jump.index(char)%2:
        rtrnString =+(char.upper())
    else:
        rtrnString.append(char.lower())
    print(rtrnString)