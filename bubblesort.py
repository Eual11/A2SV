def countSwaps(a):
    
    count=0
    cnst=len(a)
    for i in range(cnst):
    
        for j in range(cnst-1):
        
            if (a[j] > a[j + 1]):
                c = a[j]
                a[j], a[j+1] = a[j+1], c
                count+=1
    print("Array is sorted in " + str(count) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a)-1]))
