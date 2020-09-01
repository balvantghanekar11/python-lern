#tut44 enumerate function

list=["bhindi","Aloo","chopsticks","chowmein"]
i=1
for item in list:
    if i%2 is not 0:
        print(f"Jarvis please buy{item}")
    i+=1

for index,item in enumerate(list):
    if i%2==0:
        print(f"Jarvis please buy{item}")
   
#tut45 import work
import sklearn as sk
print(sk.__version__)

import sys
print(sys.path)

from sklearn.ensemble import RandomForestClassifier
#class used for machine learning 
print(RandomForestClassifier())

import myfile2
print(myfile2.a)

myfile2.myfun("this is blu")