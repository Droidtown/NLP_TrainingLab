# Form: Data/Info in Languages
本系列的練習裡，將透過實際操作 Python 程式語言來理解「自然語言」裡的資料/資訊，在程式語言裡是如何呈現的。

## 練習目標：
1. 理解「字串」(string type)
2. 理解「數字」(number type)
	- 整數型 (integer number, int)
	- 小數型 (floating number, float)
3. 理解「列表」(list type)
4. 理解「元組」(tuple type)
5. 理解「字典」(dictionary type)

## 說明：
「字串」顧名思義就是「一串字」的意思。但在電腦程式的眼裡，它並不知道什麼是一個「字 (word)」，它只知道一個一個的「字符 (character)」。

如同我們在 Week01 的課堂中討論的「什麼是一個字？」(What makes a word?) 的問題。在英文裡，乍看之下好像很好理解。只要一串字符放在一起，有獨立的意義，就是一個 "word"。

例如：
> 第一個字：gonked  
> 第二個字：nergily  
> 第三個字：get up  

看到第三個字的時候，我們可以發現，「獨立的意義」這個定義似乎有點模糊。畢竟 "He always gets up in the afternoon." 這一串符號也是有獨立的意義，不同於另一串符號 "She sometimes goes to bed late." 的意義呀！

事實上，在語言學裡，"What makes a word" 可透過疑問句的位移律 (transformation rules) 來進行確認。但對程式語言來說，我們就可以有以下的操作來表示「一個字串」：

首先在 VirtualBox 裡啟動你的 NLP_TrainingLab 開發環境，然後打開 Wing Personal 8，並在右下角找到 [Python] 的分頁，輸入以下的內容：

```python
m01 = "gonked"      #輸入左側「井號」之前的文字。輸入完後鍵入 'Enter' 鍵換行。  
m02 = "nergily"      #對 Python 而言，任何以 # 符號以後的東西都會被忽略，故可做為註解說明文字使用。
m03 = "get up"  
m04 = "He always gets up in the afternoon."    
```
 
注意到我們加了一個 m01 表示「第一個被記住的字串 (memorized_string_01)」，此外，我們加上一個等號 `=` 把右邊的字串存入 m01~m04 裡。換言之，我們把 "butterfly" 這個字串，用引號括起來，存入 m01 裡；用引號把 "soup" 這個字串括起來，存入 m02 裡，也用一樣的操作方式把 "get up" 和 "He always gets up in the afternoon." 分別存入 m03 和 m04 裡。

執行完後，你會得到如下的畫面：
![](./media/week02_01.png)

我們首先注意到的是，m01 這個字串的最後兩個字符是英文的時態詞綴 `-ed`，如果想要把它拿掉的話，我們可以這麼做：

```python
...(承續前面的程式碼)
print("原本的 m01：{}".format(m01))             #使用 print() 函式，我們先看看 m01 是什麼樣子
print("移除時態的 m01：{}.format(m01[0:-2))      #使用 m01[0:-2]，表示把 m01 的內容從第 0 個間隙位置一路算到「到數第二個間隙位置」
```

其原理如下圖所示：
![](./media/week02_02.png)

## 練習 w02_01：
> 請把以下的 "glonk" 的變形，還原成它的原形 "glonk"：  
> 1. He glonks every morning.  
> 2. I was disglonking this morning, too.

```python
word01 = "glonks"
word02 = "disglonking"
word01_org = None   #請把 None 改成你的答案。
word02_org = None   #請把 None 改成你的答案。
print(word01_org)      #你的答案應該能讓這一行印出 glonk
print(word02_org)      #你的答案應該能讓這一行印出 glonk
```

