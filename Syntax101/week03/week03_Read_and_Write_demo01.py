#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR=""):
    answerSTR = inputSTR[0:-2]
    return answerSTR

if __name__ == "__main__":
    userInputSTR = input("請輸入一個英文的規則變化動詞的過去式：")

    outputSTR = main(inputSTR=userInputSTR)
    print("你輸入的是 {}，它的原型應該是 {}！".format(userInputSTR, outputSTR))