# Crimes-in-Medellin-Forecasting
Spatio Temporal forecasting on Neighbors and Districts of Medellin as DS4A / Colombia Cohort 6 final project.

## Datasets
The datasets used on this project comes from te web page of the "Alcaldia de Medellin", it can be found on http://medata.gov.co/node/85, as 34 datasets, that have the same structured but are related to diferent topics such as Theft, Capture, homicide, among others. The datasets where united into two main groups **df_crimenes.csv**, that are all dataframes related to crimes, and **df_recursos.csv** that are the dataframes that have security resources such as the emergency call or actions such as capture or incautation, this dataframes are made using "-------" and can be downloaded from:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6783942.svg)](https://doi.org/10.5281/zenodo.6783942)

## Preprocessing and EDA
Once the dataframes are united we make and preprocessing and an EDA using `Notebooks/Preprocess and EDA.ipynb` the final dataframes with the preprocessing are **df_crimenes_2.csv** and **df_recursos_clean.csv** that can also be downloaded from:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6783942.svg)](https://doi.org/10.5281/zenodo.6783942)

## Neighbors and districts pre-processing
The forecast was developed using Neighbors and districts meaning this information have to be standarized and filled as much as possible, for this we download the ShapeFiles for Neighbors and districts from this page https://data.metabolismofcities.org/dashboards/medellin/, this files are also available on `Mapas` folder, after this process that was generated using `Notebooks/Neighbors and districts pre-processing.ipynb` we save the new dataframes on two files **Crimen_Barrios_Comunas_Cor_7.csv** and **Recurso_Barrios_Comunas_Cor_6.csv** also available for download from:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6783942.svg)](https://doi.org/10.5281/zenodo.6783942)

## Forecasting Model and Training
The forecast was developed using Neighbors and districts also we use Tensorflow+Keras, for this we develop the model used on  `Notebooks/Forecasting Model and Training.ipynb` we save the dataframes for each model on files `dataframes/Data_Predict_Captura_Barrios.csv`, `dataframes/Data_Predict_Captura_Comunas.csv`, `dataframes/Data_Predict_Hurtos_Barrios.csv`, and `dataframes/Data_Predict_Hurtos_Comunas.csv`, the results of the experiments are:

| Experiment | Train ![R^2]| Test R^2 | Weights |
| :-------- | :------- | :------------------------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key | name |
