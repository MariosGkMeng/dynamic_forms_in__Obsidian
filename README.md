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

1. file "form_lab_deleteme1.md", change the path: "file:///...\generate_form.bat" to "file:///your_path\generate_form.bat"
2. in the python script, locate the "path0" variable and change it to where you place the project folder

It is better to have all the files in the same path, otherwise you can change:

1. The path of the python file inside the .bat file (in case the .bat file is in another folder)

## 📖 Learn

ℹ --> Check below, but also: **source_C**: comments inside the form_lab_deleteme1.md file (open Obsidian in editor mode)

### Basics of [Obsidian](https://obsidian.md/)

- Use of tags
- Editor/preview mode 
- Creating links with other notes (optional)

### Peculiarities of the tool

- Logical expressions for the "#🗝/" and "#❓/" type of variables --> check **source_C**


## ℹ 👉🏼 How it works

- The `file:table_deleteme1.md` is the one that provides the `file:form_lab_deleteme1.md` with the information regarding the **fields**. 
  - The **fields** are to be written in the format `#🔰/field_1`, `#🔰/field_2`, etc. and they are expressed as columns in the table of `file:table_deleteme1.md`
- The **fields** are then communicated to `file:form_lab_deleteme1.md`, which contains a set of rules based on those fields
- The `file:form_lab_deleteme1.md` contains the **▶ Generate** button that generates the form/letter which is dependent on those **fields**

### ➕ Create new field

**_📽📽 Check [VIDEO](https://drive.google.com/file/d/1YxXR6RZbQ_JsW2rn0oa5xB0eoEN_KzH-/view?usp=sharing) 📽📽_**



