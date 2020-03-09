
## Main description goes here

import math

line = int(input())
while line:
    if line:
        ans = math.sqrt(line)
        cont = line % ans
        if cont: print('no')
        else: print('yes')
    try: line = int(input())
    except: line = ''
