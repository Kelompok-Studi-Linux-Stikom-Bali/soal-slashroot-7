import cv2
import numpy
from matplotlib import pyplot

video = cv2.VideoCapture('flag.webm')

ret, frame = video.read()

frame = numpy.array(frame)

pyplot.imshow(frame, interpolation="nearest")
pyplot.show()
