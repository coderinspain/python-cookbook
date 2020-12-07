# Exeptions
#Ba thing happen, we need to know how to handle them

"""
Comments:
Errors mostly occur at runtime that's they belong to an unchecked type.
Exceptions are the problems which can occur at runtime and compile time.
I mainly occurs in the code written by the developers.
Exceptions are divided into two categories such as checked exceptions and unchecked exceptions.
"""

#Simple decorator
def outline(func):
    def inner(*args, **kwargs):
        print('-'*20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-'*20)
    return inner


@outline
def test_one(x,y):
    try:
        #attempt
        z = x / y
        print(f'Result: {z}')
    except Exception as e:
        #catch
        print(f'Something bad happened x:{x}, y:{y} the issue was: {e}')
        
    finally:
        #moving along
        print('Complete')

test_one(10, 0)
test_one(5, 'cat')
test_one(5, 2)



#AssertionsErrors

@outline
def test_two(x,y):
    try:
        #attempt
        assert (x > 0)
        assert (y > 0)
    except AssertionError:
        #Specific
        print(f'Failed to assert x:{x}, y: {y}')
    except Exception as e:
        #catch
        print(f'Something bad happened x:{x}, y:{y} the issue was: {e}')
    else:
        #trusted
        z = x / y
        print(f'Result: {z}')        
    finally:
        #moving along
        print('Complete')


test_two(20, 0)
test_two(15, 'cat')
test_two(15, 2)


#User defined exceptions and raising
class CatError(RuntimeError):
    def __init__(self, *args):
        self.args = args

@outline
def test_cats(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be an int')
        if qty < 9:
            raise CatError('Must own more than 9 cats')
        print(f'You own {qty} casts')
    except Exception as e:
        print(f'Opp: {e.args}')
        
    finally:
        print('Complete')

test_cats('abc')
test_cats(3)
test_cats(12.3)
test_cats(11)
