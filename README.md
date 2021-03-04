# Track tennis players and the ball

## About The Project

<p align="center">
  <img src="https://raw.githubusercontent.com/MaximeBataille/tennis_tracking/blob/master/demo.PNG"/>
</p>

The goal of this project is :
- to detect and track both players, and only both players. For example, the ball boys/girls must not be recognized.
- to detect and track the ball.
- to project the location of players in bird eye view

More generally, this tool is an introduction to a more developed tool that would allow the analysis of tennis matches thanks to tracking data (distances covered, ball bounce zone, etc..).

## Key directories

* BirdEyeView.py : Class and functions to build a bird eye view animation
* Court.py : Function to display the contours of the court on video tracking
* TrackNet.py : Neural Network to detect a tennis ball in a video

* predict_video.py : Track players and the ball
* generate_bird_eye_view : Generate a bird eye view of tracking players

<!-- GETTING STARTED -->
## Getting Started


### Installation

Download yolov3 weights here https://pjreddie.com/darknet/yolo/ (YOLOV3-320, 45 FPS) and add it to Yolov3 directory. (This file is too heavy to push on github). Name this file yolov3.weights .

The best way to run predict_video.py is on google colab, which has a GPU.  I was unable to configure opencv to use the GPU on google colab. So the player detection part is not faster. The ball detection is. Any help is welcome to achieve this.
 
1. Clone the repo.
```sh
git https://github.com/MaximeBataille/tennis_tracking
```
2. Run predict_video.py to obtain a tracking video. (Google colab)
```sh
!python3 "predict_video.py"  --save_weights_path="weights_tracknet/model.1" --input_video_path="/VideoInput/video_cut.mp4" --output_video_path="/VideoOutput/video_output.avi" --n_classes=256 --path_yolo_classes="/yolov3/yolov3.txt" --path_yolo_weights="/yolov3/yolov3.weights" --path_yolo_config="/yolov3/yolov3.cfg"
```

3. Run generate_bird_eye_view.py to obtain a bird eye view. (Google colab)
```sh
!python3 "generate_bird_eye_view.py"
```

4. The generated videos are in the VideoOutput directory.

## Possible improvements

- Obtain the coordinates of the ball thanks to a second camera and thus recognize impacts with the ground or a player's racket.
- Detecting the contours of the court from any angle of view and any part of the court precisely in order to make the bird eye view projection.
- Do not recognise the players as persons but as real players. This avoids the need for image processing to detect and remove ball boys/girls, for example.

## Acknowledgements

* To track a tennis ball : Y.-C. Huang, I.-N. Liao, C.-H. Chen, T.-U. Ik, W.-C. Peng, “TrackNet: A Deep Learning Network for Tracking High-speed and Tiny Objects in Sport Applications”, Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining KDD ‘19, https://arxiv.org/pdf/1907.03698.pdf
* TrackNet on github : https://github.com/nyck33/TrackNetMirror
* To detect players with Yolov3 : Joseph Redmon, Ali Farhadi, "YOLOv3: An Incremental Improvement", University of Washington, https://arxiv.org/pdf/1804.02767.pdf
* To track players : Alex Bewley, Zongyuan Ge, Lionel Ott, Fabio Ramos, Ben Upcrof, "Simple Online and Realtime Tracking", Queensland University of Technology, University of Sydney, https://arxiv.org/pdf/1602.00763.pdf
* SORT algorithm on github, https://github.com/abewley/sort