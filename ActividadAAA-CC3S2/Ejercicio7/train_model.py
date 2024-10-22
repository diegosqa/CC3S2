from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

class ModeloML:
    def __init__(self):
        self.model = RandomForestClassifier()

    def cargar_datos(self):
        # Cargar el dataset Iris para este ejemplo
        data = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test

    def entrenar_modelo(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def evaluar_modelo(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        return accuracy, f1

