#!/usr/bin/env python
import rospy
import glob
import cv2
import sys

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def main(args):
	rospy.init_node("publish_calib_file", args)

	files = glob.glob("left-*.png");
	files.sort()

	print("All {} files".format(len(files)))

	image_pub = rospy.Publisher("image",Image, queue_size=10)
	bridge = CvBridge();


	for f in files:
		if rospy.is_shutdown():
			break
		raw_input("Publish {}?".format(f))
		img = cv2.imread(f, 0)
		image_pub.publish(bridge.cv2_to_imgmsg(img, "mono8"))

if __name__ == "__main__":
	main(sys.argv)
