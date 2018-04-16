def test():
    print "OK"

def another_func():
    print "OK"

def vulnerable_input():
        eval(raw_input())
   
test()