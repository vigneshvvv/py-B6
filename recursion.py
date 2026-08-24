def sample(num):
    if num == 0:
        return
    num -= 1
    sample(num)
    print(num)


sampleInt = int(input("Enter a number: "))
sample(sampleInt)

