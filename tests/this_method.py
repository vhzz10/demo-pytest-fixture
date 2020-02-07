from inspect import stack


def this_method():
    m = stack()[1][3]  # m aka this_method ref. https://stackoverflow.com/a/55253296/248616
    return f'{m}()'
