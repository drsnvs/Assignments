# Create a program name “employee.py” and implement the functions DA, HRA,
# PF, and ITAX. Create another program that uses the function of employee
# module and calculates gross and net salaries of an employee.

import salary as darshan
salary = float(input("Enter Income: "))
da=darshan.DA(salary)
print("After DA:\t",da)
hra=darshan.HRA(salary)
print("After HRA:\t",hra)
pf=darshan.PF(salary)
print("After PF:\t",pf)
itax=darshan.ITAX(salary)
print("After ITAX:\t",itax)
total_cut = da+hra+pf+itax
print("Total cut:\t",total_cut)
net_salary=salary-(total_cut)
print("Your Net Salary is:",net_salary)
