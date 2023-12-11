import os
from scene import Scene
import numpy as np
import imageio.v2 as imageio
from scipy.spatial.transform import Rotation

if __name__ == "__main__":
    scene = Scene()
    scene_used = ['test/image/0000004.jpg',
                  'test/image/0002587.jpg', 
                  'test/image/0002603.jpg', 
                  'test/image/0003074.jpg', 
                  'test/image/0003391.jpg', 
                  'test/image/0003633.jpg',
                  'train/image/0006857.jpg',
                  'train/image/0008825.jpg', 
                  'train/image/0010866.jpg', 
                  'train/image/0011823.jpg', 
                  'train/image/0013129.jpg', 
                  'train/image/0014341.jpg']
    
    i = np.random.randint(0,len(scene_used)) # randomly select scene to visualized

    scene.set_title("3D_Future_"+scene_used[i])

    image = imageio.imread(os.path.join("datasets/scene_level/3D_Future/",scene_used[i]))

    # due to dataset don't provied camera pose, random generate correspoing pose
    R = Rotation.from_rotvec(np.pi / 2 * np.array([0, 1, 0])).as_matrix()
    t = np.random.randn(3) * 0.1
    f = 358 / 800 * 1111
    Z = 1.0
    scene.set_opencv()

    scene.add_camera_frustum(
        "My camera/0",
        r=R[None],
        t=t[None],
        focal_length=f,
        image_width=image.shape[1],
        image_height=image.shape[0],
        z=Z,
    )
    scene.add_image(
        scene_used[i], image, r=R, t=t, focal_length=f, z=Z
    )
    scene.display(port=8888)
