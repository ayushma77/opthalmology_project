import numpy as np

from src.datasets import DRDataset

csv_path=r"data\ODIR-5K_Training_Annotations_processed.csv"

image_dataset = DRDataset( csv_path=csv_path, transforms=None)

r_mean_sum = 0
r_std_sum=0
g_mean_sum = 0
g_std_sum = 0
b_mean_sum = 0
b_std_sum = 0
total_images = len(image_dataset)

for img,_ in image_dataset:
    img_np=np.array(img)
    b_mean_sum+=img_np[2].mean()
    b_std_sum+=img_np.std()



print(r_mean_sum/len(image_dataset),r_std_sum/len(image_dataset))#=>4.522803306045762 57.93123495983965
print(g_mean_sum/len(image_dataset),g_std_sum/len(image_dataset))#=>4.991042103024577 57.93123495983965
print(b_mean_sum/len(image_dataset),b_std_sum/len(image_dataset))#=>5.356430134099938 57.93123495983965
print(4.522803306045762/255.0   ,  4.991042103024577/255.0  ,    5.356430134099938/255.0   ,    57.93123495983965/255.0)
#0.017736483553120633 0.019572714129508145 0.021005608369019366 0.22718131356799862