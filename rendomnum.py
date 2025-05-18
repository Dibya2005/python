import random
low=1
high=10
num=random.randint(low,high) #interger between low and high
print("Random number between",low,"and",high,":",num)
l=random.random() #float between 0 and 1
print("Random float between 0 and 1:",l)
options=["rock","paper","scissors"]
print("Random choice from list:",random.choice(options))
#choice is useful for selecting a random item from a list
#shuffle is useful for shuffling a list
cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
print("Original list:",cards)
random.shuffle(cards) #shuffle the list
print("Shuffled list:",cards)
