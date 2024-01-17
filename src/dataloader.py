from torch.utils.data import DataLoader

from src.datasets import DRDataset
from src.transforms import transforms
from src.config import  EPOCHS,BATCH_SIZE,TEST_CSV,TRAIN_CSV,VAL_CSV,LR,SEED

train_dataset = DRDataset(csv_path=TRAIN_CSV, transforms=transforms,has_labels=True)
val_dataset = DRDataset(csv_path=VAL_CSV, transforms=transforms,has_labels=True)
test_dataset = DRDataset(csv_path=TEST_CSV, transforms=transforms, has_labels=False)


train_data_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_data_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)
test_data_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE)

if __name__ == "__main__":
    images, labels = next(iter(train_data_loader))

    print(images, labels)
