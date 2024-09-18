# ECE2112 - Experiment 3: Python Data Analysis

This repository contains the code and solutions for **Experiment 3: Python Data Analysis**, part of my Programming Assignment 3. The tasks involve loading data, performing subsetting, slicing, and indexing operations using **Pandas**.

## Problem Descriptions

### Problem 1: Loading and Displaying Data
**File**: `Surname_Pandas-P1.py`

#### Tasks:
1. **Load Data**: Load the `cars.csv` file into a pandas DataFrame named `cars`.
2. **Display Data**: 
   - Show the first five rows of the DataFrame.
   - Show the last five rows of the DataFrame.

#### Sample Code:
```python
import pandas as pd

# Load the .csv file into a DataFrame
cars = pd.read_csv('cars.csv')

# Display the first five rows
cars.head()

# Display the last five rows
cars.tail()

```
This section outlines the solution for **Problem 2** of **Experiment 3: Python Data Analysis**, part of my Programming Assignment 3. In this problem, I perform various data extraction and manipulation tasks using **Pandas**.

## Problem 2: Data Extraction and Manipulation

**File**: `Surname_Pandas-P2.py`

In this task, I use the `cars` DataFrame from Problem 1 to perform subsetting, slicing, and indexing operations.

### Tasks:

1. **Extract Odd-Numbered Columns**:
   - Display the first five rows but only for the odd-numbered columns (columns 1, 3, 5, 7, etc.).

2. **Find Specific Car Models**:
   - Display the row that contains the `Model` of "Mazda RX4".

3. **Car Model Specifications**:
   - Determine how many cylinders (`cyl`) the car model "Camaro Z28" has.

4. **Multiple Car Models**:
   - For the car models "Mazda RX4 Wag", "Ford Pantera L", and "Honda Civic", determine the number of cylinders (`cyl`) and the gear type (`gear`).

---

### Sample Code:
```python
import pandas as pd

# Load the DataFrame
cars = pd.read_csv('cars.csv')

# 1. Extract odd-numbered columns and display the first five rows
cars.iloc[:, 1::2].head()

# 2. Find the row containing the 'Model' of Mazda RX4
cars.loc[cars['Model'] == 'Mazda RX4']

# 3. How many cylinders does the 'Camaro Z28' have?
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]

# 4. Determine cylinders and gear type for specific car models
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
```

This section provides instructions on how to save your Jupyter Notebook as a `.py` file.

## How to Save Your Jupyter Notebook as a `.py` File

Once you’ve completed your coding in Jupyter Notebook, you can export the notebook as an executable Python file (`.py`). Follow the steps below to save your work properly:

### Steps to Save the File:

1. **Open the Jupyter Notebook Interface**:
   - Ensure you are working within the Jupyter Notebook interface where your code is written.

2. **Click on the "File" Menu**:
   - At the top-left corner of the interface, click on the `File` menu.

3. **Select "Save and Export Notebook As"**:
   - In the dropdown menu, look for and click on the option labeled `Save and Export Notebook As`.

4. **Choose "Executable Script"**:
   - From the options presented, choose `Executable Script`. This will allow you to save your notebook as a Python `.py` script.

5. **Save the File**:
   - After selecting `Executable Script`, choose the desired location on your system and give the file a name with the `.py` extension (e.g., `Surname_Pandas-P1.py` or `Surname_Pandas-P2.py`).
   - Ensure that the file name follows the naming convention as specified in the experiment, for example:
     - Problem 1: `Surname_Pandas-P1.py`
     - Problem 2: `Surname_Pandas-P2.py`

---

### Example for Problem 1 and Problem 2:

- **For Problem 1**:
   - After completing the coding for loading and displaying data, save the file as `Surname_Pandas-P1.py`.

- **For Problem 2**:
   - After writing the code for data extraction and manipulation, save the file as `Surname_Pandas-P2.py`.

---

### Why Save as `.py`?

- Saving the notebook as a `.py` file allows for:
   - **Reusability**: You can execute the script outside of the Jupyter environment using a standard Python interpreter.
   - **Version Control**: Python files are easier to track with version control systems like Git.
   - **Cleaner Structure**: `.py` files focus on the core code, omitting additional metadata associated with Jupyter Notebooks.

---

Additional Info:)
For Problem 2, I used both .loc and .iloc in test cases. I found .loc to be more convenient since it allows me to reference column names directly instead of relying on column indices.

You can view all code outputs in the PA3-Codes.ipynb file for more clarity
If you have any questions or need further assistance on how to export your Jupyter notebook, feel free to reach out!
