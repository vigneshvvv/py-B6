size = 0

def reverse(index, sample):
    global size
    if len(sample) == index:
        return

    temp = sample[index]
    index += 1
    reverse(index, sample)
    sample[size] = temp
    size += 1

nums = [10,20,30,40,50]
reverse(0, nums)
print(nums)

    