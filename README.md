# Model Visualisation (model-vis)

Data science is a process of abstraction. In order to explain or to predict a real phenomena, the process start with acquiring and refining the data. It then moves between the three layers of abstraction – transformations (data abstraction), visualisations (visual abstraction) and modelling (symbolic abstraction). All these three layers of abstraction work together to try and build a truer (or more closer) representation of the real phenomena.

Data visualisation (data-vis) helps us to understand the portrait and the shape of the data. The science of data-vis for exploratory data analysis is well developed, for both static graphics (scatter plot matrices, glyph based approaches, geometric transforms like parallel coordinates) and interactive graphics (layering, brushing and linking, projections and tours) [See the talk at Strata Conference, Singapore on Visualising Multi Dimensional Data – https://www.youtube.com/watch?v=GtAe_UZGr28]. However, the power of visualisation is rarely leveraged for understanding the statistical models developed better. Model evaluation is still largely restricted through numerical summaries. Extending visualisation to statistical model can be a powerful way to improve our understanding of the model.

Model visualisation (model-vis) can help us to understand the shape of the model and compare it to the shape of the data. It allows to see the fit of the model and understand where the fit can be improved. It also allows us to better understand the parameters in the model and how the model changes when the parameters change as well as how the parameters changes when the input data changes.

The science and tools for model-vis are still very under-developed. This talks looks at practical examples of doing model-vis in regression (linear, lasso), classification (logistic, trees, LDA) and clustering (hierarchical) problems that can help us better understand the model. This includes exploring model-vis approaches that:
- Visualise the model in data space as opposed to data in model space
- Visualise the entire space of models
- Visualise the same model with varying tuning parameters
- Visualise the same model with different input datasets
- Visualise the process of model fitting as opposed to final result

Integrating these approaches for model-vis as a part of model evaluation will strengthen the understanding of the model and lead to better model building for a data scientist. Model-vis can then complement data-vis for fitting better models as well as for communicating the insight from the data science process.
