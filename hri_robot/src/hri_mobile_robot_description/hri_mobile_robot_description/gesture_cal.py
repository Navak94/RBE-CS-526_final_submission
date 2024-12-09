import cv2
import math
import numpy as np
from .handDetector import HandDetector  
from .classifier import Classifier
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16  # Import the Int16 message type

# Path to your model and labels
path = "/home/osb/hri_robot/src/hri_mobile_robot_description/hri_mobile_robot_description/Model"

class GestureRecognition(Node):
    def __init__(self, img_size=700, offset=20):
        super().__init__('gesture_recognition')  # Node name
        self.img_size = img_size  # Desired size of the image after resizing
        self.offset = offset  # Padding around the hand region
        self.detector = HandDetector(maxHands=1)  # Assuming you have this detector class
        self.classifier = Classifier(f'{path}/keras_model.h5', f'{path}/labels.txt')
        self.labels = self.load_labels()  # List of labels for prediction

        # Create a publisher for 'index_topic' with message type 'Int16'
        self.publisher_ = self.create_publisher(Int16, 'index_topic', 10)  # QoS depth 10

        # Open the video capture
        self.cap = cv2.VideoCapture(0)  # Capture from webcam
        if not self.cap.isOpened():
            self.get_logger().error("Unable to access the webcam")
            exit(1)

    def load_labels(self):
        return [
            "stop", "forward", "backward", "sideway_left", "sideway_right",
            "z_clockwise", "z_counterclockwise"
        ]

    def process_frame(self, img):

        index = 0  
        img_output = img.copy()
        hands, img = self.detector.findHands(img)  

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            img_white = np.ones((self.img_size, self.img_size, 3), np.uint8) * 255
            img_crop = img[y - self.offset:y + h + self.offset, x - self.offset:x + w + self.offset]
            aspect_ratio = h / w

            if aspect_ratio > 1:
                k = self.img_size / h
                w_cal = math.ceil(k * w)
                img_resize = cv2.resize(img_crop, (w_cal, self.img_size))
                w_gap = math.ceil((self.img_size - w_cal) / 2)
                img_white[:, w_gap:w_cal + w_gap] = img_resize
            else:
                k = self.img_size / w
                h_cal = math.ceil(k * h)
                img_resize = cv2.resize(img_crop, (self.img_size, h_cal))
                h_gap = math.ceil((self.img_size - h_cal) / 2)
                img_white[h_gap:h_cal + h_gap, :] = img_resize
 
            prediction, index = self.classifier.getPrediction(img_white, draw=False)

            cv2.putText(img_output, self.labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 255), 2)
            cv2.rectangle(img_output, (x - self.offset, y - self.offset),
                          (x + w + self.offset, y + h + self.offset), (102, 0, 204), 4)

        # Show the annotated image
        cv2.imshow("Gesture Recognition", img_output)
        cv2.waitKey(1)
        return int(index)

    def run(self):
        """Continuously processes frames and publishes the gesture index."""
        while rclpy.ok():
            success, img = self.cap.read()
            if not success:
                self.get_logger().error("Failed to read frame from webcam")
                break

            gesture_index = self.process_frame(img)

            msg = Int16()
            msg.data = gesture_index

            self.publisher_.publish(msg)

        self.cap.release()
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    gesture_recognition_node = GestureRecognition()

    try:
        gesture_recognition_node.run()
    except KeyboardInterrupt:
        gesture_recognition_node.get_logger().info("Shutting down node...")
    finally:
        gesture_recognition_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
