from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target # where, X= sepal_length, sepal_width, petal_length, petal_width and y = species/name (output/taget)
    model = RandomForestClassifier()
    model.fit(X, y)
    return model, iris