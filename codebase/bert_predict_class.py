from nltk.stem import WordNetLemmatizer
from transformers import pipeline
import numpy as np
from softmax import softmax



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
    
    # softmax and sort scores and add labels
    softmaxed_scores = softmax(np.array(scores))
    labeled_scores = []
    for score, label in zip(softmaxed_scores, class_dicts):
        labeled_scores.append([label[1], score])
    labeled_scores = sorted(labeled_scores, key=lambda item: item[1], reverse=True)
    return labeled_scores
