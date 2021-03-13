from collections import Counter
from playStats.descriptive_stas import frequency

from playStats.descriptive_stas import mode

from playStats.descriptive_stas import median
from playStats.descriptive_stas import mean


if __name__ == "__main__":

    # 测试频数
    data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    counter = Counter(data)
    print(counter.most_common())
    print(counter.most_common()[0][1])

    # 测试频率
    freq = frequency(data)
    print(freq)


# 测试众数
    data = [2, 2, 2, 1, 1, 1, 3, 3]
    mode_elements, mode_count = mode(data)

    if mode_elements:
        print(mode_elements)
        print(mode_count)
    else:
        print("mode does not exist.\n")

    # 测试中位数
    data = [1, 4, 2, 3]
    print(median(data))

    # 测试均值
    data = [1, 4, 2, 3, 5]
    print(mean(data))