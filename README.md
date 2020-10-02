# SMS SPAM Detection

## Table of Content

* [Demo](#demo)
* [Abstract](#abs)
* [Motivation](#mot)
* [About the Data](#data)
* [Modeling](#model)
    * [How Naive Bayes model can be fooled?](#fail)
* [Credits](#credits)

## Demo <a id='demo'></a>
The finished product can be viewed [here](https://spamorham-1.herokuapp.com/)

<img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/Screenshot%20(4).png'>

## Abstract <a id='demo'></a>
* [SPAM SMS Detector](https://spamorham-1.herokuapp.com/) is an **end-to-end Machine Learning NLP project** built using **Flask** and deployed to **Heroku Cloud Platform.** This app will help you predict whether the **SMS** that you recieved is **legit** (HAM) or **SPAM**. The **dataset** used for this project is taken from **Kaggle** has **5,574** records, **749 SPAM** and **4,825 HAM**, more info about the data in "[About the Data](#data)" section. 
* Out of all the **ML models** used **Naive Bayes** seems to have preformed decent with **accuracy** of **99.01%** and **precision** of **98.56%**. Built various **pipelines** with **MultinomialNB classifier** and **Bag of Words** as well as **TFIDF** approach, taking different **classification metrices** (Accuracy, Precision, f1-score, roc-auc-score) into account, also **tuned the hyperparameters**.
The final output looks something like this - 

   <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/index.png'>.

More on that in [this section](#model).
* The final **pipeline** chosen has the following **performance report** -
        <table border="1" class="dataframe">  
        <thead>    <tr style="text-align: right;">      <th></th>      <th>score</th>    </tr>  </thead>  <tbody>    <tr>      <th>accuracy</th>      <td>99.01</td>    </tr>    <tr>      <th>f1-score</th>      <td>96.14</td>    </tr>    <tr>      <th>precision</th>      <td>98.56</td>    </tr>    <tr>      <th>recall</th>      <td>93.83</td>    </tr>    <tr>      <th>roc auc score</th>      <td>96.81</td>    </tr>  </tbody></table>

## Motivation <a id='mot'></a>
* As a part of **#66daysoddata** community created by **Ken Jee** from youtube, I did this project to be **consistent** in my **DS, ML and DL** learning journey and building a **habit** of doing **Data Science** daily.
* And also because my **curiosity** in **NLP** has spiked to an extent where I have feed myself with the **text data** and perform some **analysis** on it on a daily basis. I also want to **explore**, what more I can do with **NLP**

## About the Data <a id='data'></a>
* Our dataset originally has **5,574** records, **749 SPAM** and **4,825 HAM**, which you can see from the **distribution** below.
    <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download.png'>
    * Our dataset is clearly **imbalanced**, but trust me, with **Naive Bayes** as our model used, the imbalanced dataset seems to have **no affect** on the **performance**, as our **accuracy** and **precision**, both are decent.

#### Analysis of SPAM messages - 
* **SPAM SMSs** tends to be bigger than **legit SMSs**, which is evident from the graph below.

    <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download%20(1).png' width='500px'>

    * **Mean length** of **SPAM SMSs** is close to **140**, which is almost **double** the length of **Legitmate SMS** which is close to **71**.

* The **most common words** used in **SPAM** messages can be seen from the **WordCloud** below.

    <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download%20(2).png' width='1000px'>

    * Here, is the list of **top 10 most used words** used in **SPAM Messages**

        <table border="1" class="dataframe">
        <thead>
            <tr style="text-align: right;">
            <th></th>
            <th>Word</th>
            <th>Frequency</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <th>0</th>
            <td>call</td>
            <td>388</td>
            </tr>
            <tr>
            <th>1</th>
            <td>free</td>
            <td>228</td>
            </tr>
            <tr>
            <th>2</th>
            <td>txt</td>
            <td>170</td>
            </tr>
            <tr>
            <th>3</th>
            <td>text</td>
            <td>145</td>
            </tr>
            <tr>
            <th>4</th>
            <td>mobile</td>
            <td>142</td>
            </tr>
            <tr>
            <th>5</th>
            <td>stop</td>
            <td>128</td>
            </tr>
            <tr>
            <th>6</th>
            <td>claim</td>
            <td>115</td>
            </tr>
            <tr>
            <th>7</th>
            <td>reply</td>
            <td>106</td>
            </tr>
            <tr>
            <th>8</th>
            <td>www</td>
            <td>98</td>
            </tr>
            <tr>
            <th>9</th>
            <td>prize</td>
            <td>97</td>
            </tr>
        </tbody>
        </table>

    * This graph says the same - 

        <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download%20(3).png' width='500px'>
* For **more detailed analysis**, you can have a look at my [Ipython Notebook for SPAM SMS EDA and Preprocessing](https://github.com/animesharma3/SPAM-SMS-Detection/blob/master/notebooks/Spam%20SMS%20EDA%20and%20Preprocessing.ipynb)

## Modeling <a id='model'></a>


## Credits <a id='credits'></a>
