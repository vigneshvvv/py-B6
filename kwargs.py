def employee_info(**kwargs):
    print(kwargs)
    print(type(kwargs))

def sample(*args, **kwargs):
    print(args)
    print(kwargs)

def add(a,b,c):
    print(a+b+c)

employee_info(name="Vignesh", role="Dev")
sample(10,20,30,name="Vignesh")

numbers =[10,20,30]
add(*numbers)

