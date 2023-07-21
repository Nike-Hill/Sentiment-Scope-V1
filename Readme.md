# Sentiment Scope Project

## About the Team:
Our team consisted of one amazing instructor and six other members. There were a variety of responsibilities to manage during this project, so we chose the roles that played with our strengths. The tasks ranged from processing our data before it was trained to training the model to incorporating our model onto the final site. 

- Priyansh → instructor 

- Pingyao Liu → Website Creation, Training 

- Lionel Humphreys → Training, Backend

- Owen Humphreys → Backend, Training

- Enyinnaya Ukairo → Preprocessing, 

- [Nikhil Venkat](www.nikhilvenkat.space) → Final Model Training, Design, Data Collection, and Design

- Kayden Walton → Website Creation, Preprocessing

## How To Use The Project:
There is no need to install anything! Simply nagivate to the Sentiment Scope tab on the top right corner and enter your short message to analyze. The result should be displayed shortly! 

### Templates
This Folder contains all the HTML pages for the project. 
- index.html is the main landing page for the website
- aboutus.html is the about us page
- model.html is the page with a sample of the model and where the models' output displays
- error.html is the error page, which appears automatically when an error occurs
- ans.html is a no longer used file that used to contain the display for the model's output

### Main.py, bargraph.py, and utils.py
These files contain the information for the Flask code for the website, as well as the code to access Sentiment Scope's api and display a bargraph containing it's predictions. Bargraph.py is only called when creating and displaying the bargraph.
Utils.py contains basic Flask code for setting up the website

### Static 
This folder contains all the CSS and Javascript information for the project, as well as all images and assets used in the website.
It also contains the graph.html file which stores the graph currently being displayed by Sentiment Scope's sample output.

## Technical Stack: 
The creation of the site used Flask, along with HTML, CSS, and Javascript. 

## Dataset: 
The original dataset, called Emotion Detection from Text, was downloaded from Kaggle. <br><br>
[Link to dataset](https://www.kaggle.com/datasets/pashupatigupta/emotion-detection-from-text)

## Model Details:
Our model was trained with the dataset above and the model Seethal/sentiment_analysis_generic_dataset on huggingface. 

## Libraries Used:
Through our website, we used the following libraries:
- Flask
- Requests
- Bargraph
- Plotly
- Pandas
- Json
- Os
