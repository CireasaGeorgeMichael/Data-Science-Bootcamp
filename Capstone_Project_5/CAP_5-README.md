Capstone project 5 : Image recognition classifier using the MNIST dataset.

Requirements :
 - Use the MNIST dataset ( 70000 handwritten numbers divided into a training set and a test set 60000/10000 ).
 - Create a classification model on the data.
 - Show the accuracy of the model.

Development:
 - The dataset was split into Training set, Development (Validation) set and Testing set.
 - Using The Random Forest Classifier, I trained a couple of models with different values  for the n_estimators parameter
   to see does it affect the score of each model by testing it on the development set.
 - After finding a value for the n_estimator I also used the same technique to tune the max_depth parameter.
 - With the best values for the two parameters of the classifier I trained a final model to be used on the  testing set.
 - I obtained an accuracy score of around 96%.