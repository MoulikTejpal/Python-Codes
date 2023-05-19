import re
x=input('DD-MM-YYYY: ')   # 1-1-2000 to 31-12-2999
if re.match('(0[1-9]|[12][0-9]|3[01])\-(0[1-9]|1[0-2])\-(2[0-9]{3})',x):  # '|' is or operator
    print('Matched')
else:
    print('Not Matched')