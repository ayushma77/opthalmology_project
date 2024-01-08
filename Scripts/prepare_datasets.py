import csv
import os

import pandas as pd
from sklearn.model_selection import train_test_split

BASE_DIR=r"data"
excel_file_path=r"data\ODIR-5K_Training_Annotations(Updated)_V2.xlsx"
annoted_data=pd.read_excel(excel_file_path)

csv_data=annoted_data.to_csv(os.path.join(BASE_DIR, "data.csv"), index=False)
# data = annoted_data[['Left-Fundus','Right-Fundus', 'Left-Diagnostic Keywords', 'Right-Diagnostic Keywords','N','D','G','C','A','H','M','O']].copy()
# csv_data1=data.to_csv(os.path.join(BASE_DIR, "data1.csv"), index=False)
# data1 = pd.read_csv(os.path.join(BASE_DIR, "data1.csv"))
data = annoted_data[['Left-Fundus', 'Left-Diagnostic Keywords','N','D','G','C','A','H','M','O']].copy()
left_dta_csv=data.to_csv(os.path.join(BASE_DIR, "left_data.csv"), index=False)

data = annoted_data[['Right-Fundus', 'Right-Diagnostic Keywords','N','D','G','C','A','H','M','O']].copy()
right_dta_csv=data.to_csv(os.path.join(BASE_DIR, "right_data.csv"), index=False)

# unique_left_labels = pd.unique(data1['Left-Diagnostic Keywords'])
# unique_right_labels = pd.unique(data1['Right-Diagnostic Keywords'])


# print("Unique Left Labels:", unique_left_labels)
# print("Unique Right Labels:", unique_right_labels)

# Initialize lists to store left image paths and right image paths
left_image_paths = []
right_image_paths = []
labels = []

with open(os.path.join(BASE_DIR, "left_data.csv"), newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        left_image_path, left_diagnostic,  *_ = row
        if left_diagnostic.lower() == 'cataract' :
            left_image_paths.append(left_image_path)
            labels.append('cataract')
            
        elif left_diagnostic.lower() == 'normal fundus':
            left_image_paths.append(left_image_path)
            labels.append('normal')
        elif 'lens dust' in left_diagnostic.lower() and 'normal fundus' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('normal')
        
        elif 'laser spot' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'mild nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'myelinated nerve fibers' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'epiretinal membrane' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'laser spot'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'white vessel' in left_diagnostic.lower() and 'moderate non proliferative retinopathyt'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'vitreous degeneration' in left_diagnostic.lower() and 'mild non proliferative retinopathyt'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'retina fold' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'myelinated nerve fibers' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'hypertensive retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'lens dust' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes') 
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'branch retinal vein occlusion' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'laser spot' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'cataract' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'drusen' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'white vessel' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'optic disc edema' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'vitreous degeneration' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'mild nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'white vessel' in left_diagnostic.lower() and 'moderate non proliferative retinopathyt'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'vitreous degeneration' in left_diagnostic.lower() and 'mild non proliferative retinopathyt'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'moderate nonproliferative retinopathy' in left_diagnostic.lower() and 'macular epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'severe nonproliferative retinopathy' in left_diagnostic.lower() and 'white vessel' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'laser spot' in left_diagnostic.lower() and 'proliferative diabetic retinopathy' in left_diagnostic.lower() and 'white vessel' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'mild nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'myelinated nerve fibers' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'epiretinal membrane over the macula' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'macular epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'vitreous degeneration' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'retinal pigmentation' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'mild nonproliferative retinopathy' in left_diagnostic.lower() and 'lens dust' in left_diagnostic.lower() and 'drusen'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'epiretinal membrane' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower() and 'laser spot'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'epiretinal membrane' in left_diagnostic.lower() and 'laser spot' in left_diagnostic.lower() and 'severe proliferative diabetic retinopathy'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'vitreous degeneration' in left_diagnostic.lower() and 'mild non proliferative retinopathyt'in  left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'lens dust' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'lens dust' in left_diagnostic.lower() and 'mild non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif left_diagnostic.lower() == 'moderate non proliferative retinopathy':
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif left_diagnostic.lower() == 'mild nonproliferative retinopathy':
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif left_diagnostic.lower() == 'diabetic retinopathy':
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif left_diagnostic.lower() == ' severe nonproliferative retinopathy':
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'proliferative diabetic retinopathy' in left_diagnostic.lower() and 'hypertensive retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'severe nonproliferative retinopathy' in left_diagnostic.lower() and 'hypertensive retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'severe nonproliferative retinopathy' in left_diagnostic.lower() and 'white vessel' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'dry age-related macular degeneration' in left_diagnostic.lower() and 'diabetic retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'white vessel' in left_diagnostic.lower() and 'severe nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'white vessel' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'retinal pigment epithelium atrophy' in left_diagnostic.lower() and 'diabetic retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'drusen' in left_diagnostic.lower() and 'moderate non proliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'macular epiretinal membrane' in left_diagnostic.lower() and 'severe nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'macular epiretinal membrane' in left_diagnostic.lower() and 'moderate nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'macular epiretinal membrane' in left_diagnostic.lower() and 'mild nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif left_diagnostic.lower() == '"hypertensive retinopathy,diabetic retinopathy"':
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'hypertensive retinopathy' in left_diagnostic.lower() and 'mild nonproliferative retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        elif 'post laser photocoagulation' in left_diagnostic.lower() and 'diabetic retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('diabetes')
        

        elif left_diagnostic.lower() == 'pathological myopia':
            left_image_paths.append(left_image_path)
            labels.append('myopia')
        elif left_diagnostic.lower() == 'myopic maculopathy':
            left_image_paths.append(left_image_path)
            labels.append('myopia')
        elif 'punctate inner choroidopathy' in left_diagnostic.lower() and 'myopia retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('myopia')
            
            
        elif left_diagnostic.lower() == 'hypertensive retinopathy':
            left_image_paths.append(left_image_path)
            labels.append('hypertension')
        elif 'hypertensive retinopathy' in left_diagnostic.lower() and 'suspected glaucoma' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('hypertension')
        elif 'hypertensive retinopathy' in left_diagnostic.lower() and 'optic nerve atrophy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('hypertension')
            
        elif left_diagnostic.lower() == 'wet age-related macular degeneration':
            left_image_paths.append(left_image_path)
            labels.append('AMD')
        elif left_diagnostic.lower() == 'dry age-related macular degeneration':
            left_image_paths.append(left_image_path)
            labels.append('AMD')
        elif 'wet age-related macular degeneration' in left_diagnostic.lower() and 'myopia retinopathy' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('AMD')
            
        elif 'post laser photocoagulation' in left_diagnostic.lower() and 'glaucoma' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('glaucoma')
        elif 'dry age-related macular degeneration' in left_diagnostic.lower() and 'glaucoma' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('glaucoma')
        elif left_diagnostic.lower() == 'suspected glaucoma':
            left_image_paths.append(left_image_path)
            labels.append('glaucoma')
        elif left_diagnostic.lower() == ' glaucoma':
            left_image_paths.append(left_image_path)
            labels.append('glaucoma')
    
        elif left_diagnostic.lower() == 'optic disc edema':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'macular epiretinal membrane':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == '"low image quality,maculopathy"':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
            
        elif left_diagnostic.lower() == 'macular coloboma':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'pigment epithelium proliferation':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'retinitis pigmentosa':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'myelinated nerve fibers':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'refractive media opacity':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'spotted membranous change':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'branch retinal vein occlusion':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'wedge white line change':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
            
        elif left_diagnostic.lower() == 'macular hole':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'vitreous degeneration':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'tessellated fundus':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'depigmentation of the retinal pigment epithelium':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'rhegmatogenous retinal detachment':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'suspected retinal vascular sheathing':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'central retinal vein occlusion':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'drusen':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'epiretinal membrane':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'spotted membranous change' in left_diagnostic.lower() and 'spotted membranous change' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'macular epiretinal membrane' in left_diagnostic.lower() and 'vessel tortuosity' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'old choroiditis' in left_diagnostic.lower() and 'macular epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'chorioretinal atrophy with pigmentation proliferation' in left_diagnostic.lower() and 'epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'vitreous degeneration' in left_diagnostic.lower() and 'lens dust' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'lens dust' in left_diagnostic.lower() and 'macular epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'maculopathy' in left_diagnostic.lower() and 'macular epiretinal membrane' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'drusen' in left_diagnostic.lower() and 'lens dust' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'retinitis pigmentosa':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'lens dust' in left_diagnostic.lower() and 'spotted membranous change' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'lens dust' in left_diagnostic.lower() and 'rhegmatogenous retinal detachment' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'branch retinal vein occlusion':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'epiretinal membrane' in left_diagnostic.lower() and 'myelinated nerve fibers' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif 'epiretinal membrane' in left_diagnostic.lower() and 'lens dust' in left_diagnostic.lower():
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'atrophy':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'retinochoroidal coloboma':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'chorioretinal atrophy':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
        elif left_diagnostic.lower() == 'laser spot':
            left_image_paths.append(left_image_path)
            labels.append('other disease')
            
# diagnostic_combinations = {
#     ('cataract'): 'cataract',

#     ('normal fundus'): 'normal',
#     ('lens dust','normal fundus'): 'normal',

#     ('laser spot','white vessel','moderate non proliferative retinopathy'): 'diabetes',
#     ('laser spot','vitreous degeneration','mild non proliferative retinopathyt'): 'diabetes',
#     ('laser spot','moderate non proliferative retinopathy'): 'diabetes',
#     ('laser spot','mild nonproliferative retinopathy'): 'diabetes',
#     ('mild nonproliferative retinopathy','epiretinal membrane'): 'diabetes',
#     ('mild nonproliferative retinopathy', 'myelinated nerve fibers'): 'diabetes',
#     ('epiretinal membrane', 'moderate non proliferative retinopathy', 'laser spot'): 'diabetes',
    

#     ('optic disc edema'): 'other disease',
#     ('macular epiretinal membrane'): 'other disease',
#     ('low image quality,maculopathy'): 'other disease',
#     ('macular coloboma'): 'other disease',
#     ('pigment epithelium proliferation'): 'other disease',
#     ('retinitis pigmentosa'): 'other disease',
#     ('myelinated nerve fibers'): 'other disease',
#     ('refractive media opacity'): 'other disease',
#     ('spotted membranous change'): 'other disease',
#     ('branch retinal vein occlusion'): 'other disease',
#     ('wedge white line change'): 'other disease',
#     ('macular hole'): 'other disease',
#     ('vitreous degeneration'): 'other disease',
#     ('tessellated fundus'): 'other disease',
#     ('depigmentation of the retinal pigment epithelium'): 'other disease',
#     ('rhegmatogenous retinal detachment'): 'other disease',
#     ('suspected retinal vascular sheathing'): 'other disease',
#     ('central retinal vein occlusion'): 'other disease',
#     ('drusen'): 'other disease',
#     ('epiretinal membrane'): 'other disease',
#     ('spotted membranous change','vessel tortuosity'): 'other disease',
#     ('old choroiditis','macular epiretinal membrane'): 'other disease',
#     ('chorioretinal atrophy with pigmentation proliferation','epiretinal membrane'): 'other disease',
#     ('vitreous degeneration','lens dust'): 'other disease',
#     ('lens dust','macular epiretinal membrane'): 'other disease',
#     ('maculopathy','macular epiretinal membrane'): 'other disease',
#     ('drusen','lens dust'): 'other disease',
#     ('retinitis pigmentosa'): 'other disease',
#     ('lens dust','spotted membranous change'): 'other disease',
#     ('lens dust','rhegmatogenous retinal detachment'): 'other disease',
#     ('branch retinal vein occlusion'): 'other disease',
#     ('epiretinal membrane','myelinated nerve fibers'): 'other disease',
#     ('epiretinal membrane','lens dust'): 'other disease',
#     ('atrophy'): 'other disease',
#     ('retinochoroidal coloboma'): 'other disease',
#     ('chorioretinal atrophy'): 'other disease',
#     ('laser spot'): 'other disease',
# }

for combination, label in diagnostic_combinations.items():
    if all(diagnosis in left_diagnostic.lower() for diagnosis in combination):
        left_image_paths.append(left_image_path)
        labels.append(label)
        
            
with open('left.csv', mode='w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Image Path', 'Label'])
    for left_path, label in zip(left_image_paths,labels):
        writer.writerow([left_path, label])
        