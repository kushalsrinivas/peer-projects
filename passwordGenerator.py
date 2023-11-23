import random
ltrs = "1234567890()-=qwertyuiop[]]{}asdfghjkl;':zxcvbnm,.<>/?"
length = int(input("enter the length of the password : "))
pwd = [random.choice(ltrs) for ltr in range(length)]
pwd = "".join(pwd)
print(f"your password is {pwd}")