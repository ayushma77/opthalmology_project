
import re

import numpy as np
import pandas as pd
import torch
from PIL import Image
from torchvision import transforms

from models.resnet50 import ResNet50Model

# Load the test.csv file
test_df = pd.read_csv(r'data\processed_test_ODIR-5k.csv')

# Create a DataFrame for the submission file
submissive_df = pd.DataFrame(columns=['ID','fundus', 'N', 'D', 'G', 'C', 'A', 'H', 'M', 'O'])

# Create a dictionary to store predictions
predictions = {'ID': [],'fundus':[], 'N': [], 'D': [], 'G': [], 'C': [], 'A': [], 'H': [], 'M': [], 'O': []}

# Function to preprocess the image
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return transform(image).unsqueeze(0)

# Load your pre-trained model
model = ResNet50Model(num_labels=8)
checkpoint = torch.load(r'artifacts\model_checkpoint.pt', map_location=torch.device('cpu')) 
model.load_state_dict(checkpoint['model_state_dict'])
model.eval()

# Iterate through the test set
for idx, row in test_df.iterrows():
    image_path = row['fundus']

    # Load and preprocess the image
    image = Image.open(image_path).convert('RGB')
    image_tensor = preprocess_image(image)

    # Make predictions using the pre-trained model
    with torch.no_grad():
        output = model(image_tensor)
        probabilities = torch.sigmoid(output).numpy().flatten()

    # Extract the image ID
    image_id = re.search(r'(\d+)_\w+.jpg$', image_path).group(1)

    predictions['ID'].append(image_id)
    predictions['fundus'].append(image_path)
    predictions['N'].append(round(probabilities[0], 3))
    predictions['D'].append(round(probabilities[1], 3))
    predictions['G'].append(round(probabilities[2], 3))
    predictions['C'].append(round(probabilities[3], 3))
    predictions['A'].append(round(probabilities[4], 3))
    predictions['H'].append(round(probabilities[5], 3))
    predictions['M'].append(round(probabilities[6], 3))
    predictions['O'].append(round(probabilities[7], 3))

# Create a DataFrame from the predictions dictionary
submissive_df = pd.DataFrame(predictions)

# Save the submission DataFrame to CSV
submissive_df.to_csv('submission.csv', index=False)

# Load the submission.csv file
submission_df = pd.read_csv('submission.csv')

# Create a DataFrame for the new submission1.csv
submission1_df = pd.DataFrame(columns=['ID', 'N', 'D', 'G', 'C', 'A', 'H', 'M', 'O'])

# Iterate through unique IDs in the original submission
unique_ids = submission_df['ID'].unique()
for image_id in unique_ids:
    # Get the rows for the current ID
    id_rows = submission_df[submission_df['ID'] == image_id]

    # Find the labels with the maximum probability for both left and right images
    max_label_left = id_rows[id_rows['fundus'].str.contains('left')].iloc[:, 2:].idxmax(axis=1).values[0]
    max_label_right = id_rows[id_rows['fundus'].str.contains('right')].iloc[:, 2:].idxmax(axis=1).values[0]

    # Update the new submission1_df DataFrame
    submission1_df = submission1_df._append({
    'ID': image_id,
    'N': 1 if max_label_left == 'N' and max_label_right == 'N' else 0,
    'D': 1 if max_label_left == 'D' or max_label_right == 'D' else 0,
    'G': 1 if max_label_left == 'G' or max_label_right == 'G' else 0,
    'C': 1 if max_label_left == 'C' or max_label_right == 'C' else 0,
    'A': 1 if max_label_left == 'A' or max_label_right == 'A' else 0,
    'H': 1 if max_label_left == 'H' or max_label_right == 'H' else 0,
    'M': 1 if max_label_left == 'M' or max_label_right == 'M' else 0,
    'O': 1 if max_label_left == 'O' or max_label_right == 'O' else 0
}, ignore_index=True)

# Save the new submission1.csv
submission1_df.to_csv('submission1.csv', index=False)

# Display the resulting DataFrame
print(submission1_df)