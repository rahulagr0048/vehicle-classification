# vehicle-classification
Classify vehicles in images from GTA-5
# STEP 1: Clone
1.a) Clone the repository in your local computer<br />
1.b) Add test folder in the vehicle-classification folder<br />
# STEP 2: Setup environment
2.a) Change directory to the vehicle-classification folder in command line<br />
2.b) Run the command<br />
```pip install -r requirements.txt```
# STEP 3: Classify images
3.a) Run classify.py 

<b>The required .csv file should be generated in the test folder.</b><br />

# Program structure
1) change_folder_struc.ipynb changes the structure of training data folder to subfolders '0', '1', and '2' which contains images of the respective folder names (labels) <br/>
2) train.ipynb loads the training data, trains the CNN model and saves it to saved_model <br/>
3) classify.py loads the saved CNN model, and classifies images in test data <br/>

Alternates folder contains the code of other methods that were tried. </br>

