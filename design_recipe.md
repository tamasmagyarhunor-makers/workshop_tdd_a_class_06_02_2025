# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
```text
As a User
So I know what I have to do
I want to be able write a todo list
```

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TodoList:
    # User-facing properties:
    #   todos: list

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Sets the todos property of the self object to an empty list
        pass # No code here yet

    def add_new_todo(self, todo):
        # Parameters:
        #   todo: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the todo to the self.todos list
        pass # No code here yet

    def remove_todo(self, todo):
        # Parameters:
        #   todo: string representing a todo we want to delete
        # Returns:
        #   A string telling us that the todo has been done
        # Side-effects:
        #   deletes the todo from the self.todos
        pass # No code here yet

    def get_todos(self):
        # Parameters:
        #   None
        # Returns:
        #   the list of todos from self.todos
        # Side-effects:
        #   None
        pass # No code here yet



# side effect examples
class Example():
    def __init__(self):
        self.counter = 0
    
    def raise_counter(self):
        self.counter += 1

    def get_counter(self):
        return self.counter
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given we instantiate a new TodoList
It returns a TodoList instance 
"""
todo_list = TodoList()

assert isistance(todo_list, TodoList())

"""
Given we instantiate a new TodoList
It comes with an empty list
"""
todo_list = TodoList()

assert todo_list.todos == []

"""
Given we call add_new_todo and pass in a todo
It will push this todo into the self.todos
"""
todo_list = TodoList()
todo_list.add_new_todo("buy coke")

actual = todo_list.todos
expected = ["buy coke"]


assert todo_list.todos == ["buy coke"]
assert actual == expected
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
