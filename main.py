try:
    a=int(input("enter any number:-"))
    b=int(input("enter any number:-"))
    print("what kinds of operation do you perform.press + for" \
    " a addition \n- for a substraction\n* for a multiplication\n/ for division")
    o=input("enter any operation:-")
    match o:
        case "+":
            print(f"the result is {a+b}")
  
        case "-":
            print(f"the result is {a*b}")        

        case "*":
            print(f"the result is: {a*b}")        

        case "/":
            print(f"the result is: {a/b}")    

        case default:
            print(f"there was an err: ")
except Exception as e:
    print(
        'print a valid of a and b'
    )
    