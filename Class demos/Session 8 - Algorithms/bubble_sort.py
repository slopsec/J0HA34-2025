'''
Bubble sort

How it works:

- Go through the array, one value at a time.
- For each value, compare the value with the next value.
- If the value is higher than the next one, swap the values so that 
  the highest value comes last.
- Go through the array as many times as there are values in the array.

'''

def bubble_sort(some_list):
    # Go through array as many times as values
    # Outer loop
    for i in range(len(some_list) - 1):
        # Inner loop -> swaps
        is_sorted = True
        for j in range(len(some_list) - i - 1):
            # compare element with next
            # if greater swap
            if some_list[j] > some_list[j+1]:
                # swap
                some_list[j], some_list[j+1] = some_list[j+1], some_list[j]
                is_sorted = False
        if sorted:
            break


def main():
    test_data = [5, 25, 13, 20, 53, 17, 12, 47, 29, 10]

    bubble_sort(test_data)
    print(test_data)

if __name__ == "__main__":
    main()
