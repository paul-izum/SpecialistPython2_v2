class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


def find_node_by_value(start_node, value):
    """
    Возвращает индекс ноды с заданным значением(value).
    Если нода с указанным значение(value) не найдена, дублируйте поведение методы .index() списка
    """
    i = 0
    current_node = start_node
    while current_node:
        current_node = current_node.next
        i += 1
        if current_node == None:
            print(f"искомое значение {value} не найден")
            return

        if current_node.value == value:
            print(i)
            return


def print_node_by_index(start_node, index):
    """
    Выводит в терминал значение(value) ноды с заданным индексом(index). Индексация начинается с нуля.
    Если index = 0, выводим значение ноды start_node
    Считаем, что index гарантированно > 0
    """
    i = 0
    current_node = start_node
    while current_node:
        current_node = current_node.next
        i += 1
        if i == index:
            print(current_node.value)
            return
    print(f"искомый элемент {i} не найден")

            # return current_node.value


def gen_names_list(size=None):
    import random
    names = ["Василий", "Николай", "Екатерина", "Ирина", "Линус", "Ганс", "Игнат", "Марина", "Кристина", "Кирилл"]
    if not size:
        size = random.randint(3, len(names))
    random.shuffle(names)
    return names[:size]


# Дан список из произвольного количества имен
names = gen_names_list()
print(names)

# TODO: скопируйте цепочку нод из предыдущей задачи
first_node = Node(names[0])
prev_node = first_node
for name in names[1:]:
    next_node = Node(name)
    prev_node.next = next_node
    prev_node = next_node


# TODO: Передайте первую ноду и искомое значение в функцию find_node_by_value()
#  напишите реализацию функции find_node_by_value()

value = "Василий"
find_node_by_value(first_node, value)
