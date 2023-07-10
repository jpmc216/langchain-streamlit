# Steps to run the application 

## To run the application on local machine (clone the repo)

* Download the github repo using the below command 
`git clone https://github.com/jpmc216/langchain-streamlit.git`

### To run the application using container
#### 1. To start the application 
`docker-compose up -d`

#### 2. To stop the application 
`docker-compose down`

### To run the stand-alone application (Python Version >=3.9) 

#### 1. Change directory into `streamlit`
`cd streamlit`

### 2. Run the below command to install required packages
`pip install -r requirements.txt`

### 3. Run the below command to start the application (This command will automatically open the application in a new browser tab/window)
`streamlit run Home.py`


## To run the application on GITPOD instance 

### Pre-Requisites
* Open Chrome Browser, click this URL [GITPOD](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki) and install gitpod chrome plugin.
* If you have not used gitpod before, you may need to setup an account by clicking [here](https://gitpod.io/login/) and give permissions to access your github/gitlab/bitbucket account.
  
### Steps
* Open the source code [repo](https://github.com/jpmc216/langchain-streamlit/) either on the same/new chrome tab/window. 
* You should see the GITPOD button like this ![image](https://github.com/jpmc216/langchain-streamlit/assets/14977933/482cd914-8853-4bef-9820-3464d47a749f) 
* Click on Gitpod button to open the repo on gitpod infrastructure. This will open a VS Code like IDE inside a browser.
* A start up script is created (.gitpod.yml) that will build and run the container.
* Go to "Ports" view and click the link that starts with "https://8000-" to open the app in a new browser tab/window. 
  ![image](https://github.com/jpmc216/langchain-streamlit/assets/14977933/6ae2b4c1-9124-4394-b87e-b1be06e14d09)








