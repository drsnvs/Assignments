# Create a program name “employee.py” and implement the functions DA(dearness allowance), HRA(house rent allowance), PF(profident fund), and ITAX(income tax). Create another program that uses the function of employee module and calculates gross and net salaries of an employee.

def DA(salary):
    da = salary*0.01
    da_final = salary-da
    # return da_final
    return da

def HRA(salary):
    hra = salary*0.025
    hra_final = salary-hra
    # return hra_final
    return hra

def PF(salary):
    pf = salary*0.02
    pf_final = salary - pf
    # return pf_final
    return pf

def ITAX(salary):
    if salary>0 and salary<10000:
        itax = salary*0.01
    elif salary>=10000 and salary<25000:
        itax = salary*0.02
    elif salary>=25000 and salary<50000:
        itax = salary*0.03
    else:
        itax = salary*0.05
    itax_final = salary-itax
    # return itax_final
    return itax


# salary = float(input("Enter Income: "))
# da=DA(salary)
# print("After DA:\t",da)
# hra=HRA(salary)
# print("After HRA:\t",hra)
# pf=PF(salary)
# print("After PF:\t",pf)
# itax=ITAX(salary)
# print("After ITAX:\t",itax)
# total_cut = da+hra+pf+itax
# print("Total cut:\t",total_cut)
# net_salary=salary-(total_cut)
# print("Your Net Salary is:",net_salary)