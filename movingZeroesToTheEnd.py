# Moving Zeros to the End
def exercise(input):
    for i in input:
        if i == 0:
            input.remove(i)
            input.append(i)
            
    print(input)
exercise([0, 1, 0, 3, 12])