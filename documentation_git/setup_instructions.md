# Setup Instructions

## Prerequisites

1. **Download VS Code**
   - [Download VS Code](https://code.visualstudio.com/Download)
   - Open the setup
   - Follow the installation instructions

   ![VS Code Download](/download_vs.png)

2. **Download Git**
   - [Download Git for Windows](https://git-scm.com/download/win)
   - Select "Clone a repository"
   - Enter the link to the backend: [https://github.com/coronasafe/ayushma.git](https://github.com/coronasafe/ayushma.git)
   - **OR** download the `backend_ay` folder from the drive and continue.

3. **Download a Remote Server (WSL - Ubuntu)**
   - [WSL Tutorial](https://code.visualstudio.com/docs/remote/wsl-tutorial)
   - Follow the instructions to install WSL
   - Open a remote server
 

4. **Enable Windows Subsystem for Linux**
   - Search for "Turn Windows features on or off"
   - Select "Windows Subsystem for Linux" and turn it on
   - Restart the computer when prompted
   - Add the distro (Ubuntu) and install it
   - Launch Ubuntu and set a username and password

   ![Enable WSL](/setup_remoteserver.png)
   ![Enable WSL](/setup_remoteserver1.png)
   ![Enable WSL](/setup_remoteserver2.png)
   ![Enable WSL](/setup_remoteserver3.png)
   ![Enable WSL](/setup_remoteserver4.png)
   ![Enable WSL](/setup_remoteserver5.png)
   

5. **Connect to the Distro**
   - You should see `WSL: Ubuntu`
   - Go to the `/mnt` directory to access files on Windows

   ![Connect to Distro](/setup_remoteserver5.png)

## Setting Up the Backend

1. **Open a New Folder in VS Code**
   - Select the file location in the remote server
   - Use `Ctrl + ` to open the terminal

   ![Open Folder](/backend_setup1.png)

2. **Download Docker**
   - [Download Docker](https://www.docker.com/get-started/)
   - Install using the installer
   - Continue without signing in and restart if the engine stopped
   - Make sure the Docker engine is running and restart if needed
   ![Download Docker](/backend_setup2.png)
   

3. **Install the `make` Command**
   - Install `make` using the appropriate command for your environment

   ![Install Make](/backend_setup4_make.png)
   
   

4. **Run the `make up` Command**
   - Ensure Docker is running
   - The `make` command will initiate the required installations
   - Once all dependencies are installed and containers are started, run the `make down` command to stop all containers

   ![Run Docer](/backend_setup3.png)
   ![Install Make](/backend_setup4_make2.png)

5. **Set Environment Variables**
   - In the `ayushma/.envs/.local/django` file, append the following:
     ```ini
     AI_NAME="Your api"
     OPENAI_API_KEY=sk-3axxxxxxxxxlOG
     PINECONE_API_KEY=43xxxxxxx2
     PINECONE_ENVIRONMENT=gcp-starter
     PINECONE_INDEX=default
     CURRENT_DOMAIN=http://localhost:8000
     ```
   - Set the environment variables:
     - Find the OpenAI key:
       - Login to [OpenAI API](https://login-openai-api)
       - Go to the API-Keys section and create a new key
       - Save it to a notepad
       ![Set OPENAI](/backend_setup5_apikeys.png)
       ![Set OPENAI](/backend_setup5_apikeys2.png)
     - Login to [Pinecone](https://pinecone-login)
       - Go to the API-keys section and copy the default key
       - Set the environment variable
     - Store these keys in the variable and set the Pinecone index and environment according to the index available in the Pinecone page
     ![Set OPENAI](/backend_setup5_apikeys3.png)
   - Run the `make up` command

   

## Setting Up the Frontend

1. **Install Node.js**
   - [Download Node.js](https://nodejs.org/en/download)

2. **Install Yarn**
   - Run the command:
     ```sh
     npm install --global yarn
     ```
   - Once Yarn is installed, run:
     ```sh
     yarn dev
     ```
   - If issues arise, try changing the execution policy from Restricted

   ![Install Yarn](/backend_setup6_yarn.png)

## Adding a Superuser

1. **Access the Entrypoint File**
   - Run the command:
     ```sh
     docker exec -it ayushma-django-1 /entrypoint bash
     ```
   - This accesses the entrypoint file where you can add the superuser

   ![Access Entrypoint](/backend_setup7_superser.png)

2. **Create the Superuser**
   - Run the command:
     ```sh
     python manage.py createsuperuser
     ```
   - Enter the credentials


3. **Add a New Project in the Admin Panel**
   - Go to `localhost:8000/admin`
   - Add a new project with a prompt
   - Fill in all required details

   ![Add New Project](/backend_setup8_project.png)

4. **Set the Project as Default**
   - Select the "is default" option


## Login to the Application

1. **Go to `localhost:3000` for Login**
   - Login with the credentials:
     - Email: `arghyam@arghyam.org`
     - Password: `arghyam`

   ![Login Page](path/to/images/LoginPage.png)

2. **Setup a Local Server (if needed)**
   - Change the URL from `localhost:8000` to `https://ipv4address:8000` in the backend and frontend
