# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    n = len(dataset)
    for i in range(len(dataset)):
        for j in range(i, n - 1):
            if dataset[i+1] < dataset[i]:
                temp = dataset[i+1]
                dataset[i+1] = dataset[i]
                dataset[i] = temp
        print("Current state: ", dataset)


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
