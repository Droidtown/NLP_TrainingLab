#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def convert2male(inputLIST):
    resultLIST = [] #準備一個承接變化後的空列表
    for i in inputLIST:
        resultLIST.append(i[:-1]) #把最後一個 "-a" 移除後，加到 resultLIST 裡
    return resultLIST  #別忘了把 resultLIST 回傳哦！

def convert2female(inputLIST):
    #多做一個練習，利用 range() 把男生版的名字直接在 inputLIST 就轉為女性版本。不準備承接變化的空列表。
    for i in range(0, len(inputLIST)):
        inputLIST[i] = inputLIST[i] + "a"
    return inputLIST

if __name__ == "__main__":
    femaleLIST = ["Louisa", "Roberta", "Simona", "Carla"]
    maleLIST = convert2male(femaleLIST)
    print("男生版的名字為：{}".format(maleLIST))

    femaleLIST2 = convert2female(maleLIST)
    print("女生版的名字為：{}".format(femaleLIST))
