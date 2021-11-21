

##
def find_str(target_list, index, target):
    '''
    主要用於尋找列表內的特定字串，其中此列表不限於1D
    此函示會根據輸入的index當作基準來排序列表
    Attribute:
        target_list (*list) = 目標列表\n
        index (*int) = 依據哪一行資料當作基準\n
        target (*string)= 想找的字串\n

    Example:
        example_list = [[1, 'apple'], [2, 'bird'], [3, 'bag'], [4, 'baseket'],[5, 'baseketball'], [6, 'balanced'], [7, 'basketball']]
        example_target = 'apple'
        exmaple_index = 1 # 因為欲尋找字串apple，而apple的index為1
        find_str(example_list, example_index, example_target)
        Output[1] :
    '''
    import numpy as np
    # sort the list initially
    sort_list = sorted(target_list, key=lambda x: x[index])
    # this index will change in every iteration
    current_index = int(np.ceil(len(sort_list)/2))
    # buffer storages the increment of every iteration
    buffer_index = current_index
    for i in range(current_index):
        buffer_index = int(np.ceil(buffer_index/2))
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


a = find_str(t, 1, 'apple')
