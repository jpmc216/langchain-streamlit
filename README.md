# Steps to run the application 

## To run the application on local machine (clone the repo)

Download the github repo using the below command
  ```bash
  git clone https://github.com/jpmc216/langchain-streamlit.git
  ```
&nbsp;
### Using container
#### 1. To start the application 
  ```bash
  docker-compose up -d
  ```

#### 2. To stop the application
  ```bash
  docker-compose down
  ```

&nbsp;
### Using stand-alone application (Python Version >=3.9) 

#### 1. Change directory into `streamlit`
  ```bash
  cd streamlit
  ```

#### 2. Run the below command to install required packages
```bash
pip install -r requirements.txt
```

#### 3. Run the below command to start the application (This command will automatically open the application in a new browser tab/window)
```bash
streamlit run Home.py
```


&nbsp;&nbsp;
## To run the application on GITPOD instance 

### Pre-Requisites
* Open Chrome Browser, click this URL [GITPOD](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki) and install gitpod chrome plugin.
* If you have not used gitpod before, you may need to setup an account by clicking [here](https://gitpod.io/login/) and give permissions to access your github/gitlab/bitbucket account.
  
### Steps
> 1. Open the source code [repo](https://github.com/jpmc216/langchain-streamlit/) either on the same/new chrome tab/window.

> 2. You should see the GITPOD button like this ![image](https://github.com/jpmc216/langchain-streamlit/assets/14977933/482cd914-8853-4bef-9820-3464d47a749f)

> 3. Click on Gitpod button to open the repo on gitpod infrastructure. This will open a VS Code like IDE inside a browser.

> 4. Gitpod's start up script (.gitpod.yml) will take care of building and running the container (This will roughly take 3-4 mins).

> 5. Go to "Ports" view and click the link that starts with "https://8000-" to open the app in a new browser tab/window. 
  ![image](https://github.com/jpmc216/langchain-streamlit/assets/14977933/6ae2b4c1-9124-4394-b87e-b1be06e14d09)

> 6. If you would like to share the application URL publicly, do a right click on the "State" section and make it public
  ![image](https://github.com/jpmc216/langchain-streamlit/assets/14977933/2af75041-04bd-4413-a5d4-6a5dfb9c3c91)
  








