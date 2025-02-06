from lib.example import example

def test_example():
    actual = example()
    expected = "hello"

    assert actual == expected