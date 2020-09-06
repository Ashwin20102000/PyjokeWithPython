#importing jokes here
import pyjokes

#print multiple times to get different types of Jokes

print(pyjokes.get_joke())
#Your Code is Successful.
 #Or
import pyjokes
x = int(input())
while 0 < x:
  print(pyjokes.get_joke(),end='\n')
  x-=1
