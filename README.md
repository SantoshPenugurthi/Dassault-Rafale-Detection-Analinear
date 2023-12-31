<h1 align="center"> Object Detection - Analinear</h1>

![Alt text](https://i.ibb.co/tKmJ63h/results.jpg)

# Repository Overview

This repository contains code and documentation for detecting an object with pre-trained models `task1` and with custom dataset `task2`.

## Directory Structure

- **Best_Trained_Model_with_Custom_Dataset:**
  - This directory contains the best YOLOv8 model, `best.pt`, obtained after training on a custom dataset.

- **Documentation:**
  - This directory holds documentation for Task 2, covering introduction, requirements, and analysis, proposed method and workflow, implementation, conclusion and future enhancements, and references.

- **Input:**
  - Input directory for storing relevant input data, including images and videos used in Task 1 and Task 2.

- **Output:**
  - Output directory for storing generated images and videos from Task 1 and Task 2.

- **Results:**
  - Results directory for storing model results such as confusion matrix, graph results, validation results, etc.

## Files

- **README.md:**
  - This file provides an overview of the project, directory structure, and instructions for using the scripts.

- **Task1-Object_Detection.py:**
  - Python script for detecting airplanes in images using YOLOv8. Outputs will be stored in the Output directory.

- **Task2-Dassault_Rafale_Detection_Analinear.ipynb:**
  - Main Google Colab notebook file for Dassault Rafale detection. Covers the entire process from data collection to model testing.

- **Task2-Testing_unseen_image.py:**
  - Python script for testing the best-trained model on unseen images. Outputs will be stored in the Output directory.

- **Task2-Testing_with_video_object_tracking-centroid_movement_pattern.py:**
  - Python script for testing the best-trained model with video and applying movement patterns using centroid tracking. Outputs will be stored in the Output directory.

- **Task2-Testing_with_video_object_tracking_.py:**
  - Python script for testing the best-trained model with general video object tracking. Outputs will be stored in the Output directory.

- **yolov8m.pt:**
  - This model file was created by Task1-Object_Detection.py for detecting airplanes in an image.

## Usage

2. **Task1-Object_Detection.py:**
   - Execute this script for detecting airplanes in images. It will load an image from the input directory and detect objects in an image using `yolov8m.pt`.

3. **Task2-Dassault_Rafale_Detection_Analinear.ipynb:**
   - Open and run this Google Colab notebook for implementation of Dassault Rafale detection on the custom dataset.

4. **Task2-Testing_unseen_image.py:**
   - Run this script to test the best-trained model `best.pt` on unseen images.
     
5. **Task2-Testing_with_video_object_tracking_.py:**
   - Execute this script to test the best-trained model `best.pt` with general video object tracking.

6. **Task2-Testing_with_video_object_tracking-centroid_movement_pattern.py:**
   - Use this script to test the best-trained model `best.pt` with video and apply movement patterns using centroid tracking.



Feel free to explore the documentation, scripts, and results to gain insights into the workflow and performance of the model.
