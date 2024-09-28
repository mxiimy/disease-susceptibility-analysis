# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:10:58 2024

@author: Owner
"""

from sklearn import linear_model
import numpy as np

x = np.linspace(0, 10, 100)
x = np.array([x, x])
y = np.linspace(0, 10, 100)


def get_weights(env_data: np.ndarray, gene_expression: np.ndarray):
    """
    :param x:
    :param y:
    :return:
    """
    # Get possible combinations of features by index.
    model = linear_model.LinearRegression().fit(x, y)
    return model


def predict(model, env_data: np.ndarray) -> np.ndarray:
    return model.predict(env_data)


def get_risk_score(gene_expression_vec: np.ndarray, risks: np.ndarray):
    sum(gene_expression_vec[i] * risks[i] for i in range(len(risks)))

def get_env_data(location):
    ...


if __name__ == '__main__':
    env_data = ...
    gene_expression = ...
    model = get_weights(env_data, gene_expression)

    location = ...
    sample_env_data = get_env_data(location)
    gene_expression_vec = predict(model, env_data)

    #
    risks = ...
    risk = get_risk_score(gene_expression_vec, risks)