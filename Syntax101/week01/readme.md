#Form: Words, Word Classes, Phrases

本次的練習裡，將利用課堂中提到的「構詞上的証據」來做詞彙的詞性分類 (Word classification. a.k.a Part-of-Speech classification, word categorization)

## 練習目標：

1. 執行 **week01_Form_Words_WordClasses_Phrases.py** 並取得如下的輸出結果：
```python
Is 'glonk' a verb? True
Is 'nurgy' an adjective? True
Is 'bong' a noun? True
Is 'ung' a preposition? True
```

>  操作方式：
> 1. 用 WingIDE 打開 **week01_Form_Words_WordClasses_Phrases.py** 程式碼。
> 2. 點擊畫面上方的綠色三角形，執行程式。
> 3. 觀看畫面下方跳出的結果

2. 將 `glonk`、`nurgy`、`bong` 和 `ung` 改成四個英文真正存在的詞彙。四個字的詞性分別為：動詞 see、形容詞 hungry、名詞 food 和介系詞 on。再做一次目標 1 的操作。取得如下的結果：
```python
Is 'see' a verb? False
Is 'hungry' an adjective? False
Is 'food' a noun? False
Is 'on' a preposition? False
```
> 操作方式：
> 1.  WingIDE 打開 **week01_Form_Words_WordClasses_Phrases.py** 程式碼。
> 2. 把程式中，**第 177 行**「測試 'glonk' 是不是動詞」的 `unknownWord = "glonk"` 改成 `unknownWord = "see"`。如法泡製在其後的**第 186 行**、**第 193 行**和**第 200 行**。
> 3. 點擊畫面上方的綠色三角形，執行程式。
> 4. 觀看畫面下方跳出的結果

## 討論：
明明給的是 "see"、"hungry"、"food" 和 "on" 這四個詞性和拼字都正確的詞彙了。但是程式卻沒辦法正確地辨識出它們的詞性，這是因為我們給程式的參考資料只有 corpusLIST 裡的 12 個句子。

換言之，程式只能從這 12 個句子做為素材，依據我們在 verbChecker()、nounChecker()、adjectiveChecker() 和 prepositionChecker() 中的演算法來推估它所收到的詞彙 (i.e., "see", "hungry", "food", "on") 是什麼詞性。

如果這四個字剛好很少見於 corpusLIST 的話，那麼它的推估就是無效的了。

改善的方法，就是給 corpusLIST 裡多增加一些含有 "see"、"hungry"、"food" 和 "on" …等等詞彙的英文句子。就像是給讓程式像人類學習語言時一樣，「憑著內在的規則，多閱讀文本，多接受語言刺激」這麼一來，它就能學會更多詞彙的詞性囉。

## 進階說明：
程式結構如下流程說明。  
![flowchart](https://github.com/Droidtown/NLP_TrainingLab/blob/main/Syntax101/week01/week01.drawio.png  "flowchart")

程式從進入點 **`if __name__ == "__main__":`** 開始執行。首先呼叫 `main()` 函式。而 `main()` 函式依指定的變數為 "verb", "noun", "adjective" 或 "preposition" 將資料傳給四個子函式各自進行運算後。取得結果為 True 或 False，並回傳給 `main()`。

`main()` 將結果存入 `resultBOOL`之後，印出於畫面上。