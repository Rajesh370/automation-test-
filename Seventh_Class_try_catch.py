def try_catch():
    expected_result = "Hello"
    actual_result = "Hello"
    try:
        assert expected_result == actual_result
    except AssertionError:
        print("Unmatched")
    else:
        print("Matched")

if __name__ == "__main__":
    try_catch()

