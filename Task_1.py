class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для знаходження найбільшого значення
def find_max(root):
    current = root
    # Йдемо вправо до останнього вузла
    while current.right:
        current = current.right
    return current.key

# Приклад використання
if __name__ == "__main__":
    # Створимо дерево
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.right.right = Node(40)
    root.right.left = Node(25)

    print("Найбільше значення в дереві:", find_max(root))
