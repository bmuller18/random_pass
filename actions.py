import random

#Letters and number to change in pass
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#transform str to int
quantity = input("How long should the password be?")

#If the input entry is not a number work with the error
try:
    quantityint = int(quantity)
except:
    print("Your entry is not a number")


newpass = ""
for aux in range(quantityint):
    ran = random.randint(0, (len(upper_case)-1))
    newpass += "".join(upper_case[ran])
print(newpass)