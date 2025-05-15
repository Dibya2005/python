#input()= afunction that prompts the user to enter data returns the entered data as a string
name=input("what is your name :")
age=input("how old are you:")
#age= age +1 # type error occur beacause input returns only string
print(f"hello {name}")
print(f"you are {age} years old")
age=int(age)
age+=1
print(f"age will become {age}")
#we could do type cast and input in same line
birthyear=int(input("your birth year is"))
print(f"your birth year is {birthyear}")
