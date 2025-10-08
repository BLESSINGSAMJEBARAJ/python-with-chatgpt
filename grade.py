A=int(input("Enter Tamil mark:"))
B=int(input("Enter Emglish Mark:"))
C=int(input("Enter Maths Mark:"))
D=int(input("Enter Science Mark:"))
E=int(input("Enter Social Mark:"))


total=A+B+C+D+E
average=(A+B+C+D+E)/5

print("\n ------YOUR RESULT------")

print("\nTOTAL MARKS:",total)
print("\nAVERAGE:",average)


if(average>=90):
    print("\nYOUR GRADE:A+")
elif(average>=80):
        print("\nYOUR GRADE:A")
elif(average>=70):
     print("\nYOUR GRADE:B")
elif(average>=60):
    print("\nYOUR GRADE:C")
elif(average>=50):
    print("\nYOUR GRADE:D") 
else:
    print("\nFAIL")


    
