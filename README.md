# SMS SPAM Detection

## Table of Content

* [Demo](#demo)
* [Abstract](#abs)
* [Motivation](#mot)
* [About the Data](#data)
    * [Overview](#overview)
    * [Analysis of SPAM Messages](#anal)
    * [WordCloud for SPAM Messages](#wordcloud)
    * [Commonly used words in SPAM messages](#common)
* [Modeling](#model)
    * [Why Naive Bayes?](#whyNB)
    * [The Math Behind the metrices used.](#math)
    * [How I have constructed the pipelines?](#best)
    * [Choosing best Pipeline - The Dilemma of "Accuracy" and "Precision"](#dilemma)
    * [How our Naive Bayes model can be fooled?](#fail)
* [Credits](#credits)

## Demo <a id='demo'></a>
The finished product can be viewed [here](https://spamorham-1.herokuapp.com/)

<img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/Screenshot%20(4).png'>

## Abstract <a id='abs'></a>
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
#### Overview <a id='overview'></a>
* Our dataset originally has **5,574** records, **749 SPAM** and **4,825 HAM**, which you can see from the **distribution** below.
    <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download.png'>
    * Our dataset is clearly **imbalanced**, but trust me, with **Naive Bayes** as our model used, the imbalanced dataset seems to have **no affect** on the **performance**, as our **accuracy** and **precision**, both are decent.

#### Analysis of SPAM messages - <a id='anal'></a>
* **SPAM SMSs** tends to be bigger than **legit SMSs**, which is evident from the graph below.

    <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download%20(1).png' width='500px'>

    * **Mean length** of **SPAM SMSs** is close to **140**, which is almost **double** the length of **Legitmate SMS** which is close to **71**.

* The **most common words** used in **SPAM** messages can be seen from the **WordCloud** below.
    <a id='wordcloud'></a>
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

    * This graph says the same - <a id='common'></a>

        <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/download%20(3).png' width='500px'>
* For **more detailed analysis**, you can have a look at my [Ipython Notebook for SPAM SMS EDA and Preprocessing](https://github.com/animesharma3/SPAM-SMS-Detection/blob/master/notebooks/Spam%20SMS%20EDA%20and%20Preprocessing.ipynb)

## Modeling <a id='model'></a>
<a id='whyNB'></a>
* I used **Naive Bayes** because it
    * **works well** with **large no. of features**, and after performing **Word Vectorization**, no. of features has become more than 6000.
    * **converges faster** while training the model.
    * **works well** with **categorical** data.
    * is **preferrable** while working with the **text data**.
    * **outperformed** other models like **SVM, Logistic Regression** etc.

* #### The Math behind the metrices used <a id='math'></a>

    <img src='https://i.stack.imgur.com/U0hjG.png'>

<a id='best'></a>

* I performed **GridSearchCV** 4 times, each time I aim at different **metrics** to optimize and hence constructed 4 different **pipelines**.
    * **Pipeline 1** - Aimed for better **Accuracy**
    * **Pipeline 2** - Aimed for better **F1-Score**
    * **Pipeline 3** - Aimed for better **Precision**
    * **Pipeline 4** - Aimed for better **ROC-AUC**

* **Confusion Matrix** for all the pipelines can be seen below - 
    * **Pipeline 1: Accuracy**
        <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/pipe1.png'>

    * **Pipeline 2: F1-Score**
        <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/pipe2.png'>

    * **Pipeline 3: Precision**
        <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/pipe3.png'>

    * **Pipeline 4: ROC-AUC-Score**
        <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/pipe4.png'>

* **Performance Report** of all the **Pipelines** - 
    <table border='1'>
    <thead>
        <tr>
        <th></th>
        <th>pipeline1</th>
        <th>pipeline2</th>
        <th>pipeline3</th>
        <th>pipeline4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <th>accuracy</th>
        <td>0.990117</td>
        <td>0.990117</td>
        <td>0.977538</td>
        <td>0.983827</td>
        </tr>
        <tr>
        <th>f1-score</th>
        <td>0.961404</td>
        <td>0.961404</td>
        <td>0.906367</td>
        <td>0.934783</td>
        </tr>
        <tr>
        <th>precision</th>
        <td>0.985612</td>
        <td>0.985612</td>
        <td>1.000000</td>
        <td>0.992308</td>
        </tr>
        <tr>
        <th>recall</th>
        <td>0.938356</td>
        <td>0.938356</td>
        <td>0.828767</td>
        <td>0.883562</td>
        </tr>
        <tr>
        <th>roc auc score</th>
        <td>0.968144</td>
        <td>0.968144</td>
        <td>0.914384</td>
        <td>0.941264</td>
        </tr>
    </tbody>
    <table>

* When we aim for better **accuracy** and **f1-score**, we get exactly same report. Therefore, **Pipeline1** and **Pipeline2** will work similarly, which is evident from their **Confusion Metrices**.

* When we aimed for better **precision**, we get **Zero False Positives**, but it has impacted other metrices like **Accuracy, Recall, f1-score and ROC-AUC-Score**

* **Pipeline4** worked fine.

* Their **performance** can be seen from the **graph** below - 

    <img src='https://raw.githubusercontent.com/animesharma3/SPAM-SMS-Detection/master/images/index.png'>.

* ### Choosing Best Pipeline - The Dilemma of Accuracy and Precision<a id='dilemma'></a>

    * **Why I am stressing on Precision?**<a id='prec'></a>
        * Because our **goal** is to **reduce** the **False Postives**, which means **SMSs which are falsely predicted as SPAM**, otherwise the user might miss on some important SMSs and **maximizing precision** will help us in **minimizing false positive**, which is evident from the formula of precision, for which you can refer [this section](#math)
       * **Pipeline 1** gives **best accuracy** and **decent precision**
       * **Pipeline 3** gives **best precision** with **zero false positives** but **screws up other scores**. 

* Keeping all these things in mind, I have chosen **pipeline1** which uses **Naive Bayes Classifier** and **TF-IDF Word Vectorizer**

* The **Final Classification Report** for this pipleine is shown below - 
<table border="1" class="dataframe">  
        <thead>    <tr style="text-align: right;">      <th></th>      <th>score</th>    </tr>  </thead>  <tbody>    <tr>      <th>accuracy</th>      <td>99.01</td>    </tr>    <tr>      <th>f1-score</th>      <td>96.14</td>    </tr>    <tr>      <th>precision</th>      <td>98.56</td>    </tr>    <tr>      <th>recall</th>      <td>93.83</td>    </tr>    <tr>      <th>roc auc score</th>      <td>96.81</td>    </tr>  </tbody></table>


### How Our Naive Bayes Model can be Fooled? <a id='fail'></a>
I humbly **acknowledge** that my **NB model** can be **fooled** easily, if we stuff our **SMS** with **lots and lots of "hammy words"** (meaning the words that generally doesn't appear in SPAM messages [Wordcloud](#wordcloud)). 
Therefore, the **Choice of words** can easily **fool** our **model**

For more details you can have a look at my [Ipython notebook for NLP Pipeline building](https://github.com/animesharma3/SPAM-SMS-Detection/blob/master/notebooks/SMS%20SPAM%20Classifier%20-%20NLP%20Pipeline%20Building.ipynb).

## Credits <a id='credits'></a>
* **Google Colaboratory** for providing the **computational power** to **build** and **train** the **models**.
* **Heroku Cloud Platform** for making the **deployment** of this **project** possible.
* **#66daysofdata** community created by **KenJee** that is keeping me **accountable** and **consistent** in my **Data Science Journey**.
