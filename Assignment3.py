customers = [
"Ahmed", "Sara", "Omar", "Mona",
"Ali", "Nour", "Youssef", "Hana",
"Khaled", "Mariam", "Hassan", "Laila"
] 

scores = [
91, 45, 78, 66, 88, 30,
72, 95, 51, 60, 84, 39
]

#for name,s in zip(customers,scores):
    #print(f"{name} has a score of {s}")

risk_levels=[]

for name, s in zip(customers, scores):
    if 100>= s>= 85:
        risk_levels.append("High")
    elif 84>=s>=60:
        risk_levels.append("Medium")
    elif s<60:
        risk_levels.append("Low")

#print(risk_levels)

num_high=0
num_medium=0
num_low=0
for s in risk_levels:
    if s=="High":
        num_high+=1
    elif s=="Medium":
        num_medium+=1
    else:
        num_low+=1

high_num=scores[0]
high_name=customers[0]
for n,m  in zip(scores,customers):
    if n>=high_num :
        high_num=n
        high_name=m
    else:
        continue

#print(high_name , high_num)

low_num=scores[0]
low_name=customers[0]
for n,m  in zip(scores,customers):
    if n<=low_num :
        low_num=n
        low_name=m
    else:
        continue

#print(low_name , low_num)
print(f"Name  Score  Risk")
print("------------------")
for i,m,j in zip(customers,scores,risk_levels):
    print (f"{i} , {m} , {j}")

#Average Score
average_score=0
for i in scores:
    average_score+=i

average_score=average_score/len(scores)

print ("=============== SUMMARY ================")
print(f"High Risk: {num_high}")
print(f"Medium Risk: {num_medium}")
print(f"Low Risk: {num_low}")
print(f"Average Score: {average_score:.2f}")
print()
print(f"Best Customer: {high_name}({high_num})")
print(f"Worst  Customer: {low_name}({low_num})")

print()
print()
print()

while n:
    print("========== MENU ==========")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("0. Exit")
    print("==========================")
    n=int(input("Enter your choice:"))
    if n==0:
        print("Goodbye!")
        break
    elif n==1:
        s=input("Enter a customer's name: ")
        if s in customers:
                for n , i ,r in zip(customers,scores,risk_levels):
                    if s ==n:
                        print(f"customer's name {n}")
                        print(f"customer's score {i}")
                        print(f"customer's risk {r}")
        else:
            print("Customer not found")


    elif n==2:
        s=input("Enter a customer's name: ")
        if s in customers:
            for n , i ,r in zip(customers,scores,risk_levels):
                if s ==n:
                    print(f"customer's name {n}")
                    print(f"customer's score {i}")
                    print(f"customer's risk {r}")
        else:
            print("Customer not found")

    else:
        print("Invalid choice!")