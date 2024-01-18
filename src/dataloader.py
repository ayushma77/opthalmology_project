from pathlib import Path

from torch.utils.data import DataLoader

from config import BATCH_SIZE, EPOCHS, LR, SEED, TEST_CSV, TRAIN_CSV, VAL_CSV
from datasets import DRDataset
from transforms import transforms


def check_file_existence(file_path):
    file_path = Path(file_path)
    if file_path.is_file():
        print(f"File found: {file_path}")
    else:
        print(f"File not found: {file_path}")

# Check file existence for each CSV file
check_file_existence("/content/opthalmology_project/data/processed_train_ODIR-5k.csv")
check_file_existence("/content/opthalmology_project/data/processed_val_ODIR-5k.csv")
check_file_existence("/content/opthalmology_project/data/processed_test_ODIR-5k.csv")

train_dataset = DRDataset(csv_path=TRAIN_CSV, transforms=transforms,has_labels=True)
val_dataset = DRDataset(csv_path=VAL_CSV, transforms=transforms,has_labels=True)
test_dataset = DRDataset(csv_path=TEST_CSV, transforms=transforms, has_labels=False)


train_data_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
val_data_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)
test_data_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE)

if __name__ == "__main__":
    images, labels = next(iter(train_data_loader))

    print(images, labels)
