# Kaggle Competitions

**Author:** [Raphael Berly](https://www.linkedin.com/in/raphaelberly), data scientist at [Erento](https://www.erento.com/info/jobs/).

### Overview

This repository gathers my work on several Kaggle competitions I participated to.

Hereby a list of the different competitions:

* [Titanic](#titanic)
* [Stack Overflow](#stack-overflow)


-----

### Titanic

This public kaggle competition, which is hosted [here](https://www.kaggle.com/c/titanic), aims at predicting the survival of passengers from Titanic. A dataset containing 891 observations and 10 features is provided for training.

This objective with this project was to implement the training phase as properly as possible, using the whole sklearn workflow (pipelines, unions, etc). One can find all the details and explanations about this in the file *Notebook.ipynb*.

A scripted version has also been implemented, and can be found in the folder *src*. It basically simulates the case where one would have to re-run the script on new train & test sets on a regular basis.

This version of the model has a precision of 78.9%. Some improvement leads are given in the  last part of the Notebook.

-----

### Stack Overflow

This private competition was hosted on Kaggle by [Data School](http://www.dataschool.io) as part of the **Machine Learning with Text in Python** eight-week training session.

The objective was to predict the status (Open or Close) of a post, based on its content and metadata.

The approach which was the following:

* Step 1: Loading and going through the data
* Step 2: Feature engineering (creating numerical features out of the data and meta-data)
* Step 3: Training a model on the engineered numerical features only
* Step 4: Vectorizing text data and training a model on the resulting document-term matrix
* Step 5: Combining engineered numerical features and vectorized text data. Two method were tested. The first one is model stacking, *i.e.* making both models from step 3 and 4 vote. The second one consists of concatenating vectorized text data and engineered numerical features, and training one model on the resulting dataset.

The best results were obtained with the second method. Such a submission scored with a log loss of 0.46281 for the public score and of 0.46369 for the private score, ranking 3rd of the competiton.
