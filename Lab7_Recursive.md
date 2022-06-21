# Lab7: 很厲害的東西 - 遞迴(Recursive, Recursion) ? 


<a name="000"/>
---

## 目錄(Table of Contents)

[Lab 7-1 什麼是遞迴 (What Is Recursion) ?](#111)

[Lab 7-2 遞迴圖形 (e.g., Fractal in Nature)](#112)

[Lab 7-3 遞迴經典應用](#113)

---
<a name="111"/>
## Lab 7-1 什麼是遞迴 (What Is Recursion) ?

### 1. 請用您自己的說法或是方式來介紹什麼是遞迴 (What Is Recursion) ?
Ans: 簡單來說，遞迴就是”在程式中自己呼叫自己” (什麼意思?)。比較學術的定義是函式中有呼叫自己(Self Calling)的敘述。

### 2. 遞迴建議的使用時機為何?
Ans: 在解決問題時，我們經常會遇到無法輕鬆使用 loop 或是 if statement就能處理的問題，像是走迷宮問題遇到死路時需要回到上一層計算、或是在解決河內塔問題時儘管操作相同，卻因為每次要進行操作的參數不同而需要寫重複的程式碼等等。此時，一個經常被納入考慮的方法，就是利用遞迴的概念來撰寫一個函式。

### 3. 參考程式今日介紹的程式 (R100, R110, R120), 完成1+2+...+30的加法練習

![image](https://user-images.githubusercontent.com/89304181/172033102-d0af25e1-bf14-44c3-b823-0b17dda82518.png)

![image](https://user-images.githubusercontent.com/89304181/172033159-dbaf3f4b-8437-4f7a-9e9c-a3fc1f7d3fe4.png)

[return to content](#000) 

<a name="112"/>

## Lab 7-2 遞迴圖形 (e.g., Fractal in Nature)

### 1. Add (3,1), (4,0), (5,1)
![image](https://user-images.githubusercontent.com/89304181/173219532-e8582a22-cae1-41cf-ba44-d0b7e5db7ed4.png)

### 2. Add (1.5, 0),(2, 0.5),(1, 0.5),(1.5, 1)
![image](https://user-images.githubusercontent.com/89304181/173219538-aed14fca-9341-4c9a-8595-6bee6801d8bd.png)

### 3. 海龜的“指令”只是一串字符: 試試看畫個八卦來看看
![image](https://user-images.githubusercontent.com/89304181/173219543-e972a4b5-7b62-4e17-91c1-b62c76d10873.png)

### 4. 海龜的“指令”只是一串字符: 試試看畫個六邊形 & 四邊形來看看
![image](https://user-images.githubusercontent.com/89304181/173219575-b88ea249-7b79-4cbc-bf2e-b0e8b2806a90.png)

![image](https://user-images.githubusercontent.com/89304181/173219580-55854418-8ea9-4a8e-be23-88d464bab446.png)

### 5. 用"字符串重寫"的方法,畫個八卦來看看

![image](https://user-images.githubusercontent.com/89304181/173219632-2de2347c-59c0-47c0-ae7d-cafdc9cc4d79.png)

plot_coords(turtle_to_coords(transform_sequence()))

### 6. 執行以下設定(transformations: 1 --> 3), 看到的圖形為何? 請解釋為什麼會有這樣改變?

````python
plot_coords(turtle_to_coords(transform_multiple('L', {
    'L': '-RF+LFL+FR-',
    'R': '+LF-RFR-FL+'
````
![image](https://user-images.githubusercontent.com/89304181/173219726-020a233d-b1fc-4dd5-838a-690ad6924d76.png)


### 7. 執行以下設定(iterations:90 --> 45), 看到的圖形為何? 請解釋為什麼會有這樣改變?

````python
plot_coords(turtle_to_coords(transform_multiple('L', {
    'L': '-RF+LFL+FR-',
    'R': '+LF-RFR-FL+'
}, 5), 45)) # transform_multiple(sequence, transformations, iterations)

````
![image](https://user-images.githubusercontent.com/89304181/173219998-7d5e5566-8245-47ae-8fea-155b2fd1dc0e.png)

### 8. 試試看參考分支龜圖形 (Branching Turtle Graphics)的方式, 完成以下圖形
````pytho

# ']' 命令告訴它到最後記住的位置 (e.g., (0,1))。 一旦海龜回到記憶的位置，
# 它就會立即忘記它，所以下一次調用 ']' 時，它會回到之前的最後記憶位置。
````
![image](https://user-images.githubusercontent.com/89304181/173220089-da586428-0186-4c76-a024-916fde99f516.png)

### 9. 參考l_plot()方式, 完成以下圖形

![image](https://user-images.githubusercontent.com/89304181/173220099-52c498bb-f321-4f95-9baa-07196a46881d.png)

### A. 參考l_plot()方式, 完成以下圖形

![image](https://user-images.githubusercontent.com/89304181/173220106-961efcbc-6858-4761-baa5-77fe8aa5489d.png)

[return to content](#000) 

<a name="113"/>

## Lab 7-3 遞迴經典應用

### 1. 試說明費波納契(Fibonacci)數列, 以及Python實作的參考作法?
Ans: 費波納契(Fibonacci)數列，此數列的公式如下：
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) 		n >= 2

thus, 費波納契(Fibonacci)數列 = [1, 1, 2, 3, 5, 8, 13, 21, ...]     

![image](https://user-images.githubusercontent.com/89304181/174704153-f757916e-6d90-45ae-a7bf-31cad57ee66a.png)

### 2. 試說明河內塔演算法, 以及Python實作的參考作法 (6圓盤)?
Ans: 移動規則如下：
    1：每次只能移動一個圓盤。
    2：只能移動最上方的圓盤。
    3：必須保持小的圓盤在大的圓盤上方。

![image](https://user-images.githubusercontent.com/89304181/174704415-e7c26353-5834-4072-9989-2b70c8a8b9f1.png)

### 3. 試說明碎形(fractal)是什麼以及實例? Python實作的參考作法?
Ans: 碎形，又稱分形、殘形，通常被定義為「一個粗糙或零碎的幾何形狀，可以分成數個部分，且每一部分都是整體縮小後的形狀」，即具有自相似的性質。 碎形在數學中是一種抽象的物體，用於描述自然界中存在的事物。人工碎形通常在放大後能展現出相似的形狀。

![image](https://user-images.githubusercontent.com/89304181/174704639-c0a0fb25-b5ae-4119-acb2-3cdd66a5ff26.png)

````
from fractal import IFS

code = [
    [0.195, -0.488, 0.344, 0.443, 0.4431, 0.2452, 0.2],
    [0.462, 0.414, -0.252, 0.361, 0.2511, 0.5692, 0.2],
    [-0.637, 0, 0, 0.501, 0.8562, 0.2512, 0.2],
    [-0.035, 0.07, -0.469, 0.022, 0.4884, 0.5069, 0.2],
    [-0.058, -0.07, -0.453, -0.111, 0.5976, 0.0969, 0.2]
]

ifs = IFS([500,500])
ifs.setCoordinate()
ifs.setPx(500, 0, 0)
ifs.setIfsCode(code)
ifs.doIFS(200000)
ifs.wait()

````
![image](https://user-images.githubusercontent.com/89304181/174705338-4d9c8569-c55a-4bd0-a801-bdb55efc2d7c.png)

Reference: [Draw Fractal Image By Python](https://github.com/Grace-TA/fractal)




[return to content](#000) 
