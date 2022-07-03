# dynamic_forms_in__Obsidian
A dynamic form/essay/letter generator based on [Obsidian](https://obsidian.md/) (which you'll need to **install** to use this tool).

**_📽📽 VIDEO OF [SIMPLE EXAMPLE](https://drive.google.com/file/d/1bAL7fB533kJPgGvDSwcS1tzJrEs7ko5a/view?usp=sharing) 📽📽_** (sorry for using GoogleDrive link, GitHub does not allow me to upload larger than 10MB files and I lack the patience to format/cut/you-get-the-point)


# STEPS

## 🛠 Installations

### 🛠🛠 Install [Obsidian](https://obsidian.md/)

[Obsidian](https://obsidian.md/) is a free, flexible note-taking tool that supports numerous capabilities. It is very "lightweight" (in terms of CPU), provides nices visualizations, connects notes with each other, runs commands and many other capabilities.

#### Community plugins

You will need to **install and enable** the following community plugins:

1. Advanced Tables

Before you do so, make sure to deactivate safe-mode, so that community plugins can be activated (safe mode ensures that no plugin deletes your note files accidentally, which rarely happens).

#### Learn the basics of Obsidian

Check the Help guide of Obsidian for that.

### 🛠🛠 Install Python

Install Python (preferably 3.7+)

#### Install Python packages

1. numpy
2. os
3. re
4. subprocess
5. genericpath
6. turtle

For help on how to install those packages, check this [link](https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing). _Install from pip_ is the quickest way to do so

## 📂 Adjust paths 

There are some paths inside the files of the project which require manual adjustment:

1. file "form_lab_deleteme1.md", change the path: "[▶ Generate](file:///...\generate_form.bat)" to "[▶ Generate](file:///your_path\generate_form.bat)"
2. in the python script, locate the "path0" variable and change it to where you place the project folder

