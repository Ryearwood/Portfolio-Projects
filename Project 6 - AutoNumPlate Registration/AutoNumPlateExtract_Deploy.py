# Load Libraries
import cv2
import numpy as np
import imutils
import easyocr
import streamlit as st

# Set Title for Deployed Project
st.title("Image-Based Automatic Number Plate Extraction")
# Display Markdown text in App Screen
text = """ 
           The following notebook outlines a small project to be able to detect and extract license plate information from an image.\n
           This can be built out to automate parking lot metering or even production line work in scale.\n
           The following documentation can be used as a resource: \n
           1) [EasyOCR Doumentation](https://github.com/JaidedAI/EasyOCR)\n
           2) [OpenCV Documentation](https://docs.opencv.org/4.5.0/)\n
           3) [Streamlit Documentation](https://docs.streamlit.io/)\m
           
           Please see the corresponding Notebook for Tutorial Walkthrough on Automatic Number Plate Extraction -- There are specific areas that can help to improve the extraction results vastly
       """
st.markdown(text,unsafe_allow_html=True)

# OCR and Text Extraction Function
def extract_license(img):
    # Load Image using Cv2 Library - adjust colour channel
    gryscle = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Noise Reduction
    bifilter = cv2.bilateralFilter(gryscle, 11, 17, 17)
    # Edge Detection
    edges = cv2.Canny(bifilter, 30, 200)
    # Detect Contours
    points = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Grab Contour point locations
    contours = imutils.grab_contours(points)
    # Sort and store contours based on sizes in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    # Loop through detected contours and grab the locations of the license plate
    locations = None
    for contour in contours:
        approx_pos = cv2.approxPolyDP(contour, 10, True)
        if len(approx_pos) ==4:
            locations = approx_pos
            break
    # Create mask using numpy and shape of image for scale
    mask = np.zeros(gryscle.shape, np.uint8)
    new_image = cv2.drawContours(mask, [locations], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    # find every position where image is NOT black
    (x,y) = np.where(mask==255)

    # Grab coordinates of image
    (x1,y1) = (np.min(x), np.min(y))
    (x2,y2) = (np.max(x), np.max(y))

    # Slice the portion of the image by coordinate range
    crop_img = gryscle[x1:x2+1, y1:y2+1]
    st.image(cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB))
    
    # Use EasyOCR to extract text from license plate
    render = easyocr.Reader(['en'])
    result = render.readtext(crop_img)
    txt = result[0][-2]
    return txt

# Main Execution function
def main():
    
    # User upLoaded image
    uploaded_file = st.file_uploader("Upload file", type=["png", "jpg"])
    show_file = st.empty()
    
    # Check if Loaded file is an Image or not
    if uploaded_file is not None:
        # Display the uploaded image
        show_file.image(uploaded_file)
        
        # OpenCv requires data to be in specific format --- here we will adjust and convert it accordingly
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # Execute License Plate Extraction 
        plate = extract_license(opencv_image)
        st.write(f"Extracted License Plate: {plate}")
        
    else:
        show_file.info("Please upload an image of type: " + ", ".join(["png", "jpg"]))

if __name__=="__main__":
    # Execute ANPR Function
    main()