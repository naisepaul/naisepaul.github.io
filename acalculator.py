# 10345047  Naise Paul  
#########################

from math import sin,cos,factorial,sqrt
import os 
    
class Calculator(object):

    def add(self,x,y):
        number_types = (int, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
             raise ValueError
    
    def subtract(self,x,y):
        number_types = (int, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError 
  
    def divide(self, x, y):
        number_types = (int, float)
        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'NaN'
            else :    
                return x / float(y)
        else:
            raise ValueError

    def multiply(self, x, y):
        number_types = (int, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError  
    
    def exponent(self, x, y):
        number_types = (int, float)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError   
            
    def squareroot(self, x):
        number_types = (int, float)
 
        if isinstance(x, number_types): 
            return sqrt(x)
        else:
            raise ValueError
      
    def square(self, x):
        number_types = (int, float)
 
        if isinstance(x, number_types): 
            return x * x
        else:
            raise ValueError   
                             
    def sin(self, x):
        number_types = (int, float)
 
        if isinstance(x, number_types): 
            return sin(x)
        else:
            raise ValueError        
            
    def cos(self, x):
        number_types = (int, float)
 
        if isinstance(x, number_types): 
            # x=degrees(x)
            return cos(x)
        else:
            raise ValueError
            
    def factorial(self,n):
        number_types = int
        if n == 0:
            return 1
        if n < 0:
            return None
        if n>0  :
            return factorial(n)
        else:
            raise ValueError  
       
               
if __name__ == '__main__':    

    calc=Calculator()
       
    def output():
            
        print '''\t\t  Main  Calculator Functios
        
        1. Press 1 for Add
        2. Press 2 for subtract
        3. Press 3 for Divide
        4. Press 4 for Multiplication
        5. Press 5 for Exponent
        6. Press 6 for Squareroot
        7. Press 7 for Square
        8. Press 8 for Sin of radians
        9. Press 9 for Cos of radians
        10.Press 10 for Factorial 
		
        Press 'Q' to Exit '''
    
    def select1(num1,num2):
        while True:        
            numb1 = raw_input("Enter first number  : ")
            try :
                num1=float(numb1)                    
            except:
                print "Enter numerical Value"
                continue
              
            numb2 = raw_input("Enter second number  : ")
            try:
                num2= float(numb2)
            except:
                print "Enter numerical Value"
                continue
            return num1, num2    
        
    def select2(num):
        while True:        
            numb = raw_input("Enter the number  : ")
            try :
                num=float(numb)                    
            except:
                print "Enter numerical Value"
                continue
            return num    
    
    while True:       
        os.system('cls')  # cleaning the screen
        output() 
        choice = raw_input("Enter choice(1/2/3/4.../10):") 
        if choice.lower()=='q':
            break
        try:
            choice = int(choice)            
        except:
            print "Please Enter Correct Value"
            continue 
        if choice<1 or choice>10 :
            print "Please Enter The Value Between 1 and 10"	
        if choice == 1:                       
            num1,num2 = select1(1,2)  
            print "sum is equal to ", calc.add(num1,num2)            
            raw_input("press any key") 
        
        if choice == 2:           
            num1,num2 = select1(1,2)   #  giving two dummy numbers for returning num1 and num2
            print "Answer equal to ", calc.subtract(num1,num2)
            raw_input("press any key")  
            
        if choice == 3:           
            num1,num2 = select1(1,2) 
            print "Answer equal to ", round(calc.divide(num1,num2),4)
            raw_input("press any key")   
        
        if choice == 4:           
            num1,num2 = select1(1,2)
            print "Answer equal to ", round(calc.multiply(num1,num2),4)
            raw_input("press any key")    
        
        if choice == 5:                              
            num1,num2 = select1(1,2)
            print "Answer equal to ", calc.exponent(num1,num2)
            raw_input("press any key") 
                            
        if choice == 6:      
            num=select2(1)
            print "Answer equal to ", round(calc.squareroot(num),4)              
            raw_input("press any key")
   
        if choice == 7:           
            num=select2(1)
            print "Answer equal to ", calc.square(num)
            raw_input("press any key")    
        
        if choice == 8:           
            num=select2(1)                    
            print "Sin",num, "equals" , round(calc.sin(num),4)
            raw_input("press any key") 

        if choice == 9:                              
            num=select2(1)            
            print "cos",num, "equals" , round(calc.cos(num),4)
            raw_input("press any key")
            
        if choice == 10:                             
            num=select2(1)
            print "Answer equal to ", calc.factorial(num)
            raw_input("press any key")             
                       