from sklearn.svm import SVC

X = [[1,1],[2,2],[9,9],[10,10]]
y = [0,0,1,1]

model = SVC()
model.fit(X,y)

print(model.predict([[3,3]]))