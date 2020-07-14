import random
from pandas import DataFrame
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, BaggingClassifier, \
    GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
from sklearn.decomposition import PCA
def type(X,Y):
    rfc = RandomForestClassifier()
    classifier =LogisticRegression()  # SVC(kernel="linear") #svm.SVC(kernel='rbf',C=1,gamma='auto')
    gnb =GaussianNB() #BernoulliNB()#MultinomialNB()#
    gnb2=BernoulliNB()
    gnb3=MultinomialNB()
    svc = LinearSVC(C=0.5)
    EXT =ExtraTreesClassifier(criterion='gini', bootstrap=True,n_estimators=80,oob_score=True)
    EXT2 = ExtraTreesClassifier(criterion='entropy', bootstrap=True,n_estimators=125,oob_score=True)
    bag = BaggingClassifier(DecisionTreeClassifier(), n_estimators=100)
    model = GradientBoostingClassifier()
    model2=AdaBoostClassifier()
    model3=GradientBoostingClassifier()
    model4=LinearDiscriminantAnalysis()
    model5=QuadraticDiscriminantAnalysis()

    Y=shuffle(Y)#不對稱洗牌
    X=shuffle(X)#不對稱洗牌

    bag.fit(X, Y)
    classifier.fit(X, Y)
    rfc.fit(X, Y)
    gnb.fit(X, Y)
    gnb2.fit(X, Y)
    gnb3.fit(X, Y)
    EXT2.fit(X, Y)
    EXT.fit(X, Y)
    svc.fit(X,Y)
    model.fit(X,Y)
    model2.fit(X,Y)
    model3.fit(X,Y)
    model4.fit(X,Y)
    model5.fit(X,Y)


    pred = EXT.predict(X+Y).ravel()  # 預測 一維化
    pred_2=EXT2.predict(X+Y).ravel()  # 預測 一維化
    pred2 = gnb.predict(X + Y).ravel()  # 預測 一維化
    pred2_2 = gnb2.predict(X + Y).ravel()  # 預測 一維化
    pred2_3 = gnb3.predict(X + Y).ravel()  # 預測 一維化
    pred3=svc.predict(X + Y).ravel()
    pred4=bag.predict(X + Y).ravel()
    pred5=classifier.predict(X + Y).ravel()
    pred6=rfc.predict(X + Y).ravel()
    pred7=model.predict(X + Y).ravel()
    pred7_2 = model2.predict(X + Y).ravel()
    pred7_3 = model3.predict(X + Y).ravel()
    pred7_4 = model4.predict(X + Y).ravel()
    pred7_5= model5.predict(X + Y).ravel()



    print("ExtraTreesClassifier_gini",pred)
    print("ExtraTreesClassifier_entropy",pred_2)
    print("GaussianNB",pred2)
    print("BernoulliNB", pred2_2)
    print("MultinomialNB",pred2_3)
    print("LinearSVC(C=0.5)",pred3)
    print("BaggingClassifier(DecisionTreeClassifier(), n_estimators=100)", pred4)
    print("LogisticRegression", pred5)
    print("RandomForestClassifier", pred6)
    print('''model = GradientBoostingClassifier()  
    model2=AdaBoostClassifier()
    model3=GradientBoostingClassifier()
    model4=LinearDiscriminantAnalysis()
    model5=QuadraticDiscriminantAnalysis()''')
    print(pred7)
    print(pred7_2)
    print(pred7_3)
    print(pred7_4)
    print(pred7_5)
    print(model4.predict_log_proba(X + Y).ravel())
    print(model4.predict_proba(X+Y).ravel())


s = []
while len(s) < 100:
    r=str(random.randint(1,11))
    s.append(r)
    print(r)
    print("s=",s)

X_train=DataFrame(s)
Y_train=DataFrame(reversed(s))
type(X_train,Y_train)
