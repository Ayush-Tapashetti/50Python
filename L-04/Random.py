import random
"""1"""
l=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(l))

"""2"""
random.shuffle(l)
print(l)

"""3"""
print(random.randint(0,100))

"""4"""
coin = random.choice(["heads", "tails"])
print(coin)