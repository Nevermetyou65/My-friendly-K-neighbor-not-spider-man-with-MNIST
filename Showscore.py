from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

def show_score(param_dict, Xtrain, ytrain, cv=3, scoring="accuracy"):

    knn = KNeighborsClassifier(**param_dict)
    score = cross_val_score(estimator=knn, X=Xtrain, y=ytrain,
    cv=cv, scoring=scoring, n_jobs=-1)

    print("Scores:", score, "mean:", score.mean(), "std:", score.std())
    print("==================================================================")