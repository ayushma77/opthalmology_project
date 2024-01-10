# 1 Prepare dataset
from torch.utils.data import Dataset
import csv
# from src.utilis import read_as_csv, label_to_idx
from PIL import Image
def read_as_csv(csv_file):
    image_path = []
    labels = []
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            image_path.append(row[0])
            labels.append(row[1])
    return image_path, labels

class ODRDataset(Dataset):
    def __init__(self, csv_path, transforms=None):
        images, labels = read_as_csv(csv_path)
        self.images = images
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return len(self.images)

    def __str__(self):
        return f"ImageDataset with {self.__len__()} samples"

    def __getitem__(self, label):
        image_path = self.images[label]
        label= self.labels[label]
        
        image = Image.open(image_path).convert("RGB")

        if self.transforms:
            image = self.transforms(image)

        return image, label

