def add_everything_up(a,b):  # будет складывать числа(int, float) и строки(str)
    try:
        if isinstance(a, (int, float)) == True and isinstance(b, (int, float)) == True: # проверяем, что являются числами
            result = round(a + b, 3) # суммируем и округляем до 3-х знаков
        else:
            result = a + b 
        return result
    except TypeError:
        result = str(a) + str (b)
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))