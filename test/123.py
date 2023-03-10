list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
step = 2
element = "A"
for x in list_:
    if step < len(list_):
        list_.insert(step, element)
        step = step + 3
print(list_)


list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
step = 2
element = "A"
list_ = [x for x in list_]