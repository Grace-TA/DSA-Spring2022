# Lab8: 排序與搜尋 (Sort & Search)

<a name="000"/>

## 目錄(Table of Contents)

[1. 試說明什麼是排序 (Sorts)? 為什麼要學排序?](#111)

[2. 請執行課程中介紹六種排序法的Python程式並試著說明其方法與結果](#222)

[3. 試說明什麼是搜尋 (Search)?](#333)

[4. 請執行課程中介紹二種搜尋法的Python程式並試著說明其方法與結果](#444)

[5. 挑戰題: 自由選擇, 想讓自己變得更強的同學可試試!](#555)

<a name="111"/>

## 1. 試說明什麼是排序 (Sorts)? 為什麼要學排序?

### 什麼是排序 (Sorts)?
> 在計算機科學與數學中，一個排序演算法（英語：Sorting algorithm）是一種能將一串資料依照特定排序方式進行排列的一種演算法。最常用到的排序方式是數值順序以及字典順序。有效的排序演算法在一些演算法（例如搜尋演算法與合併演算法）中是重要的，如此這些演算法才能得到正確解答。排序演算法也用在處理文字資料以及產生人類可讀的輸出結果。基本上，排序演算法的輸出必須遵守下列兩個原則：

>1.1 輸出結果為遞增序列（遞增是針對所需的排序順序而言）

>1.2 輸出結果是原輸入的一種排列、或是重組

Source: https://zh.wikipedia.org/

### 為什麼要學排序?

>排序是學習遞歸和迭代的時間和空間複雜度分析的最佳算法之一。 例如，桶排序、插入排序、選擇排序、堆排序和計數排序的分析是學習各種類型循環的最佳、最壞和平均情況分析的好主意。

[return to content](#000) 

<a name="222"/>

## 2. 請執行課程中介紹六種排序法的Python程式並試著說明其方法與結果. (每個方法只要選一支來說明即可.)

### 2.1 泡泡排序 (Bubble Sort) → 起手式! → 由左到右PK

### A. Use 2 for loops

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176988410-758332b5-88c2-42fa-b802-ac88411bb274.png">

### B. Use Python built-in function (i.e., sort(), short(reverse=True))

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176988482-02e6f0c1-0c1f-4db3-ae21-20e42d4cb891.png">

### 2.2 選擇排序 (Selection Sort) → Min → Swap

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176988882-056ed46c-1ba3-4c15-a62b-0d5b86ffd2fe.png">

### 2.3 插入排序 (Insertion Sort) → 和左邊的數比

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176989340-434bd802-b270-423e-9890-4baf2b1880a6.png">

### 2.4 Heap Sort (堆積排序法) → tree

````python
# ch9_9.py
class Heaptree():
    def __init__(self):
        self.heap = []                              # 堆積樹串列
        self.size = 0                               # 堆積樹串列元素個數

    def data_down(self,i):
        ''' 如果節點值大於子節點值則資料與較小的子節點值對調 '''
        while (i * 2 + 2) <= self.size:             # 如果有子節點則繼續
            mi = self.get_min_index(i)              # 取得較小值得子節點
            if self.heap[i] > self.heap[mi]:        # 如果目前節點大於子節點
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]  
            i = mi

    def get_min_index(self,i):
        ''' 傳回較小值的子節點索引 '''
        if i * 2 + 2 >= self.size:                  # 只有一個左子節點
            return i * 2 + 1                        # 傳回左子節點索引
        else:           
            if self.heap[i*2+1] < self.heap[i*2+2]: # 如果左子節點小於右子節點
                return i * 2 + 1                    # True傳回左子節點索引
            else:
                return i * 2 + 2                    # False傳回右子節點索引

    def build_heap(self, mylist):                       
        ''' 建立堆積樹 '''
        i = (len(mylist) // 2) - 1                  # 從有子節點的節點開始處理
        self.size = len(mylist)                     # 得到串列元素個數
        self.heap = mylist                          # 初步建立堆積樹串列
        while (i >= 0):                             # 從下層往上處理
            self.data_down(i)
            i = i - 1

    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        print('Element count = %d' % len(self.heap), self.heap)
        self.heap.pop()
        self.data_down(0)
        return min_ret

data = [10, 21, 5, 9, 13, 28, 3]
print("原始串列 : ", data)
obj = Heaptree()
obj.build_heap(data)                                # 建立堆積樹串列
print("執行後堆積樹串列 = ", obj.heap)
sort_h = []
for i in range(len(data)):
    sort_h.append(obj.get_min())
print("排序結果 : ", sort_h)
````
<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176989672-610f15a4-3e55-4d73-8331-b88c7f2c5824.png">

### 2.5 Quick Sort (快速排序) → recursive

````python
import random

def quick_sort(nLst):
    ''' 快速排序法 '''
    if len(nLst) <= 1:
        return nLst

    left = []                           # 左邊串列
    right= []                           # 右邊串列
    piv = []                            # 基準串列
    pivot = random.choice(nLst)         # 隨機設定基準
    print('pivolt result:', pivot)
    for val in nLst:                    # 分類
        if val == pivot:
            piv.append(val)             # 加入基準串列
        elif val < pivot:               # 如果小於基準
            left.append(val)            # 加入左邊串列
        else:
            right.append(val)           # 加入右邊串列
    return quick_sort(left) + piv + quick_sort(right)
        
data = [6, 1, 5, 7, 3, 9, 4, 2, 8] 
print("原始串列 : ", data)
print("排序結果 : ", quick_sort(data))

````

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176989958-9dc09ad7-a2af-4320-9475-95624d3008f9.png">


### 2.6 Merge Sort (合併排序法) → recursive

````python
def merge(left, right):
    ''' 兩數列合併 '''
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right

    print('left, right, oupt =', left, right, output)    
    return output

def merge_sort(nLst):
    ''' 合併排序 '''
    if len(nLst) <= 1:                      # 剩下一個或0個元素直接返回
        return nLst    
    mid = len(nLst) // 2                    # 取中間索引
    print('len(nLst) // 2 = ', mid, nLst[:mid], nLst[mid:] )
    # 切割(divide)數列
    left = nLst[:mid]                       # 取左半段
    right = nLst[mid:]                      # 取右半段
    # 處理左序列和右邊序列
    left = merge_sort(left)                 # 左邊排序
    right = merge_sort(right)               # 右邊排序
    # 遞迴執行合併
    return merge(left, right)               # 傳回合併

data = [6, 1, 5, 7, 3, 9, 4] 
print("原始串列 : ", data)
print("排序結果 : ", merge_sort(data))

````

<img width="220" alt="image" src="https://user-images.githubusercontent.com/89304181/176990200-1497547a-b97b-4135-aea3-10c431e89920.png">

[return to content](#000) 

<a name="333"/>

## 3. 試說明什麼是搜尋 (Search)? 

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/176993084-59d63192-e624-43b2-8530-309e2a9c5686.png">

[return to content](#000) 

<a name="444"/>

## 4. 請執行課程中介紹二種搜尋法的Python程式並試著說明其方法與結果. (每個方法只要選一支來說明即可.)

## 4.1 順序搜尋法:

> 線性搜尋，又稱為循序搜尋（sequential search），是一個在序列中找尋目標的方法。正如字面上的意義，線性搜尋會按照順序疊代序列，挨家挨戶比對每個元素與目標值是否相等，若相等則停止疊代，並回傳搜尋所得結果。線性搜尋乍看之下，是最簡單實作也最 naïve 的實作，效能應該不怎麼好。事實上，在資料量不多時（少於 100 個元素），線性搜尋的效能也不會太差，但對於資料量大時　＋　＂運氣不好＂，那就要找很久，對吧？。

````python
# ch10_1.py
def sequential_search(nLst):
    for i in range(len(nLst)):

        if nLst[i] == key:      # 找到了
            return i            # 傳回索引值
        else:
          print('在 %d 索引位置找, no found!' % i)

    return -1                   # 找不到傳回-1

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
key = eval(input("請輸入搜尋值 : "))
index = sequential_search(data)
if index != -1:
    print("在 %d 索引位置找到了共找了 %d 次" % (index, (index + 1)))
else:
    print("查無此搜尋號碼")

````
### Result

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/177027154-203385d4-e33b-443e-b087-31eb5ab7743f.png">

## 4.2 二分搜尋法:

> 取 已排序資料的中間索引的值，來確認是否為要搜尋的數，若不是，則將資料以中間索引分為兩半。此時便比較待搜尋的值與中間索引的值的大小，若比較小，則選擇較小的那一半資料，反之亦然。接著再繼續從一半的資料中取中間索引的值做比較，重複以上的步驟，直到找到為止。

````python
# ch10_2.py
def binary_search(nLst):
    print("列印搜尋串列 : ",nLst)
    low = 0                     # 串列的最小索引
    high = len(nLst) - 1        # 串列的最大索引
    middle = int((high + low) / 2)  # 中間索引
    times = 0                   # 搜尋次數
    while True:
        times += 1
        print('No.%d: L%d:%d M%d:%d: , H%d:%d' % (times, low,nLst[low], middle,nLst[middle], high, nLst[high]))

        if key == nLst[middle]: # 表示找到了
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1    # 下一次往右邊搜尋
        else:
            high = middle - 1   # 下依次往左邊搜尋
        middle = int((high + low) / 2)  # 更新中間索引
        if low > high:          # 所有元素比較結束
            rtn = -1
            break
    return rtn, times

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
print('1. Original data: ', data)
sorted_data = sorted(data)      # 排序串列
print('2. Sorted data: ', sorted_data)
key = int(input("請輸入搜尋值 : "))

print('3. Binary serach start ...')
index, times = binary_search(sorted_data)
if index != -1:
    print("4. 在索引 %d 位置找到了,共找了 %d 次" % (index, times))
else:
    print("查無此搜尋號碼")

````

#### Result

<img width="555" alt="image" src="https://user-images.githubusercontent.com/89304181/177027304-3e00ea29-46f4-4409-a764-1ceec4b9c192.png">

[return to content](#000) 

<a name="555"/>

## 5. 挑戰題: 想讓自己變得更強的同學可試試! 

### Q1: 請同學寫一個程式, 用順序搜尋法來自動找到以下List內的最小值,並回傳完成搜尋所需的步數

data = [99, 22, 10, 30, 90, 77, 65, 1, 88]

````python
data = [99, 22, 10, 30, 90, 77, 65, 1, 88]

def minvalue(nLst):
  minval = 9e99 # initial value of minval
  for i in nLst:
    if i < minval:
      minval = i
      print('Get a smaller value, %d' % i)
  return minval

print('List內的最小值 = %d' % minvalue(data))

''' Output Result
Get a smaller value, 99
Get a smaller value, 22
Get a smaller value, 10
Get a smaller value, 1
List內的最小值 = 1
'''
````



### Q2: 請同學寫一個程式, 用二分搜尋法來自動找到以下List內的最小值,並回傳完成搜尋所需的步數

data = [99, 22, 10, 30, 90, 77, 65, 1, 88]

````python
def binary_search(nLst):
    print("列印搜尋串列 : ",nLst)
    low = 0                     # 串列的最小索引
    high = len(nLst) - 1        # 串列的最大索引
    middle = int((high + low) / 2)  # 中間索引
    times = 0                   # 搜尋次數
    while True:
        times += 1
        print('No.%d: L%d:%d M%d:%d: , H%d:%d' % (times, low,nLst[low], middle,nLst[middle], high, nLst[high]))

        if key == nLst[middle]: # 表示找到了
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1    # 下一次往右邊搜尋
        else:
            high = middle - 1   # 下依次往左邊搜尋
        middle = int((high + low) / 2)  # 更新中間索引
        if low > high:          # 所有元素比較結束
            rtn = -1
            break
    return rtn, times

data = [99, 22, 10, 30, 90, 77, 65, 1, 88]

print('1. Original data: ', data)
sorted_data = sorted(data)      # 排序串列
print('2. Sorted data: ', sorted_data)

key = sorted_data[0] # Obtain the min value from sorted data

print('3. Binary serach start ...')
index, times = binary_search(sorted_data)
if index != -1:
    print("4. 在索引 %d 位置找到了,共找了 %d 次" % (index, times))

''' Output Result
1. Original data:  [99, 22, 10, 30, 90, 77, 65, 1, 88]
2. Sorted data:  [1, 10, 22, 30, 65, 77, 88, 90, 99]
3. Binary serach start ...
列印搜尋串列 :  [1, 10, 22, 30, 65, 77, 88, 90, 99]
No.1: L0:1 M4:65: , H8:99
No.2: L0:1 M1:10: , H3:30
No.3: L0:1 M0:1: , H0:1
4. 在索引 0 位置找到了,共找了 3 次
'''

````

### Q3: 一樣的List, 誰比較快找到最小值, 為什麼? 2022.06.30

> Ans: 在此具有9個Element的List中, Linear Search要4個Steps; 而Bineary Search要3個Steps; 因此, Bineary Search比較快;
> 此外, 由於在Time Complexity的特性之下, Linear Search is O(n), Bineary Search is O(log(n)); 在List Size越大的情況之下, > Binary Search會有更佳的表現.

![image](https://user-images.githubusercontent.com/89304181/177028404-d345b0b9-2923-4992-b8eb-59f86ac9dbe5.png)


[return to content](#000) 
