## Folder Structure

``````
└───PowerAnalysis_simulation
│
└───1_PsyProprecessed_shuffled
│
└───2_PsyProprecessed_shuffled_group
│
└───3_MainScript
│
└───4_StatisticalAnalysis
│
└───5_helper_function
│
└───README




``````
1_PsyProprecessed_shuffled: This script aimed to process the shuffled blocks of experiment 2 and 3. The experiment 1 has no shuffled blocks. And the script is aimed to process the raw data.
2_PsyProprecessed_shuffled_group: This script aimed to process the preprocessed data and merge them.
3_MainScript: These scripts preprocess the EEG data and extract ERP.
4_StatisticalAnalysis: Holds scripts dedicated to statistical testing and analysis. 
5_helper_function: Contains helper functions used in the main scripts to simplify tasks like data loading, transformation, and visualization.