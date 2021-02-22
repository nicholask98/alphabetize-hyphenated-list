user_input = input('Enter a hyphen-separated sequence of words:\n')
x = user_input.split('-')
x.sort()
for index, item in enumerate(x):
    if index == len(x) - 1:
        print(item)
    else:
        print(item + '-', end = '')
