# Energy Efficiency ML Model

This repository shows on example on how to run a regression model based on the energy efficiency dataset, described and available at the following url: https://archive.ics.uci.edu/ml/datasets/Energy+efficiency. A deep learning approach, as well as an AutoML based model are given as examples in the file EDA.ipynb.

The automl model is chosen as the deployed example is containerized in a Docker image in order to facilitate simple universal deployment, with a REST api provided for a curl-based json command line interface. This repo also serves as a simple example on how to deploy an ML model in a containerized environment which serves predictions using a REST api.

### The choice for tree based models, and data pre-processing

From a quick exploratory analysis, and the uncovering of a highly fractured feature space, it becomes immediately clear that a tree based approach is best suited for this problem. Beyond having the capacity to capture highly non-linenar interactions, tree-based models also provide the added convenience of minimal data processing. Standardization of input data is therefore not required as may be necessary for a linear model, neural networks, or any model which is sensitive to the range of the different features being considered. In the notebook EDA.ipynb, one such model deep learning model is given as an example.

### Model selection, multiple regression models, and a simple baseline

The implemented model makes use of h2o's AutoML functionality to find the most appropriately suited model for the regression task. Unforunately H20 currently does not provide support for multiple output modeling and hence separate models are necessary for each output regressor. One alternative to this approach is sklearn's Decision Tree Regressor, which is capable of regressing multiple targets with a single model; this is adopted as a baseline.

One potential drawback with using one model per target response is an increased computational cost at the training phase. However, even with such considerations, H2o's AutoML feature far outperforms the baseline, and hence is recommended at the small expense of additional training time, especially since the data set is small, feature space is non high-dimensional, and there are only two target variables.

### Deploying and running the model:

Deploying and running the model is provided in a containerized form making running and deployment simple. To run locally, be sure that a Docker server is running, and first build the image by running:

`make build`

and then type:

`make run`

to deploy the docker container. In order to interact with the running services, all that is necessary is a call to curl passing along a JSON formatted string with feature space coordinates. For example:

`curl http://localhost:5000 -d '{"X1": 0.98, "X2": 514.5, "X3": 294, "X4": 110.25, "X5": 7, "X6": 4, "X7": 0, "X8": 0}'`

Thanks!


