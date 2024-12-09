import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .gesture_cal import *
from std_msgs.msg import Int16  

index=Int16()
vel=Twist()

class CmdVelPublisher(Node):
    def __init__(self):

        super().__init__('cmd_vel') 

        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.subscription = self.create_subscription(
            Int16,                  
            'index_topic',        
            self.listener_callback, 
            10                      
        )
        self.subscription  

    def listener_callback(self, msg):
        index=msg.data
        match index:
            case 0:
                vel.linear.x = 0.0
                vel.linear.y = 0.0
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 0.0
                return vel
            case 1:
                vel.linear.x = 1.5 
                vel.linear.y = 0.0
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 0.0
                return vel
            case 2:
                vel.linear.x = -1.5
                vel.linear.y = 0.0
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 0.0  
                return vel
            case 3:
                vel.linear.x = 0.0
                vel.linear.y = 1.5
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 0.0
                return vel
            case 4:
                vel.linear.x = 0.0
                vel.linear.y = -1.5
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 0.0
                return vel
            case 5:
                vel.linear.x = 0.0
                vel.linear.y = 0.0
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 1.0
                return vel
            case 6:
                vel.linear.x = 0.0
                vel.linear.y = 0.0
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = -1.0
                return vel
            # case 7:
            #     vel.linear.x = 0.5
            #     vel.linear.y = 0.0
            #     vel.linear.z = 0.0
            #     vel.angular.x = 0.0
            #     vel.angular.y = 0.0
            #     vel.angular.z = 0.5
            #     return vel
            # case 8:
            #     vel.linear.x = -0.5
            #     vel.linear.y = -0.5
            #     vel.linear.z = 0.0
            #     vel.angular.x = 0.0
            #     vel.angular.y = 0.0
            #     vel.angular.z = 0.5
            #     return vel
            case _:
                vel.linear.x = 0.0
                vel.linear.y = 0.0
                vel.linear.z = 0.0
                vel.angular.x = 0.0
                vel.angular.y = 0.0
                vel.angular.z = 0.0
                return vel
            
    def timer_callback(self):
        self.publisher.publish(vel)

def main(args=None):
    rclpy.init(args=args)  
    node = CmdVelPublisher()  
    
    try:
        rclpy.spin(node)  
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()