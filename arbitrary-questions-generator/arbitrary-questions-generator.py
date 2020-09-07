import random

def getInteger(prompt):
	result = int(input(prompt))
	return result

def combine_remove_and_sort(list1, list2):
    return sorted(list(set(list1+list2)))

print("\n")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("++ ARBITRARY QUESTION GENERATOR ++")
print("----------------------------------")
print("\n")

range1 = getInteger("Enter Initial Range: ")
range2 = getInteger("Enter Ending Range: ")
range3 = getInteger("Enter the numbers of expected output: ")

print("________________________\n________________________\n")
#print("________________________\n________________________\n")
#print("________________________\n________________________\n")
#print("________________________\n________________________\n")


range4 = (((range2+1)-range1)/range3)

random_number_list_1 = []

for i in range(0, range3):
    random_number = random.randrange(1, int(range4+1))
    random_number += range4*i
    random_number_list_1.append(int(random_number))


random_number_list_2 = []
random_number_list_3 = []

if random_number_list_1[range3-1] > range2 :
	random_number_list_1[range3-1] = random.randrange((range3-1)*(range4+1), range2+1)

if len(random_number_list_1) < range3:
	range5 = range3 - len(random_number_list_1)
	random_number_list_2 = random.sample(range(range1, range2), range5)
	random_number_list_3 = combine_remove_and_sort(random_number_list_1, random_number_list_2)
	print(random_number_list_3)

else:
	print(random_number_list_1)

print("\n")
