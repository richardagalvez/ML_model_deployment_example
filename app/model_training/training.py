"""
This file trains two models, one for each regressor.
"""

import h2o
import pandas as pd
from h2o.automl import H2OAutoML

def load_training_data(data_url: str, train_fraction: float):
    """
    Description:
        Function which retrieves data from website url and returns the train/test split.
    
    Input:
        data_url: the source of our dataset.
        train_fraction: parameter specifying how much of the training data to use for training.
        seed: random seed making experiments reproducible.
        
    Returns:
        train and test h2o dataframes.
    """

    print(f'downloading training data from: \n{data_url}')
    data = pd.read_excel(data_url)
    data = h2o.H2OFrame(data)

    splits = data.split_frame(ratios = [train_fraction], seed = 1)
    train = splits[0]
    test = splits[1]

    return train, test


def train_models(data_url: str, train_fraction=0.8, max_train_time=15):
    """
    Description:
        Function which trains two models, one for each response variable (y1, y2).
        A leaderboard is also printed out so one may see which models fared best.
    
    Input:
        data_url: the source of our dataset
        max_train_time (seconds): specifies the max number of seconds for automl to run.
        seed: random seed making experiments reproducible.
        
    Returns:
        Two trained models for each response variable (y1, y2) in that order.
    """
    
    train, test = load_training_data(data_url, train_fraction)   

    print('Running in automl mode:')

    model_y1 = H2OAutoML(max_runtime_secs=max_train_time, seed=1, project_name='ee-model-y1')
    model_y1.train(y='Y1', training_frame=train.drop(['Y2'], 1), leaderboard_frame=test)

    model_y2 = H2OAutoML(max_runtime_secs = max_train_time, seed = 1, project_name = 'ee-model-y2')
    model_y2.train(y='Y2', training_frame=train.drop(['Y1'], 1), leaderboard_frame=test)

    print('')
    print(model_y1.leaderboard)
    print('')
    print(model_y2.leaderboard)

    return model_y1, model_y2
    



