# HRI MOBILE ROBOT DOCUMENTATION
---

- [HRI MOBILE ROBOT DOCUMENTATION](#hri-mobile-robot-documentation)
  - [Prerequsites](#prerequsites)
  - [Project Package](#project-package)
  - [Running Gazebo](#running-gazebo)
  - [Running Rviz](#running-rviz)
  - [Teleoperation with Joystick](#teleoperation-with-joystick)
  - [Teleoperation with Gesture](#teleoperation-with-gesture)

## Prerequsites
---

- Mediapipe library version 0.10.5 (command to install mediapipe library`pip install mediapipe==0.10.5`).
- Protobuf library version 3.19.0 (command to install mediapipe library`pip install protobuf==3.19.0`).
- Flatbuffers library version 24.3.25 (command to install mediapipe library`pip install flatbuffers==24.3.25`).
- Tensorflow library version 2.9.3 (command to install mediapipe library`pip install tensorflow==2.9.3`).
- Code works best with **ROS2 Humble and Gazebo 11(Classic)**.


## Project Package
---

- Download `hri_robot` workspace and unzip it.
- Now open terminal and go to the *hri_robot* path.
- First enter `cd hri_robot` then `colcon build` and once build is complete source the install folder by typing `source install/setup.bash` as illustrated in below image. 

> **Note**: Never build workspace inside src folder.

![Build Package](https://imgur.com/0tY0Zpp.png)
![Note](https://imgur.com/1BSBXwG.png)

## Running Gazebo
---

- After sourcing the **install/setup.bash** type `ros2 launch hri_mobile_robot_description gazebo.launch.py world:= src/hri_mobile_robot_description/worlds/final_world.world` to spwan gazebo model in our custom world file.
  
![Running gazebo command](https://imgur.com/e8OdkUh.png)

- This will spawn robot in gazebo and it will look like image similar to demonstrated below.

![Gazebo GUI](https://imgur.com/EWflWWR.png)

> **Note**: Gazebo will be already in the play phase. So, no need to play the simulation manually.

## Running Rviz
---

> **Note**: Run *Gazebo* first to visualize model in Rviz.
- Open new terminal and source the terminal.
- After sourcing the **install/setup.bash** type `ros2 launch hri_mobile_robot_description display.launch.py` to visualise the model in rviz.
  
![Running rviz command](https://imgur.com/V4nPF6T.png)

- This will visualize robot in Rviz and it will look like image similar to as demonstrated below.

![Rviz GUI](https://imgur.com/xlfhr0c.png)

- Indeed, there are some steps as shown below to setup Rviz
  - **TF**
    - Close tf by unchecking the box in Rviz.
  
    ![Close TF](https://imgur.com/9iZEkdU.png)
  - **Camera**
    - In bottom left there is a add button click the button which will open a pop up same as below.
    - Select `By topic` option and click on the `Camera(raw)` which will activate the *OK* button at bottom of dialogue box.
    - Click ok button to visualize camera feed.  
  
    ![Rviz Popup](https://imgur.com/0BlC6Wb.png)
    - Now maximize the Camera option in Display section and uncheck the **visiblity** option.
    
    ![Camera visibility disable](https://imgur.com/isv0GEy.png)

  - **Lidar**
    - In bottom left there is a add button click the button which will open a pop up same as below.
    - Select `By topic` option and click on the `LaserScan` which will activate the *OK* button at bottom of dialogue box.
    - Click ok button to visualize laser scan or lidar mapping.  
    
    ![Rviz Popup](https://imgur.com/gME4TrS.png)

    - Maximize the Laser option in Display section and increase the size of laser points.
    
    ![Laser scan points](https://imgur.com/NYvAOtL.png).

## Teleoperation with Joystick
---
- Connect joystick with PC/Laptop.
- Once the **Gazebo** and **Rviz** are running fine, open new terminal and run launch file by typing following command `ros2 launch hri_mobile_robot_description joystick.launch.py`

![Joystick Launch file](https://imgur.com/n2piWta.png)

- The Joystick node has successfully start. Moving further, switch to gazebo tab and follow the below image of joystick to operate robot.
  - **Linear x** axis is maped to **axis 1** of the joystick.
  - **Linear y** axis is maped to **axis 0** of the joystick. 
  - **Angular z** axis is maped to **axis 3** of the joystick. 
  - There are two modes Turbo Mode and Normal Mode for robot.
    - Turbo Mode enables fast movements.
    - Normal Mode is used for make precise movements.
  
> **Note**: To move the robot, it is necessary to hold down a mode button. For example, if you press and hold the L1 (Turbo mode) button while using the joystick axis to control movement, the robot will move. However, if you release the L1 button, the robot will immediately stop moving, even if the joystick axis is still being operated.

![Joystick axis](https://imgur.com/tHPTdNJ.png)

![Joystick mode](https://imgur.com/yZhkbsc.png)

## Teleoperation with Gesture
---
- Run Gazebo and Rviz meanwhile close the terminal running joystick launch file.
- Once the Gazebo and Rviz is initiated successfully open new terminal and run launch file by typing following command `ros2 launch hri_mobile_robot_description gesturerec.launch.py`

![Gesture Launch file](https://imgur.com/KsPx3l9.png)

- Running this will open a window for capturing gestures.
  ![Camera Window](https://imgur.com/GLNpbLl.png)

- There are total 7 gestures as shown below.
  1. stop
  2. forward
  3. backward
  4. sideway left
  5. sideway right
  6. z clockwise
  7. z counterclockwise

  ![Gestures](https://imgur.com/Fl2eSGf.png)

> **Note**: The node will stop and throw resize error if the hand distance from camera crosses a limit. The error will look as shown below. To resolve it run the launch file again.
  
  ![Error](https://imgur.com/x0PAJpz.png)