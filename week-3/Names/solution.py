"""Розв'язок до завдання 'names search':
https://cms.ucu.edu.ua/mod/vpl/view.php?id=362103&userid=9890
Має неповне покриття тестів на cms на 0.66/1"""
def find_names(file_path: str) -> tuple:
    """
    The function returns tuple, which contains 3 elements:
    the first - set of 3 the most popular names,
    the second - tuple with number of names that appear once, and a set of those names,
    the third - tuple with a letter with which most of the names start, 
    the number of that names, and a number of children with that names.
    """
    def selection_sort(lst: list) -> list:
        """ 
        The function sorts the lst using the selection sort algorithm.
        >>> selection_sort([10, 8, 7, 1, 2, 0, 5, 11, 4, 13])
        [0, 1, 2, 4, 5, 7, 8, 10, 11, 13]
        """
        length = len(lst)
        for i in range(length):
            min_index = i
            for j in range(i + 1, length):
                if lst[j] < lst[min_index]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]
        return lst

    name_counter = {}
    rare_names = set()
    rare_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        file.readline()
        lines = file.readlines()
        for line in lines:
            info = line.strip().split(' \t')
            name = info[0]
            count = int(info[-1][1:-1])
            if name in name_counter:
                name_counter[name] += count
            else:
                name_counter[name] = count
    sorted_names = selection_sort(list(name_counter.values()))[::-1]
    top_names = set()
    for name, count in name_counter.items():
        if count in sorted_names[:3]:
            top_names.add(name)

    for name, count in name_counter.items():
        if count == 1:
            rare_count += 1
            rare_names.add(name)

    return top_names, (rare_count, rare_names)
