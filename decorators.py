#Decorators are useful to reuse functions, in this way you can add instructions before and after functions

PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('what is the password?')
        if password == PASSWORD:
            return func()
        else:
            print('Incorrect password')
    return wrapper

@password_required
def needs_password():
    print('Password is correct')

def upper(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result.upper()
    return wrapper

@upper
def say_my_name(name):
    return 'Hello {}'.format(name)

def run():
    print(say_my_name('Ricardo'))
    #needs_password()


if __name__ == '__main__':
    run()