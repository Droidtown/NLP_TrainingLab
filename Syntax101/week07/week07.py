#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR, targetSTR):
    counterINT = 0
    for i in ("\n", ",", "."):   #利用迴圈，把要清除的標點符號依次取出，並取代成空字串，清理掉。
        inputSTR = inputSTR.replace(i, "")
    inputLIST = inputSTR.split(" ")  #把 inputSTR 用 .split() 切成列表型態
    for i in inputLIST:
        if i == targetSTR:  #比對到一次，counter 就加 1
            counterINT = counterINT + 1
        else:               #沒有比對到，就算了
            pass
    return counterINT

if __name__ == "__main__":
    #讀入 news.txt 檔
    with open("./media/news.txt", "r", encoding="utf-8") as f:
        textSTR = f.read()
    #把 textSTR 傳入 main() 裡
    targetWordSTR = "Musk"
    resultINT = main(textSTR, targetWordSTR)
    print("{} 出現了 {} 次".format(targetWordSTR, resultINT))

    targetWordSTR = "Musk's"
    resultINT = main(textSTR, targetWordSTR)
    print("{} 出現了 {} 次".format(targetWordSTR, resultINT))