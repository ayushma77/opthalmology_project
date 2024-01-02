import pandas as pd
import os
from sklearn.model_selection import train_test_split
BASE_DIR=r"data"
excel_file_path=r"data\ODIR-5K_Training_Annotations(Updated)_V2.xlsx"
annoted_data=pd.read_excel(excel_file_path)
csv_data=annoted_data.to_csv(os.path.join(BASE_DIR, "data.csv"), index=False)

left_data = annoted_data[['Left-Fundus', 'Left-Diagnostic Keywords']].copy()
left_data.columns = ['Image', 'Label']
right_data = annoted_data[['Right-Fundus', 'Right-Diagnostic Keywords']].copy()
right_data.columns = ['Image', 'Label']

# Concatenate left and right data
merged_data = pd.concat([left_data, right_data], index=False)
merged_data.to_csv(os.path.join(BASE_DIR, "train.csv"), index=False)


