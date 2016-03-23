# AP Statistics: End of the project

>Jay Ma, Nick Lin

### 1. Question:
***

Does the quality of the computer really depends on the price of the computer? Will the higher price of the PC shows the better quality?



### 2. Data Set

Sources:

https://vincentarelbundock.github.io/Rdatasets/datasets.html

**Ecdat	Computers	Prices of Personal Computers**

Format .CSV

### 3.Data Analysis

We want to find the confidence interval of slope between the price and the quality of a computer.
So we need to see whether the conditions are met.

**Assume y=quality, x=price**


Check Conditions:

We’ll use our LINER acronym:


```
Linear: The (true) relationship between x and y is linear, the residual plot is randomly distributed under and above the residual=0 line. 
Independent: Individual observations are independent of each other, the sample is randomly assigned and less the 10% of the whole population, which is all the computers.
Normal: The residual histogram shows no strong skewness.
Equal SD: The residual is roughly equally distributed under and above the residual=0 line.
Random: The data come from a well-designed random sampling.
```

Use Ordinary least squares (OLS).

1.Import Data into Python Dict Data

2.Formulate the quality value according to the specific value

3.Plot the data

4.Linear Regression y = mx + b

```
m = 0.455789547667
b = 0.250230589531
Mean = 1011.9100495286787
Std = 570.70164409207905
```

The OLS Result:

![](http://i4.tietuku.cn/379469de85c2e3fd.png)

Graphs:

![](http://i4.tietuku.cn/8e9669f55186e27d.png)

5.Calculate

And we use computer to calculate the 95% confidence interval, which is (0.450-0.461).





### 4. Conclusion

We are 95% confident that the interval from 0.450 to 0.461 captures the slope of the true regression line relating the computer quality y and computer price x.