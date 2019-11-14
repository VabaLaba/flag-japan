'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import argparse

n=int(input())
if n%2!= 0:
 raise argparse.ArgumentTypeError('You need use only even numbers! ')
s=12*n#area
length=3*n//2
weight=4*n//2
print('#'*n*4)
for i in range(n*3-2):
#if n==4:
  print ('#' + '  ' *(2*n-2)+ '  ' + '#' )
  for j in range(n*3-2):
      
     print ('#' + '  ' *(2*n-2)+ '  ' + '#' )
##elif n==

print('#'*n*4)
