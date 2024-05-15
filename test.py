test_list = [1, 2, ["3 1", "3 2","3 3"], 4]

level = 1
def func(arg):
    for i in arg:
        global level
        level += 1
        print(level, i)

func(test_list)