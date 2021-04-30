size_list = []


def append_to_size_list(x):
    global size_list
    size_list.append(x)


def clean_size_list():
    global size_list
    size_list = []


def get_max_size_list():
    global size_list
    return max(size_list)


def get_min_size_list():
    global size_list
    return min(size_list)
