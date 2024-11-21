import datetime
from mydep import test as mydep_test
from my_other_dep import test as my_other_dep_test
mydep_test()
my_other_dep_test()

def wait_fot_print():
    from time import sleep
    sleep(3)
    print("hello world")
print("moshe")
wait_fot_print()

print("test")