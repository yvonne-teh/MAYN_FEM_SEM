import numpy as np

def softmax(x):
    # Compute softmax values for each sets of scores in x.
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def softmax_dict(d: dict) -> dict:
    x = []
    for entry in d.items():
        x.append(entry[1])
    for softmaxed_value, key in zip(softmax(x), d):
        d[key] = softmaxed_value
    return d