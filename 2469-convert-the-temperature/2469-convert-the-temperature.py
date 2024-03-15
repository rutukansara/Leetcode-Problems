class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = [0] *2

        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.8) + 32
        
        ans[0] = kelvin
        ans[1] = fahrenheit

        return ans