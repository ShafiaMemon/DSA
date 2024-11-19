def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore the right half
        else:
            high = mid - 1

    return -1  # Element not found

# Example usage
if __name__ == "__main__":
    arr = [10, 12, 34, 40, 98, 60, 73, 80]
    target = int(input("Enter the number to search: "))

    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
