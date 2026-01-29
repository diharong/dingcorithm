def find_max_num(array):
    # 이 부분을 채워보세요!
    # array.sort()
    # return array[-1]
    for number in array:
        is_max_num = True
        for compare_number in array:
            if number < compare_number:
                is_max_num = False
        if is_max_num :
            return number


# 3 -> 5, 6, 1, 2, 4
# 5 -> 6, 1, 2, 4
# 6 -> 1, 2, 1
# 1 -> 2, 4
# 2 -> 4

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))