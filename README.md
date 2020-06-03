# Final Project JCDS Purwadhika
## Loan Predicting with Machine Learning
Alvin Hizra's Final Project of Job Connector Data Science Purwadhika Digital Technology School Bandung.

Loan Prediction is common project of loan company or bank to investigate 
wheter their potential customer is going to be default customer or not.
Machine learning is a method to help this project. Using classification learning,
so we can predict what a potential customer status is.

In this project, let me discuss best metric I made, how I get it, and in conclussion
section, I will also describe other insights I found.

The Data is from this Kaggle link.

https://www.kaggle.com/chiragc/loan-defaulting-prediction

### Pre-Processing
From the data, I merge three csv files into one dataframe. First, I change
two files that contains monthly default value of users into one dataframe
that contains each user's default value in the period. Then, one data remaining
is about background of each users. I delete two columns that contains about 66%
NaN value and reduce a little rows from other columns that contains NaN value
as well.

So last sighting of the dataframe after pre-processing is going to be looked
like this.

### Modelling
I used a few classification models for predicting loan. From all of them, I choose RandomForestClassification to be upgraded.
Then, I do oversampling with SMOTE, but the result is no better. So I choose predicting without oversampling. The Result is 77% f1-score for training data and 86% for its recall default value. For testing data, I get 63% f1-score with 61% recall default value.

### Dashboard
Thanks to Colorlib.com, I have built a beauty dashboard to support this Loan Predictor Modelling. There are 5 pages, which are:

#### Home
This page is to fill features for predicting Loan status. There is 9 features which is, family size, contract type, gender, 
province, age, group history type, monthly expense, and loan amount.
![Untitled](https://user-images.githubusercontent.com/60774740/81801257-51234b80-953e-11ea-8c00-9d0aedb2032b.png)

### Prediction
This page tells the result of the input that we give at Home page.
![Untitled2](https://user-images.githubusercontent.com/60774740/81801524-c3942b80-953e-11ea-978a-873ab88a2c92.png)

### Data
This page shows some datas that I have been cleaned and prepared for modelling.
![Untitled3](https://user-images.githubusercontent.com/60774740/81801784-24bbff00-953f-11ea-9990-1d34e9006edb.png)

### Plot
This page shows some plots. There are barplot for loan status in each Province, heatmap of loan amount of each Province,
histogram of customer's age and loan amounts.
![Untitled4](https://user-images.githubusercontent.com/60774740/81801792-28e81c80-953f-11ea-977b-3563b151b41e.png)

### Author
This page tells you more about me.
![Untitled5](https://user-images.githubusercontent.com/60774740/81801805-2d143a00-953f-11ea-9941-a919c7605071.png)
