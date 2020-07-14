import os
from random import choice
from collections import Counter
import numpy as np
import tensorflow as tf
from keras import callbacks
from keras.layers import Dense, Activation, Dropout
from keras.models import Sequential
import matplotlib.pyplot as plt
with open("data.txt","r+",encoding="utf-8") as f:
    data = f.read().split("\n")
f.close()
X=[]#1-6
Y=[]#特別
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
for sp in data:
    cont = 1
    for p in sp.split("\t"):
        if cont % 7==0:
            Y.append(int(p))
        elif p !="":
            X.append(int(p))
        cont+=1
#--------------------------model---------------------------------------
while '' in X:
   X.remove('')
X_train=np.array(X).astype(np.int32)
Y_train=np.array(Y).astype(np.int32)
print(X_train)

RX_train=np.ones(len(X)).astype(np.int32)

model= Sequential()
model.add(Dense(12, input_shape=(1,)))
model.add(Activation("hard_sigmoid"))
model.add(Dropout(0.5))

# model.add(Dense(6, input_shape=(3,)))
# model.add(Activation("softmax"))
# model.add(Dropout(0.5))

model.add(Dense(20, input_shape=(1,)))
model.add(Activation("sigmoid"))
model.add(Dropout(0.5))

tf.keras.callbacks.BaseLogger(stateful_metrics=None)
# lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
#     initial_learning_rate=1e-2,
#     decay_steps=40,
#     decay_rate=0.7)
# optimizer = tf.keras.optimizers.SGD(learning_rate=lr_schedule)
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optimizer='Adadelta'
model.compile( loss=loss,optimizer=optimizer)#,metrics=['accuracy'])


model.fit(X_train,RX_train,batch_size=380,epochs=10,verbose=1)

#model.predict(X_train)
# PDS=(PD>0.5)
# print(PDS)
#X_table=model.predict_classes(X_train)
PD=model.predict(X_train)#model.predict_classes(X_train)
PD=list(PD.ravel())
print(PD)
print("-"*80)
PD2=model.predict(Y_train)#model.predict_classes(X_train)
PD2=list(PD2.ravel())
print(PD2)
print("-"*80)
balls=list(range(1,40))
Sball=list(range(1,10))
# balls = [balls[i:i + 6] for i in range(0, len(balls), 6)]
# print(balls)

ans=[]
SP=[]
conts=1

for a in range(len(PD)):
    H = (PD[a] * 100)
    H2=round(np.percentile(balls, round(H)))
    ans.append(int(H2))
    #print(PD[a])
    if conts %6==0:
        S=round(np.percentile(Sball, round(H)))
        SP.append(int(S))
    conts+=1
# print(Counter(SP))
# print(Counter(ans))
# print(Counter(X_train))
print("---"*80)
c=1
for an in Counter(ans):
    if c <= 6:
        print(an)
    c+=1
c=1
for an in Counter(SP):
    if c <= 1:
        print("SP:",an)
    c+=1
# print(len(SP))
# print(len(ans))
# print(len(X_train))
callbacks.Callback()
callbacks.History()
callbacks.TensorBoard(log_dir='./logs', histogram_freq=0, batch_size=32, write_graph=True, write_grads=False, write_images=False, embeddings_freq=0, embeddings_layer_names=None, embeddings_metadata=None, embeddings_data=None, update_freq='epoch')
callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=10, verbose=0, mode='auto', min_delta=0.0001, cooldown=0, min_lr=0)
from keras.models import model_from_json

model.save_weights("model.weight")
from keras.models import load_model

model.save('model.h5')  # creates a HDF5 file 'model.h5'
