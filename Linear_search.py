def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 12, 34, 40, 98, 60, 73, 80]
    target = int(input("Enter the number to search: "))
    
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
