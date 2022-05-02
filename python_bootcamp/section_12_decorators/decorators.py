def new_decorator(original_function):

    def wrap_func():

        print('some extra code before the original function')

        original_function()

        print('some extra code after the original function')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print('i want to be decorated')

func_needs_decorator()
