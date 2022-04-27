# Form: Data/Info in Languages
本系列的練習裡，將透過實際操作 Python 程式語言來理解「自然語言」裡的資料/資訊，在程式語言裡是如何呈現的。程式能力很像騎腳踏車或是游泳，如果你想確實掌握的話，一定要親手試試看哦！

如果在實作的過程中遇到任何問題，歡迎你到我們的 Discord 伺服器的 #nlp 頻道裡提問哦！
[連結：https://discord.gg/g5Enb5zAyK](https://discord.gg/g5Enb5zAyK)

## 練習目標：
各種程式語言裡都有「條件判斷」的寫法。在 Python 裡，這種功能主要是由 `if...else...` 所扮演的。這項功能，別說在自然語言裡了，其實在人類的認知裡也是不斷地在做。

人類的認知系統就是不斷地在判斷「一樣？不一樣？」就如同我們在做語言分析的時候也是不斷地在比較「這個音和那個音，一不一樣？這個詞彙和那個詞彙，雖然詞綴不同，但字根是一樣還是不一樣？」

本次學習 `if...else...` 的篇幅較長，且會結合之前 week01 到 week06 的內容一併操作。

## 說明：
一個 [if...else...條件判斷式] 的基本結構長這個樣子：  

```python
if 條件A == 條件B:
    做某些操作
else:  #else 指的是「其它情況下」。口語上可以讀做「要不然…」
    做其它操作
```
然而，有時候我們的判斷不是只有 [條件A] 和 [條件B] 兩項而已，可能有三項甚至是多項，此時的 [if...else...] 進階的結構是長這樣子：
```python
if 條件A == 條件B:
    做某些操作
elif 條件A == 條件C:
    做另一些操作
elif 條件A == 條件D:
    做另一些操作
else:  #else 指的是「其它情況下」。口語上可以讀做「要不然…」
    做其它操作
```
其中， `elif...` 的段落是可以多現多組的。

和 `=` 單一等號表示「賦值」的用法不同的是，這裡用的兩個等號 `==` 可以理解成是一個問句，搭配 `if...` 來使用的意思是「是不是等值於…」。因此 `if 條件A == 條件B:` 意思就是「條件A 是不是等值於 條件B」。

在做 `if...else...` 的條件判斷時，除了使用 `==` 來表示「等值」之外，也可以用 `!=` 來表示「不等值」。這個 `!` 的用法，和語言學裡的邏輯語意學是一致的，用來表示「否定」。

既然可以比「是不是等值於…」，自然也可以做「是不是大於…」或「是不是小於…」。寫法也非常簡單直覺：

```python
x = 8
y = 12
if x > y:
    print("x 比 y 大")
elif x < y :
    print("x 比 y 小")
else: #依三一律，兩數字若 X 不大於 Y，也不小於 Y，那麼 X 必然等於 Y
    print("x 等於 y")
```
或是，如果你設計程式的條件是允許接受「`>=` 大於等於」或是「`<=` 小於等於」的話，那麼也能這樣寫：

```python
x = 8
y = 12
if x >= y:
    print("x 比 y 大")
elif x <= y :
    print("x 比 y 小")
else: #依三一律，兩數字若 X 不大於 Y，也不小於 Y，那麼 X 必然等於 Y
    print("既不是大於等於，也不是小於等於，這兩數的關係違反三一律吧！")
```

對 Python 而言，我們也能表示「在兩者之間」，寫法像這樣：

```python
x = 8
y = 12
z = 10
if x < z < y:
    print("z 比 x 大，但比 y 小")
else:
    print("x, z, y 三者的關係不是由小到大")
```

講了這麼多，好像都只是在比大小。但「條件」可不是只有大小而已。我們也可以使用列表 (list) 或是字串 (string) 的一些方法來使用 `if...else...` 條件判斷式。

```python
str01 = "internationalization"
str02 = "nation"

if str02 in str01:
    print("str01 內包含 str02")
else:
    print("str01 內不包含 str02")
```

或是

```python
str01 = "inter-nation-al-iza-tion"
str02 = "nation"
list01 = str01.split("-") #利用 .split() 把 str01 分切成 list01 的列表型式

if str02 in list01:
    print("list01 內包含 str02")
else:
    print("list01 內不包含 str02")
```

此時，你應該可以想像得到，我們可以結合 `for...` 和 `if...else...` ，利用 `-ing` 和 `-ed` 的詞綴來抓出一篇文章中所有可能的「規則動詞」：

```python
textSTR = """US diplomats returned to Ukraine today for the first time since Russia invaded Ukraine, according to a source familiar with the matter.
The diplomats crossed into the country from Poland and traveled to the western city of Lviv for a day trip, according to the source. 
The visit comes after US Secretary of State Antony Blinken told Ukrainian President Volodymyr Zelensky that the US would send diplomats into the country starting this week when he visited the Ukrainian capital over the weekend. """

textSTR = textSTR.replace("\n", "") #移除段落切換時的換行
textSTR = textSTR.replace(".", "").replace(",", "") #移除標點符號
textLIST = textSTR.split(" ") #利用空格將整篇文章變成 list 的列表形式
possibleVerbLIST = [] #準備一個空列表，用來承接稍後抓出來的可能動詞

for i in textLIST:  #以 for...迴圈掃過整個 textLIST，一次拿一個元素出來
    if i.endswith("ed"):  #用 if...條件判斷式，配合 .endswith() 來判斷這個元素 i 是不是以 "ed" 結尾
        possibleVerbLIST.append(i)  #若是，則把這個元素 i 用 .append() 加到 possibleVerbLIST 裡
    elif i.endswith("ing"): #用 if...條件判斷式，配合 .endswith() 來判斷這個元素 i 是不是以 "ing" 結尾
        possibleVerbLIST.append(i)  #若是，則把這個元素 i 用 .append() 加到 possibleVerbLIST 裡
    else:
        pass #pass 表示什麼也不做。直接略過

print("全文中可能的動詞有：{}".format(possibleVerbLIST))
```

這麼一來，就能利用 `for...迴圈` 和 `if...else...條件判斷式` 的結合，快速地掃出目標詞彙。想查詢字串型態的資料，除了 .endswith() 以外還有哪些內建的方法也可以搭配 `if...else...條件判斷式` 使用的話，可以查看這個網頁裡的總結：[https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)。只要是說明文字裡出現 "***Returns true...***" 開頭的文字，就表示這個方法會回傳「是」或「不是」做為答覆，這就是可以放在 `if...else...條件判斷式` 裡的東西了。

除了字串的操作以外，也可以用列表配合 `in` (可讀做「在裡面」) 來操作 `if...else...條件判斷式`：

```python
textSTR01 = "US diplomats returned to Ukraine today for the first time since Russia invaded Ukraine, according to a source familiar with the matter."
textSTR02 = "The diplomats crossed into the country from Poland and traveled to the western city of Lviv for a day trip, according to the source."
textSTR03 = "The visit comes after US Secretary of State Antony Blinken told Ukrainian President Volodymyr Zelensky that the US would send diplomats into the country starting this week when he visited the Ukrainian capital over the weekend."

targetWord = "US" #從 textSTR01, textSTR02, textSTR03 三個字串裡，找出哪一個含有 US 這個字

for i in [textSTR01, textSTR02, textSTR03]:
    textSTR = i.replace("\n", "") #把元素 i 的內容移除段落切換時的換行，然後存入 textSTR
    textSTR = textSTR.replace(".", "").replace(",", "") #移除標點符號
    textLIST = textSTR.split(" ") #利用空格將整篇文章變成 list 的列表形式
    if targetWord in textLIST:  #如果 targetWord 在 textLIST 裡面
        print("在文本 {} 裡，找到目標詞 {}！".format(i, targetWord))
    else:
        pass
```


## 練習 w07_01：
> 在 main() 方法裡設計你的程式，仿照上面的程式，用盡你已知的一切 Python 知識，計算 news.txt 文章中出現了幾次 Musk，以及幾次 Musk's。

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def main(inputSTR, targetSTR):
    #<在此行以下設計你的程式。別忘了把答案透過 return 做回傳哦！>
    return None
    
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
  
```
