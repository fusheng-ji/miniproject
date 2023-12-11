# Mini-Project

## Datasets

First download from [Google Drive](https://drive.google.com/drive/folders/18i8eydHa6n2hnHUVirDFi22QDCzPLDaS?usp=drive_link)  the dataset folder, and put it under the root path.

- Object-level

  - Objaverse-Xl
    - [Description](https://github.com/allenai/objaverse-xl)
    - Can be downloaded by the API provied in the [Colab tutorial](https://colab.research.google.com/drive/15XpZMjrHXuky0IgBbXcsUtb_0g-XWYmN?usp=sharing)
  - MVImageNet
    - [Download link](https://github.com/GAP-LAB-CUHK-SZ/MVImgNet)
  - OminiObject3D
    - [Description](https://omniobject3d.github.io/)
    - [Download link](https://opendatalab.com/OpenXDLab/OmniObject3D-New/tree/main)
    - Used cat: beauty_blender
  - Google Scanned Object
    - [Descrption](https://research.google/resources/datasets/scanned-objects-google-research/)
    - Used: [Weisshai_Great_White_Shark](https://app.gazebosim.org/GoogleResearch/fuel/models/Weisshai_Great_White_Shark)
  - NeRF-based dataset
    - [Download link](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1)
    - LLFF
    - synthetic
- Scene-level

  - Scannet++
    - [Download link](https://kaldir.vc.in.tum.de/scannetpp/dashboard)
    - downloaded: DSLR only (2 MP): 112 GB
  - 3D-Future
    - [Download link](https://tianchi.aliyun.com/specials/promotion/alibaba-3d-future#)
    - Only contain Single view
    - Select randomly 6 scenes from train/test set
  - RealEstate10K
    - [Download link](https://google.github.io/realestate10k/download.html)
    - used: test/ec2745428712d42b

## Visualization

### Task: Visualize the multi-view camera viewpoints
This part using the Python + webasm/js/css/html and can be used instantly (does not need any C++ compilation).
![visualization_omni3d](https://github.com/fusheng-ji/miniproject/blob/main/asset/visualization_omni3d.mov)

![visualization_3d_future](https://github.com/fusheng-ji/miniproject/blob/main/asset/visualization_3d_future.mov)


```
pip install requirement.txt
python OminiObject3D.py / 3D_Future.py 
open your browser with localhost:8888
```

## Epipolar Geometry

### Task: Draw the epipolar line between two views

Using SIFT to find Keypoint, experiment on the book_002/008.png and book_002/010.png from dataset/OmniObject3D.
<img src="https://github.com/fusheng-ji/miniproject/blob/main/asset/epipolar_line.PNG" align="center">

```
python epipolar_draw.py
```

### Task: Do the stereo rectification for two views
<img src="https://github.com/fusheng-ji/miniproject/blob/main/asset/stereo_rectification.PNG" align="center">

```
python stereo_rectification.py
```

## References

The main structure of Visualization Part is builded on [Alex Yu's plenoctrees](https://github.com/sxyu/nerfvis/tree/master). Thanks for your wonderful work!
