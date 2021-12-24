class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numlist=[i for i in range(1,n+1)]
        for num in numlist:
            c=numlist.index(num)
            if num%15==0:
                numlist[c]='FizzBuzz'
            elif num%3==0:
                numlist[c]='Fizz'
            elif num%5==0:
                numlist[c]='Buzz'
            else:
                numlist[c]=str(num)
        return numlist
