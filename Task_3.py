class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для знаходження суми всіх значень у дереві
def find_sum(root):
    # Якщо дерево порожнє, сума дорівнює 0
    if root is None:
        return 0
    
    # Сума дорівнює значенню поточного вузла плюс сума значень у лівому і правому піддереві
    return root.key + find_sum(root.left) + find_sum(root.right)

# Приклад використання
if __name__ == "__main__":
    # Створимо дерево
    root = Node(20)
    root.left = Node(10)
    root.right = Node(30)
    root.left.left = Node(5)
    root.left.right = Node(15)

    print("Сума всіх значень у дереві:", find_sum(root))
