# Gesture IO
 _4th year Gesture Based UI Development project. This project uses machine learning and neural networks to allow users to perform certain actions by with specific gestures. This project utilises the device's webcam and captures a gesture performed by the user. This gesture is then processed and given as an input to a neural network, trained using our own gestures. If the model recognises the gesture performed, an action tied to that gesture will then be performed (such as opening a URL or opening a program on the device.)_
<div style="text-align:absolute"><img src="https://github.com/cormacmchale/SignWriter/blob/master/images/ef6e61f1-aa83-4aa1-880b-c93a8769a931_200x200.png" /></div>

### Developers
* Cormac McHale.
* Kevin Niland.

### Development
* **Language:** Python.
* **Using:** Computers.

## How it works
<div style="text-align:center"><img src="https://github.com/cormacmchale/SignWriter/blob/master/images/project_flow_diagram.PNG" /></div>

 ## Project Layout
 This project contains two distinct "parts" that both work together:
 * **Model**: The model has been trained using our own gestures. The model was trained in a very similar way to how we trained a model to recognise hand-written digits using the MNIST dataset ([Cormac McHale - Neural Network Project](https://github.com/cormacmchale/KerasNeuralNetwork), [Kevin Niland - Neural Network Project](https://github.com/kevinniland97/Recognition-of-hand-written-digits-using-the-MNIST-dataset)). The gestures used to train the model were performed mainly by Cormac. Currently, there are three gestures the user can perform: open hand, a peace sign, and a fist. To get an idea of how well the gesture recognition works, we gathered some data from other participants and recorded the results:
 <div style="text-align:absolute"><img src="https://github.com/cormacmchale/SignWriter/blob/master/images/table.PNG" /></div>
 
 * **Frontend**: The frontend was done using tkinter. Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. The frontend accesses the device's webcam, contains entry boxes for the user to specify what each gesture will do/open. The open hand gesture opens a URL, the peace sign gesture is unassigned as of yet, and the fist gesture will open a program on the user's device.

## Capturing the gesture
To capture a gesture performed by the user, the user must perform a gesture within the defined area of the webcam. Once performed, the image of the gesture is converted to a numpy array, at which point it is then put through the trained model. The application has been set up in a way that will remove unnecessary background noise from the image i.e. it will only capture the user's hand and ignore background items such as chairs, windows, walls, etc.

## Performing an action
Once the application has captured the gesture, processed it, and put it through the trained model, the application will then perform a certain action based on the gesture the user makes. The action in question is based on what the user enters into the textboxes provided (for example, the user can open a URL or program).

## Requirements
Several different libraries were used to develop the application. Before running the project, install the below libraries and packages first:
* OpenCV - `pip install opencv-python`.
* Keras - `pip install Keras`.
* NumPy - `pip install numpy`.
* Pillow - `pip install Pillow`.
* Tkinter (Should already come pre-installed if you are using Python 3).

## How to run
1. Download or clone the project repo using `git clone https://github.com/cormacmchale/GestureIO`.
2. To run the application, use `python .\MainApp.py` from the root of the project.

## Issues
Throughout the development of the project, we kept track of any design decisions, development decisions, and issues we encountered using the __Issues__ tab of the this repository. Below are links to each issue, where a more detailed desciption of each is provided:
#### Closed Issues
The below issues have been closed and are considered finished/fully implemented in the context of the application:
* [Gesture Ideas](https://github.com/cormacmchale/GestureIO/issues/10) - Here we discussed what gestures we decided to go with and what each gesture does in the context of the application.
* [GUI - Webcam and UI](https://github.com/cormacmchale/GestureIO/issues/9) - Here we discussed the GUI itself and how the user interacts with it.
* [GUI Design](https://github.com/cormacmchale/GestureIO/issues/8) - Here we discussed the design of the GUI and how it came about.
* [Building the dataset](https://github.com/cormacmchale/GestureIO/issues/7) - Here we discussed the building of the dataset, where we used our own gestures, and how it was used to train the model that gestures the user performs will be compared against.
* [Extracting an object from an image](https://github.com/cormacmchale/GestureIO/issues/6) - To enable us to develop an accurate gesture recognition application, we had to find a way to extract a particular object from an image.
* [Accessing the webcam](https://github.com/cormacmchale/GestureIO/issues/5) - Accessing the webcam is one of the main aspects of the application, the specifics of which are discussed here.
* [Accessing the typing functionality on a machine](https://github.com/cormacmchale/GestureIO/issues/4) - We briefly discussed the possibility of accessing the typing functionality of the user's device, however, it was decided that this functionality wouldn't be included in the application.
* [Gesture recognition](https://github.com/cormacmchale/GestureIO/issues/3) - How the application attempts to recognise a gesture is discussed here.
* [Finding an appropriate development environment](https://github.com/cormacmchale/GestureIO/issues/1) - Here we briefly discussed the hardware, language, and IDE we used to develop the application.

#### Open Issues
The below issues are open and are considered as possible features to be implemented in future versions of the application:
* [Building an executable](https://github.com/cormacmchale/GestureIO/issues/12) - We intended to have the entire application as an executable, however, we ran into problems in trying to do that.
* [Building the app](https://github.com/cormacmchale/GestureIO/issues/2) - General discussion on building the application.

## Conclusion (Cormac McHale)
I had the most fun during the project while designing the dataset required to train the model and as such spent most of my time doing/thinking about this. In my admittedly limited experience (From my research it seems anything below post-graduate only scratches the surface) I have come to the conclusion that pre-processing and organization of the data is the thing that allows for the most creativity while building AI based Gesture recognition software in the context of being a developer. What Neural Networks do esentially is try to approximate the most correct output for an input vector it has never encountered before.... Back propogation, perceptrons and all of the calculus that will adjust the weights and biases was developed a long time ago by very intelligent people, you don't have the option to try and change it, I definitely didn't anyway. The hardware that collects the raw data is designed by engineers that may have never considered a Neural Network as a possible recipient of the generated data, I found that my job as a software devloper was to bridge the gap inbetween these two components as [effectively as possible](https://github.com/cormacmchale/GestureIO/issues/7). My feelings on this now is that if you are trained as a software developer on a team building something similar then this is where you would be most effective. While researching the project I was also very surprised to find that many people who adopted the same approach we had to recognizing a gesture based input had built similar applications. See [here](https://github.com/cormacmchale/GestureIO/tree/master/gesturepdf). Finally one thing that became very obvious to me while building the project is the unimaginable amount of processing operations that a computer can perform on image data in a short space of time. To the point where I've realised there was times in the past where I've worried about how other solutions in projects I've done might affect the speed of the program even though I'm certain now thinking back I was nowhere near the limits of a modern computers capabilities. Always good to gain a better understanding of the tools you are using.

## Conclusion (Kevin Niland)
After choosing the [language and hardware to develop the application](https://github.com/cormacmchale/GestureIO/issues/1), the first action I took was to decide what [gestures](https://github.com/cormacmchale/GestureIO/issues/10) we were going to get working with the application. Initially, we had planned to have an application that would recognise hand gestures from American Sign Language (ASL), however we decided it best to first get simple hand gestures working first. The hand gestures I went with in the end were an open hand gesture,  peace sign gesture, and fist gesture. I decided on these as these are significantly different from each other and relatively simple gestures to perform, which would make the job of training the model easier. After the model was trained and was able to predict a gesture, the frontend was then designed and implemented. The [frontend](https://github.com/cormacmchale/GestureIO/issues/9) was inspired by [Myo Connect's Keyboard Mapper interface](https://support.getmyo.com/hc/en-us/articles/204660665-Using-the-Keyboard-Mapper-in-Myo-Connect), where each of the gestures is presented to the user. Each gesture performs a specific action such as opening a URL or opening an application the user's device. Accompanying this, the device's webcam is also displayed within the application window. Within the window, there is a designated area where the user performs a gesture. 
