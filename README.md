# AI Trainer Project
Simple AI trainer app using ***OpenCV Python*** and <a href="https://google.github.io/mediapipe/">***MediaPipe Python***</a><br>
It detects exercising-pose, which is given realtime, and counts "proper" reps! 

### How to use
1. Choose type: **bicep curl** or **squat**<br>
 ![image](https://user-images.githubusercontent.com/67196344/131671166-55fd85d0-2774-480d-83f4-9992070f2caf.png)
2. You can have 5 seconds to set up


https://user-images.githubusercontent.com/67196344/131781539-5693deb0-418e-4bf7-b16a-26c21b9a85a0.mp4


3. Make sure the camera looks at the leftside of your body.
4. Time to start workout! It will count reps for you :)


https://user-images.githubusercontent.com/67196344/131844397-a3395e7d-b592-4c01-9e82-f38567d07a38.mp4



https://user-images.githubusercontent.com/67196344/131844459-503c8362-66e6-4c2e-9c43-0c2e6cc8333d.mp4



### How it works
1. Getting landmarks on the body using ***MediaPipe***: <a href="https://google.github.io/mediapipe/solutions/pose.html">Pose Estimation</a>
2. Depending on the exercise chosen, it calculates the angles between joints which actually matter
3. It only counts "proper" reps, by checking the range of important angle(s)

#### Things to be improved
- Applying it to various kinds of exercises<br>
- Improving accuracy, especially when face of a user's is not shown: applying improved DL model<br>
- Detecting multiple people<br>
- User interface<br>
etc.
