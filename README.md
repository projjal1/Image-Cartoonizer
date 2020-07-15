# Image-Cartoonizer

A Python Script to create Cartoon effects on a given Image file using OpenCV.
This project is an implementation of Bilateral Filters, Upscaling and Downscaling the image to create blur effects on the image.
Next to preserve edges from being decomposed we apply median blur to maintain a vivid color spectrum.
Lastly, we merge two images to generate a cartoonized effect

<h2>Requirements</h2>
<ul>
<li>Python 3.5+</li>
<li>OpenCv 2</li>
</ul>

<pre>Usage :  python script.py -i [path-to-image]  </pre>

<h2>Point to Note:</h2>
This script might not work on some JPEG image files due to inconsistency in the alpha-channels. This is due to varying color channels when taken 
from high-end devices or modified version from LightRoom, Photoshop, etc.

<h2>Attribution</h2>
[Tejas Rama](https://highontechs.com/computer-vision/cartooning-an-image-with-opencv/)
