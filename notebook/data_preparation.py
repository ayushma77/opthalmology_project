# %%
import pandas as pd
import os

# %%
excel_file_path=r"..\data\ODIR-5K_Training_Annotations(Updated)_V2.xlsx"
annoted_data=pd.read_excel(excel_file_path)

# %%
annoted_data

# %%

data = pd.read_csv("..\data\data.csv")

# %%
print(data.columns)


# %%
#unique_left_labels = pd.unique(data['Left-Diagnostic Keywords']).tolist()
keywordsL = [ keyword  for keywords in data['Left-Diagnostic Keywords'] for keyword in keywords.split('，')]
keywordsR = [ keyword  for keywords in data['Right-Diagnostic Keywords'] for keyword in keywords.split('，')]

unique_keywordsL = set(keywordsL)
unique_keywordsR = set(keywordsR)

print(len(unique_keywordsL),len(keywordsL))
print(len(unique_keywordsR),len(keywordsR))

#unique_right_labels = pd.unique(data['Right-Diagnostic Keywords']).tolist()

# %%
# Define keywords to exclude
exclude_keywords = ["lens dust", "optic disk photographically invisible", "low image quality", "image offset"]

# %%
# Remove specified keywords from both left and right columns
data['Left-Diagnostic Keywords'] = data['Left-Diagnostic Keywords'].apply(lambda x: '，'.join([kw for kw in x.split('，') if kw not in exclude_keywords]))
data['Right-Diagnostic Keywords'] = data['Right-Diagnostic Keywords'].apply(lambda x: '，'.join([kw for kw in x.split('，') if kw not in exclude_keywords]))

# Save the updated DataFrame to the original CSV file, overwriting the existing file
csv_file_path = '../data/data_updated.csv'
data.to_csv(csv_file_path, index=False)

print(f'Updated CSV file created at: {csv_file_path}')

# %%
# Filter out rows with excluded keywords
filtered_dataL = data[~data['Left-Diagnostic Keywords'].str.contains('|'.join(exclude_keywords))]
filtered_dataR = data[~data['Right-Diagnostic Keywords'].str.contains('|'.join(exclude_keywords))]
# Extract unique keywords from the remaining data
remaining_keywordsL = [keyword for keywords in filtered_dataL['Left-Diagnostic Keywords'] for keyword in keywords.split('，')]
unique_remaining_keywordsL = set(remaining_keywordsL)
remaining_keywordsR = [keyword for keywords in filtered_dataR['Right-Diagnostic Keywords'] for keyword in keywords.split('，')]
unique_remaining_keywordsR = set(remaining_keywordsR)
# Print the number of unique keywords and the total number of keywords
print(len(unique_remaining_keywordsL), len(remaining_keywordsL))
print(len(unique_remaining_keywordsR), len(remaining_keywordsR))

# %%
# def map_labels(original_labels, mapping_dict):
#     return [mapping_dict[label] for label in original_labels]

# label_mapping_dict = {
#     'normal': 'N',
#     'diabetes': 'D',
#     'AMD': 'A',
#     'glaucoma': 'G',
#     'cataract': 'C',
#     'hypertension': 'H',
#     'myopia': 'M',
#     'other disease': 'O',
# }

# original_labels = ['normal', 'diabetes', 'cataract', 'AMD', 'glaucoma', 'hypertension', 'myopia', 'other disease']
# mapped_labels = map_labels(original_labels, label_mapping_dict)



# %%
def create_label(diagnostic_keywords):
    keywords = set(diagnostic_keywords.split('，'))  # Split the keywords into a set
    
    if 'normal fundus' in keywords:
        return "N"
    if any(keyword in keywords for keyword in ["diabetic retinopathy","suspected diabetic retinopathy", "mild nonproliferative retinopathy", "moderate non proliferative retinopathy", "severe nonproliferative retinopathy","severe proliferative diabetic retinopathy","proliferative diabetic retinopathy",'"hypertensive retinopathy,diabetic retinopathy"']):
        return "D"
    if 'cataract' in keywords:
        return "C"
    if any(keyword in keywords for keyword in ["glaucoma", "suspected glaucoma"]):
            return "G"
    if any(keyword in keywords for keyword in ["wet age-related macular degeneration", "dry age-related macular degeneration"]):
        return "A"
    if 'hypertensive retinopathy' in keywords:
        return "H"
    if  any(keyword in keywords for keyword in ["pathological myopia", "myopia retinopathy","myopic maculopathy"]):
            return "M"
    return "O"



# %%
data['Left-label'] = data['Left-Diagnostic Keywords'].apply(lambda x: create_label(x))
data['Right-label'] =data['Right-Diagnostic Keywords'].apply(lambda x: create_label(x))

# %%
csv_file_path = '../data/ODIR-5K_Training_Annotations_processed.csv'
data.to_csv(csv_file_path, index=False)

print(f'CSV file created at: {csv_file_path}')

# %%
images_to_remove = [
    '2174_right.jpg',
		'2175_left.jpg',
		'2176_left.jpg',
		'2177_left.jpg',
        "2177_right.jpg",
		'2179_left.jpg',
        "2178_right.jpg",
		'2180_left.jpg',
		'2181_left.jpg',
		'2182_left.jpg',
		'2957_left.jpg'
		'2179_right.jpg',
		'2180_right.jpg',
		'2181_right.jpg',
		'2182_right.jpg',
		'2957_right.jpg']

# Remove rows corresponding to the specified images
data = data[~data['Left-Fundus'].isin(images_to_remove)]
data = data[~data['Right-Fundus'].isin(images_to_remove)]

# Save the modified DataFrame back to the CSV file
data.to_csv(csv_file_path, index=False)

# %%
left_fundus = data['Left-Fundus']
left_label = data['Left-label']
left_keywords = data['Left-Diagnostic Keywords']
right_fundus = data['Right-Fundus']
right_label = data['Right-label']
right_keywords = data['Right-Diagnostic Keywords']
id = data['ID']
age = data['Patient Age']
sex = data['Patient Sex']

# separate train and test split
from sklearn.model_selection import train_test_split
SEED = 42
id_train, id_val = train_test_split(id,test_size=0.1,random_state=SEED)
data_root_dir = r"data"


train_left_fundus = data[data['ID'].isin(id_train)]['Left-Fundus']


train_left_label = data[data['ID'].isin(id_train)]['Left-label']
train_left_keywords = data[data['ID'].isin(id_train)]['Left-Diagnostic Keywords']

train_right_fundus = data[data['ID'].isin(id_train)]['Right-Fundus']
train_right_label = data[data['ID'].isin(id_train)]['Right-label']
train_right_keywords = data[data['ID'].isin(id_train)]['Right-Diagnostic Keywords']


val_left_fundus = data[data['ID'].isin(id_val)]['Left-Fundus']
val_left_label = data[data['ID'].isin(id_val)]['Left-label']
val_left_keywords =data[data['ID'].isin(id_val)]['Left-Diagnostic Keywords']
val_right_fundus = data[data['ID'].isin(id_val)]['Right-Fundus']
val_right_label =data[data['ID'].isin(id_val)]['Right-label']
val_right_keywords = data[data['ID'].isin(id_val)]['Right-Diagnostic Keywords']

# stack left and right columns vertically
train_fundus = pd.concat([train_left_fundus, train_right_fundus],axis=0,ignore_index=True,sort=True)
train_label = pd.concat([train_left_label,  train_right_label],axis=0,ignore_index=True,sort=True)
train_keywords = pd.concat([train_left_keywords,train_right_keywords],axis=0,ignore_index=True,sort=True)

val_fundus = pd.concat([val_left_fundus, val_right_fundus],axis=0,ignore_index=True)
val_label = pd.concat([val_left_label,val_right_label],axis=0,ignore_index=True)
val_keywords = pd.concat([val_left_keywords,val_right_keywords],axis=0,ignore_index=True)

train_df_left_right_separate_row = pd.concat([train_fundus,
                                              train_label,
                                              train_keywords],axis=1,sort=True,
                                              keys = ['fundus','label','keywords']) # stack horizontally
val_df_left_right_separate_row = pd.concat([  val_fundus,
                                              val_label,
                                              val_keywords],axis=1,sort=True,
                                              keys=['fundus','label','keywords']) # stack horizontally

# Construct full paths for train set
train_df_left_right_separate_row['fundus'] = train_df_left_right_separate_row['fundus'].apply(lambda x: os.path.join(data_root_dir, "ODIR-5K_Training_Images\ODIR-5K_Training_Dataset", str(x)))

# Construct full paths for validation set
val_df_left_right_separate_row['fundus'] = val_df_left_right_separate_row['fundus'].apply(lambda x: os.path.join(data_root_dir, "ODIR-5K_Training_Images\ODIR-5K_Training_Dataset", str(x)))


# %%
train_df_left_right_separate_row.to_csv('../data/processed_train_ODIR-5K.csv',index=False)
val_df_left_right_separate_row.to_csv ('../data/processed_val_ODIR-5K.csv',index=False)


# %%
len(data),len(id_train),len(id_val),len(train_fundus),len(val_fundus),len(train_df_left_right_separate_row),len(val_df_left_right_separate_row)


# %%
from glob import glob

from pandas import DataFrame
from pathlib import Path

test_root_dir = '../data/ODIR-5K_Testing_Images/ODIR-5K_Testing_Images'
test_paths = glob(f'{test_root_dir}/*.jpg')

relative_paths = [str(Path(p).relative_to('../')) for p in test_paths]
test_df = DataFrame(data={'fundus':relative_paths})
test_df.to_csv('../data/processed_test_ODIR-5k.csv',index=False)

# %%



