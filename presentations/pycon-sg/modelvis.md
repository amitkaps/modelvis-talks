theme: Fira

# [fit] **Visualising**
# [fit] Machine Learning Models

**Amit Kapoor**
@amitkaps

--- 

![](images/see.jpg)
> We don’t see things as they are, we see them as we are.
-- Anais Nin

---

![fit](images/elephant1.jpg)

---

> "And so these men of Indostan
Disputed loud and long,
Each in his own opinion
Exceeding stiff and strong,
Though each was partly in the right,
And all were in the wrong."

*— John Godfrey Saxe*

---

![](images/see.jpeg)
> "Data is just a clue to the end truth"
-- Josh Smith

---

![](images/lens.jpeg)
## Making sense of the world through a data lens

---

![fit](images/pendelum.gif)

---

![](images/layers.jpg)
## Layers of Abstraction

---

![](images/layers2.jpg)
## **Data** Abstraction
## **Visual** Abstraction
## **Model** Abstraction

---

> "Geometry without algebra is dumb! Algebra without geometry is blind!" 
-- David Hestenes

---

![](images/singapore.jpg)
## Trading Game
### When to **Buy, Hold or Sell** the stock?

---

![](images/stock.jpg)
## Stock of Shares
### Start at **1000 shares**

---

![](images/money.jpg)
## Price of Shares 
### Starting at **Price SGD 100**

---

![](images/time.jpg)
## Time in a day
### **500 minutes** of trading

---

## Visualise the data

---

![fit](images/money-vis1.png)

---

## Simple Model 
### One Minute Strategy
### If **price > 5%**, then **Sell** 1 share
### If **price < 5%**, then **Buy** 1 share 

---

## Visualise the model 
### **(1)** within the **data space**

---

![fit](images/money-vis2.png)

---

## Visualise the model 
### **(2)** with **varying model** parameters
### **(3)** for the process of **model fitting**

#### *Model Bounds - From 1% to 10%*

---

![fit](images/money-vis3.png)

---

## Visualise the model 
### **(4)** with **entire model space**
#### *Add one more model - 2 minute strategy*

---

![fit](images/money-vis6.png)

---

## Visualise the model 
### **(5)** with **different input datasets**
#### *Add five input datasets*

---

![fit](images/money-vis4.png)

---

![fit](images/money-vis5.png)

---

## Model Vis Approach
### within the **data space** <br> with **varying model** parameters <br> for the process of **model fitting** <br> with **entire model space** <br> with **different input datasets**

---

![](images/art.jpeg)
## Model Visualisation is more an **Art**, than a Science.

---

![](images/glass.jpg)
### Aid the transition of **implicit knowledge** in the data and your head to **explicit knowledge** in the model.

---

![](images/frame.jpg)
## Frame
### "An approximate answer to the right problem is worth a good deal"

---

![](images/acquire.jpg)
## Acquire
### "80% perspiration, 10% great idea, 10% great output"

---

![](images/refine.jpg)
## Refine
### "All data is messy."

---

![](images/transform.jpg)
## Transform
### "The world does not work on the scales it happens to be measured on."

---

![](images/explore.jpg)
## Explore
### "I don't know, what I don't know."

---

![](images/model.jpg)
## Model
### "All models are wrong, but some are useful"

---

![](images/insight.jpg)
## Insight
### "If you can’t explain it simply, you don’t understand it well enough."

---

## **Transform**
## **Explore**
## **Model**

---

## ML Approach
### Focus on improving the **predictive ability** of the model
### Being careful to fairly **assess it** (train vs. test)

---

## Black boxes
### The model does a **really good job**, but you **don’t know why.**

---

## Challenges
### How do you apply real world knowledge to the model? 
### Will it work in the long-term, as fundamentals change?

---

![](images/weaklink.png)

---

### ML Approach : Model Vis
#### DIMENSIONALITY REDUCTION : within the **data space** 
#### FEATURE SELECTION : with **varying model** parameters 
#### CROSS-VALIDATION : for the process of **model fitting** 
#### ENSEMBLE : with **entire model space** 
#### BOOTSTRAP : with **different input datasets** 

---

## **Ideas** to develop on Model Visualisation

---

![](images/wine.jpg)
## Predicting the Quality of Wine
### 1599 Observation with 12 dimensions
---

## 1 target <br> *based on sensory data* <br> 

### **Wine Quality**

---

![fit](images/explore-quality.png)

---

### 11 features <br> *based on physicochemical tests* 

#### **alcohol** <br> **density, pH** <br> **residual sugar** <br> **fixed acidity, volatile acidity, citric acid** <br> **chlorides, free sulfur dioxide, total sulfur dioxide, sulphates**

---

![fit](images/explore-single.png)
### Dual Variable Exploration 

---

![fit](images/explore-single.png)

---

![fit](images/explore-dual.png)
### Three Variable Exploration 

---

![fit](images/explore-dual.png)

---

![fit](images/parallel.png)
### Multidimensional Exploration 

---

![fit](images/parallel.png)

---

![fit](images/parallel-select.png)

---

## Linear Regression
### **quality ~ f(alcohol, pH,... sulphates)**
#### model score = 0.36

---

## Visualise the model 
### **(1)** within the **data space**

---

## Add **predicted data**
### Use data generated from model as regular data - manipulate it and visualise it in many different ways.

---

![fit](images/model-all.png)

---

## Visualise the model 
### **(3)** with the process of **model fitting**

---

## Use **residuals**
### To subtract patterns from the data, while adding them to the model

---

![fit](images/model-residual1.png)

---

![fit](images/model-residual2.png)

---

## Binary Classification
### **Class 0** (Low): Quality = [3,4,5]
### **Class 1** (High): Quality = [6,7,8]

---

![fit](images/classify-plot.png)

---

## Play with **Projections**
### Be able to view the data in **multiple projections** - guided tours, projection pursuit 

---

![fit](images/classify-projection.png)


---

## Logistic Regression
### model score - 0.74

---

![fit](images/classify-logistic-pred.png)

---

## Evaluate **Boundaries** 
### Sample data with border probabilities to create boundaries

---

![fit](images/classify-logistic-prob.png)

---

## Evaluate **Boundaries**
### Create a **mesh** of entire range of data

---

## Mesh - **Logistic Regression**

---

![fit](images/classify-logistic.png)

---


## Mesh - **Quadratic Discriminant Analysis**

---

![fit](images/classify-qda.png)

---

## Mesh - **Random Forest**

---

![fit](images/classify-random.png)

---

## **Not Easy!**
### Selective approaches articulated
### Curse of Dimensionality
### Poor interactive tools
### Limited package development in Python

---

## Work in Progress

### **Projection** module
### **Bootstrap** module
### **Cross Validation** module 

---

## Model Visualisation
### [https://github.com/amitkaps/modelvis](https://github.com/amitkaps/modelvis)

---

![left](images/credits.jpeg)

## **Amit Kapoor** <br> *Crafting Visual Stories with Data*
## [@amitkaps](http://twitter.com/amitkaps)
## [amitkaps.com](http://amitkaps.com)
