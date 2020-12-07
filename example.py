import json
from pathlib import Path
import matplotlib.pyplot as plt

from utils import load_image, draw_annotation

with open(Path(__file__).parent / 'annotation/RLADD01000006301_RLSDD01000006282.json') as file:
    annotation = json.load(file)

# we'll assume the dataset is in the home folder
#  change the path if needed
image = load_image(Path('/nmnt/t-hdd/data/CTLungCa-500').expanduser(), annotation)
draw_annotation(image, annotation)
plt.savefig('RLADD01000006301_RLSDD01000006282.png')
