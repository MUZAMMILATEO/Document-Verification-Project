# 📄 Document Verification Project

A machine learning pipeline for automated document verification, MLOps integration, and cloud deployment.

---

## 📦 Setup Requirements

- [Install Anaconda](https://www.anaconda.com/)
- [Download Visual Studio Code (VS Code)](https://code.visualstudio.com/download)
- [Install Git Bash](https://git-scm.com/)
- [Flowchart Tool (Whimsical)](https://whimsical.com/)
- [MLOps Monitoring Tool (Evidently AI)](https://www.evidentlyai.com/)
- [MongoDB Cloud Account](https://account.mongodb.com/account/login)
- [Dataset (EasyVisa)](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)

> 🔗 **MongoDB Connection Template:**
> ```bash
> mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
> ```

---

## 🛠️ Git Workflow

```bash
git add .
git commit -m "Updated"
git push origin main
```

## 🚀 How to Run the Project
1. Create a new Conda environment:
```bash
conda create -n visa python=3.8 -y
```

2. Activate the environment:
```bash
conda activate visa
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🏗️ Project Workflow Structure

```
- constants/
- entity/
- components/
- pipeline/
- main.py
```

## 🌐 Environment Variables
Before running, set the following:

```bash
export AWS_ACCESS_KEY_ID=<your_aws_access_key_id>
export AWS_SECRET_ACCESS_KEY=<your_aws_secret_access_key>
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
```

## 🚀 AWS CI/CD Deployment with GitHub Actions
### 1. Login to AWS Console
---
### 2. Create an IAM User for Deployment
Required Access:
```EC2: Virtual machines.
ECR: Elastic Container Registry for Docker images.
```
Description: About the deployment
```
1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2
```
Attach Policies:
```
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
```
---
### 3. Create an ECR Repository
```
Repository URI: <your_repository_uri>
```
---
### 4. Launch an EC2 Instance
- **Operating System:** Ubuntu

---

### 5. Install Docker on EC2

```bash
# (Optional) Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y
```

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

```bash
# Configure Docker Permissions
sudo usermod -aG docker ubuntu
newgrp docker
```
---

## 6. Configure EC2 as a Self-Hosted Runner

1. Go to GitHub: **Settings → Actions → Runners → New Self-Hosted Runner**  
2. Choose **Ubuntu** and follow the on-screen instructions.
---
## 7. Setup GitHub Secrets
```bash
- `AWS_ACCESS_KEY_ID`  
- `AWS_SECRET_ACCESS_KEY`  
- `AWS_DEFAULT_REGION`  
- `ECR_REPO`
```

## 📈 CI/CD Workflow Overview

1. Build a Docker image from the source code.  
2. Push the Docker image to the AWS ECR.  
3. Launch an EC2 instance.  
4. Pull the Docker image from ECR inside the EC2.  
5. Run the Docker container on EC2.

---

## 📫 Contact

For questions, feedback, or collaboration, feel free to reach out to **Muzammil Khan** at [m.khan@utwente.nl](mailto:m.khan@utwente.nl) — I’d love to hear from you!  

