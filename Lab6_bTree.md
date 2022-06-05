# Lab6: 二元樹(Binary Tree)?

## 1. 什麼是Binary Tree? 有什麼優點?
Ans: 二元樹的定義: 二元樹可以為空集合; 每 1 個節點最多只有 2 個子節點，左節點與右節點; 有次序關係，左節點會排在右節點之前，不能顛倒. 優點是容易實作，且能快速找到任意節點的父節點與左右子節點。 缺點是當二元樹稀疏或不平衡時，就會相當浪費記憶體。 故較為適用於Complete Binary Tree 或Full Binary Tree，較不適用於Skewed Binary Tree。 另一個缺點是增加和刪除節點時，需要搬移多個節點。


## 2. 若我們有9000萬(9e7)筆的數列要從其中搜尋，若使用二元樹(Binary Tree)的方法，和沒有排序的陣列(Array)資料比較，其效率會差多少倍? 請參考實作程式完成計算。

![image](https://user-images.githubusercontent.com/89304181/172033359-7cc8957a-abf9-4209-9b64-43fde178ca17.png)

## 3. 如何使用Python快速建立含32個元素的串列，同時將此串列內容設為9，最後列出此串列的資料型態和內容??

![image](https://user-images.githubusercontent.com/89304181/172033451-b42695be-17fa-4143-8326-312e179eca28.png)

## 4. 如何使用random.randint建立100~200之間含24個元素的串列，這個程式列出執行結果時，最後列出此串列的資料型態和內容??

![image](https://user-images.githubusercontent.com/89304181/172033493-74541537-18e7-46c2-9e46-301fe9931150.png)

## 5. 如何使用10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32系列(List)數字建立二元樹, **這個程式列出執行結果時，同時會列出此陣列的索引值??

![image](https://user-images.githubusercontent.com/89304181/172034025-1f1fef60-c96f-48b0-b29f-b28fbbc94c11.png)

The error is cuased by the initial defintion of binary tree size; thus, we can check the list size and calculate the size of full binary tree to solve the issue.

![image](https://user-images.githubusercontent.com/89304181/172034098-4b8c9237-06e5-452a-af11-d985c910a555.png)

## 6. Level 10 的Binary Tree 最多可以有幾個Ｎode, 為什麼呢?

![image](https://user-images.githubusercontent.com/89304181/172034258-28ee24da-e3c5-4e59-9849-43a55161408d.png)

![image](https://user-images.githubusercontent.com/89304181/172034293-5aa6e9e6-1eeb-45cf-90c7-bf2e9f841f28.png)

## 7. 用Python寫一個程式可輸入Level數，並自動計算此Binary Tree 最多可以有 幾個Ｎode。

![image](https://user-images.githubusercontent.com/89304181/172034354-e0b995c2-93e1-49e9-9fc1-5ed28488703e.png)

## 8. 如何使用10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32數字建立二元樹, 並使用中序列印, 並計算此二元樹的深度(i.e., 層數) ?

![image](https://user-images.githubusercontent.com/89304181/172036814-997ad3ac-3116-4fae-a7c5-820482e6e12c.png)


## 9. 如何使用10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32數字建立二元樹, 並使用前序列印, 並計算此二元樹的深度(i.e., 層數) ?

![image](https://user-images.githubusercontent.com/89304181/172036826-66de5126-96d8-4caf-84c4-b4f0a613c68d.png)


## 10. 如何使用10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32數字建立二元樹, 並使用後序列印, 並計算此二元樹的深度(i.e., 層數) ?

![image](https://user-images.githubusercontent.com/89304181/172036848-acd51af7-59ea-48d8-9337-933f60d12f34.png)



