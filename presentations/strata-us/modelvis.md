theme: Olive Green, 8

# [fit] **Visualising ML Models**
## ___
## Amit Kapoor
## @amitkaps

---

# **Story**
## ___
## “We don’t see things as they are, we see them as we are.”
### *— Anais Nin*

---

# **The Blind Men & the Elephant**
## ___
### “And so these men of Indostan
### Disputed loud and long,
### Each in his own opinion
### Exceeding stiff and strong,
### Though each was partly in the right,
### And all were in the wrong.”
#### — *John Godfrey Saxe*

---

# **The Elephant: Data**
## ___
## “Data is just a clue to the end truth”
### *— Josh Smith*

---

# **The Men: Building Models**
## ___
## "All models are wrong, but some are useful"
### *— George Box*

---

# **Layers of Abstraction**
## ___
## **Data** Abstraction
## **Visual** Abstraction
## **Model** Abstraction

---

# **Machine Learning (ML) Speak**
## ___
## **Data** Transformation
## **Visual** Exploration
## **Model** Building

---

# **ML Pipeline**
## ___

### Data Transformation  — — — —  Model Building
###    *(Tidy Data)*                                 
###         │                                 
###         │                                 
###         │                                 
### Visual Exploration   
###    *(Data-Vis)*       

---

# **ML Pipeline++**
## ___

### Data Transformation  — — — —  Model Building
###    *(Tidy Data)*                 **_(Tidy Model)_**      
###         │                           │     
###         │                           │     
###         │                           │     
### Visual Exploration           **Model Exploration**
###    *(Data-Vis)*                   **_(Model-Vis)_**

---

# **Model-Vis Approach**
## ___
### **[0]** Visualise the **data space**
### **[1]** Visualise the **predictions in the data space**
### **[2]** Visualise the **errors in model fitting**
### **[3]** Visualise with **different model parameters**
### **[4]** Visualise with **different input datasets**
### **[5]** Visualise the **entire model space**
### **[6]** Visualise the **entire feature space**
### **[7]** Visualise the **many models together**

---

# **Model-Vis Examples**
## ___
## **Regression** (n < 50, p = 4)
## **Classification: 2 class** (n ~ 5K, p = 785)

---

# **Regression: Small**
## ___
## Cars dataset - **price vs kmpl**
## Scraped from **comparison** website
## Refined & **tidied** up
## **Base version** for **petrol** cars
## Price **< ₹ 1,000K**, n = **42**

---

**brand**    **model**    **price**    **kmpl**    **type**        **bhp**
Tata     Nano       199    23.9	   Hatchback    38
Suzuki   Alto800    248    22.7	   Hatchback    47
Hyundai  EON        302    21.1	   Hatchback    55
Nissan   Datsun     312    20.6	   Hatchback    67
...      ...        ...    ...     ...         ...

Suzuki   Ciaz       725	   20.7	   Sedan        91
Skoda    Rapid      756	   15.0	   Sedan       104
Hyundai  Verna      774	   17.4	   Sedan       106
VW       Vento      785	   16.1	   Sedan       104

---

###   [0] Visualise the **data space**

![fit original](figures/fig_cars_00.png)

---

###   [1] Visualise the **predictions in the data space**
![fit original](figures/fig_cars_01.png)

---

###   [2] Visualise the **errors in model fitting**
![fit original](figures/fig_cars_02.png)

---

###   [3] Visualise with **different model parameters**
![fit original](figures/fig_cars_03.png)

---

###   [4] Visualise with **different input datasets**
![fit original](figures/fig_cars_04.png)

---

###   [5] Visualise the **entire model space**

![fit original](figures/fig_cars_05.png)

---

###   [6] Visualise the **entire feature space**

![fit original](figures/fig_cars_06.png)

---

###   [7] Visualise the **many models together**


![fit original](figures/fig_cars_07.png)

---

# **Model-Vis Approach**
## ___
### **[0]** Visualise the **data space**
### **[1]** Visualise the **predictions in the data space**
### **[2]** Visualise the **errors in model fitting**
### **[3]** Visualise with **different model parameters**
### **[4]** Visualise with **different input datasets**
### **[5]** Visualise the **entire model space**
### **[6]** Visualise the **entire feature space**
### **[7]** Visualise the **many models together**

---

# **Model-Vis & ML Approach**
## ___
### **[0]** **DATA VIS**: the data space
### **[1]** **PREDICTION**: the predictions in the data space
### **[2]** **VALIDATION**: the errors in model fitting
### **[3]** **TUNING**: with different model parameters
### **[4]** **BOOTSTRAP**: with different input datasets
### **[5]** **ENSEMBLE**: the entire model space
### **[6]** **FEATURES**: the entire feature space
### **[7]** **N-MODELS**: the many models together

---

# **Model-Vis Methods**
## ___
## Limited **standard** methods articulated
## Adapt to **data** and **domain** type
## Scope for **innovation** and **development**

---

# **Model-Vis Key Concept**
## ___
## Use visualisation to aid the transition of **implicit knowledge** in the data and your head to **explicit knowledge** in the model.

---

# **Classification: 2 Class**
## ___
## MNIST - **digit recognition**
## Reduced to 2-class - **1** and **2**
## 784 dimensions - **28 x 28 gray pixel map**
## n > **5000**

---

###   MNIST dataset: Examples of number **1** and **2**

![fit original](figures/fig_mnist_00a.png) ![fit original](figures/fig_mnist_00b.png) 

---

###  Visualise the **data space**

![fit original](figures/fig_mnist_00c.png) ![fit original](figures/fig_mnist_00d.png) 

---

###  Identify the features - **Symmetry** & **Intensity**

![fit original](figures/fig_mnist_00e.png) ![fit original](figures/fig_mnist_00f.png) 

---

###   Visualise the **reduced feature space**

![original](figures/fig_mnist_06.png)

---

###   Visualise the **predictions in the data space**
![fit original](figures/fig_mnist_01a.png)

---

###   Visualise the **errors in model fitting**
![fit original](figures/fig_mnist_02.png)

---

###   Visualise the **predictions boundaries**
![fit original](figures/fig_mnist_01b.png)

---

###   Visualise with **different model parameters**
![fit original](figures/fig_mnist_03.png)

---

# **n/p/N Model-Vis challenge**
## ___
## **n** -- Large and big data
## **p** -- High dimensional data
## **N** -- Multiple models

---

# How to **scale** for **large p**?
## ___
## **Curse** of dimensionality
## Mesh approach **computationally expensive**
## Need to use **projections**

---

###   For **entire feature space** - **t-SNE projection**

![original](figures/fig_mnist_06a.png)

---

###   Map the **error on the projection** 
![original](figures/fig_mnist_02a.png)

---

# **n/p/N Model-Vis approach**
## ___
## **n** -- use **Binning** or **Sampling** 
## **p** -- use **Projections**
## **N** -- use **Summaries**

--- 

# In Practice - **Model Explosion**
## ___
## **Entire Model Space**
## + Add **Tuning** Models
## + Add **Bootstrap** Models
## + Add **Ensemble** Models
## + Add **Cross-Validation** Models

---

# **Challenge with Model-Vis**
## ___
## Keep track of **prediction** & **errors**
## Keep track of **model output parameters**

---

# **Tidy Model**
## ___
## Augment **predictions** & **errors** to dataset
## Create **output parameters** data frame
## Visualise like **Tidy Data**

---

# **Tooling still nascent**
## ___
## R: **tidyverse** (esp. **broom** and **purr**)
## Python: **pybroom**, experimental packages

---

# **Model-Vis**
## ___
## Similar challenges **to Data-Vis**
## More an **Art**, than a Science
## Essential in **ML Model Pipeline**
## Both **to Explain** or **to Predict**
## Scope for **easier tooling**

---

# **Model-Vis**
## ___
### Model Visualisation Mini-Site (Coming Soon!)
### [http://modelvis.amitkaps.com](http://modelvis.amitkaps.com)
###    
### Code
### [https://github.com/amitkaps/modelvis](https://github.com/amitkaps/modelvis)

---

# [fit] **Visualising ML Models**
## ___
## Amit Kapoor
## @amitkaps
##    
## [amitkaps.com](http://amitkaps.com)
