Capstone project 6 : Unsupervised Machine Learning on the US Arrests dataset.

The dataset used for this project is from the US Arrests Kaggle challenge .
A description of the data is given as: “This data set contains statistics,
in arrests per 100,000 residents, for assault, murder, and rape in each of the
50 US states in 1973. Also given is the percent of the population living in urban areas.”

Requirements :
 - Load teh data and preprocess it.
 - Apply two clustering techniques on the data.
 - Describe your findings in markdown and graphs.

Development:
 - The dataset had initially 5 columns :
   - ####City
     I moved this column as teh index column and renamed it to States since it was a more 
     appropriate name that described the column data
   - ####Murder
     Murder arrests (per 100,000)
   - ####Assault
     Assault arrests (per 100,000)
   - ####UrbanPop
     Percent of urban population
   - ####Rape
     Rape arrests (per 100,000)
    
 - Generate an in-depth Principal Component analysis on the data
 - Check for data correlations and possible redundancy of variables.
 - Use Hierarchical Clustering and show dendrogram with different linkage methods.
 - Use KMeans Clustering and show scatter plot of the clusters formed with the data from the first 
   two principal components.