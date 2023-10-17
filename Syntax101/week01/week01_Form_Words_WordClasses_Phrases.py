#!/usr/bin/env python3
# -*- coding:utf-8 -*-



def main(wordSTR="", wordClass="", refLIST=[]):
    '''
    main() is the main function of this program
    input:
        wordSTR   => string: the word to be tested
        wordClass => string: "verb", "noun", "adjective", "preposition"
        refLIST   => list: corpus of reference sentences
    output:
        True => boolean (the wordSTR belongs to the wordClass)
        False => boolean (the wordSTR does not belong to the wordClass)
    '''
    if wordClass == "":
        return "Please specify a word class. e.g., verb, noun, adjective, preposition"
    else:
        if wordClass in ("verb", "noun", "adjective", "preposition"):
            pass
        else:
            return "Please specify a word class. e.g., verb, noun, adjective, preposition"

    if refLIST == []:
        return "Please provide sentences for word class alculation"
    else:
        pass

    if wordClass == "verb":                                #wordClass="verb" => use verbChecker() to check if wordSTR is a verb.
        resultBOOL = verbChecker(wordSTR, refLIST)
    elif wordClass == "adjective":
        resultBOOL = adjectiveChecker(wordSTR, refLIST)    #wordClass="adjective" => use adjectiveChecker() to check if wordSTR is an adjective.
    elif wordClass == "noun":
        resultBOOL = nounChecker(wordSTR, refLIST)         #wordClass="noun" => use nounChecker() to check if wordSTR is a noun.
    else:
        resultBOOL = prepositionChecker(wordSTR, refLIST)  #Check if wrodSTR is a preposition

    return resultBOOL

def verbChecker(wordSTR, refLIST):
    '''
    verbChecker() checks if the wordSTR is a verb with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is a verb)
        False => boolean (the wordSTR is not a verb)
    '''
    # Because an English verb may ends with no affix, with affix -s, with affix -ing and with affix -ed
    # (Verbs with past {-ed}, participles {-ing}, {-en}, gerund {-ing}.), we design a checkingLIST as
    # below and see if wordSTR, wordSTRs, wordSTRing, wordSTRed are in the refLIST.
    # If they all of them can be found in the refLIST, it is very possible that the wordSTR is an English verb.

    resultBOOL = True
    for i in ("", "s", "ing", "ed"): #Here lists all possible verb endings with/without affixes
        if wordSTR+i in ",".join(refLIST):
            pass
        else:
            resultBOOL = False
    return resultBOOL

def adjectiveChecker(wordSTR, refLIST):
    '''
    adjectiveChecker() checks if the wordSTR is a adjective with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is an adjective)
        False => boolean (the wordSTR is not an adjective)
    '''
    # Because an English adjective may ends with no affix, with affix -er, with affix -est and with affix -ly,
    # we design a checkingLIST as below and see if wordSTR, wordSTRer, wordSTRest, wordSTRly are in the
    # refLIST. If they all of them can be found in the refLIST, it is very possible that the wordSTR is
    # an English verb.

    if wordSTR.endswith("y"):            #This block deals with words ends with -y and turns it into -i. e.g., hungry -> hungri
        wordSTRstem = wordSTR[:-1]+"i"
    else:
        wordSTRstem = wordSTR

    counter = 0
    if wordSTRstem in ",".join(refLIST):
        counter = counter + 1

    for i in ("er", "est", "ly"):
        if wordSTRstem+i in ",".join(refLIST):
            counter = counter + 1
        else:
            pass

    if counter >= 2:
        resultBOOL = True
    else:
        resultBOOL = False

    return resultBOOL

def nounChecker(wordSTR, refLIST):
    '''
    nounChecker() checks if the wordSTR is a noun with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is a noun)
        False => boolean (the wordSTR is not a noun)
    '''
    # Because an English noun may ends with no affix, with affix -s, with a determiner the/a/an goes before it,
    # we design a checkingLIST as below and see if wordSTR, wordSTRs, the/a/an wordSTR are in the
    # refLIST. If they all of them can be found in the refLIST, it is very possible that the wordSTR is
    # an English noun.
    resultBOOL = True
    for i in ("", "s"):  # Nouns with plural {-s}.
        if wordSTR+i in ",".join(refLIST):
            break
        elif " a {} ".format(wordSTR) in ",".join(refLIST):
            break
        elif " an {} ".format(wordSTR) in ",".join(refLIST):
            break
        elif " the {} ".format(wordSTR) in ",".join(refLIST):
            break
        else:
            resultBOOL = False
    return resultBOOL

def prepositionChecker(wordSTR, refLIST):
    '''
    prepositionChecker() checks if the wordSTR is a preposition with the refLIST as reference.
    input:
        wordSTR => string
        refLIST => list
    output:
        True  => boolean (the wordSTR is a preposition)
        False => boolean (the wordSTR is not a preposition)
    '''
    # Because an English prepositions do not change its form in any contexts (Prepositions are morphologically inert.)
    # we design a checkingLIST as below and see if a bare wordSTR exists and it cannot be a verb, a noun or an adjective.
    # If it cannot be used as a verb, as a noun or as an adjective, it is very possible that the wordSTR is an English preposition.

    resultBOOL = True
    if verbChecker(wordSTR, refLIST):        #Use verbChecker() to see if it is morphologically like a verb.
        resultBOOL = False
    elif adjectiveChecker(wordSTR, refLIST): #Use adjectiveChecker() to see if it is morphologically like an adjective.
        resultBOOL = False
    elif nounChecker(wordSTR, refLIST):      #Use nounChecker() to see if it is morphologically like a noun.
        resultBOOL = False
    return resultBOOL



if __name__ == "__main__":
    # [注意] 本程式的設計目的在於簡單地示範如何利用 Python 程式語言來執行語言分析工作。本程式中的函式 (function)
    # 仍需調整與深化以便在生產環境中使用。
    # [Notice] This is a simple demonstration showing how to use Python to do linguistics,
    # The functions provided may need further improvement for production purpose.

    #[tw] 利用以下提供的語料 (corpus) 和前述的函式 (function) 計算輸入的「未知詞」的詞性
    #[en] Determine categorical status of the unknown word with the corpus and the functions provided:
    corpusLIST = ["John likes to glonk in the afternoons",
                  "He never glonks on Sundays",
                  "He started glonking when he was fourteen",
                  "He once glonked an out-of-work actress",
                  "He’s never glonken any of his classmates",
                  "John was feeling nurgy, but happy",
                  "He’s nurgier than anyone I know"
                  "He’s been behaving very nurgily all week",
                  "John is a bong, and so is Fred",
                  "In fact, they’re both typical bongs",
                  "She put the car ung the garage",
                  "She made sure that it was right ung",
                ]


    #[tw] 測試 'glonk' 是不是動詞
    #[en] Test if 'glonk' is a verb or not.
    unknownWord = "listen"
    category = "verb"
    resultBOOL = main(wordSTR=unknownWord, wordClass=category, refLIST=corpusLIST)
    print("Is '{}' a {}? {}".format(unknownWord, category, resultBOOL))

    #[tw] 測試 'nurgy' 是不是形容詞
    #[en] Test if 'bong' is an adjective or not.
    unknownWord = "nurgy"
    category = "adjective"
    resultBOOL = main(wordSTR=unknownWord, wordClass=category, refLIST=corpusLIST)
    print("Is '{}' an {}? {}".format(unknownWord, category, resultBOOL))

    #[tw] 測試 'bong' 是不是名詞
    #[en] Test if 'bong' is a noun or not.
    unknownWord = "bong"
    category = "noun"
    resultBOOL = main(wordSTR=unknownWord, wordClass=category, refLIST=corpusLIST)
    print("Is '{}' a {}? {}".format(unknownWord, category, resultBOOL))

    #[tw] 測試 'ung' 是不是介系詞
    #[en] Test if 'ung' is a preposition or not.
    unknownWord = "ung"
    category = "preposition"
    resultBOOL = main(wordSTR=unknownWord, wordClass=category, refLIST=corpusLIST)
    print("Is '{}' a {}? {}".format(unknownWord, category, resultBOOL))
