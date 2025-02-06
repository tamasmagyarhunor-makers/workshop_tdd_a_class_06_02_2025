class TodoList():
    def __init__(self):
        self.todos = []

    def add_new_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        if len(self.todos) == 0:
            raise Exception("Can not operate on empty list")
        result = f"{todo} has been done"
        self.todos.remove(todo)
        return result
