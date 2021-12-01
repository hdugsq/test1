import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from joblib import dump
label = pd.read_csv('train2.csv')
train_data=label.values
X = train_data[:,1:]
y = train_data[:,0]
y=y.astype(float)
best_clf = None
best_score = 0
train_scores = []
test_scores = []
b_scaler=None
for i in range(10):
    # create neural network using MLPClassifer
    shuffed_indexes=np.random.permutation(440)
    train_indexes=shuffed_indexes[0:420]
    test_indexes=shuffed_indexes[420:440]
    clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(3, 3), learning_rate='constant',
       learning_rate_init=0.001, max_iter=100000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)
    X_train, X_test = X[train_indexes], X[test_indexes]
    y_train, y_test = y[train_indexes], y[test_indexes]
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    clf.fit(X_train, y_train)
    train_score = clf.score(X_train, y_train)
    train_scores.append(train_score)
    test_score = clf.score(X_test, y_test)
    test_scores.append(test_score)
    if test_score >= best_score:
        best_score = test_score
        best_clf = clf
        b_scaler=scaler
print(test_scores)
X_test = b_scaler.transform(X_test)
in_sample_error = [1 - score for score in train_scores]
test_set_error = [1 - score for score in test_scores]
test_score = best_clf.score(X_test, y_test)
y_pred = best_clf.predict(X_test)
print(y_pred)
test_error = 1 - test_score
print('test_score：%s' % test_score)
print('test_error：%s' % test_error)