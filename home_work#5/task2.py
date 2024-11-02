class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вспомогательный метод для вставки
    def _insert(self, root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
            root.left.parent = root
        else:
            root.right = self._insert(root.right, value)
            root.right.parent = root
        return root

    # Вставка узла
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    # Вспомогательный метод для поиска
    def _search(self, root, value):
        if root is None or root.value == value:
            return root
        if value < root.value:
            return self._search(root.left, value)
        return self._search(root.right, value)

    # Поиск элемента
    def search(self, value):
        result = self._search(self.root, value)
        return result is not None

    # Вспомогательный метод для нахождения минимального значения
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Удаление узла
    def _delete_node(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self._delete_node(root.left, value)
        elif value > root.value:
            root.right = self._delete_node(root.right, value)
        else:
            # Узел с одним потомком или без потомков
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Узел с двумя потомками: получаем наименьший в правом поддереве
            temp = self._min_value_node(root.right)
            root.value = temp.value
            root.right = self._delete_node(root.right, temp.value)

        return root

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    # Вспомогательный метод для печати дерева
    def _print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left:
                self._print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self._print_tree(node.right, level + 1, "R--- ")

    # Печать дерева
    def print_tree(self):
        if self.root is None:
            print("Дерево пусто")
        else:
            self._print_tree(self.root)

# CLI интерфейс для работы с деревом
def cli():
    bst = BinarySearchTree()
    while True:
        command = input("Введите команду (insert, search, delete, print, exit): ").strip().lower()
        if command == "insert":
            value = int(input("Введите значение для вставки: "))
            bst.insert(value)
        elif command == "search":
            value = int(input("Введите значение для поиска: "))
            found = bst.search(value)
            print(f"Элемент {'найден' if found else 'не найден'}")
        elif command == "delete":
            value = int(input("Введите значение для удаления: "))
            bst.delete(value)
        elif command == "print":
            bst.print_tree()
        elif command == "exit":
            break
        else:
            print("Неизвестная команда, попробуйте снова.")

if __name__ == "__main__":
    cli()

def demo_cli():
    bst = BinarySearchTree()
    
    # Демонстрация вставки элементов
    print("Демонстрация вставки элементов в дерево:")
    for value in [50, 30, 70, 20, 40, 60, 80]:
        print(f"\nВставляем {value} в дерево.")
        bst.insert(value)
        bst.print_tree()
        input("Нажмите Enter, чтобы продолжить...")

    # Поиск элемента
    print("\nДемонстрация поиска элементов:")
    search_values = [40, 90]
    for value in search_values:
        print(f"\nИщем {value} в дереве.")
        found = bst.search(value)
        print(f"Элемент {'найден' if found else 'не найден'}")
        input("Нажмите Enter, чтобы продолжить...")

    # Удаление элемента
    print("\nДемонстрация удаления элементов:")
    delete_values = [20, 30, 50]
    for value in delete_values:
        print(f"\nУдаляем {value} из дерева.")
        bst.delete(value)
        bst.print_tree()
        input("Нажмите Enter, чтобы продолжить...")

if __name__ == "__main__":
    demo_cli()
