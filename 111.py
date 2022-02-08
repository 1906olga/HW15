dict_users = {'olga': 'ooooo', 'anna': 'aaaaa', 'nina': 'nnnnn', 'alena': 'aaaa'}


def decorate(func: any) -> bool:
    def wrapper(username: any, password: any) -> bool:
        if not check_password(username, password):
            return False
        if not authenticate(username, password):
            return False
        return func(username, password)

    return wrapper


def check_password(username: str, password: str) -> bool:
    return dict_users.get(username) == password


def authenticate(username: any, password: any) -> bool:
    return True


@decorate
def login(username: any, password: any) -> bool:
    return True


if __name__ == '__main__':
    count = 3
    while count != 0:
        user = login(username=input(), password=input())
        if user == True:
            print(f'successful authorization')
            break
        else:
            count -= 1
            print('wrong password! enter password again. you have ', count, 'attempts')
    else:
        print(f'attempts are over! you are blocked')
