# Automatic Dart Detection

This project demonstrates an **Automatic Dart Detection system** using object detection models implemented on a Raspberry Pi with a Pi Camera. The system detects steel-tip darts on a cork dartboard and maps their positions for automated scoring.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Components](#software-components)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Limitations](#limitations)

---

## Introduction
The goal of this project is to create a low-cost, automated dart scoring system using machine learning. Current commercial systems, like the Prodigy Dartboard, cost upwards of $800–$1,000, while this solution achieves similar results at a fraction of the cost (around $150).

Key highlights:
- Built using the YOLOv5s object detection model for efficient dart detection.
- Runs on a **Raspberry Pi Model 3B+** with a Pi Camera Module v2.
- Detects dart locations with a confidence level of ~95%.

---

## Features
- **Object Detection**: Identifies darts and dart tips on a cork dartboard.
- **Custom Dataset**: A tailored dataset of 500+ images was created for training.
- **Affordable**: Total cost of the system is significantly lower than commercial solutions.
- **Expandable**: Provides a foundation for additional features like real-time scoring.

---

## Hardware Requirements
- Raspberry Pi Model 3B+ (or higher)
- Pi Camera Module v2 (8MP)
- Cork dartboard and steel-tip darts
- Power supply and peripherals for Raspberry Pi

---

## Software Components
1. **Model**: YOLOv5s by Ultralytics, optimized for lightweight embedded devices.
2. **Libraries**: 
   - Python 3.9.16
   - OpenCV
   - PyTorch
   - ImgLabel (for annotation and bounding box creation)
   - Picamera2 (for image capture)
3. **Scripts**: 
   - Training scripts for YOLOv5
   - Image capture and annotation tools
   - Detection scripts for testing the model on Raspberry Pi

---

## Dataset
The dataset consists of over 500 images of darts on a dartboard. Key steps include:
1. **Image Collection**: Captured images using Python-based scripts on the Raspberry Pi.
2. **Annotation**: Bounding boxes were created for full darts and dart tips using ImgLabel.
3. **Format Conversion**: XML annotations were converted to YOLOv5’s required `.txt` format.

---

## Model Training
Training was performed on a desktop computer due to the Raspberry Pi’s limited resources:
- **Metrics**: High precision and recall observed in validation metrics.
- **Challenges**: Raspberry Pi Model 3B+ had limitations in running real-time detection.

### Results:
- Darts and dart tips were detected with high accuracy, though shadows occasionally caused false positives.

---

## Limitations
### Current Limitations:
- **Performance**: Real-time detection was not feasible due to hardware limitations.
- **Detection Time**: Approximately 20 seconds per detection on Raspberry Pi Model 3B+.
