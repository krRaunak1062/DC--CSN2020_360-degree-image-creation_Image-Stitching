# DC--CSN2020_360-degree-image-creation_Image-Stitching
A multi-camera stitching pipeline to create high-resolution 360° panoramic images.
This project implements feature matching and blending algorithms to turn individual camera feeds into a single immersive view.

# CSN2020: 360° Multi-Camera Image Stitching
## The Vision
#### The goal of this project is to create seamless **360-degree immersive images** using a rig of multiple standard cameras.
Instead of relying on a single expensive 360° device, we leverage the power of multiple sensors to capture high-detail environments. Our software handles the complex task of "stitching" these individual perspectives into one continuous, spherical image.
# Our Approach
We've simplified the process into three core phases:
1. **Multi-View Capture**: Syncing several cameras to capture a full $360^{\circ}$ field of view with overlapping edges.
2. **Smart Alignment**: Using computer vision to detect common points between different camera angles.
3. **Seamless Blending**: Smoothing out the "seams" and adjusting exposure so the final image looks like it was taken by a single lens.
## Features
- **Automatic Stitching**: Turn a folder of raw images into a panorama with one script.
- **Error Correction**: Handles minor misalignments between camera angles.
- **High Resolution**: Supports large-scale image processing for VR-ready outputs.
