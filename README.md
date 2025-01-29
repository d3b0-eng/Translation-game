# Translation-game
This web app built with python and streamlit allows the user to translate french to italian words and viceversa. The dataset of the words are contained in a `.csv` file, and the user can add new ones to the dataset from the *Add word* page. 
In the homepage, the user must first select the number of words to translate. The script then selects randomly from the main dataset the equivalent number of words chosen by the user.
The user can then check if the translation provided by him is correct or worng, and a score is provided, according to how many correct guesses the user did. 

## How to run the code
At the moment, I have not deployed the app, so it can be run just locally on your machine following these steps
### 1. Install dependencies
Open your terminal and install the dependencies
```console
pip install streamlit
pip install streamlit-lottie
```
### 2. Create the folder and the subfolders
Create a folder for your main workspace. Inside it, create the assets and pages folder. The assets folder is used to store the animations files and the csv file. The pages folder contains the streamlit pages that can be accessed from the homepage through the navigation bar
### 3. Run the Hompeage.py script
Open the folder where your Homepage file is located on the terminal, then run the script 
```console
streamlit run Homepage.py
```
