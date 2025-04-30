def cal_sum(num):
    if num==0:
        return 0
    return cal_sum(num-1)+num
print(cal_sum(int(input("Enter the number:- "))))