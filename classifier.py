import pandas as pd
import numpy as np
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import naive_bayes
from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing


twenty_train=fetch_20newsgroups(subset='train',shuffle=True)
twenty_train.target_names
print("\n".join(twenty_train.data[0].split("\n")[:3]))


count_vect=CountVectorizer()
X_train_counts=count_vect.fit_transform(twenty_train.data)
X_train_counts.shape





tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)


from sklearn.linear_model import SGDClassifier
text_clf_svm=Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf-svm',SGDClassifier(loss='hinge',alpha=1e-3,n_iter=5,random_state=42))])




_ = text_clf_svm.fit(twenty_train.data, twenty_train.target)
predicted_svm = text_clf_svm.predict(twenty_test.data)
print(np.mean(predicted_svm == twenty_test.target))

from sklearn.model_selection import GridSearchCV
#parameters={'vect_ngram_range':[(1,1),(1,2)],'tfidf_use_idf':(True,False),'clf_alpha':(1e-2,1e-3)}
#gs_clf=GridSearchCV(text_clf,parameters,n_jobs=2)
#gs_clf=gs_clf.fit(twenty_train.data,twenty_train.target)

