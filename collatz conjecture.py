#Andres Gerardy
#collatz conjecture
#This is a proram that shows the collatz sequence for any positive integer, as well as the max and average of said sequence.
sequence=[]#i made the list start out as empty and new elements are added every time the while loop_stopper=1 loop runs
y=1
index=0
print("Hi, welcome to Andres' Collatz conjecture program")
learn=input("Would you like learn what collatz conjecture is (yes/no)")
if learn=="yes":
    print("Collatz conjecture is basicaly you pick any positive integer, if its even you divide by 2, if its odd you multiply by 3 and add 1. For all positive integers, this will result in a sequence that will eventually hit 4 and be endlessly caught in the loop 4,2, and 1.")
while y>0:
    num1=int(input("Try it out by entering a number"))
    original_number=num1
    num2=num1
    #If I just put num1 in the final print statement it would always print "1", not the original input.
    loop_stopper=1
    compiler=1
    total=0
    if num1<=0:
        loop_stopper=2
    #Collatz conjecture only works for positive numbers.
    else:
        loop_stopper=1
    while loop_stopper==2:
        print("Please choose a positive number.")
        num1=int(input())
        if num1<=0:
            loop_stopper=2
#if the user continues to enter in  anegative number I want loop stopper 2 be 2 so that it continues to ask them for a positive number
        else:
            loop_stopper=1
            original_number=num1
    #I want the original number to be updated to the new positive number chosen by the user.
    while loop_stopper==1:
    #loop stopper=1 is when the program finds the collatz sequence for the number
        if num1%2==0:
            num1=num1/2
            print(num1)
            compiler+=1
            total+=num1
            sequence.append(num1)
#I want every value num1 takes on to be added to sequence
            if (num1>num2):
                num2=num1
#i want to stre the maximum of the collatz sequence to e stored in the variable num2
            else:num2=num2
        elif num1==1:
            print("The collatz sequence for",original_number,"is",compiler,"numbers long with a max of",num2,"and an mean of",total//compiler)
            def function(sequence, reduction):
                index = 0
                for i in range(int(len(sequence))):
                    index += 1
                    for j in range(int((int(sequence[index])) / reduction)):
                        print("*", end="")
                    print()
            if num2>149 and num2<300 and (total//compiler)<200:
                print("graph of the fuction looks approximately like")
#149 is the maximum characters allowed in a line in IDLE so I wanted to scale the graph down by a scale of 1/10 if the maximum number exceeded the amount of characters allowed per line.
                function(sequence,10)
            elif num2>300 and (total//compiler)<300 :
                print("graph of the fuction looks approximately like")
                function(sequence,20)
# If its  really big number where alot of the elements in sequence are greater than 149, the graph will still not show the fluctiation of numbers unless I scale it down even more.
            elif (total//compiler)>300 and (total//compiler)<500:
                print("graph of the fuction looks approximately like")
                function(sequence,30)
            elif (total//compiler)>=1500:
                print("The sequence is too big to graph.")
#If they chose a very big number, it will take a while to print all the *s and every element of the graph will max out at 149
            else:
                function(sequence,1)
#If the number is small, I don't need to scale it down for the graph to show the fluctation of numbers, thats why I just divide by 1.
            loop_stopper-=1
            do_another=input("Would you like to try another?(yes/no)")
            if do_another!="yes":
                y=0
        else:
            num1=(num1*3)+1
            print(num1)
            compiler+=1
            total+=num1
            sequence.append(num1)
            if (num1>num2):
                 num2=num1
            else:num2=num2
