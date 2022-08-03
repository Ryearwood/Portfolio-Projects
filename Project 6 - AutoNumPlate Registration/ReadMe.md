# Image-Based Automatic Number Plate Extraction
---
#### Project Status: [Completed]
---
## Project Intro
The purpose of this project is to build a simple, but intuitive License Plate Extractor from images of vehicles passed to it. There are a few general purposes for such a tool, but the most widely known business application would be in the automation of parkinging/payment systems (Such as the automatic registration of vehicles coming into/out of a company parking lot) - this can save both the employees time arriving and leaving work, while also saving the business resources by detecting vehicles that do not have authorization to park in the lot area. There are, of course, many other use-cases as well but this is just a general example.

### Methods Used
* Noise Reduction & Channel Adjustment
* Contouring & Image Masking
* Edge Detection
* Text Extraction

### Technologies Used
* Python
* VSCode
* Numpy, Jupyter Lab
* Streamlit
* OpenCV
* EasyOCR

## Project Description
In this project, the main goal is to explore the uses of two main python libraries and their capabilities - OpenCV and EasyOCR to detect a License Plate from a picture of a vehicle. Once the image is received:

1) The color channel is adjusted to Grayscale to make edge detection and contouring easier
2) Noise Reduction is done on the raw image
3) Followed by Localization of Edges that are detected
4) Once the localized edges are detected, Contouring is done to located the landmarks in the filtered image
5) Contours are stacked in a Tree format in descending order -- contours with 4 landmarks (rectange/square) are isolated
6) Masking is applied to the rest of the filtered image
7) Contoured area is overlaid on top of masked image and isolated to enlarge the cropped license plate
8) EasyOCR module is then executed on the enlarged license plate image and text data is extracted

## Project Scope and Needs

- GPU (CUDA Supported through PyTorch) or CPU (MultiThreading Possible)
- Machine Learning Applications
- Image Processing with OpenCV2
- Text Extraction with Easy OCR
- Array Manipulation with Numpy
- Visualization with Matplotlib
- Deployment through Streamlit

## Getting Started

1. Clone this repository (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository//).
2. Raw Data is kept [here](https://github.com/Ryearwood/Portfolio-Projects/tree/main/Project%206%20-%20AutoNumPlate%20Registration/Images)   
3. Follow Environment Setup instructions [Here](https://github.com/Ryearwood/Portfolio-Projects/blob/main/Project%206%20-%20AutoNumPlate%20Registration/Environment_Setup_Instructions.txt)
4. Download and install requirements.txt [Here](https://github.com/Ryearwood/Portfolio-Projects/blob/main/Project%206%20-%20AutoNumPlate%20Registration/requirements.txt)
5. Download Appropriate Pytorch version (GPU vs CPU) - Follow guide [Here](https://pytorch.org/get-started/locally/)
6. From CLI:
        - `cd ~/Project 6 - AutoNumPlate Registration`
        - `streamlit run AutoNumPlateExtract_Deploy.py`

## Featured Notebooks/Analysis/Deliverables
* [ANPR Streamlit Deployment Script](https://github.com/Ryearwood/Portfolio-Projects/blob/main/Project%206%20-%20AutoNumPlate%20Registration/AutoNumPlateExtract_Deploy.py)
* [Automatic Number Plate Extraction Walkthrough](https://github.com/Ryearwood/Portfolio-Projects/blob/main/Project%206%20-%20AutoNumPlate%20Registration/AutoNumPlateExtraction_Walkthrough.ipynb)


## Contact
* Feel free to contact with me via [Linkedin!](https://www.linkedin.com/in/yearwoodrussell/)