def give_me_stats(func):
    def inner_func():
        print('before')
        func()
        print('after')
    return inner_func

@give_me_stats
def display_hello():
    print('hello')

display_hello = give_me_stats(display_hello)

# display time of day before and after hello
display_hello()