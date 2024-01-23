# AcousticEventsDB

A collection of acoustic recordings, made in various acoustic conditions. This project is an advanced system for simulating acoustics in different environments, such as halls, corridors, or dressing rooms, using various building materials

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Usage](#usage)
* [Additional Resources](#Additional-Resources)
* [Project Status](#project-status)






## General Information
- **Problem to Solve:** AcousticEventsDB was created to address the lack of realistic simulation tools for various acoustic environments. The project enables the assessment of the impact of different acoustic conditions - such as the geometry of rooms and the materials used - on sound quality, which is crucial in many fields, from architectural design to sound engineering.
- **Project Goal:** The main goal of AcousticEventsDB is to provide an advanced, yet easy-to-use tool for acoustic simulations. I want to enable professionals and sound enthusiasts to conduct realistic acoustic tests without the need for physical access to various environments.
- **Motivation for Undertaking the Project:** The project was initiated from my passion for acoustics, sound, and Machine Learning. Seeing a gap in the available simulation tools, I decided to create AcousticEventsDB to fill this space and combine my interests in one innovative tool.

## Technologies Used
- **Python ver. 11.7:** The programming language used to create the entire project, providing comprehensive capabilities and support for scientific and acoustic libraries.
- **Numpy:** A Python library for scientific computing, offering support for large, multi-dimensional arrays and matrices, along with a wide range of mathematical functions for operations on these arrays.
- **MatPlotLib:** A library for creating static, interactive, and animated visualizations in Python.
- **Librosa:** A library for music and audio analysis, providing tools for audio feature extraction, signal analysis, visualization, and more.
- **Pyroomacoustics:** A library specializing in acoustic simulations and sound processing in rooms.
Soundfile: A library for reading and writing sound files.

## Features
- **Simulation of various acoustic environments:** Enables the simulation of sound in various environments, such as halls, corridors, dressing rooms, using variable dimensions and materials.
- **Assessment of the impact of geometry and materials:** The system allows for the assessment of how the geometry of a room and the materials used affect the quality of sound.
- **Adding background noise at different SNR levels:** The ability to add background noise to sound simulations at different Signal-to-Noise Ratio (SNR) levels, which is useful in testing and analyzing audio devices.
- **Generating and saving sound simulations and visualizations:** The project allows for the saving of simulated sound recordings and the generation of charts and spectrograms for further analysis.
- **Multithreaded handling of file processing:** Utilizing multithreading for efficient processing of multiple sound files simultaneously.

## Screenshots


## Usage
Place the sound files in .wav format in a folder (e.g., **D:\Audio\Input\Nr.1**).
Run the script.
The simulation results, including recordings and charts, will be saved in the **D:\Audio\Output folder**.

## Additional Resources
Along with the source code of the AcousticEventsDB project, the repository also includes a folder containing special audio recordings. These recordings were made in an anechoic chamber, which ensures exceptionally clean sound quality and the absence of external acoustic disturbances. They are particularly useful for tests and simulations within the project.

**Recordings Folder**
**Location in the Repository:** The folder with these recordings can be found in the project's repository under the name Audio.
**Application:** These recordings are ideal for testing and demonstrating the simulation capabilities of the AcousticEventsDB project, offering realistic source material.

## Project Status
The project is in progress
