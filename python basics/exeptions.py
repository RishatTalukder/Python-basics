while True:
    a = input()
    b = input()
    if a=='q' or b == 'q':
        break 
    
    try:
        answere = int(a)/int(b)
    
    except ValueError:

        print("ur syntex is not numbers")
        
    
    else:
        print(answere)
    


# try:
#     print(3/0)

# except ZeroDivisionError:
#     print("sorry you can't devide with zero")