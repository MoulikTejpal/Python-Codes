pan=input()
if len(pan)==10 and pan[:5].isalpha() and pan[5:9].isdigit() and pan[9:].isalpha():
    if pan[:5].isupper() and pan[9:].isupper:
        print('Valid')
    else:
        print('Invalid')
else:
    print('Invalid')