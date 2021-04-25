def count_num_func(num):
    '''
    计数指定数字
    '''
    # split_list = []
    # for one in range(0, 15):
    #     split_list += list(str(one))
    # print(split_list.count(str(num)))

    print(sum([str(i).count('5') for i in range(num + 1)]))


if __name__ == '__main__':

    print("结果：")
    count_num_func(123456)

