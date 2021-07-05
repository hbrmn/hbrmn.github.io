---
title: 'NMR data processing with ssNake'
date: 2021-06-28
permalink: /posts/2021/08/2021-06-28-ssnake-howto/
  - NMR
  - processing
  - how-to
---

Below you can find how to install and use (ssNake)[https://www.ru.nl/science/magneticresonance/software/ssnake/], for the processing and analysis of NMR data.

# Installation

## Windows - Standalone

You can obtain ssNake through this (link)[https://www.ru.nl/publish/pages/914099/ssnake_v1_3_installer_windows.zip]. The installation is straightforward and will leave you with an executable to directly launch the software.

## Linux / Python source code

In order to run ssNake on Linux or on any other operating system with a present Python 3 installation, you can directly (download)[https://github.com/smeerten/ssnake/archive/refs/heads/master.zip] its source code or use git to clone it into a new directory:

````bash
mkdir ssNakeDir #This line is optional
git clone https://github.com/smeerten/ssnake.git ssNakeDir

(or simply)

git clone https://github.com/smeerten/ssnake.git

````
After downloading you can simply navigate to "src" folder inside the installation folder and execute ssNake.py with Python:

```Bash
python3 ssNakeDir/src/ssnake.py
```

# Fitting 

After you are satisfied with the processing of your dataset you can try to fit the spectrum using a number of built-in functions:

 - Lorentian/Gaussian 
 - CSA
 - Quadrupole
 - Quadrupole + CSA
 - Czjzek
 - Czjzek MQMAS
 - External (SIMPSON)
 - Function

In the following the general fitting procedure is demonstrated on a few example datasets.

# Lorentzian / Gaussian Fitting

Open up the dataset

# Czjzek Fitting

Open up the dataset Czjezk_example. Since this data has already been processed in Topspin, we need to only perform a few and sometimes optional steps. First, we do a baseline correction of the dataset (Tools ---> Baseline correction), and secondly normalize (Matrix ---> Normalize) the spectrum in order to keep the integral values of the fit components in managable sizes.

Once this is done we choose the Czjzek fitting option in the Fitting dropdown menu:



A number of advanced tutorials can be found (here)[https://github.com/smeerten/ssnake_tutorials].

