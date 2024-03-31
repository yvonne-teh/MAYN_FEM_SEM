# MAYN Semantic Relations Software Project

Welcome to the MAYN Semantic Relations Software Project! This repository contains all the code and data used by Team MAYN for their project. Below is a structured guide through the project, explaining the purpose of each code and data file in the repository.

## Codebase

The `Codebase` directory contains all the code used in the project. Python was the primary language, with occasional use of Jupyter Notebooks. Performance analysis, particularly advanced confusion matrices, was conducted in R. The project utilized computing resources through Google Colab for Fine-Tuning, but the code is adaptable to other computing providers.

## Preprocessing

The `Preprocessing` directory includes scripts used to restructure raw data for further use, along with guidelines for verb masking and masked sentences.

- `Satz_umformer.py`: Script for reformulating sentences and extracting verbs.
- `Semeval_reader.py`: Script to parse sentences in the TRAIN_FILE and organize them into a list.
- `Masking Guidelines`: Annotator guidelines for verb masking in manually masked sentences.
- `Test_sentences.txt`: Text file containing masked sentences.

## Zero-Shot

The `Zero-Shot` directory contains scripts used for zero-shot testing.

- `algo.md`: Algorithm used for zero-shot testing.
- `Bert_predict_class.py`: Script to feed masked sentences into BERT and predict the class.
- `Softmax_and_log_dicts.py`: Contains dictionaries for each class with verb frequencies, as well as softmax and log functions.
- `LOG_and_SOFTMAX_result.ipynb`: Notebook for evaluating masked sentences and obtaining zero-shot results.

## Interpretability

The `Interpretability` directory contains a notebook used to obtain and visualize interpretability results for BERT.

- `Token_importance_visualizer.ipynb`: Script for replacing each word in a sentence with an UNK token and visualizing importance using cosine similarities between predictions.

## Fine-Tuning

The `Fine-Tuning` directory contains scripts used for fine-tuning and testing.

### Performance

- `Semeval_multiclassification.ipynb`: Notebook for evaluating sentences with a feedforward NN-model.

### Interpretability

- `Semeval_multiclassification.ipynb`: Notebook for obtaining interpretability results for the fine-tuning model using methods similar to zero-shot testing.

## Data

The `Data` directory contains all results obtained from the project.

### SemEval

In the `SemEval` folder, the training set from the original SemEval-2010 Task 8 is included. This data is used for extracting verbs, evaluating zero-shot MLM, and fine-tuning the Multi-Classifier Neural Network.

### Zero-Shot

Contains results from zero-shot testing.

### Performance

- `Zero-Shot Results Log csv`: Zero-shot results with log.
- `Zero-Shot Results Softmax csv`: Zero-shot results softmaxed.
- `Confusion Matrix Log ZS rmd`: Confusion matrix for log results.
- `Confusion Matrix Softmax ZS`: Confusion matrix for softmax results.

### Interpretability

Results used for qualitative interpretability analysis.

- `Interpretability zero-shot.pdf`: Cherry-picked sentences for interpretability analysis of the zero-shot model.

### Fine-Tuning

Contains results from fine-tuned testing.

### Performance

- `Neural_net_results.csv`: Results from the NN-model.
- `Confusion Matrix NN Fine-Tuned.rmd`: Confusion matrix for NN performance.

### Interpretability

Results used for interpretation.

- `Interpretability_fine_tuning.pdf`: Cherry-picked sentences for qualitative analysis of model interpretability.
