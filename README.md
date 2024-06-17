![](https://github.com/Bikram-Sankhari/Social-Network-API/blob/main/Logo.png?raw=true)
# A Collection of Social Networking APIs

![](https://img.shields.io/badge/Python-3.12-green) ![](https://img.shields.io/badge/Django-5.0-blue) ![](https://img.shields.io/badge/DRF-3.15-red)

 Watch them in action at - https://youtu.be/YbyxrlfNy3c

## Table of Contents
  * [Usage](#usage)
    + [Sign Up a New User](#sign-up-a-new-user)
    + [Log a User In](#log-a-user-in)
    + [Log a User Out](#-log-a-user-out)
    + [Search Users](#-search-users)
    + [Send Friend Request](#-send-friend-request)
    + [Accept Friend Request](#-accept-friend-request)
    + [Reject Friend Request](#-reject-friend-request)
    + [List All Friends](#-list-all-friends)
    + [List All Pending Friend Requests](#-list-all-pending-friend-requests)
  * [Installation Guide](#installation-guide)
    + [Windows Setup](#windows-setup)
      - [1. Make a clone of this repo at your preferred location](#1-make-a-clone-of-this-repo-at-your-preferred-location)
      - [2. Open the just cloned "Social-Network-API" directory in terminal](#2-open-the-just-cloned-social-network-api--directory-in-terminal)
      - [3. Create a Virtual Environment](#3-create-a-virtual-environment)
      - [4. Activate the Virtual Evironment](#4-activate-the-virtual-evironment)
      - [5. Install the required packages](#5-install-the-required-packages)
      - [6. Create necessary tables in the Database](#6-create-necessary-tables-in-the-database)
      - [7. Good to go. Run the server](#7-good-to-go-run-the-server)
    + [Linux Setup](#linux-setup)
      - [1. Go to your Home Directory](#1-go-to-your-home-directory)
      - [2. Clone the repository](#2-clone-the-repository)
      - [3. Change working Directory to the newly cloned "Social-Network-API" Directory in terminal](#3-change-working-directory-to-the-newly-cloned-social-network-api-directory-in-terminal)
      - [4. Create a Virtual Environment](#4-create-a-virtual-environment)
      - [5. Activate the Virtual Environment](#5-activate-the-virtual-environment)
      - [6. Install the required packages](#6-install-the-required-packages)
      - [7. Enable 8000 port](#7-enable-8000-port)
      - [8. Create necessary tables in the Database](#8-create-necessary-tables-in-the-database)
      - [9. Good to go. Run the server](#9-good-to-go-run-the-server)
  * [Open Issues](#open-issues)
  * [Want to Contribute?](#want-to-contribute)
    + [1. Create a Fork of this Repository](#1-create-a-fork-of-this-repository)
    + [2. Clone Your Fork](#2-clone-your-fork)
    + [3. Create a New Branch with a name that best describes the contribution you are about to make](#3-create-a-new-branch-with-a-name-that-best-describes-the-contribution-you-are-about-to-make)
    + [4. Now you can work on your new Branch](#4-now-you-can-work-on-your-new-branch)
    + [5. Commit the changes in your new Branch and push the code to your Forked Repository](#5-commit-the-changes-in-your-new-branch-and-push-the-code-to-your-forked-repository)
    + [6. Give a Pull request to this Upstream Repo](#6-give-a-pull-request-to-this-upstream-repo)
  * [Found a BUG 🐞 ??](#found-a-bug--)


## Usage
- <h3>Sign Up a New User</h3>
   Endoint: /register/

   Request Method: POST
   
   Data Required: "email", "password"

- <h3>Log a User In</h3>
   Endoint: /login/

   Request Method: POST
   
   Data Required: "email", "password"

  
- <h3>(*) Log a User Out</h3>
   Endoint: /logout/

   Request Method: POST
   
   Data Required: NULL

- <h3>(*) Search Users</h3>
   Endoint: /search/

   Request Method: GET
   
   Data Required: "q"


- <h3>(*) Send Friend Request</h3>
   Endoint: /send/

   Request Method: GET
   
   Data Required: "id"

- <h3>(*) Accept Friend Request</h3>
   Endoint: /accept/

   Request Method: GET
   
   Data Required: "id"

- <h3>(*) Reject Friend Request</h3>
   Endoint: /reject/

   Request Method: GET
   
   Data Required: "id"

- <h3>(*) List All Friends</h3>
   Endoint: /list_friends/

   Request Method: GET
   
   Data Required: NULL

- <h3>(*) List All Pending Friend Requests</h3>
   Endoint: /list_friend_requests/

   Request Method: GET
   
   Data Required: NULL

(*)  Indicates for Authenticated Users only
  
------------



## Installation Guide

### Prerequisites
- Python version 3.12 or higher
- Git Installed

### Windows Setup

#### 1. Make a clone of this repo at your preferred location

	git clone https://github.com/Bikram-Sankhari/Social-Network-API.git

#### 2. Open the just cloned "Social-Network-API" directory in terminal

#### 3. Create a Virtual Environment

	python -m venv env

#### 4. Activate the Virtual Evironment

	env\Scripts\activate

#### 5. Install the required packages

	pip install -r requirements.txt


#### 6. Create necessary tables in the Database

	python manage.py migrate

#### 7. Good to go. Run the server

	python manage.py runserver

## And CONGRATULATIONS You can now test the APIs on your localhost (127.0.0.1:8000) !!!!! 🥳

------------

### Linux Setup

#### 1. Go to your Home Directory
- Open Terminal by pressing CTRL + ALT + T

- Change working directory to your home directory

	  cd ~

#### 2. Clone the repository

	git clone https://github.com/Bikram-Sankhari/Social-Network-API.git

#### 3. Change working Directory to the newly cloned "Social-Network-API" Directory in terminal


	cd Social-Network-API/

#### 4. Create a Virtual Environment

	python3 -m venv env

#### 5. Activate the Virtual Environment

	source env/bin/activate

#### 6. Install the required packages

	pip install -r requirements.txt


#### 7. Enable 8000 port
- Install 'ufw' package to enable 8000 port

	  sudo apt install ufw

- Enable 8000 port

	  sudo ufw allow 8000


#### 8. Create necessary tables in the Database

	python3 manage.py migrate

#### 9. Good to go. Run the server

	python3 manage.py runserver

## And CONGRATULATIONS You can now test the APIs on your localhost (127.0.0.1:8000) !!!!! 🥳
------------

## Open Issues

### 1. Sending/Accepting/Rejecting friend request should be done over POST requests instead of GET
> As these operatiions make changes in the Database, they should be done over a POST request. But as they require the user to be authenticated, everytime you will need to obtain a CSRF token from another endpoint and include it in the Header of the POST request, which will make the APIs a little bit complex. So to keep the things simple I have implemented them in this way.

------------

## Want to Contribute? 
All contributions are Welcome. If you want to contribute to this project follow the steps.

### 1. Create a Fork of this Repository
See [GitHub Documentation for Forks](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

### 2. Clone Your Fork


	git clone <URL TO YOUR FORK>

### 3. Create a New Branch with a name that best describes the contribution you are about to make


	git checkout -b <YOUR BRANCH NAME>

### 4. Now you can work on your new Branch
> After making the changes, Test your code well before committing

### 5. Commit the changes in your new Branch and push the code to your Forked Repository

See [This Documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

### 6. Give a Pull request to this Upstream Repo
See [The GitHub Documentation on Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
> Be Descriptive about the Contribution you have made

------------


## Found a BUG 🐞 ??
As this Application is in the very early stage of it&apos;s development lifecycle, it is anticipated that there are some bugs in the code. So if you find out one, then Please -
Let me know directly by Email: bikramsankhari2024@gmail.com

------------
