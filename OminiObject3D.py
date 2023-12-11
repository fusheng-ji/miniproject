import os
from scene import Scene
import numpy as np
import json
import cv2

if __name__ == "__main__":
    scene = Scene()

    scene_used = ["beauty_blender_001",
                  "beauty_blender_002",
                  "beauty_blender_003",
                  "beauty_blender_004"]
    
    index = np.random.randint(0,len(scene_used)) # randomly select scene to visualized

    scene.set_title("OminiObject3D/"+scene_used[index])
    with open(os.path.join("datasets/object_level/OminiObject3D/blender_renders/beauty_blender/",scene_used[index],"render/transforms.json"), "r") as json_data:
        trans = json.load(json_data)

    scene.set_opengl()
    

    
    camera_angle_x = float(trans['camera_angle_x'])
    image_path = os.path.join("datasets/object_level/OminiObject3D/blender_renders/beauty_blender/",scene_used[index],"render/images/")
    num = len(os.listdir(r"./"+image_path))
    image_list = []
    R = []
    T = []

    for i in range(num):
        image = cv2.imread(os.path.join(image_path + "r_"+str(i)+".png"))
        image_list.append(image)
        trans_matrix = np.matrix(trans['frames'][i]['transform_matrix'])# (4,4)
        R.append(trans_matrix[:3, :3])
        T.append(np.reshape(np.array(trans_matrix[:3, 3]),(3,)))
        if i == 0:
            H, W = image.shape[:2]
            focal = .5 * W / np.tan(.5 * camera_angle_x)
    
    print("load finished")
    scene.add_images(
                    scene_used[index],
                    image_list,
                    r=R,                # r: c2w rotation (N, 3, 3) or (N, 4) etc
                    t=T,                # t: c2w translation (N, 3,)
                    focal_length=focal, # focal_length: focal length (in pixels, real image size as loaded will be used)
                    z=0.5,               # z: size of camera
                    with_camera_frustum= True
                )
    scene.add_axes()
    scene.display(port=8888)