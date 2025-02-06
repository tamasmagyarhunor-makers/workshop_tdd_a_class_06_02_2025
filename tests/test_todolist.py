from lib.todolist import  TodoList
import pytest

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

"""
Given we call add_new_todo and pass in a todo
It will push this todo into the self.todos
"""
def test_add_todo_to_list_coke():
    todo_list = TodoList()
    todo_list.add_new_todo("buy coke")

    actual = todo_list.todos
    expected = ["buy coke"]


    assert todo_list.todos == ["buy coke"]
    assert actual == expected

def test_add_todo_to_list_milk():
    todo_list = TodoList()
    todo_list.add_new_todo("buy milk")

    actual = todo_list.todos
    expected = ["buy milk"]


    assert todo_list.todos == ["buy milk"]
    assert actual == expected

"""
Given we call remove_todo and pass in a todo
It will delete this todo from the self.todos
"""
def test_todo_remove_todo_from_todo_list():

    todo_list = TodoList()
    todo_list.add_new_todo("buy coke")
    todo_list.add_new_todo("go for walk")

    actual_string = todo_list.remove_todo("buy coke")
    actual_list = todo_list.todos

    expected_string = "buy coke has been done"
    expected_list = ["go for walk"]

    assert actual_string == expected_string
    assert actual_list == expected_list

"""
Given we call remove_todo on an empty self.todos list
It will throw an error
"""
def test_remove_todo_returns_error_when_called_on_empty_list():
    todo_list = TodoList()

    with pytest.raises(Exception) as e:
        todo_list.remove_todo("buy coke")

    error_message = str(e.value)

    assert error_message == "Can not operate on empty list"
