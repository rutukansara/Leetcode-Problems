class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            result.append(i)
        for number in range(len(result)):
            if result[number] %3==0 and result[number]%5 == 0:
                result[number] = "FizzBuzz"
            elif  result[number] %3 == 0:
                result[number] = "Fizz"
            elif result[number] %5 == 0:
                result[number] = "Buzz"
            else:
                result[number] = str(result[number])
        
        return result