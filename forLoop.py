for i in range(1,5):
    print(i)

for i in range(1, 9, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)


numbers = [122,123,124,125,126,127,128]

for i in range(len(numbers)):
    print(numbers[i])

for i in numbers:
    # print(i)
    if i == 123:
        print("number exist")
        # break
        continue

    print(i)


for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])