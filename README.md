# My-friendly-K-neighbor-not-spider-man-with-MNIST
Hello New Yorker, how are you doing dude? :grin:

Because of the pandemic and my school is close right now so this might be a good time for me to dig in something I've always been interested.
And here in this repository, the ***first images (hand-written digits) recognization model*** I have built using a real famous dataset 
namely MNIST created by god of computor vision,Yann LeCun.

## SO...:speaker:
This repository is the first one about machine learning in my github but it's not like this is my first experience.
I just don't have time :laughing: (still, I am a noive after all)

This time I focus on classification task using K-nerarest neighbors algorithm (via sklearn) to build a model that can predict hand-written digit images
In the notebook files:
- the **"building_knn.ipynb"** is simply how I build the Knn model as well as select the best set of hyperparameters that make my model has the best generalization ability.
  - note: I didn't use GridSearchCV to find the hyperparameters because I tried and It took over 2 hours to finish. I just did it manually but you can try  :satisfied:
- in **"knnwithaugmentation.ipynb"**, I added a litle bit of technique called "data augmentation" to the training set (specifically specking, the by 1 pixel shifted images)
  to see if it can help me improve the generalization ability of knn model
  
# Actually, this is an exercise in the textbook I'm reading... :book:
Well, since my school is close right now, I want to use the time to further my knowledege. 
Afer searching for a while, I've come across the book named [Hands-On Machine Learning](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) authored by Aurélien Géron.
And undoubtedly this is one of the great books for sure, you guys better check it out

## Packages :package:
The code is entirely written in Python 3.8.8 and the main packages I utilized are:
- numpy
- scipy
- matplotlib
- sklearn


