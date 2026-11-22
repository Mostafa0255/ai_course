#Task 1 
num_team=int(input("Enter the Num Of team "))
num_months=int(input("Enter The Num of months the project will take "))
monthly_salary=int(input("Enter The Monthly salary "))
cloud_cost=int(input("Enter The Total cloud cost for the whole project "))

salary_cost=num_team*num_months*monthly_salary
subtotal=salary_cost+cloud_cost
vat=subtotal*0.14
total=subtotal+vat

print(f"Salary cost = {salary_cost:,.2f} , Subtotal = {subtotal:,.2f} , VAT = {vat:,.2f} , Total = {total:,.2f}")

#Task 2

message=input("Enter the customer's message: ")
hours_open=float(input("How many hours has the ticket been open? "))


if "payment" in message:
    Team="Billing"
elif "delivery" in message:
    Team="Logistics"
elif "error" in message :
    Team="Tech"
else:
    Team ="General"

if hours_open >= 24 :
    priority = "HIGH"
else:
    priority = "Low"

print(f"Team: {Team}")
print(f"Priority: {priority}")