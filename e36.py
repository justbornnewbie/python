value = [99, 'no data', 95, 94, 'no data']
def fun(val):
    return [i for i in val if isinstance(i, int)]

fun(value)