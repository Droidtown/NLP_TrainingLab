#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(openFileNameSTR="", saveFileNameSTR=""):
    #把檔案讀出來，注意此時使用的是 "r" 模式，表示是「讀取」。
    with open(openFileNameSTR, "r", encoding="utf-8") as f:
        contentText = f.read()
    print("讀出來的檔案內容為：{}".format(contentText))

    #把讀出來的文字內容，全部改為首字大寫
    contentText = contentText.title()

    #然後再存入新檔。
    with open(saveFileNameSTR, "w", encoding="utf-8") as f:
        f.write(contentText)

    return None #沒有回傳任何值。做完就做完了！

if __name__ == "__main__":
    #先設定好原始檔案為 oldFileNameSTR
    oldFileNameSTR = "./corpus/sample_news.txt"
    #再設定好稍後要存起來的新檔名到 newFileNameSTR 裡
    newFileNameSTR = "./capitalized_news.txt"

    #呼叫 main() ，並且把要打開的舊檔以及要寫入的新檔兩個檔名都交給它
    main(openFileNameSTR=oldFileNameSTR, saveFileNameSTR=newFileNameSTR)
    #完成！你可以看看在 week03_Read_and_Write_demo02.py 的旁邊是不是多了一個文字檔案，檔名就是 newFileNameSTR 裡設定的呢？