import h2o
def predict(input, models: list):
    Y1_prediction = models[0].predict(input).flatten()
    Y2_prediction = models[1].predict(input).flatten()
    return Y1_prediction, Y2_prediction