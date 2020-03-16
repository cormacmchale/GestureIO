# Gesture IO
 _4th year Gesture Based UI Development project. This project uses machine learning and neural networks to allow users to perform certain actions by with specific gestures. This project utilises the device's webcam and captures a gesture performed by the user. This gesture is then processed and compared against a model, trained using our own gestures. If the model recognises a gesture performed, an action tied to that gesture will then be performed (such as opening a URL or opening a program on the device._
<div style="text-align:absolute"><img src="https://github.com/cormacmchale/SignWriter/blob/master/images/ef6e61f1-aa83-4aa1-880b-c93a8769a931_200x200.png" /></div>

### Developers
* Cormac McHale
* Kevin Niland

### Development
* **Language:** Python
* **Using:** Computers

## How it works
<div style="text-align:center"><img src="https://github.com/cormacmchale/SignWriter/blob/master/images/project_flow_diagram.PNG" /></div>

 ## Project Layout
 This project contains two distinct "parts" that both work together:
 * **Model**: The model has been trained using our own gestures. The model was trained in a very similar way to how we trained a model to recognise hand-written digits using the MNIST dataset ([Cormac McHale - Neural Network Project](https://github.com/cormacmchale/KerasNeuralNetwork), [Kevin Niland - Neural Network Project](https://github.com/kevinniland97/Recognition-of-hand-written-digits-using-the-MNIST-dataset)). The gestures used to train the model were performed mainly by Cormac. Currently, there are three gestures the user can perform: open hand, a peace sign, and a fist. To get an idea of how well the gesture recognition works, we gathered some data from other participants and recorded the results:
 <div style="text-align:absolute"><img src="https://github.com/cormacmchale/SignWriter/blob/master/images/table.png" /></div>
 
 * **Frontend**: The frontend was done using tkinter. Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. The frontend accesses the device's webcam, contains entry boxes for the user to specify what each gesture will do/open. The open hand gesture opens a URL, the peace sign gesture will ..., and the fist gesture will open a program on the user's device.

## Capturing the gesture
