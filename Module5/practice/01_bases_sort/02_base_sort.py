# Все алгоритмы сортировки из examples/ оберните в функции

def bubble_sort(nums:list):
    # nums = [5, 2, 1, 8, 4]
    # print("before sort = ", nums)
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    # print("after sort = ", nums)
    return nums

def sort_choice(nums:list):
    # nums = [5, 2, -1, 8, 4, -4, 7]
    # print("before sort = ", nums)
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1
    # print("after sort = ", nums)
    return nums


def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums:list):

    def quick_sort(nums):
        # Создадим вспомогательную функцию, которая вызывается рекурсивно
        def _quick_sort(items, low, high):
            if low < high:
                # Индекс опорного элемента
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    import random
    numbers = []
    for i in range(size):
        numbers.append(random.randint(at, to))
    return numbers
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: список из size произвольных элементов в диапазоне at..to 
    """


# протестируйте функции сортировки, используя gen_list() для создания сортируемых списков

ln = gen_list(15,-100,100)
print(ln)

bubble_sort(ln)
print(ln)

sort_choice(ln)
print(ln)

quick_sort(ln)
print(ln)
