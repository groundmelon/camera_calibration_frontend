## Camera Calibration Frontend ##

STEREO NOT TESTED YET!

Modified from [camera_calibration](http://wiki.ros.org/camera_calibration)

This modified version can save `calibrationdata.tar.gz` **at any time**, regardless of calibrated or not. You don't need to wait for the long calibration time when you just need the raw images.

Also, it will pop up a window showing where the saved chessboards are. 

For example:

![extra_window](extra_window.png?raw=true)

There is also another simple and naive tool: publish_calib_file.py, for publishing all png files in the current folder.
