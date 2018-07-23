#coding: utf-8

import sys
form = input().rstrip()

opePluMin = []    #+と-をいれる
opeProDiv = []    #*と/をいれる

#符号をsearchする
for target in ['+','-','*','/']:
    index = -1
    while True:
        index = form.find(target, index+1)
        if index == -1:
            break
        if (target=='+' or target=='-'):
            opePluMin.append(index)
        if (target=='*' or target=='/'):
            opeProDiv.append(index)

#並び替える
opePluMin.sort()
opeProDiv.sort()

#符号場所一覧
opeNum = opePluMin+opeProDiv
opeNum.sort()

#print(opePluMin)
#print(opeProDiv)
#print(opeNum)

#データをストック
data = []
j = 0
for i in range(len(opeNum)):
    data.append(int(form[j:opeNum[i]]))
    j = opeNum[i]+1
data.append(int(form[j:]))
#print(data)

#乗除算処理
for i in opeProDiv:
    #opeNum中のアドレス
    opeAdd = opeNum.index(i)
    #実際の演算子
    sign = form[i]
    if sign=='*':
        data[opeAdd] *= data[opeAdd+1] * 1.0
    elif sign=='/':
        try:
            data[opeAdd] /= data[opeAdd+1] * 1.0
        except ZeroDivisionError:
            print("ZeroDivisionError!!")
            exit()
    del data[opeAdd+1]
    del opeNum[opeAdd]
#    print(data)


#和差処理
for i in opePluMin:
    sign = form[i]
    if sign=='+':
        data[0] += data[1]
    elif sign=='-':
        data[0] -= data[1]
    del data[1]
#    print(data)

print(">> " + str(data[0]))
