import numpy as np
    
number = np.random.randint(1,101)
    
count = 0
    
while True:
    count+=1
    predict_number = int(input("search number at 1 to 101 "))
        
    if predict_number > number:
        print("Number must be smaller")
            
    elif predict_number < number:
        print("Number must be bigger")
            
    else:
        print(f"You are predict number! This number = {number}, for {count} counts")
        break
                    
        