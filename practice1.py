# Question1：简单的字符串排序
#coding=utf-8
l = input()

c_array = []
n_array = []
result = []

for i in l:
    if i.isalpha():
        c_array.append(i)
    else:
        n_array.append(i)
        
n_array.sort()
c_array.sort()

result.extend(n_array)
result.extend(c_array)

print(''.join(result))

-----------------------------------------------------------------

# Question2:字符映射
# dic:保存对应关系  mid：用来存放中间变量
dic = []
mid = []

# 生成最初字符串数字对应关系
for index in range(26):
    mid.extend(chr(index+ ord('a')))
    if ((index + 1) % 3 == 0) | (index == 25):    # 遇到三个时加入另一个数字，25是因为最后的数字不够对应三个元素
        dic.append(mid)
        mid = []


# 获取输入的值并且存储为list
l = input()
i_index = []
for item in l:
    i_index.extend(item)

# 生成对应关系
# res里存放是结果数组  flag是标志是否是第一次循环
res = []
flag = 0
for item in i_index:
    if flag == 0:
        res = dic[int(item)-1]    # 如果是第一次循环，就直接赋值就好
    else:
        res = [(x + y) for x in res for y in dic[int(item)-1]]    # 生成两个数组的笛卡尔积
    flag = 1    # 第一次循环后，将标志位记为1
res.sort()    # 排序

# 输出结果
for i in range(len(res)):
    print(res[i], end=' ')
