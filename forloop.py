#execute a block of code a fixed number of time
#we can iterat over a rasnge string,sequence
# while loop is useful if you wnt to iterate something posiibly infinite example user input
for x in range(1, 11):
  print(x)
#to count backwards we can use reverse function
for x in reversed(range(1,11)):
  print(x)
for x in range(1, 11,2): #it will count at 2 2 gap between each

  print(x)
credit_card="2222-3456-1239-2978"
for x in credit_card:
  print(x)
for x in range(1,23):
  if x==13:
    continue #continue e skip kora major num ata
  else:
    print(x)
for x in range(1,23):
  if x==13:
    break #braek out of the loop intirely
  else:
    print(x)