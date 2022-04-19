# Form: Data/Info in Languages
本系列的練習裡，將透過實際操作 Python 程式語言來理解「自然語言」裡的資料/資訊，在程式語言裡是如何呈現的。程式能力很像騎腳踏車或是游泳，如果你想確實掌握的話，一定要親手試試看哦！

如果在實作的過程中遇到任何問題，歡迎你到我們的 Discord 伺服器的 #nlp 頻道裡提問哦！
[連結：https://discord.gg/g5Enb5zAyK](https://discord.gg/g5Enb5zAyK)

## 練習目標：
Python 裡支援兩種迴圈，一個是有終點的 [for 迴圈]，另一種是沒有終點的 [while 迴圈]。[for 迴圈] 能搭配我們之前提到的「元素」或是「索引」來操作。而 [while 迴圈] 則需要不停地操作迴圈成立條件。本週我們先練習 [while 迴圈]。
1. while + 迴圈成立條件

## 說明：
一個 [while 迴圈] 的結構長這個樣子：  

```python
給 [迴圈成立條件] 一個初始值
while [迴圈成立條件]成立:
    做些操作
    更新[迴圈成立條件]
```
需要特別注意的是，只要 [**迴圈成立條件**] 是 True，那麼程式就會繼續執行 [**做些操作**] 的部份。因此我們需要考慮是不是會一個不小心寫出了一個「迴圈成立條件永遠都成立」的無限迴圈。

例如：

```python
#無限迴圈示範
xCounter = 1
while xCounter >= 1:
    xCounter = xCounter + 1
    print("xCounter 最新的值是 {}".format(xCounter))
```

如果你的程式陷入這種***無限迴圈***，在 WingIDE 下，請點擊工具列上的紅色方塊讓它停止；在終端機 (Terminal) 或是 Windows 的命令提示字元視窗裡的話，請同時按下 `Ctrl + c` 兩個鍵讓它停下來。然後修正你的 [while 迴圈]。

一個 [while 迴圈] 的執行邏輯是這樣的…

如同下圖所示：
<kbd>
![](./media/whileLoop01.gif)
</kbd>

在上圖中，可以看到三個最重要的條件一定要有！

1. 初始條件
2. 迴圈成立條件：一旦這個條件不存在，就會離開這個 [while 迴圈]
3. 更新條件：[while 迴圈] 的成立條件必需要是持續更新的，否則就會寫出一個永遠走不出去的無限迴圈。

一般而言 [while 迴圈] 和語言學比較沒有關係。但是它在做 NLP 的資料清洗 (data wash) 的時候是很重要的前處理步驟。

比如說，我們可能讀入了一篇文本，把它切成列表 (list) 以後，裡面有很多空行或是我們不需要的字串。


如下圖所示：
<kbd>
![](./media/whileLoop02.gif)
</kbd>

在輸入的 `inputText` 裡，有許多的空行寫著 "**N/A**"。由於我們不知道裡面有幾個 "**N/A**"，但我們希望做的事情是「只要有 "**N/A**"，就把它移除 (**`.remove()`**)。那麼就可以先利用 **`.split("\n")`** 把字串切成一個列表 sLIST。

接下來的邏輯就是：

1. 以 sLIST 有 "**N/A**" 做為初始條件。
2. 當 sLIST 裡面還存在著 "**N/A**" 的時候…當做迴圈成立條件。
3. 只要迴圈成立，就把 sLIST 裡的 "**N/A**" 透過 **`.remove()`** 來移除，以此來更新 sLIST，做為這個 [while 迴圈] 的更新條件。

我把程式碼列在下面，你可以試一試：

```python
inputText = """John\n
N/A\n
N/A\n
Mary\n
Jack"""

sLIST = inputText.split("\n")
print("原本的 sLIST: {}".format(sLIST))
while "N/A" in sLIST:
    sLIST.remove("N/A")
print("處理完後的 sLIST:{}".format(sLIST))
```
也就是把 adjLIST 的第 i 個元素取出來，把它加上 "-ne" 的詞尾以後，再把它塞回 adjLIST 的第 i 個位置。


## 練習 w06_01：
> 上面的範例裡，處理完後的 sLIST 裡還有一堆空字串 "" 。請試著完成下列的 [while 迴圈] 來把這些空字串移除，讓處理後的 sLIST 變成 `['John', 'Mary', 'Jack']` 這樣的內容吧。

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputLIST):
    #<在此行以下設計你的程式。別忘了把答案透過 return 做回傳哦！>
    return None
    
if __name__ == "__main__":
    sLIST = ['John', '', '', '', 'Mary', '', 'Jack']
    print("處理前的 sLIST:{}".format(sLIST))
    sLIST = main(sLIST)
    print("處理後的 sLIST:{}".format(sLIST))
```
