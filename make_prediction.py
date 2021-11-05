from imageai.Classification import ImageClassification
from pathlib import Path
prediction = ImageClassification()

prediction.setModelTypeAsInceptionV3()

model_path = Path(__file__).parent / "training_data/treeorme/models/model_ex-008_acc-0.960265.h5"

prediction.setModelPath(r"C:\Users\andrewss\git\christmas_card_2021\training_data\treeorme\models\model_ex-008_acc-0.986755.h5")

prediction.loadModel()

image_to_test = Path(__file__).parent / "training_data/treeorme/test/simon.jpg"

predictions,probabilities = prediction.classifyImage(str(image_to_test))

print(predictions, probabilities)
