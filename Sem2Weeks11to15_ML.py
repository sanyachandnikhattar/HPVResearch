import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression #importing library for Logistic Regression
from sklearn.svm import SVC #importing library for SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score, roc_curve #importing for AuC
from sklearn.metrics import confusion_matrix #importing for confusion matrix
import pickle

with open("/Users/sanyakhattar/Desktop/HPV/df_results_network2.pkl", "rb") as file:
    data = pickle.load(file)

print(len(data))

#print(data.head())

selected_column = 'Selected' #what is the selected column?
X = data.drop(columns=[selected_column]) #make X the 480ish 0's ?
Y = data[selected_column] #make Y the 20ish 1's?

new_df = data #pickle and CSV are same data frame
#check: is this the way to make pickle and CSV the same data frame?

#selected column is what to classify

#plots may be difficult --> not two dimensional
#multiple columns; difficult 

#only train data w/ training data set, test with test data set
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.2, stratify = Y, random_state = 42)
#Y is 20 1's
#X is 480ish 0's
#0.2 testing
#0.8 training

#Logistic Regression
logistic_model = LogisticRegression(max_iter=2500, class_weight={0: 1, 1: 14.21651}) #something between 14 and 15 optimal weight for 1 --> logistic regression 
#between 14 and 14.25 --> optimal for increasing true positives, BUT decreases AuC
#between 14.25 and 14.45 --> seems most optimal for AuC, but decreases some true positives
#14.21651 --> seems to minimize false positives and higher threshold of AuC
#14.21651 appears to be "sweet spot"
logistic_model.fit(X_Train, Y_Train)

#SVM
svm_model = SVC(probability=True, class_weight={0: 1, 1: 24.34905}) #between 24 and 25 optimal weight for 1 --> SVM
#found a sweet spot value of 24.35, better than 24.75 for 1 weight because now SVM has more true positives (60) than false (50), and more true negatives (3) than false (1)
#SVC: Support Vector Classifier; specific implementation of more general SVM
#tailored for classification tasks
#24.34905 --> making AuC go above 0.5, while keeping Confusion Matrix clean!!
svm_model.fit(X_Train, Y_Train)

#Decision Tree
dt_model = DecisionTreeClassifier(random_state = 42)
dt_model.fit(X_Train, Y_Train) #train the decision tree model

#Making predictions/probabilities for Logistic Regression and SVM (different from Decision Trees)
y_prob_logistic = logistic_model.predict_proba(X_Test)[:, 1]#probabilities for positive class
print (y_prob_logistic)
y_prob_svm = svm_model.predict_proba(X_Test)[:, 1] #probabilities for positive class
print (y_prob_svm)

#Make prediction for the Decision Tree
y_pred_decisiontree = dt_model.predict(X_Test) #use predict method rather than predict_proba as Decision Trees compute probabilities differently
print (y_pred_decisiontree)

#AuC --> way to evaluate algorithm accuracy
#diagonal line, if area under curve is 1, then perfectly accurate
#want a desired threshold of AuC >= 0.5

print (Y_Test.shape)
print (y_prob_logistic.shape)
#Calculate AuC for Logistic Regression, SVM
auc_logistic = roc_auc_score(Y_Test, y_prob_logistic)
auc_svm = roc_auc_score(Y_Test, y_prob_svm)

#have to approach AuC for Decision Tree differently as Decision Trees do NOT output probabilities
#treating class predictions as probabilities for AuC calculation
auc_decisiontree = roc_auc_score(Y_Test, y_pred_decisiontree)
 
print (f"Logistic Regression AUC: {auc_logistic}") #good, greater than 0.5 WITH column 1
print (f"SVM AUC: {auc_svm}") #good, greater than 0.5 WITH column 1
print (f"Decision Tree AUC: {auc_decisiontree}") #good, greater than 0.5
print ("\n")


#checking documentation predict_proba and roc_auc_score
#predict_proba gives ACTUAL PROBABILITIES where as predict_ only gives the CLASSES
#What is RoC: Receiver Operating Characteristic Curve 

#confusion matrix
#Logistic Regression
y_pred_logistic = (y_prob_logistic > 0.5).astype(int) #store as integers (0, 1 --> true or false)
confusion_matrix_logistic = confusion_matrix(Y_Test, y_pred_logistic)
print ("Logistic Regression Confusion Matrix: ")
print(confusion_matrix_logistic)
print ("\n")
#110, 0
#4, 0
#not exactly what we want, don't want false positives

#SVM
#y_pred_svm = (y_prob_svm > 0.5).astype(int)
y_pred_svm = svm_model.predict(X_Test) #changing to predict
confusion_matrix_svm = confusion_matrix(Y_Test, y_pred_svm)
print ("SVM Confusion Matrix: ")
print(confusion_matrix_svm)
print ("\n")

#Decision Tree 
y_pred_decision = (y_pred_decisiontree > 0.5).astype(int)
confusion_matrix_decision = confusion_matrix(Y_Test, y_pred_decision)
print ("Decision Tree Confusion Matrix: ")
print (confusion_matrix_decision)
print ("\n")
#find a model that makes I 1,1 above 90
#find a model that makes I 2,2 above 3

#importance score

# Logistic Regression Feature Importance
importance_logistic = logistic_model.coef_[0]
# Summarize feature importance
for i, v in enumerate(importance_logistic):
    print(f'Logistic Feature: {X.columns[i]}, Score: {v}')

#SVM Feature Importance
if isinstance(svm_model.kernel, str) and svm_model.kernel == 'linear':
    # SVM Feature Importance for linear kernel
    importance_svm = svm_model.coef_[0]
    # Summarize feature importance
    for i, v in enumerate(importance_svm):
        print(f'SVM Feature: {X.columns[i]}, Score: {v}')
else:
    print("Feature importance is not straightforward to obtain for non-linear kernels in SVM.")
    #NOTE: SVM FEATURE IMPORTANCE DOESN'T WORK

# Decision Tree Feature Importance
importance_dt = dt_model.feature_importances_
# Summarize feature importance
for i, v in enumerate(importance_dt):
    print(f'Decision Tree Feature: {X.columns[i]}, Score: {v}')

#decision tree: probably best model for poster
#compare three classification models

#mess around with class weight for logistic regression and decision tree
#see if you can find a better confusion matrix with different class weights

#see top 5 importance features based on the best model

#NumLinkstoMinus: how many neighbors with Negative (important)
#AverageNeighborPosThreshold:

#Top 5 for Logistic Regression (Number)
#1. AverageNeighborEdgeWeight: 2.5...
    #how influential the node is --> higher the number, connected to many links, more influence on the community
#2. AverageDispersion: 1.08...
    #network feature --> look up definition + adapt to project
#3. LocalReachingCentralirt: 0.63...
    #network feature --> "                                   "
#4. AverageShortestPathLengths: 0.417...
    #network feature --> "                                   "
#5. NumLinkstoMinus: 0.23065...
    #how many people you are connected with that have negative opinion (doesn't assume anything about you/base node)