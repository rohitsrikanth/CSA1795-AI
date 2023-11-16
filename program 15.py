from sklearn.tree import DecisionTreeRegressor, export_text
dataset = [
    [20000, 2, 1, 0, 25000],
    [40000, 3, 2, 1, 20000],
    [60000, 5, 3, 1, 18000],
    [80000, 4, 1, 0, 22000],
]
X = [[car[0], car[1], car[2], car[3]] for car in dataset]
y = [car[4] for car in dataset]
regressor = DecisionTreeRegressor()
regressor.fit(X, y)
tree_rules = export_text(regressor, feature_names=["mileage", "age", "brand", "engine type"])
print("Decision Path:")
print(tree_rules)
