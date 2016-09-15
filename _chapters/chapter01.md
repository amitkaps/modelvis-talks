---
layout: default
title: Chapter 01 - Introduction
permalink: chapter01
---

# 1. Introduction

##### Read Bret Victor's essay on [Up and Down the Layers of Abstraction](worrydream.com/LadderOfAbstraction/)

Data science is a process of abstraction. In order to explain or to predict a real phenomena, the process start with framing the problem, acquiring & refining the data and then moves between the three layers of abstraction - transformations (data abstraction), visualisations (visual abstraction) and modelling (symbolic abstraction). All these three layers of abstraction work together to try and build a truer (or more closer) representation of the real phenomena.

##### See talk on [Visualising Multi-Dimensional Data](https://www.youtube.com/watch?v=X8rNDvPNg30)

Data visualisation (data-vis) helps us to understand the portrait and the shape of the data. The science of data-vis for exploratory data analysis is well developed, for both static graphics (scatter plot matrices, glyph based approaches, geometric transforms like parallel coordinates) and interactive graphics (layering, brushing and linking, projections and tours).  However, the power of visualisation is rarely leveraged for understanding the models developed better. Model evaluation is still largely restricted through numerical summaries.

```

Data Transformation  — — — —  Model Building
    (Tidy Data)                              
         │                                 
         │                                 
         │                                 
 Visual Exploration   
     (Data-Vis)
  
```
Extending visualisation to model building can be a powerful way to improve our understanding of the model. We can use visualisation to aid the transition of *implicit knowledge* in the data and your head to *explicit knowledge* in the model.

Model visualisation (model-vis) can help us to understand the shape of the model and compare it to the shape of the data. It allows to see the fit of the model and understand where the fit can be improved. It also allows us to better understand the parameters in the model and how the model changes when the parameters change as well as how the parameters changes when the input data changes.

```

Data Transformation  — — — —  Model Building
    (Tidy Data)                (Tidy Model) 
         │                          |       
         │                          |      
         │                          |      
 Visual Exploration          Model Exploration
     (Data-Vis)                 (Model-Vis)
  
```

## Model-Vis Approach

[0] Visualise the data space   
[1] Visualise the predictions in the data space   
[2] Visualise the errors in model fitting   
[3] Visualise with different model parameters   
[4] Visualise with different input datasets   
[5] Visualise the entire model space   
[6] Visualise the many models together   

Let us take a small dataset `cars` to understand the concepts in model-vis.


##### See the Code

##### [chapter01-Py.ipynb](http://nbviewer.jupyter.org/github/amitkaps/modelvis/blob/master/notebooks/chapter01-Py.ipynb)

##### [chapter02-R.ipynb](http://nbviewer.jupyter.org/github/amitkaps/modelvis/blob/master/notebooks/chapter01-R.ipynb)

### [0] Visualise the data space

The starting point for any model-vis is to visualise the data. In this case as we only have three variables, we can start with a scatter plot between `kmpl` and `price` and use colour to visualise the `type` of car.

![](assets/images/01-00-data.png)


### [1] Visualise the predictions in the data space

![](assets/images/01-01-prediction.png)

### [2] Visualise the errors in model fitting

![](assets/images/01-02-errors.png)

### [3] Visualise with different model parameters

### [4] Visualise with different input datasets

### [5] Visualise the entire model space

### [6] Visualise the many models together

<br>

[<- previous](\)
| [home](\)
| [next ->](\chapter02)
