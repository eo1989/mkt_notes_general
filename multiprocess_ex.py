import itertools as it
import multiprocessing as mp
import random

import numpy as np
import pandas as pd


def _assemble_neg_pos_pairs(y_test, prob_predict, subset_percentage = 0.1):
    df = pd.concat([y_test, prob_predict], axis = 1)
    df = df.sample(frac = subset_percentage)
    cols = list(df)
    true_label = cols[0]
    predicted_probability = cols[1]
    neg_df = df.loc[df[true_label] == 0]
    neg_probs = neg_df[predicted_probability].to_list()

    pos_df = df.loc[df[true_label] == 1]
    pos_probs = pos_df[predicted_probability].to_list()

    return list(it.product(neg_probs, pos_probs))


def _find_discordants(pairs):
    discordants = 0
    if pairs[0] >= pairs[1]:
        discordants += 1
    return discordants


def find_concordant_discordant_ratio_somers_d(y_test, prob_predic, model_uid):
    pairs = _assemble_neg_pos_pairs(y_test, prob_predic)
    with mp.Pool(processes = mp.cpu_count()) as pool:
        result = pool.map(_find_discordants, pairs)
    pairs = len(result)
    discordant_pairs = sum(result)
    concordant_discordant_ratio = 1 - (discordant_pairs / pairs)
    concordant_pairs = pairs - discordant_pairs
    somers_d = (concordant_pairs - discordant_pairs) / pairs
    pd.DataFrame({'concordant_discordant_ratio': [concordant_discordant_ratio], 'somers_d': [somers_d]}).to_csv(f'{model_uid}_concordant_discordant.csv', index = False)


if __name__ == "__main__":
    df = pd.DataFrame({
        'target': np.random.randint(0, 2, size = 5_000),
        'pred': [random.random() for _ in range(5_000)]
    })
    find_concordant_discordant_ratio_somers_d(df['target'], df['pred'], model_uid='test')