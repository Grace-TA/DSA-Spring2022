# ch9_8.py    
def insertion_sort(nLst):
    ''' 插入排序 '''
    n = len(nLst)
    if n == 1:                          # 只有1筆資料
        print("第 %d 次迴圈排序" % n, nLst)
        return nLst
    print("第 1 次迴圈排序", nLst)
    for i in range(1,n):                # 迴圈
        for j in range(i, 0, -1):
            if nLst[j] < nLst[j-1]: 
                nLst[j], nLst[j-1] = nLst[j-1], nLst[j]
            else:
                break
        print("第 %d 次迴圈排序" % (i+1), nLst)
    return nLst

data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", insertion_sort(data))


    
