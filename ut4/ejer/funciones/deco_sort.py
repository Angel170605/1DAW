def deco_sort(extract_evens):
    def wrapped(*args, **kwargs):
        start_n = 0
        sort_list = []
        for arg in extract_evens(*args, **kwargs):
            if arg > start_n:
                sort_list.append(arg)
                start_n = arg
            else:
                sort_list.insert(0, arg)
        return wrapped

    return deco_sort


@deco_sort
def extract_evens(*values):
    return (v for v in values if v % 2 == 0)


print(extract_evens(8, 1, 4, 2, 5))
