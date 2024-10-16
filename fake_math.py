def divide(first, second): # выбает ошибку при попытке поделить на ноль
    if second == 0:
        result_fm= 'Ошибка'
    else:
        result_fm = first/second
    return result_fm
#print(result)