import torch
import numpy as np
from torch import nn
from torch import optim

x = np.random.rand(100, 1)
y = 2 + 9 * x + .2 * np.random.randn(100, 1)
idx = np.arange(100)
np.random.shuffle(idx) # 打散索引
train_idx = idx[:80] # 取前 80 筆為訓練資料
val_idx = idx[80:] #取後 20 筆為驗證資料
x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]
device = 'cuda' if torch.cuda.is_available() else 'cpu'
x_train_tensor = torch.from_numpy(x_train).to(device)
y_train_tensor = torch.from_numpy(y_train).to(device)
print(type(x_train), type(x_train_tensor), x_train_tensor.type())
x_train_tensor.type()
x_train_tensor.cpu().numpy()
a = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)
a = torch.randn(1).to(device)
b = torch.randn(1).to(device)
a.requires_grad_()
b.requires_grad_()
torch.manual_seed(7)
a = torch.randn(1, requires_grad=True, device=device)
b = torch.randn(1, requires_grad=True, device=device)


class PyTorchLinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        # 使用 nn.Parameter 來表示 a, b 為參數
        self.a = nn.Parameter(torch.randn(1, requires_grad=True))
        self.b = nn.Parameter(torch.randn(1, requires_grad=True))

    def forward(self, x):
        # 計算我們的輸出，也就是預測
        return self.a + self.b * x


model = PyTorchLinearRegression()  # .to(device)
print(model.state_dict())
lr = 1e-1
epochs = 500
MSELoss = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=lr)
for epoch in range(epochs):
    model.train()
    # 不用再手動做 output 了
    # yhat = a + b * x_tensor
    yhat = model(x_train_tensor)

    loss = MSELoss(y_train_tensor, yhat)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

print(model.state_dict())

from torch.utils.data import Dataset

class SLRDataset(Dataset):
    def __init__(self, x_tensor, y_tensor):
        self.x = x_tensor
        self.y = y_tensor

    def __getitem__(self, index):
        return (self.x[index], self.y[index])

    def __len__(self):
        return len(self.x)


def build_train_step(model, loss_fn, optimizer):
    def train_step(x, y):
        # 訓練模式
        model.train()

        # 預測
        yhat = model(x)

        # 計算 loss
        loss = loss_fn(y, yhat)

        # 計算梯度
        loss.backward()

        # 更新參數並清零梯度
        optimizer.step()
        optimizer.zero_grad()
        print("yhat=",yhat[yhat>5])
        # 回傳 loss
        return loss.item()

    # 回傳會在函數內被呼叫的訓練過程
    return train_step


# 以我們定義好的 model, lossfunction 和 optimizer 來建立 train_step
train_step = build_train_step(model, MSELoss, optimizer)
for epoch in range(epochs):
    # 執行一次訓練並回傳 loss
    loss = train_step(x_train_tensor, y_train_tensor)

# 確認參數
print(model.state_dict())
# 不用傳到 GPU 上
x_train_tensor = torch.from_numpy(x_train)
y_train_tensor = torch.from_numpy(y_train)
training_data = SLRDataset(x_train_tensor, y_train_tensor)
print(training_data[0])
from torch.utils.data import DataLoader
train_loader = DataLoader(dataset=training_data, batch_size=16, shuffle=True)
next(iter(train_loader))
losses = []
train_step = build_train_step(model, MSELoss, optimizer)
for epoch in range(epochs):
    for x_batch, y_batch in train_loader:
        # 現在 dataset 存放在 CPU 上，訓練的時候我們要把它轉移到 GPU 上
        x_batch = x_batch.to(device)
        y_batch = y_batch.to(device)

        loss = train_step(x_batch, y_batch)
        losses.append(loss)

model.eval()
print(model.state_dict())
print(losses[-1])
#device='cpu'

