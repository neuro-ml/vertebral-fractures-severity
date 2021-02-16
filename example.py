import json
from pathlib import Path
import matplotlib.pyplot as plt

from utils import load_image, draw_annotation

with open(Path(__file__).parent / 'annotation/RLAD42D007-22975_RLS6A01002SVR_2418297.json') as file:
    annotation = json.load(file)

# we'll assume the dataset is in the home folder
#  change the path if needed
image = load_image(Path('~/CT_LUNGCANCER_500').expanduser(), annotation)
draw_annotation(image, annotation)
plt.savefig('RLAD42D007-22975_RLS6A01002SVR_2418297.png')
