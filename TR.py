import datetime
import os
import time

import torch
import numpy as np
from matplotlib import pyplot as plt
#np.random.seed(7) # 用來確保每次生成的隨機資料是一樣的，否則訓練結果無法比較
def tr():
    x = np.random.randn(100, 1)
    y = 2.5 + 4.5 * x + .2 * np.random.randn(100, 1)  # randn 的 n 為 normal distribution
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    idx = np.arange(100)
    np.random.shuffle(idx)  # 打散索引
    train_idx = idx[:80]  # 取前 80 筆為訓練資料
    val_idx = idx[80:]  # 取後 20 筆為驗證資料
    x_train, y_train = x[train_idx], y[train_idx]
    x_val, y_val = x[val_idx], y[val_idx]
    x_train_tensor = torch.from_numpy(x_train).to(device)
    y_train_tensor = torch.from_numpy(y_train).to(device)
    #print(type(x_train), type(x_train_tensor), x_train_tensor.type())

    # 隨機給定數值，初始化 a, b 的值
    # np.random.seed(7)
    a = np.random.randn(3)
    b = np.random.randn(3)
    # 設定學習率
    lr = 1e-1
    # 設定 epochs
    n_epochs = 5000
    for epoch in range(n_epochs):
        # 計算模型的預測
        yhat = a + b * x_train
        # print("yhat:",yhat)
        # 用預測和標記來計算 error
        error = (y_train - yhat)
        # print("error:",error)
        # 用 error 來計算 loss
        loss = (error ** 2).mean()

        # 計算兩個參數的梯度
        a_grad = -2 * error.mean()
        b_grad = -2 * (x_train * error).mean()

        # 用梯度和學習率來更新參數
        a = a - lr * a_grad
        b = b - lr * b_grad

    print("ans:", end="")
    #print(a, b)
    A = list(a)
    B = list(b)
    #C = A + B
    A = [round(x, 0) for x in A]
    B = [round(x, 0) for x in B]
    print(A, B)
    for aa in A:
        ans.append(int(aa))
    for bb in B:
        ans.append(int(bb))
    #print(C)

ans=[]
for i in range(260):
    tr()

today =(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%m_%d")
path = today+"Tensor_3R"
if not os.path.isdir(path):
    os.mkdir(path)
skip=200
number=1
with open(path+"/test.txt","w+",encoding="utf8") as f:
    for i in range(1,780,3):
        judge = ""
        if int(ans[i]+ans[i+1]+ans[i+2]) >= 11:
            judge += "大"
        elif int(ans[i]+ans[i+1]+ans[i+2]) < 11:
            judge += "小"
        if int(ans[i]+ans[i+1]+ans[i+2]) % 2 == 1:
            judge += "單"
        elif int(ans[i]+ans[i+1]+ans[i+2]) % 2 == 0:
            judge += "雙"

        if (number+skip ) == 201:
            f.write("--------10-11點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 221:
            f.write("--------11-12點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 241:
            f.write("--------12-13點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 261:
            f.write("--------13-14點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 281:
            f.write("--------14-15點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 301:
            f.write("--------15-16點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 321:
            f.write("--------16-17點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 341:
            f.write("--------17-18點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 361:
            f.write("--------18-19點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 381:
            f.write("--------19-20點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 401:
            f.write("--------20-21點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 421:
            f.write("--------21-22點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 441:
            f.write("--------22-23點--------------\n")
            time.sleep(0.1)
        elif (number+skip ) == 461:
            f.write("--------EX額外--------------\n")
            time.sleep(0.1)
        f.write("第" + str(number+skip) + "期 " + str(ans[i]) + "," + str(ans[i + 1]) + "," + str(ans[i + 2]) + ",總和:" + str(
            ans[i] + ans[i + 1] + ans[i + 2]) +","+judge+ "\n")
        number+=1
