import pandas as pd      #In this part of the program All the required librarys are imported 
import itertools
from itertools import combinations
from itertools import chain
import os
import time
df=pd.read_csv(r"F://Dataset/Dataset2.csv",header=None) #Storting the Data from CSV file into Dataframe DF

df #heres how our Dataframe looks like
No_Trans=int(input("Enter the number of transactions in the database"))
print('')
Max=int(input("Enter the number of maximum items in one transaction "))
print('')
min_sup=float(input("Enter the minimum suppourt (do not include the percent sign %)"))
print('')
min_sup=(min_sup/100)*No_Trans#Taking the value of minimum support and confidence from user
conf=float(input("Enter the minimum confidence (do not include the percent sign %)"))
print('')
conf=conf/100
l=[]                      #Storing all the transaction in a nested list 
for i in range(No_Trans):
    l.append([str(df.values[i,j])for j in range(0,Max)])
print("These are the input Transactions")
print('')
print(l)
#This part of the program creates the list which contain all the itmes which are in input transaction     
items=list(set(chain(*l)))
items.remove('nan')
#print(items)
l1=[]       #Calculating L1 That is taking all the element who's minimum suppourt is greater than minimum given by thre user.
count=0
for j in range(len(items)) :
    count=0
    for i in range(len(l)):
        x=items[j]
        if x in l[i]:
            count=count+1
    if count>=min_sup:
        l1.append(items[j])
print('')        
#print(l1)
def count_1(p1): #This function gives the value of the perticluar itemset is present how many times in the actual transactions
    p1=list(p1)
    counter=0
    for i in range(len(l)):
        t1=l[i]
        if set(p1).issubset(set(t1)):
            counter=counter+1
    return(counter) 
F=[]                                        #This is the Brute-Force algorithm  
start=time.time()
print('')
print('List of all frequent itemsets by Brute Force')
print('')                                   #This part of the program calculates the L1,L2,L3... according to input
for i in range(1,len(l[0])+1):              #And gives the Assosiation rules 
    k=list(combinations(items,i))
    F1=[]
    for j in range(len(k)):
        count=0
        for m in range(len(l)):
            if set(k[j]).issubset(set(l[m])):
                count=count+1
        if count>=min_sup:
            F1.append(k[j])
    F.append(F1)
    print(F1)
    print('')
    
end=time.time()
print("Assosiation Rules are")
print('')
for o in range(len(F)):
    for g in range(len(F[o])):
        s=F[o][g]
        g1=[]
        for i in range(1,len(s)):
            g1=list(combinations(s,i))
            for j in range(len(g1)):
                x1=list(g1[j])
                y1=list(set(s)^set(x1))
                confi=count_1(list(s))/count_1(list(x1))
                if confi>=conf:
                    print(x1,'--->',y1)
                    print('confidence=',confi)
                    print('')
BruteTime=end-start
print('Total Time Taken By Brute-Force is')
print(end-start)
print('')
print('')
start=time.time()                 #This is the Apriori algorithm
F=[]                              #This part of the program calculates the L1,L2,L3... according to input
F1=[]                             
l1=[]
count=0
print('Frequent itemset in L1,L2,L3.... By Apriori are')
for j in range(len(items)) :
    count=0
    for i in range(len(l)):
        x=items[j]
        if x in l[i]:
            count=count+1
    if count>=min_sup:
        l1.append(items[j])
F.append(l1)
print(l1)
print('')
print('')
H=list(combinations(l1,2))
for i in range(3,len(l[0])+1):
    a=[]
    for j in range(len(H)):
        count=0
        for k in range(len(l)):
            x=H[j]
            y=set(l[k])
            if set(x).issubset(y):
                count=count+1
        if count>=min_sup:
            a.append(H[j])
    F.append(a)

    print(a)
    print('')
    print('')
    b=list(set(chain(*a)))
    H=list(combinations(b,i))
    F1.append(a)
print("Assosiation Rules are")    
for o in range(len(F1)):                         #This part gives the Assosiation rules
    for g in range(len(F1[o])):
        s=F1[o][g]
        g1=[]
        for i in range(1,len(s)):
            g1=list(combinations(s,i))
            for j in range(len(g1)):
                x1=list(g1[j])
                y1=list(set(s)^set(x1))
                confi=count_1(list(s))/count_1(list(x1))
                if confi>=conf:
                    print(x1,'--->',y1)
                    print('confidence=',confi)
                    print('')
end=time.time()
AprioriTime=end-start
print('Total time take by Apriori is')
print(end-start)    
print('')    
print('For this Dataset while the value of mimum suppourt is ',min_sup,' and minimum confidence is ',conf,'the time taken to')
print('to calculate the Frequent itemset and al the assosication rules by Brute Force is ', BruteTime,' and by')
print('Apriori is ',AprioriTime)
if BruteTime>AprioriTime:
    print('In this case Apriori is ',(BruteTime/AprioriTime),' Time faster than Brute-Force')
    
    	
