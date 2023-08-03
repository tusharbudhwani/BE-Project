**Predictal - A One-Stop Medical Solution for Early Diagnosis of Multiple Diseases**

**Project Description**

There are multiple techniques in machine learning that can do predictive analysis on a large amount of data in a variety of industries. Predictive analysis in healthcare is a difficult endeavor, but it can eventually assist practitioners in making timely decisions regarding patients’ health and treatment based on massive volume of data. In this world, a human being suffers from many diseases. Diseases can have a physical, but also a psychological impact on people. Mainly for four reason, diseases are formed: (i) infection, (ii) deficiency, (iii) heredity and (iv) body organ dysfunction. Diseases like breast cancer, diabetes, and heart-related diseases are causing many deaths globally but most of these deaths are due to lack of timely check-ups of the diseases. The above problem occurs due to lack of infrastructure and a low ratio of doctors to the population. Supporting the same, according to the World Health Organization (WHO), the ratio of doctors to patients is 1:1000 whereas in India the doctor-to-population ratio is 1:1456 indicating a shortage of doctors. These diseases can be a serious threat to mankind if not diagnosed early. Therefore, early recognition and diagnosis of these diseases can save a lot of lives. To address these life threatening issues, we aim to develop a one-stop medical solution platform for early recognition and diagnosis of various diseases like Breast cancer, Diabetes, Heart diseases, Chronic kidney diseases, Parkinson’s disease, liver diseases and prediction of disease from symptoms using the concept of Machine Learning.

**Architecture Diagram**

**Web App Landing Page**

- The home page the user is greeted with after opening the web-app. The below page explains the process through which users can generate the early diagnosis prediction of a disease.


- The user design consists of a menu list to the left of the page which consists of a list of diseases *Predictal* is currently capable of providing results to i.e. *Predictal* consists of seven prediction sub-system namely, the Diabetes Prediction system, the Heart Disease Prediction system, the Breast Cancer Disease Prediction system, the Parkinson’s Disease Prediction system, the Kidney Disease Prediction system, the Liver Disease Prediction system and the Predict Disease through Symptom system.
- The user can choose a disease from the menu which will direct him/her to its corresponding page. For example the user wants to predict if he/she has a chance of diabetes or not given their clinical parameters. In that case the user selects the “Diabetes Prediction” section from the menu. The page looks like below.


- On landing to the diabetes prediction page the user can see a small introduction about the disease and a number of input fields and labels on top of them explaining the attribute name required to be inputted. These input fields are capable of inputting only float values hence the user is expected to input their clinical parameters in the same format.
- After entering values into the required fields, the user can click on the “Diabetes Test Result” button to generate the final result. The same can be seen in the following image.

.

- The same process can be followed for each sub-system.

**Built With**

- Python
- Streamlit

**Setup and Installation**

- Download the code folder “50\_AP\_22-23”.
- The folder consists of a folder “Predictal – A One Stop Medical Solution for Early Diagnosis of Multiple Diseases”. This folder then consists of the model weights, the datasets and the main file.
- Change to the working directory.

cd “C:\Users\dell\Desktop\Predictal – A One Stop Medical Solution for Early Diagnosis of Multiple Diseases”

- Install all dependencies (preferably in a virtual env).
- Run the app in terminal.

streamlit run "C:\Users\dell\Desktop\ Predictal – A One Stop Medical Solution for Early Diagnosis of Multiple Diseases \Multiple Disease pred.py"

- Open the local host port the server is using in a browser by clicking on the link displayed in the terminal in case it does not automatically pop-up

**References**

- Multiple Disease Prediction System <https://www.irjet.net/archives/V9/i3/IRJET-V9I3312.pdf> 
- <https://docs.streamlit.io/>


