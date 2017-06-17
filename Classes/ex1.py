class RomanNumeral():
    def convert(self, num):
       val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
       syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
       roman_num = ''
       i = 0
       while  num > 0:
           for _ in range(num // val[i]):
               roman_num += syb[i]
               num -= val[i]
           i += 1
       return roman_num
        
rob1 = RomanNumeral()
print rob1.convert(5)
print RomanNumeral().convert(50)
