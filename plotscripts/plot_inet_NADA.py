#!/usr/bin/env python
__author__ = 'jules'

from visualCortex.resultParser import *
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import sys
import seaborn as sns


def main():

    data = parseResultFile(sys.argv[1])
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    bandwidth = data['"testNetwork.rtcWebClient.RTCWebApp.MediaPayloadGen[0]"']['"Currently Measured Output" "Rate"']
    quality = data['"testNetwork.rtcWebClient.RTCWebApp.MediaPayloadGen[0]"']['"Currently Selected" "VideoQuality"']
    frame_size = data['"testNetwork.rtcWebClient.RTCWebApp.MediaPayloadGen[0]"']['"Frame size before" "adjustment"']
    target_bit_rate = data['"testNetwork.rtcWebClient.RTCWebApp.MediaPayloadGen[0]"']['"ccTargetBitrate " "ETV"']
    encoder_transitions = data['"testNetwork.rtcWebClient.RTCWebApp.MediaPayloadGen[0]"']['"EncoderTransitionTimestamps " "ETV"']

    bandwidth_x, bandwidth_y = zip(*bandwidth)
    bandwidth_y_bits = [x* 8 for x in bandwidth_y]
    plt.plot(bandwidth_x, bandwidth_y_bits, label="Measured Bitrate")

    target_bit_rate_x, target_bit_rate_y = zip(*target_bit_rate)
    plt.plot(target_bit_rate_x, target_bit_rate_y, label="Target Bitrate")
    #quality_x, quality_y = zip(*quality)
    #plt.plot(quality_x, quality_y, label="Video Quality")
    #frame_size_x, frame_size_y = zip(*frame_size)
    #plt.plot(frame_size_x, frame_size_y, label="frame Size")

    boxes = []
    for transition in encoder_transitions:
        rect = mpatches.Rectangle((transition[0],1), 0.1, 60000000)
        boxes.append(rect)
        #plt.axvline(transition[0], color='r')

    collection = PatchCollection(boxes, cmap=plt.cm.hsv, alpha=0.3)

    #ax.set_yscale("log", nonposy='clip')
    ax.add_collection(collection)
    ax.set_xlim(0,20)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()


