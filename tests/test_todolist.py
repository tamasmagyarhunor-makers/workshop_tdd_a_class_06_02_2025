from lib.todolist import  TodoList

"""
Given we instantiate a new TodoList
It returns a TodoList instance 
"""
def test_todo_insantiates_todo_list():
    todo_list = TodoList()

    assert isinstance(todo_list, TodoList)

"""
Given we instantiate a new TodoList
It comes with an empty list
"""
def test_todo_instantiates_with_empty_list():
    todo_list = TodoList()

    assert todo_list.todos == []