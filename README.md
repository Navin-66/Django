# Django Todo App

## Overview

This Django Todo App is a simple yet effective task management system developed using the Django web framework. It allows users to create, update, and delete tasks, helping them stay organized and productive.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Deployment to Azure](#deployment-to-azure)
  - [Azure Resource Group and Virtual Network Setup](#azure-resource-group-and-virtual-network-setup)
  - [Deploy Django App as Azure Web App](#deploy-django-app-as-azure-web-app)
  - [Integrate Azure Chatbot Service](#integrate-azure-chatbot-service)
- [Additional Resources](#additional-resources)

## Setup Instructions

### Prerequisites

- Python installed on your local machine
- Git installed on your local machine (optional)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/django-todo-app.git
   ```

   Or download the ZIP file and extract it to your desired location.

2. **Navigate to the project directory:**

   ```bash
   cd django-todo-app
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **Linux/macOS:**

     ```bash
     source venv/bin/activate
     ```

5. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The app will be accessible at `http://localhost:8000`.

## Deployment to Azure

### Azure Resource Group and Virtual Network Setup

1. **Create a new resource group in the Azure portal.**
2. **Set up a virtual network within the resource group.**

### Deploy Django App as Azure Web App

1. **Create a new web app service in the Azure portal.**
2. **Configure the web app and deploy your Django app using Git, GitHub Actions, or any preferred deployment method.**
![NAVEEN1](https://github.com/Navin-66/Django/assets/113427260/87dcd99c-bd3d-46a9-9520-fba2692fdf06)
![NAVEEN2](https://github.com/Navin-66/Django/assets/113427260/c7770caa-7d7b-442a-95cf-3568021fe346)
![NAVEEN3](https://github.com/Navin-66/Django/assets/113427260/d1b80f89-0c95-4c14-a6b4-7916f380d659)
![NAVEEN4](https://github.com/Navin-66/Django/assets/113427260/75cc4b2c-2764-4281-8738-cf6a56a88030)



### Integrate Azure Chatbot Service

1. **Create a new chatbot service in the Azure portal.**
2. **Configure the chatbot and integrate it with your Django app for task management or user interactions.**



