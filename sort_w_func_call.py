import sys

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

def main():
    arr = [5, 1, 4, 2, 8]
    bubbleSort(arr)
    print(arr)

if __name__ == "__main__":
    sys.exit(main())