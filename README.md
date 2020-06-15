# Final Project JCDS Purwadhika
## Loan Predicting with Machine Learning
Alvin Hizra's Final Project of Job Connector Data Science Purwadhika Digital Technology School Bandung.

Loan Prediction is a common project of loan companies or banks to investigate 
whether their potential customer is going to be the default customer or not.
Machine learning is a method to help this project. Using classification learning,
so we can predict what a potential customer status is.

In this project, let me discuss the best metric I made, how I got it, and in the conclusion
section, I will also describe other insights I found.

The Data is from this Kaggle link.

https://www.kaggle.com/chiragc/loan-defaulting-prediction

### Pre-Processing
From the data, I merge three csv files into one dataframe. First, I change
two files that contain the monthly default value of users into one dataframe
that contains each user's default value in the period. Then, one data remaining
is about the background of each user. I delete two columns that contains about 66%
NaN value and reduce a little rows from other columns that contains NaN value
as well.

So, the last sighting of the dataframe after pre-processing is going to look
like this.
![Capture](https://user-images.githubusercontent.com/60774740/83596124-0cfbf780-a58e-11ea-8125-04d1e34a0e09.PNG)

*birth_date column is dropped later.*

### Returned value
Returned value is my formula to help me judge model output. This formula is 
written like this.

<img src="https://render.githubusercontent.com/render/math?math=returned = (recall0 * n0 * m0) + ( (1-recall1) * n1 * m1) / loanedmoney">

Where:
- n0 : number of people on test data whom not default
- n1 : number of people on test data whom default
- m0 : mean of loan amount
- m1 : how much loan amount returned until the most default month.
- loaned_money : sum of loan amount of predicted customer who not default

### Modelling
I used some classification models for predicting loans. RandomForestClassification 
turns out to be the best model that produced the best metrics and returned value 
produced.
| Recall Default   |      f1-score      |  Returned Value |
|----------|:-------------:|------:|
| 0.28 |  0.64 | 0.983 |

So, to upgrade the result, I try to find the best threshold by auc roc, do RandomizedSearchCV
and do SMOTE oversampling. After doing that back and forth, it turns out the best result
is produced after doing oversampling, finding best parameters, then finding the best threshold.

This is the result.
| Recall Default   |      f1-score      |  Returned Value |
|----------|:-------------:|------:|
| 0.72 |  0.58 | 0.987 |

f1-score is reduced, but we a little bit upgraded the returned value.

### Conclusion
Overall, what an amazing project we have, hopefully this is helping us to get
better understanding at classification machine learning.

I think we still can improve our result via GridSearchCV. And I assume the data is
not fully complete. Like, if you look at Province columns, the datas are not
common province names, they are just alphabetic. The same situation happens with 
columns, like group, contract type, and history type. If we have an explanation of those
columns, I think we could get better features and improve our result.

Some insights I get from the data are:
- The company should add interest about 2%.
- The company needs to upgrade the loan market in Province D, F, L because they produce a high amount of loan.
- The company also needs to expand the market to Province G because there are almost no default customer provinces and a big ratio of no default customers. 
- On Province J, they need to campaign to people who older than 45 and/or has typical for contract type A or history type A
- Start Massive Campaign on Province N


### Dashboard
Thanks to Colorlib.com, I have built this beauty dashboard to support this Loan Predictor Modelling. There are 5 pages, which are:

#### Home
This page is to fill features for predicting Loan status. There is 9 features which is, family size, contract type, gender, 
province, age, group history type, monthly expense, and loan amount.
![Untitled](https://user-images.githubusercontent.com/60774740/81801257-51234b80-953e-11ea-8c00-9d0aedb2032b.png)

### Prediction
This page tells the result of the input that we give at the Home page.
![Untitled2](https://user-images.githubusercontent.com/60774740/81801524-c3942b80-953e-11ea-978a-873ab88a2c92.png)

### Data
This page shows some datas that I have cleaned and prepared for modelling.
![Untitled3](https://user-images.githubusercontent.com/60774740/81801784-24bbff00-953f-11ea-9990-1d34e9006edb.png)

### Plot
This page shows some plots. There are barplot for user status in each Province, heatmap of loan amount of each Province,
histogram of customer's age and loan amounts.
![Untitled4](https://user-images.githubusercontent.com/60774740/81801792-28e81c80-953f-11ea-977b-3563b151b41e.png)

### Author
This page tells you more about me.
![Untitled5](https://user-images.githubusercontent.com/60774740/81801805-2d143a00-953f-11ea-9941-a919c7605071.png)

##### Thanks for reading! 
