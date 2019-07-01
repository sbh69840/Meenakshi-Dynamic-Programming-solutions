import timeit
mysetup = "from Minimum_weights import Minimum_weights"
mycode = '''
Minimum_weights(int(input())).solve()
'''
timeit(setup=mysetup,code=mycode)