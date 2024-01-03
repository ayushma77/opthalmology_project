import os

import pandas as pd
from sklearn.model_selection import train_test_split

BASE_DIR=r"data"
excel_file_path=r"data\ODIR-5K_Training_Annotations(Updated)_V2.xlsx"
annoted_data=pd.read_excel(excel_file_path)

csv_data=annoted_data.to_csv(os.path.join(BASE_DIR, "data.csv"), index=False)

# left_data = annoted_data[['Left-Fundus', 'Left-Diagnostic Keywords']].copy()
# left_data.columns = ['Image', 'Label']
# right_data = annoted_data[['Right-Fundus', 'Right-Diagnostic Keywords']].copy()
# right_data.columns = ['Image', 'Label']

# # Concatenate left and right data
# merged_data = pd.concat([left_data, right_data], ignore_index=True)
# train_csv=merged_data.to_csv(os.path.join(BASE_DIR, "train.csv"), index=False)

data = annoted_data[['Left-Fundus','Right-Fundus', 'Left-Diagnostic Keywords', 'Right-Diagnostic Keywords','N','D','G','C','A','H','M','O']].copy()
csv=data.to_csv(os.path.join(BASE_DIR, "data1.csv"), index=False)


import csv

# Initialize lists to store left image paths and right image paths
left_image_paths = []
right_image_paths = []
labels = []

# Assuming 'data.csv' is the file containing your data
with open('data/data1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row if it exists
    for row in reader:
        left_image_path, right_image_path, left_diagnostic, right_diagnostic, *_ = row
        
        # Check if the condition is met for 'cataract' and 'normal fundus'
        if left_diagnostic.lower() == 'cataract' and right_diagnostic.lower() == 'normal fundus':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('cataract')
        elif left_diagnostic.lower() == 'normal' and right_diagnostic.lower() == 'contaract':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('cataract')
            
        elif left_diagnostic.lower() == 'macular hole' and right_diagnostic.lower() == 'normal fundus':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        # Check if the condition is met for 'normal fundus' and 'normal fundus'
        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'normal fundus':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('normal')
        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'branch retinal artery occlusion':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'depigmentation of the retinal pigment epithelium':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
            
        elif left_diagnostic.lower() == 'moderate non proliferative retinopathy' and right_diagnostic.lower() == 'moderate non proliferative retinopathy':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('diabetes')
        elif left_diagnostic.lower() == 'mild non proliferative retinopathy' and right_diagnostic.lower() == 'mild non proliferative retinopathy':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('diabetes')

        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'vitreous degeneration':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        
        elif left_diagnostic.lower() == 'epiretinal membrane' and right_diagnostic.lower() == 'normal fundus':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'epiretinal membrane' and right_diagnostic.lower() == 'epiretinal membrane':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == ' macular epiretinal membrane' and right_diagnostic.lower() == 'macular epiretinal membrane':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'retinal pigmentation' and right_diagnostic.lower() == 'retinal pigmentation':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'pathological myopia' and right_diagnostic.lower() == 'pathological myopia':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('myopia')
        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'macular epiretinal membrane':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        
        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'myelinated nerve fibers':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
            
        elif left_diagnostic.lower() == 'normal fundus' and right_diagnostic.lower() == 'pathological myopia':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('myopia')
        elif left_diagnostic.lower() == 'pathological myopia' and right_diagnostic.lower() == 'normal fundus':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('myopia')
            
        elif left_diagnostic.lower() == 'drusen' and right_diagnostic.lower() == 'drusen':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'hypertensive retinopathy' and right_diagnostic.lower() == 'hypertensive retinopathy':
            left_image_paths.append(left_image_path)
            right_image_paths.append(right_image_path)
            labels.append('hypertension')
            
            
# Write the image paths and labels to a new CSV file
with open('output.csv', mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Image Path', 'Label'])  # Write header
    for left_path, right_path, label in zip(left_image_paths, right_image_paths, labels):
        writer.writerow([left_path, label])
        writer.writerow([right_path, label])

print("CSV file 'output.csv' created with image paths and labels.")