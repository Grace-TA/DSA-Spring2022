# Lab7: 很厲害的東西 - 遞迴(Recursive, Recursion) ? 

## Lab 7-1 什麼是遞迴 (What Is Recursion) ?

### 1. 請用您自己的說法或是方式來介紹什麼是遞迴 (What Is Recursion) ?
Ans: 簡單來說，遞迴就是”在程式中自己呼叫自己” (什麼意思?)。比較學術的定義是函式中有呼叫自己(Self Calling)的敘述。

### 2. 遞迴建議的使用時機為何?
Ans: 在解決問題時，我們經常會遇到無法輕鬆使用 loop 或是 if statement就能處理的問題，像是走迷宮問題遇到死路時需要回到上一層計算、或是在解決河內塔問題時儘管操作相同，卻因為每次要進行操作的參數不同而需要寫重複的程式碼等等。此時，一個經常被納入考慮的方法，就是利用遞迴的概念來撰寫一個函式。

### 3. 參考程式今日介紹的程式 (R100, R110, R120), 完成1+2+...+30的加法練習

![image](https://user-images.githubusercontent.com/89304181/172033102-d0af25e1-bf14-44c3-b823-0b17dda82518.png)

![image](https://user-images.githubusercontent.com/89304181/172033159-dbaf3f4b-8437-4f7a-9e9c-a3fc1f7d3fe4.png)


## Lab 7-2 Lab 7-2 遞迴圖形 (e.g., Fractal in Nature)

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
