from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf



def predict(request):
    return render(request, "predict1.html")


def result(request):

    data = pd.read_csv(r'C:\Users\ldipe\diabetes.csv')

    X = data.iloc[:,0:-1].values
    y = data.iloc[:,-1].values
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    ann = tf.keras.Sequential()

    ann.add(tf.keras.layers.Dense(units=12,activation='relu'))
    ann.add(tf.keras.layers.Dense(units=12,activation='relu'))
    ann.add(tf.keras.layers.Dense(units=12,activation='relu'))
    ann.add(tf.keras.layers.Dense(units=1,activation='sigmoid'))

    ann.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

    ann.fit(X_train,y_train,batch_size=12,epochs=100)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
   
    prediction = ann.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result1 = ""
    if prediction==[1]:
        result1 = "Positive"
    else:
        result1 = "Negative"
    return render(request, "predict/predict1.html", {"result2":result1})

def predict_view(request):
	return render(request, 'predict/predict1.html')
