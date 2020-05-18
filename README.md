# Final Project JCDS Purwadhika
Alvin Hizra's Final Project of Job Connector Data Science Purwadhika Digital Technology School Bandung.

This Project is about Machine Learning and applying it to predict Loan Default. The Data is from this Kaggle link.

https://www.kaggle.com/chiragc/loan-defaulting-prediction

### Modelling
I used a few classification models for predicting loan. From all of them, I choose RandomForestClassification to be upgraded.
Then, I do oversampling with SMOTE, but the result is no better. So I choose predicting without oversampling. The Result is 77% f1-score for training data and 86% for its recall default value. For testing data, I get 63% f1-score with 61% recall default value.

### Dashboard
Thanks to Colorlib.com, I have built a beauty dashboard for support this Loan Predictor Modelling. There are 5 pages, which are:

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
