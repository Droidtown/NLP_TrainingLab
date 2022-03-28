#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR=""):
    answerLIST = inputSTR.split(" ") #用空格把 inputSTR 切開成為一個 list
    answerSTR = answerLIST[-1] #既然動詞在最後一個位置，那就把 list 的最後一個字取出來就好了。
    answerSTR = answerSTR.replace(".", "") #別忘了，最後還有一個「句號」的 . 要刪除，這裡我用了 .replace() 來把 "." 取代成 ""，也就是刪除的意思。
    return answerSTR  #最後回傳 answerSTR
    
if __name__ == "__main__":
    inputSTR01 = "Ich kann den Mann sehen."
    answerSTR = main(inputSTR=inputSTR01)
    print("第一句的動詞為：{}".format(answerSTR))
    
    inputSTR02 = "Ich sah einen Mann, der einen Apfel aß."
    answerSTR = main(inputSTR=inputSTR02)
    print("第二句的動詞為：{}".format(answerSTR))