# find_indices.py

def find_indices(arr, target_sum):
    indices = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                indices.append(i)
                indices.append(j)
    return indices

if __name__ == "__main__":
    try:
        # Input array
        arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
        target_sum = int(input("Enter the target sum: "))

        result_indices = find_indices(arr, target_sum)

        if result_indices:
            print(f"Indices of elements that sum to {target_sum}: {result_indices}")
        else:
            print(f"No pairs found that sum to {target_sum}.")
    except ValueError:
        print("Please enter valid integers.")