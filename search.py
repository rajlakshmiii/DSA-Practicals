def linear_search(customer_list, target_id):
    for i in range(len(customer_list)):
        if customer_list[i] == target_id:
            return i
    return -1


def binary_search(sorted_list, target_id):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target_id:
            return mid
        elif sorted_list[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return -1

customer_list = [105, 203, 307, 412, 518, 625, 731]

target_id = int(input("Enter Customer Account ID to search: "))

# Linear Search
linear_result = linear_search(customer_list, target_id)

if linear_result != -1:
    print("Linear Search: Customer ID found at index", linear_result)
else:
    print("Linear Search: Customer ID not found")


# Binary Search
sorted_list = sorted(customer_list)
binary_result = binary_search(sorted_list, target_id)

if binary_result != -1:
    print("Binary Search: Customer ID found at index", binary_result)
else:
    print("Binary Search: Customer ID not found") 