def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Wrong Input!'
        except Exception as e:
            return e
    return inner
