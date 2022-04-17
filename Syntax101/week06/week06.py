#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputLIST):
    #以 main() 收到的 inputLIST 做為初始條件
    while "" in inputLIST:    #如果 "" 空字串存在於 inputLIST 裡的話，這個迴圈的條件就成立！
        inputLIST.remove("")  #把 inputLIST 裡的空字串移除，改變了 inputLIST 裡的值，以此做為更新條件。
    return inputLIST

if __name__ == "__main__":
    sLIST = ['John', '', '', '', 'Mary', '', 'Jack']
    print("處理前的 sLIST:{}".format(sLIST))
    sLIST = main(sLIST)
    print("處理後的 sLIST:{}".format(sLIST))