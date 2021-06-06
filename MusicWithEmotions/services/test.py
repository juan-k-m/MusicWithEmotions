import random
scale = ["C", "D", "E", "F", "G", "A", "B"]
random_list = []
random_list2 = []
for i in range(5):
    r=random.randint(0,len(scale)-1)
    random_list.append(r)
for i in range(5):
    r=random.randint(2,6)
    random_list2.append(r)

print(random_list2)