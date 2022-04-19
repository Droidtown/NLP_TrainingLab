# Form: Data/Info in Languages
本系列的練習裡，將透過實際操作 Python 程式語言來理解「自然語言」裡的資料/資訊，在程式語言裡是如何呈現的。程式能力很像騎腳踏車或是游泳，如果你想確實掌握的話，一定要親手試試看哦！

如果在實作的過程中遇到任何問題，歡迎你到我們的 Discord 伺服器的 #nlp 頻道裡提問哦！
[連結：https://discord.gg/g5Enb5zAyK](https://discord.gg/g5Enb5zAyK)

## 練習目標：
Python 裡支援兩種迴圈，一個是有終點的 [for 迴圈]，另一種是沒有終點的 [while 迴圈]。[for 迴圈] 能搭配我們之前提到的「元素」或是「索引」來操作。而 [while 迴圈] 則需要不停地操作終止條件 (endding condition)。本週我們先練習 [for 迴圈] 的三種變形。
1. for... + 元素
2. for... + 索引
3. for... + 元素的索引


## 說明：
一個 [for 迴圈] 的結構長這個樣子：  

```python
for 變數_i in 可依次取元素的東西_(字串、列表、元組...等):
    對 變數_i 做些操作
```
如此一來，[for 迴圈] 就會依次取出其後 `可依次取元素的東西` 中一次取出一個東西，當做 `變數_i` 來操作。這是一種 [for... + 元素] 的操作。

如同下圖所示：
<kbd>
![](./media/forLoop01.gif)
</kbd>

在上圖中，`可依次取元素的東西` 是一個 LIST，裡面有 5 個元素。而 [for 迴圈] 就每次取一個當做是 `變數_i`，再接著做其後的操作。先把這個 `變數_i` 變成大寫，然後存入 `upperSTR` 裡，再把 `upperSTR` 印出來。就可以依序得到 "THIS", "IS", "A", "DEMO", "LIST" 了。

除了放 LIST 以外，也可以放字串或是元組…等「**可被依次取元素**」的東西。這裡介紹一個 `range(x, y)` 的函式。它會回傳從 `x` 起算一直到 `y` 之前的整數值。這一個一個的整數值，也是一種**可被依次取元素**的東西。所以也能放在 [for 迴圈] 裡使用：

如下圖所示：
<kbd>
![](./media/forLoop02.gif)
</kbd>
看到這裡，應該想像得到…既然我們可以取整數，而不論是 string 的字串、list 的列表或是 tuple 的元組都可以用一個數字來取它的內容。回想一下…  

```python
dataSTR = "bicycle"
dataLIST = ["a" "bicycle"]
dataTUPLE = ("a", "bicycle")

print(dataSTR[1]) #取出 dataSTR 裡的第 1 個元素
print(dataLIST[1]) #取出 dataLIST 裡的第 1 個元素
print(dataTUPLE[1]) #取出 dataTUPLE 裡的第一個元素
```

那麼，我們就可以結合 LIST 和 range() 來操作一個列表內的東西，就像這樣：
<kbd>
![](./media/forLoop03.gif)
</kbd>

說白了，[for 迴圈] 就是自然語言裡的「每」與「都」(語言學的行話叫「全稱量化詞」)。像我們想理解這句話「每個人都帶了水壺」的意義的話，那麼在 [for 迴圈] 裡就會像這樣…

```python
peopleLIST = ["John", "Mary", "Peter"]
statusLIST = []
for p in peopleLIST:
    statusLIST.append(p+"帶了水壺")
```

如此一來，就能得到：

```python
statusLIST = ["John 帶了水壺", "Mary 帶了水壺", "Peter 帶了水壺"]
```

的命題了。這裡的「每」和「都」就是在你的心裡提示了「要理解這句話，你可得一個一個檢查過，才能確定這句話是真的」。這個「一個一個來」的部份，就是前文中提到的**從`可依次取元素的東西` 中一次取出一個東西**，也就是 [for 迴圈] 的奧義了。

這個東西在 NLP 的時候有什麼用呢？比如說，我們手上有法文的陽性形容詞列表：

```python
masculineLIST = ["paysan", "européen", "bon"]
```

而我們知道這幾個字的陰性變化，就是把它加上 "-ne" 的詞尾時，把它變成陰性的形容詞列表的方法，就可以這麼做：  

```python
masculineLIST = ["paysan", "européen", "bon"]
feminineLIST = []

for i in masculineLIST:
    feminineLIST.append(i+"ne")

print(feminineLIST)
```

在上面的例子裡，我們是特別準備了一個「陰性」的空列表來承裝變形後的結果。如果我們不準備新的空列表，而希望在原來的列表裡直接做操作的話，就可以這麼做：

```python
adjLIST = ["paysan", "européen", "bon"]

for i in range(0, len(adjLIST)):
    adjLIST[i] = adjLIST[i]+"ne"

print(adjLIST)
```
也就是把 adjLIST 的第 i 個元素取出來，把它加上 "-ne" 的詞尾以後，再把它塞回 adjLIST 的第 i 個位置。


## 練習 w05_01：
> 下列的英文名字都是有男生版和女生版的。男生版的名字，就是把女生版裡的最後一個 "-a" 拿掉就可以了。試試看用 [for 迴圈] 可以怎麼做？

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def convert2male(inputLIST):
    #<在此行以下設計你的程式。別忘了把答案透過 return 做回傳哦！>
    return None
    
if __name__ == "__main__":
    femaleLIST = ["Louisa", "Roberta", "Simona", "Carla"]
    maleLIST = convert2male(inputLIST)
    print("男生版的名字為：{}".format(maleLIST))
```
