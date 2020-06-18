# Cancer-detection-data-analysis-prediction

## Details about the Data Analysis 
1. Importing the given dataset into our main program.
2. Separating the Data Frame into Target and Feature Attributes.
3. Then we need to look for values that are needed to be encoded. If required, then we need to encode it using Label 
   Encoder Classifier from sklearn.preprocessing package.
4. To prevent our model from over fitting, we need to select only those Feature attributes having higher 
   feature importance.
5. Then we need to split the dataset into Training and Testing dataset.Using train_test_split classifier and 
   setting the test size to 0.2%. Now Preprocessing of our dataset is complete, we shall move forward to Train 
   the required classifiers which we will be using.
6. Training the classifiers (Logistic Regression, GaussianNB, KNNeighbors, Decision Tree) with x_train, y_train.
7. Testing our trained model to predict the outcome.
8. Finding individual accuracies of each model
9. Displaying the Confusion Matrix for the prediction made by all the classifiers
10. After that we make a Strong Model or the Voting Classifier to check and compare it with the models made.
11. We then provide an inference of which model to choose.
12. Finally we compare between the strong and weak model and bring out the best of result.
13. We then create an user interface and therefore take the details from user 
14. We pass the data through a framework and calculate the tendency of Breast cancer by nurturing the data
	through the best model we had predicted above
15. We therefore are able to predict if the patient have the breast cancer or not.
