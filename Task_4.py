class Comment:
    def __init__(self, text, author):
        self.text = text  # Текст коментаря
        self.author = author  # Автор коментаря
        self.replies = []  # Список відповідей
        self.is_deleted = False  # Прапорець, що вказує, чи був коментар видалений
    
    # Метод для додавання відповіді
    def add_reply(self, reply):
        self.replies.append(reply)
    
    # Метод для видалення коментаря
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    # Метод для відображення коментаря та його відповідей
    def display(self, indent=0):
        # Створення відступу залежно від рівня вкладеності
        prefix = "    " * indent
        if self.is_deleted:
            print(f"{prefix}{self.text}")
        else:
            print(f"{prefix}{self.author}: {self.text}")
        
        # Рекурсивно відображаємо всі відповіді
        for reply in self.replies:
            reply.display(indent + 1)

# Приклад використання
if __name__ == "__main__":
    # Створюємо кореневий коментар
    root_comment = Comment("Яка чудова книга!", "Бодя")
    
    # Додаємо відповіді
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)
    
    # Додаємо відповідь на відповідь
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)
    
    # Видаляємо коментар Андрія
    reply1.remove_reply()
    
    # Виводимо структуру коментарів
    root_comment.display()
