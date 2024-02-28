class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

def func(e):
    if e == 1:
        raise InvalidDataException()
    elif e == 2:
        raise ProcessingException()
    else:
        print('Все супер!')

def func2(case):
    try:
        func(case)
    except ProcessingException as e:
        print(f'Внимание: {e}')
    except InvalidDataException as e:
        print(f'Ошибка: {e}')

func2(case=1)i.total_fuel))