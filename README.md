<img width="200" alt="image" src="https://github.com/rttle/Bank-Churn-Kaggle-Challenge/assets/143844181/dbbeb760-7ac3-4d53-84ce-a08071725da1">

# Effect of Season on Air Contaminant Concentration
This repository holds a statistical analysis on the relationship between the season and air contaminant concentration. The data was taken from the City of New York: https://catalog.data.gov/dataset/air-quality.

## Overview
This statistical analysis uses air quality data from New York city and tests whether there is statistical significance in the effect of season on the air contaminant concentration. In particular, the analysis looks at the relation between season and the air contaminant, Fine Particulate Matter (‘PM2.5’). The dataset is a mix of categorical and numerical features, totaling to 12 features. A two sample t-test was done, and the resulting p-value was 4.1999e-05. Using alpha = 0.5, the p-value being less than 0.5 means that there is sufficient evidence that season has an effect on the concentration of PM2.5.

## Project Context
This repository encompasses Rachel’s personal work taken from a group project for the UTA course, Python for Data Science 1, in Fall 2023. The work is able to stand alone; however, there are some instance where contaminants were not used for cohesion with the work of other teammates.

## Summary of Workdone
### Data
- Data: Type: Tabular
  - Input: CSV file of features
- Size: 16122 Air Contaminant Readings, 12 features

### Preprocessing / Clean up
**Missing Values/Duplicates.** There were no missing values nor duplicates to deal with in the provided dataset for all features besides one labeled ‘Message.’

**Dropped.** The ‘Message’ column that had only NULL values. All contaminant readings that did not have any season information.

**Feature Engineering.** One additional feature was created, ‘Season’.

### Data Visualization
The figure below shows the seasonal data available from the dataset.
 
![image](https://github.com/user-attachments/assets/e8d9f7ac-3165-4dc5-90b7-0fde52903e93)

The following figure is a histogram for the contaminant Ozone. The histogram is meant to show the different distributions of Winter and Summer data for the contaminant Ozone. However, as seen from the figure, there is only Summer data. The contaminant Sulfur Dioxide in a similar vein only has Winter data. Thus. The two contaminants could not be used for statistical analysis regarding effect of season.
 
![image](https://github.com/user-attachments/assets/e25cfbef-d723-4c9a-ba55-8f0af6b9ed6a)

The figure below is a histogram for PM2.5, which does show the different distributions for Winter and Summer data.

![image](https://github.com/user-attachments/assets/f0e36e5f-11a7-4e94-8ae1-914d6df777e9)

### Statistical Analysis
Statistical Analysis is only done on PM2.5 because Ozone and Sulfur Dioxide only had readings in one season. Nitrogen Dioxide was not used for cohesion for the group project context of this work.

The statistical test used was a two-tailed, two sample t-test with an alpha of 0.5. The chosen test was determined to be appropriate because of the sample size for PM2.5 was ~3400. Given that sample size, even if the sample is not normal in shape, because the sample size is sufficiently large, a t-test is still appropriate.

The following are the null and alternative hypotheses:
	H0: The mean of the mean readings of PM2.5 in winter is equal to that of summer.
  Ha: The mean of the mean readings of PM2.5 in winter is not equal to that of summer.

Both a pooled and non-pooled t-test was done. The results are shown below.

![image](https://github.com/user-attachments/assets/74e44ebb-795d-439d-920a-15892590fcae) 

### Conclusions
With an alpha value of 0.5, there is sufficient evidence that the mean of the mean readings of PM2.5 in winter is not equal to that of summer. This is true under both the pooled or non-pooled t-test. Thus, the use of python to run statistical analysis on air contaminant data has resulted in the finding that season does have an effect on air contaminant concentrations.

## How to reproduce results
To reproduce results, download the Air Quality dataset from the data.gov link. Then ensure that the AirQuality_Preprocessing.py file is downloaded from this repository and run the AirQuality_Visualization+StatAnalysis.ipynb notebook also found in this repository.

## Overview of files in repository
- **AirQuality_Preprocessing.ipynb:** Notebook that takes the provided dataset and prepares it as a dataframe to be used for statistical analysis.
- **AirQuality_Visualization+StatAnalysis.ipynb:** Notebook that takes a dataset, creates visualizations of the data and runs a statistical analysis on the data.
- **AirQuality_Preprocessing.py:** Module created to wrap all preprocessing done to the dataset in the preprocessing notebook. 

## Data
Data is from the City of New York, found on data.gov website. https://catalog.data.gov/dataset/air-quality

## Citations
- *Microgrammes per cubic metre*, WWW.UK-AIR.DEFRA.GOV.UK, https://uk-air.defra.gov.uk/air-pollution/glossary.php?glossary_id=37#37.
- *Parts per billion*, WWW.GREENFACTS.ORG, https://www.greenfacts.org/glossary/pqrs/parts-per-billion.htm.

