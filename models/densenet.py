import torch
import torch.nn as nn
from torchsummary import summary
from torchvision import models


class DenseNetModel(nn.Module):
    def __init__(self, num_labels):
        super(DenseNetModel, self).__init__()

        # Load pre-trained DenseNet model
        self.densenet = models.densenet121(pretrained=True)

        # Freeze all parameters in the pre-trained model
        for param in self.densenet.parameters():
            param.requires_grad = False

        # Replace the final layer of the classifier
        in_features = self.densenet.classifier.in_features

        self.densenet.classifier = nn.Sequential(
            nn.Linear(in_features, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, 256),
            nn.ReLU(inplace=True),
            nn.Linear(256, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, num_labels),
        )

    def forward(self, x):
        return self.densenet(x)


# if __name__ == "__main__":
#     model = DenseNetModel(num_labels=8)
#     # Move the model to GPU
#     device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#     model.to(device)

#     x = torch.rand(1,3,224,224).to(device)
#     o = model(x)
#     print(o)
#     summary(model, input_size=(3, 224, 224))
