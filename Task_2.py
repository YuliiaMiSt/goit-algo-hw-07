class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для знаходження найменшого значення
def find_min(root):
    current = root
    # Йдемо вліво до останнього вузла
    while current.left:
        current = current.left
    return current.key

# Приклад використання
if __name__ == "__main__":
    # Створимо дерево
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)

    print("Найменше значення в дереві:", find_min(root))
