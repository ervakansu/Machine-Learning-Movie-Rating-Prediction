from DataPreprocessor import *
# Importing Libraries
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

def add(x,y):
    temp = float(x) + y
    return str(temp)
                 
# Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators=999, criterion='entropy', random_state=0,
                                    class_weight='balanced', n_jobs=-1)
classifier.fit(X_train, Y_train.ravel())

# Predicting the Test set results
Y_pred = classifier.predict(X_test)
Y_pred = Y_pred.reshape(-1,1)
mRounder = np.vectorize(round_off)
z1 = np.vectorize(add)
ARRAYS_WITH_PREDS = []
for i in np.arange(-0.5,0.6,0.1):
    ARRAYS_WITH_PREDS.append(z1(Y_pred,i))
#print_full(np.c_[Y_pred,Y_test])
final_accuracy = 0
for preds in ARRAYS_WITH_PREDS:
    final_accuracy+=accuracy_score(Y_test,preds,normalize=True,sample_weight=None)

print 'Accuracy = ',final_accuracy*100, '%'

