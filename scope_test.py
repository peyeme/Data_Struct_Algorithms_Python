def scope_test():

    def do_local():
        spam = "local spam"
        test = spam

    def do_nonlocla():
        nonlocal spam
        test = spam
        spam = "nonlocal spam"

    def do_globallocal():
        global spam
        test = spam
        spam = "global spam"
        spam = "why"

    spam = 'test spam'
    do_local()
    print("After local assignment:", spam)
    do_nonlocla()
    print("After nonlocal assignment:", spam)
    do_globallocal()
    print("After global assignment:", spam)

scope_test()
print("After function:", spam)