# continue
# break
# pass
# print 1 to 10
for item in range(0, 10):  # [1,2,3,4,5,6,7,8,9,10]
    item += 1
    if item == 1:
        pass  # Do nothing for item 1
    if item == 3:
        continue  # skip the interation when item is 5
    # Exit the loop when item is 5
    if item == 5:
        pass

    if item == 7:
        continue

    if item == 9:
        break
    print(item, end=",")
