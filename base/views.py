from django.shortcuts import render
import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import log_loss
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn import linear_model

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from django.shortcuts import HttpResponse
from django.http import HttpRequest

def home(request):
    return render(request, 'home.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv('C:\\Users\\USER\\Downloads\\diabetes dataset.csv')

    x= data.drop('Outcome',axis=1)
    y= data['Outcome']
    #split your data into training and test data
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,shuffle=False)

    model = linear_model.LogisticRegression()
    model.fit(x_train,y_train) 
    val1= float(request.GET['n1'])
    val12= float(request.GET['n2'])
    val3= float(request.GET['n3'])
    val4= float(request.GET['n4'])
    val5= float(request.GET['n5'])
    val6= float(request.GET['n6'])
    val7= float(request.GET['n7'])
    val8= float(request.GET['n8'])

    pred=model.predict([[val1, val12, val3, val4, val5,val6,val7,val8 ]])

    result1 =""
    if pred==[1]:
        result1= "<span style='font-size: larger;'>Our model predicts you are <b style='color: red;'>positive</b> for Diabetes</span>"
    else:
        result1= "<span style='font-size: larger;'>Our model predicts you are <b style='color: black;'>negative</b> for Diabetes</span>"


    return render(request, "predict.html", {"result2":result1})
  