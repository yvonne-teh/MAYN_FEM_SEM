from nltk.stem import WordNetLemmatizer
from transformers import pipeline
import numpy as np


# BERT maskierten satz geben
def bert_predict(sentence):
    model = pipeline('fill-mask', model='bert-base-uncased')
    pred = model(sentence)
    # bert wahrscheinlichkeiten neu verteilen
    
    return pred

# verb stemmen
def get_verb_lemma(verb: str) -> str:
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(verb, pos='v')


def softmax_basic(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def softmax_dict(d: dict) -> dict:
    x = []
    for entry in d.items():
        x.append(entry[1])
    for softmaxed_value, key in zip(softmax_basic(x), d):
        d[key] = softmaxed_value
    return d

# mit dicts vergleichen
def predict_class(bert_predictions, class_dicts):
    scores = []
    score = 0
    for d in class_dicts:
        for prediction in bert_predictions:
            try:
                verb = get_verb_lemma(prediction['token_str'])
                score += d[0][verb] * prediction['score']
            except KeyError:
                continue

        scores.append((score))
        score = 0
    
    # softmaxen und nach labels sortieren
    softmaxed_scores = softmax_basic(np.array(scores))
    labeled_scores = []
    for score, label in zip(softmaxed_scores, class_dicts):
        labeled_scores.append([label[1], score])
    labeled_scores = sorted(labeled_scores, key=lambda item: item[1], reverse=True)
    return labeled_scores
