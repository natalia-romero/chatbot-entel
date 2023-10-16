import pandas as pd
import time
from sklearn import metrics
import nltk
import numpy as np
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

evaluations = []
evaluations_std = []

def getDataFrame(doc):  # función CSV a DataFrame
    df = pd.read_csv(doc)
    return df

def fit_and_evaluate(km, X, name=None, n_runs=5):
    name = km.__class__.__name__ if name is None else name

    train_times = []
    scores = defaultdict(list)
    for seed in range(n_runs):
        km.set_params(random_state=seed)
        t0 = time()
        km.fit(X)
        train_times.append(time() - t0)
        scores["Homogeneity"].append(metrics.homogeneity_score(categories, km.labels_))
        scores["Completeness"].append(metrics.completeness_score(categories, km.labels_))
        scores["V-measure"].append(metrics.v_measure_score(categories, km.labels_))
        scores["Adjusted Rand-Index"].append(
            metrics.adjusted_rand_score(categories, km.labels_)
        )
        scores["Silhouette Coefficient"].append(
            metrics.silhouette_score(X, km.labels_, sample_size=2000)
        )
    train_times = np.asarray(train_times)

    print(f"clustering done in {train_times.mean():.2f} ± {train_times.std():.2f} s ")
    evaluation = {
        "estimator": name,
        "train_time": train_times.mean(),
    }
    evaluation_std = {
        "estimator": name,
        "train_time": train_times.std(),
    }
    for score_name, score_values in scores.items():
        mean_score, std_score = np.mean(score_values), np.std(score_values)
        print(f"{score_name}: {mean_score:.3f} ± {std_score:.3f}")
        evaluation[score_name] = mean_score
        evaluation_std[score_name] = std_score
    evaluations.append(evaluation)
    evaluations_std.append(evaluation_std)


data = getDataFrame("docs/chats.csv")

#normalizar texto
data = data['text'].str.lower().str.replace(r'[^\w\s]', '')

#vectorizar
stopwords = nltk.corpus.stopwords.words('spanish')
vectorizer = TfidfVectorizer(
    max_df=0.5,
    min_df=5,
    stop_words=stopwords,
)
matrix = vectorizer.fit_transform(data)

#k-means
categories = ['good','normal','bad']

kmeans = KMeans(
    n_clusters=3,
    max_iter=100,
    n_init=3,
)

fit_and_evaluate(kmeans, matrix, name="KMeans\non tf-idf vectors")