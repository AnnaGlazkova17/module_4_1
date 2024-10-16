from math import inf # выдает бесконечность при делении на ноль
def divide(first, second):
    if second == 0:
        return inf
    else:
        result_tm = first / second

    return result_tm