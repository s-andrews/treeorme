from imageai.Classification.Custom import ClassificationModelTrainer
from pathlib import Path

model_trainer = ClassificationModelTrainer()

#model_trainer.setModelTypeAsMobileNetV2()
model_trainer.setModelTypeAsInceptionV3()

datadir = Path(__file__).parent / "training_data/treeorme"

model_trainer.setDataDirectory(str(datadir))

model_trainer.trainModel(
    num_objects=2,
    num_experiments=10,
    enhance_data=True,
    show_network_summary=True,
)