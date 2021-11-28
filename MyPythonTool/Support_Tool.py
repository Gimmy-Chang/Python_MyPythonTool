'''
Author : Gimmy Chang
Date : 2021/11/21
'''

## 尋找列表內資料list[list[]]
def find_list_data(target_list, index, target):
    '''
    This function is for seaching the specific data(*str, *int), but the input should be the
    list format not excluded 1D.
    One of the attribute "index" is the key to sort and find your target data.
    The function is built on binary method for searching that spent less time.
    The structure of the list of all the data and the dimension should be the same.
    Attribute:
        target_list (*list) = 目標列表，不限於任何資料型態\n
        index (*int) = 依據哪一行資料當作基準\n
        target (*str, *int)= 想找尋的資料\n

    Example1:
        example_list = [[1, 'apple'], [2, 'bird'], [3, 'bag'], [4, 'baseket'],[5, 'baseketball'], [6, 'balanced'], [7, 'basketball']]
        example_target = 'apple'
        example_index = 1 # 因為欲尋找字串apple，而apple的index為1
        find_list_data(example_list, example_index, example_target)
        Output1: Tried 4 times
                [1, 'apple']
    Example2:
        example_list = [[1, 'apple',3], [2, 'bird',3455], [3, 'bag',3455435], [4, 'baseket',678768],[5, 'baseketball',1231], [6, 'balanced',4], [7, 'basketball',423423]]
        example_target = 4
        example_index = 2  # 因為欲尋找字串apple，而apple的index為1
        find_list_data(example_list, example_index, example_target)
        Output2: Tried 3 times
                [6, 'balanced', 4]
    '''
    import numpy as np
    nestlist_num = checklist(target_list)
    # Checking
    if nestlist_num < 0:
        raise Warning('Your input is not a List format')

    # sort the list initially
    sort_list = sorted(target_list, key=lambda x: x[index])
    # this index will change in every iteration
    current_index = int(np.ceil(len(sort_list)/2))
    # buffer storages the increment of every iteration
    buffer_index = current_index

    # Main
    for i in range(int(np.ceil(np.sqrt(current_index*2)))):
        buffer_index = int(np.ceil(buffer_index/2))
        # if current_index > len(sort_list):
        #     current_index = len(sort_list)
        #     continue
        if sort_list[current_index][index] > target:
            current_index = current_index - buffer_index
        elif sort_list[current_index][index] == target:
            print('Tried %d times' % (i+1))
            print(sort_list[current_index])
            return sort_list[current_index]
        else:
            current_index = current_index + buffer_index
    else:
        print("There's no '%s' inside you list!!!!" % str(target))

def checklist(target_list, n = 0):
    '''
    For checking the structure of the list, this will return the amount of the nested list
    Attribute:
        target_list (*list) = target data
        n (*int) = No need to input, this is represent the amount of the nested list.
                   If your input is a list format, output will return an amount that n > 0.
                   If not return -1
    Example1:
        checklist([[1],[2]])
        Output1: 2
    Example2:
        checklist((1,2,3))
        Output2: -1
    '''
    if type(target_list) == list:
        n += 1
        return checklist(target_list[0], n = n)
    elif type(target_list) != list and n == 0:
        return -1
    else:
        return n