import pandas as pd 

## Carregar o dataset 
vehicles_01 = "./vehicles-data-analysis/entry_dataset/gta_data_batch_1.csv" 
vehicles_02 = "./vehicles-data-analysis/entry_dataset/gta_data_batch_2.csv" 
vehicles_03 = "./vehicles-data-analysis/entry_dataset/gta_data_batch_3.csv" 

dataset_00 = pd.read_csv(vehicles_01)
dataset_01 = pd.read_csv(vehicles_02)
dataset_02 = pd.read_csv(vehicles_03)

#print dos datasets
print(dataset_00)
print(dataset_01)
print(dataset_02)
