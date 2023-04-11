---
title: 'NMR data processing with ssNake'
date: 2021-06-28
permalink: /posts/2021/08/2021-06-28-ssnake-howto/
  - NMR
  - processing
  - how-to
---

Below you can find some instructions on how to install and use [ssNake](https://www.ru.nl/science/magneticresonance/software/ssnake/), for processing and analyzing NMR data.

# Installation

## Windows - Standalone

You can obtain an executable ssNake installer through this [link](https://www.ru.nl/publish/pages/914099/ssnake_v1_3_installer_windows.zip). The installation is straightforward and will leave you with an executable to directly launch the software.

## Linux / Python source code

In order to run ssNake on Linux or on any other operating system with a present Python 3 installation, you can directly [download](https://github.com/smeerten/ssnake/archive/refs/heads/master.zip) its source code or use git to clone it into a new directory:

````bash
mkdir ssNakeDir #This line is optional
git clone https://github.com/smeerten/ssnake.git ssNakeDir

(or simply)

git clone https://github.com/smeerten/ssnake.git
````
After downloading you can simply navigate to the "src" folder inside the installation folder and execute ssNake.py with Python:

````Bash
python3 ssNakeDir/src/ssnake.py
````

# Processing data
Once ssNake's GUI is loaded, you can open a new dataset via `File --> Open` which will either display an FID (like in my case) or a spectrum, depending on whether your data was already processed before or not. In this example I loaded a ^{29}Si MAS NMR experiment on lithium disilicate measured on a Varian machine:

![Loaded FID](/images/ssNake-howto/FID_loaded.jpg "Raw FID after loading a Varian dataset.")

The most common processing functionalities are found in the Tools and Matrix tabs. For the current example I truncated the FID after 1024 points using `Matrix --> Sizing` and after applying the changes by clicking on "ok" performed a zero-filling up to 2048 points. The resulting FID looks like this:

![sized FID](/images/ssNake-howto/FID_sized.jpg "Zero-filling the FID.")

A window function can be applied via `Tools --> Apodize`. In the current example I applied roughly a Gaussian windowsfunction with roughly 100 Hz of width. Note how the window function is displayed in green and the raw FID remains as a gray shade:

![apodized FID](/images/ssNake-howto/FID_apodization.jpg "Applying a Gaussian windows function.")

Lastly, I shifted the FID six points to the left via `Matrix --> Shift Data`:

![left-shifted FID](/images/ssNake-howto/FID_leftshifted.jpg "Left-shifting the FID six points.")

By the way, you can zoom-in and -out of your data by dragging a box with your left-mouse button, drag your data around with the right-mouse button, scale your data with the mouse-wheel, and - perhaps most importantly - reset to the default view by double-right clicking.

Once we are all set we can finally Fourier-Transform the FID by clicking on the "Fourier" labeled button in the bottom-left corner of the main window, using the shortcut `Ctrl + F`, or via `Transforms --> Fourier Transform`. For my data this results in the following spectrum:

![Spectrum after FFT](/images/ssNake-howto/Spec_raw.jpg "Spectrum resulting from Fourier Transformation.")

Before continuing you might want to change the abscissa label to ppm instead of Hz. This can be done in the Axis tab below the spectrum:

![Axis Tab](/images/ssNake-howto/Spec_raw.jpg "The Axis Tab let's you choose the Units of the abscissa.")

Now it's time to correct the phase. `Tools --> Phasing -> Phase` will take you to the interactive phase correction window in which you can apply zeroth- and first-order phase correction by clicking on the respective arrow buttons. Note that by holding down Ctrl or Shift you can apply a 10x or 100x multiplier to the applied amount on each click. Here, I applied enough first-order correction to get the barely visible spinning-sidebands facing up and then adjusted the zero-order correction accordingly:

![Phasing the spectrum](/images/ssNake-howto/Spec_phase.jpg "Phasing the spectrum.")

At this point the spectrum looks already pretty decent. A baseline correction, however, will surely be useful in order to obtain a better lineshape deconvolution later. In ssNake, baseline corrections, accessible via `Tools --> Baseline Correction`, are implemented in a rather clever way. Instead of the often-encountered spline fitting tools encountered in other software, the baseline will be fitted using a polynomial or sine/cosine function. Conveniently you get to select which parts of the spectrum are to be ignored, namely all NMR signals. The latter is done by left-clicking once to mark the onset of an NMR signal and left-clicking a second time to span a region which is then marked in red. Lastly, the degree of the fitting function is defined - best chosen by trying around - and clicking on `Fit`. The result may then look similar to this:

![Baseline correction](/images/ssNake-howto/Spec_baselinecorr.jpg "Applying a sine/cosine baseline correction.")

Now you are basically done. In my case, I find it convenient to additionally normalize my data with respect to the signal maximum which makes fitting the data easier afterwards:

![Normalizing the spectrum](/images/ssNake-howto/Spec_normalized.jpg "Normalizing the data.")

The final result of the ^{29}Si MAS NMR spectrum of a vitreous lithium disilicate sample then looks like this:

![Final result](/images/ssNake-howto/Spec_final.jpg "Final spectrum.")

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



A number of advanced tutorials can be found [here](https://github.com/smeerten/ssnake_tutorials).

