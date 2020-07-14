import datetime
import time
import numpy as np
import tensorflow as tf
import MySQLdb
from keras import backend
from keras.layers import Conv1D
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sqlalchemy import func
from tensorflow.python.keras.layers import Dense, Activation, Dropout, LSTM, TimeDistributed
from tensorflow.python.ops import rnn
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#--------------------------資料夾--------------------------------
today =(datetime.datetime.now()+datetime.timedelta(days=7)).strftime("%m_%d")
path = today+"keras_3R"
if not os.path.isdir(path):
    os.mkdir(path)
#--------------------------SQL取資料-------------------------------------
db = MySQLdb.connect("127.0.0.1", "root", "wyuwdymijh00", "main_user",3000, charset='utf8')
cursor = db.cursor()
SQL="SELECT * FROM roll_3m  LIMIT 480"
cursor.execute(SQL)
db.commit()
data=cursor.fetchall()#總資料X
SQL="SELECT * FROM roll_3m_ans ORDER BY RAND() LIMIT 480"
cursor.execute(SQL)
db.commit()
data2=cursor.fetchall()#總資料Y
X=[]#資料庫
Y=[]#計算資料庫

for dt in data:
    for v in dt[1].split(","):
        X.append(v)
for dt2 in data2:
    for v in dt2[1].split(","):
        Y.append(v)
#.................輸出散資料後續3個一組
#np.set_printoptions(suppress=True, threshold=np.nan)
#--------------------------model---------------------------------------
X_train=np.array(X).astype(np.int32)
Y_train=np.array(Y).astype(np.int32)





model= tf.keras.models.Sequential()
model.add(Dense(4, input_shape=(1,)))
model.add(Activation("softmax"))
model.add(Dropout(0.4))

model.add(Dense(8, input_shape=(3,)))
model.add(Activation("softmax"))
model.add(Dropout(0.5))

model.add(Dense(12, input_shape=(5,)))
model.add(Activation("softmax"))
model.add(Dropout(0.3))

# model.add(LSTM(4,return_sequences=False,input_shape=(1,1,1)))
# model.add(Activation("softmax"))
# model.add(Dropout(0.6))
tf.keras.callbacks.BaseLogger(stateful_metrics=None)
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate=1e-2,
    decay_steps=80,
    decay_rate=0.7)
optimizer = tf.keras.optimizers.SGD(learning_rate=lr_schedule)
#optimizer='Adadelta' #! rmsprop  #! Adagrad #! Adadelta #X NAG #X Monentum #!可以直接使用 X需要處裡
loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#"squared_hinge"

#loss="mean_squared_error "#mean_absolute_error #mean_absolute_percentage_error #mean_squared_logarithmic_error #squared_hinge #hinge #categorical_hinge #logcosh
model.compile( loss=loss,optimizer=optimizer)



#history=model.fit(X_train,Y_train,batch_size=200,epochs=200,verbose=1)
model.fit(X_train,Y_train,batch_size=1440,epochs=500,verbose=1)
PD=model.predict(X_train)

#PD=np.sort(PD)#排列
max= np.percentile(PD, 100)#最大的數值
min=np.percentile(PD, 0)#最小的數值

H15=np.percentile(PD, 15)
H30=np.percentile(PD, 30)
H45=np.percentile(PD, 45)
H60=np.percentile(PD, 60)
H80=np.percentile(PD, 80)

ans=[]
for P in PD:
    for D in P:
        print("原始數值:",D)
        if D>=min and D<=H15:
            ans.append(1)
        elif D>=H15 and D<=H30:
            ans.append(2)
        elif D>=H30 and D<=H45:
            ans.append(3)
        elif D>=H45 and D<=H60:
            ans.append(4)
        elif D>=H60 and D<=H80:
            ans.append(5)
        else:
            ans.append(6)

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

# print(PD)
# print(max,min)
# print(ans)
print(backend.backend())
print(len(ans))
loss_and_metrics = model.evaluate(X_train, Y_train, batch_size=128)
print(loss_and_metrics)
# model.summary()
saver = tf.saved_model #可指定需要儲存的tensor，不指定則全部儲存
if not os.path.exists('my_model'):
    os.mkdir('./my_model')
    saver.save(model,'./my_model/')
f.close()
