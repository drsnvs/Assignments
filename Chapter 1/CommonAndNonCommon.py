check = input("Enter Number Want to check : ")
number_list = [1,2,3,4,5,6,7,9,10,11,12,13,14,15]

if check.isnumeric():
    if int(check) in number_list:
        print("Yes")
    else:
        print("No")
else:
    print("Enter Only Numeric.")