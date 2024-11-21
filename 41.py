def check_in_interval(what_to_ask, min_value, max_value, ):
     current_value = int(input(what_to_ask))
     if min_value < current_value < max_value:
        return True
     return False

result = check_in_interval("enter your age: ",0, 20,)
if result:
    print("your age has been entered")
experience = check_in_interval("enter years pf experience: ", 2, 10,)
if experience:
    print("you have experience ")