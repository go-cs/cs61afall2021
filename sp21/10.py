'''
Author: your name
Date: 2022-01-10 12:40:30
LastEditTime: 2022-01-10 12:45:45
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sp21\10.py
'''
t = (2, 0, 9, 10, 11)
s = 0
k = 0
while k < len(t):
    x = t[k]
    s += x
    k += 1
print(s)

print("================================")
s1 = 0
for x in t:
    s1+=x
print(s1)
