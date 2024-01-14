import csv
import os
from os.path import join

import matplotlib.pyplot as plt
import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset

labels_to_index_map = {"N": 0, "D": 1, "G": 2,"C":3,"A":4,"H":5,"M":6,"O":7}

def label_to_idx(label):
    return labels_to_index_map.get(label, -1)

def read_as_csv(csv_file, has_labels=True):
    image_paths = []
    labels = []

    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        
        fundus_index = header.index("fundus")

        for row in reader:
            image_paths.append(row[fundus_index])

            if has_labels:
                label_index = header.index("label")
                labels.append(row[label_index])

    return image_paths, labels if has_labels else image_paths

class DRDataset(Dataset):
    def __init__(self, csv_path, transforms=None, has_labels=True):
        images, labels = read_as_csv(csv_path, has_labels=has_labels)
        self.images = images
        self.labels = labels if has_labels else None
        self.transforms = transforms

    def __len__(self):
        return len(self.images)

    def __str__(self):
        return f"ImageDataset with {self.__len__()} samples"

    def __getitem__(self, index):
        image_path = self.images[index]
        label_name = self.labels[index] if self.labels is not None else None
        label = label_to_idx(label_name) if label_name is not None else None

        image = Image.open(image_path).convert("RGB")

        if self.transforms:
            image = self.transforms(image)
        return image, label
