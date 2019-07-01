def table(n):
    def print_tab(i):
        if i<=10:
            print("{0} x {1} = {2}".format(n,i,n*i))
            print_tab(i+1)
    print_tab(0)
table(5)
            
