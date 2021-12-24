class Solution: 
    def select(self, arr, i):
        for k in range(len(arr)):
            if arr[k] < arr[i]:
                arr[k], arr[i]=arr[i],arr[k]
    def selectionSort(self, arr,n):
        for j in range(n):
            mini = j

            for i in range(j + 1, n):
    
                if arr[i] < arr[mini]:
                    mini = i
    
            (arr[j], arr[mini]) = (arr[mini], arr[j])
