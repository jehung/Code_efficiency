#!/bin/python3

## A string contains many patterns of the form 1(0+)1 where (0+) represents any non-empty consecutive sequence of 0's. The patterns are allowed to overlap.
## Write code to return the total number of substrings fitting the above pattern.


import sys
import import regex as re

def patternCount(string):   
    '''
    counter = 0
  
    try:
        start = s.index('10')
            
        for i in range(start+2, len(s)):
            end = s[i]
            if end == '0':
                new = s[start:i+1]
            elif end == '1':
                new = s[start:i+1]
                if new.isdigit():
                    counter += 1
                start = i
            else:
                new = s[start:i]

        return counter

    except:
        return 0
    '''
    
    #return (re.findall('(1(0+)1)', string))
    m = (re.findall('(?=([1][0]{1,2000}[1]))', string))
    return len(m)    
    
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
