class Function:

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        args = arg1 +arg2  
        self.args = args    
        print "sum is {} + {} = {}". format(self.arg1, self.arg2, self.args)
       
    
    def next_function(self):
        num1 = 4
        num2 = 2
        sum = num1 - num2
        return sum


    def other_function(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        sum = num1 - num2
        return sum    

    

func1 = Function(5,1)

print func1.next_function()
print func1.other_function(2, 2)