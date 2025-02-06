from lib.example import example

def xtest_example():
    actual = example()
    expected = "hello"

    assert actual == expected