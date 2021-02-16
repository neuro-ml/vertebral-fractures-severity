from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import rainbow

import pydicom


def load_image(root, annotation):
    """
    Load the image for the corresponding annotation.

    Parameters
    ----------
    root
        path to the `CTLungCa-500` folder.
    annotation
        the annotation loaded from one of the files in the `annotation` folder.
    """
    folder = Path(root) / 'dicom' / annotation['Folder']
    assert folder.exists(), 'Wrong dataset root'

    files = []
    for file in folder.glob('**/*'):
        if file.is_dir():
            continue

        dc = pydicom.dcmread(str(file))
        if dc.SeriesInstanceUID == annotation['SeriesInstanceUID']:
            files.append(dc)

    return np.stack([
        dc.pixel_array * dc.RescaleSlope + dc.RescaleIntercept
        for dc in sorted(files, key=lambda x: int(x.InstanceNumber))
    ], -1)


def choose_sagittal(annotation):
    """Choose the sagittal index on which the annotation is best visible."""
    indices = []
    for expert in annotation['Annotation'].values():
        indices.append(np.array(expert)[..., 1].mean())
    return int(np.mean(indices))


def draw_annotation(image, annotation):
    """Draw the annotation on a sagittal slice from the image."""
    idx = choose_sagittal(annotation)

    plt.figure(figsize=(10, 10))
    plt.imshow(image[:, idx].T, cmap='gray')

    colors = rainbow(np.linspace(0, 1, len(annotation['Annotation'])))
    for color, (expert, points) in zip(colors, annotation['Annotation'].items()):
        # drop the sagittal index
        points = np.array(points)[..., [0, 2]]
        # collapse all segments
        points = points.reshape(-1, 2, 2)

        for i, segment in enumerate(points):
            plt.plot(*segment.T, c=color, linewidth=3, label=expert if i == 0 else '')

    plt.tight_layout()
    plt.axis('off')
    plt.legend()
