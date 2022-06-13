def try_catch():
    x = 5
    y = 0
    try:
        print(x/y)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try_catch()