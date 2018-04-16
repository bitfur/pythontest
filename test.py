def test():
    print "OK"

def another_func():
    print "OK"

def vulnerable_input(msg):
        print eval(msg)

vulnerable_input("__import__('os').listdir('.')")        
test()