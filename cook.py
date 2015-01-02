import os
from glob import glob

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import cross_val_score, KFold
from sklearn import decomposition
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.naive_bayes import MultinomialNB
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.decomposition import TruncatedSVD
from sklearn import metrics

def get_fullpath(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

def file2list(filename):
    with open(filename, 'r') as f:
        rawdata = f.read()
    return rawdata

def init_data():
    target = './data/*.txt'
    files = glob(target)
    return map(file2list, files)

def analysis_by_naivebayes(fileaname, sep=',', msg='raw'):
    rawdata = pd.read_csv(get_fullpath(fileaname), sep=sep)

    y = np.array(rawdata['category'])
    vectorizer = CountVectorizer(max_df=10, min_df=1)
    X = vectorizer.fit_transform(np.array(rawdata['receipt word']))
    # X = TfidfTransformer().fit_transform(X)

    nb = MultinomialNB()
    nb.fit(X, y)
    print('Navie Bayes metric {} ================================='.format(msg))
    print('score {}'.format(nb.score(X, y)))

    kf = KFold(len(y), n_folds=5)
    scores = cross_val_score(nb, X, y, cv=kf)
    print('KFold {}'.format(sum(scores)/5))

def analysis_by_kmeans(fileaname, sep=',', tfidf=True, msg='raw'):
    rawdata = pd.read_csv(get_fullpath(fileaname), sep=sep)

    y = np.array(rawdata['category'])
    vectorizer = CountVectorizer(max_df=10, min_df=1)
    X = vectorizer.fit_transform(np.array(rawdata['receipt word']))
    if tfidf:
        X = TfidfTransformer().fit_transform(X)
        print(X)

    kmeans = KMeans()
    kmeans.fit(X)

    print('KMeans metric {} ================================='.format(msg))
    print('homogeneity {}'.format(metrics.homogeneity_score(y, kmeans.labels_)))
    print('completeness {}'.format(metrics.completeness_score(y, kmeans.labels_)))
    print('v_measure {}'.format(metrics.v_measure_score(y, kmeans.labels_)))
    print('adjusted_rand {}'.format(metrics.adjusted_rand_score(y, kmeans.labels_)))
    print('adjusted_mutual_info {}'.format(metrics.adjusted_mutual_info_score(y,  kmeans.labels_)))

def analysis_by_nmf():
    initdata = init_data()

    vectorizer = CountVectorizer(max_df=10, min_df=1)
    X = vectorizer.fit_transform(initdata)
    X = TfidfTransformer().fit_transform(X)
    # print(X)
    nmf = decomposition.NMF(n_components=2).fit(X)
    feature_names = vectorizer.get_feature_names()

    for topic_idx, topic in enumerate(nmf.components_):
        print "Topic #%d:" % topic_idx
        #print " ".join([str(i) for i in topic.argsort()[:-100:-1]])
        print " ".join([feature_names[i] for i in topic.argsort()[:-50:-1]])

    # print euclidean_distances(nmf.components_, initdata[1].split('\n')[5])
    # print euclidean_distances(nmf.components_, X[1,:])

if __name__ == '__main__':
    analysis_by_naivebayes('data/all_raw.csv', msg='raw')
    analysis_by_naivebayes('data/all_morph_n.tsv',sep='\t', msg='n processed')
    analysis_by_naivebayes('data/all_morph_nv.tsv',sep='\t', msg='nv processed')
    # analysis_by_kmeans('data/raw_all.csv', msg='raw')
    # analysis_by_kmeans('data/all.tsv', sep='\t', msg='processed')
    # analysis_by_kmeans('data/raw_all.csv', tfidf=True, msg='tfidf=true raw')
    # analysis_by_kmeans('data/raw_all.csv', tfidf=False, msg='tfidf=false raw')
    # analysis_by_kmeans('data/all.tsv', sep='\t', tfidf=True, msg='tfidf=true processed')
    # analysis_by_kmeans('data/all.tsv', sep='\t', tfidf=False, msg='tfidf=false processed')

    # analysis_by_nmf()

