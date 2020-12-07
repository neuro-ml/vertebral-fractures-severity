[[arxiv]](https://arxiv.org/abs/2005.11960) [[springer]](https://link.springer.com/chapter/10.1007/978-3-030-59725-2_70)

This repository contains annotated vertebrae heights for 100 randomly selected 
images from the [MoscowRadiology-CTLungCa-500](https://mosmed.ai/en/datasets/ct_lungcancer_500/)
dataset. 

The annotation was prepared for the paper [Keypoints Localization for Joint Vertebra Detection and Fracture Severity Quantification](https://arxiv.org/abs/2005.11960) 
and was used to train and evaluate the vertebrae fractures detection algorithm. 

We urge the community to use the dataset and annotation in their research 
in order to be able to compare different methods for vertebrae fractures detection.

# Usage

`example.py` contains an example of matching the annotation with images from the dataset.

# Questions

If you have any questions please feel free to open an [issue](https://github.com/neuro-ml/vertebral-fractures-severity/issues).

# Cite

If you have used the annotation and the MoscowRadiology-CTLungCa-500 dataset in a scientific publication, please cite 
our paper, the dataset's paper, and the annotation's paper.


 - Pisov M. et al. (2020) Keypoints Localization for Joint Vertebra Detection and Fracture Severity Quantification. In: Martel A.L. et al. (eds) Medical Image Computing and Computer Assisted Intervention – MICCAI 2020. MICCAI 2020. Lecture Notes in Computer Science, vol 12266. Springer, Cham. https://doi.org/10.1007/978-3-030-59725-2_70
 - S.P. Morosov, N.S. Kulberg, V.A. Gombolevskiy, N.V. Ledikhova, I.A. Sokolina, A.V. Vladzimirskiy, A.S. Bardin. (2018) Tagged results of lung computed tomography scans (RU 2018620500).
 - Petraikin AV, Belaya ZhE, Kiseleva AN, Artyukova ZR, Belyaev MG, Kondratenko VA, Pisov ME, Solovev AV, Smorchkova AK, Abuladze AR, Kieva IN, Fedanov VA, Iassin LR, Semenov DS, Kudryavtsev ND, Shchelykalina SP, Zinchenko VV, Akhmad ES, Sergunova KA, Gombolevskiy VA, Nisovtsova LA, Vladzymyrskyy AV, Morozov SP. Artificial intelligence for diagnosis of vertebral compression fractures using a morphometric analysis model, based on convolutional neural networks. Problems of Endocrinology 2020;66(5):45-57
 
# License

The annotation is distributed according to the [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/),
which means that you can freely use the data for any non-commercial purpose 
as long as you give appropriate credit to the authors.
