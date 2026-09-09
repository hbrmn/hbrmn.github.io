---
title: 'NMR data processing with ssNake'
date: 2025-04-11
modified: 2026-09-09
permalink: /posts/2021/08/2021-06-28-ssnake-howto-processing/
excerpt: 'Process an NMR FID in ssNake: sizing, apodization, Fourier transformation, phase correction, and baseline correction.'
tags:
  - NMR
  - ssNake
  - processing
  - how-to
---

This tutorial takes a $^{29}$Si MAS NMR dataset from a lithium disilicate glass through basic processing in [ssNake](https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake). We will start with the free-induction decay (FID) and finish with a phased, baseline-corrected spectrum ready for analysis.

The screenshots show the version used for the original example. Menu names and installation requirements may differ between releases. The processing parameters below belong to this dataset; they are not defaults for every experiment.

## Install ssNake

Official development moved from GitHub to the [Radboud GitLab repository](https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake) starting with version 1.5, as documented in the [original repository](https://github.com/smeerten/ssnake). Start with the installation instructions supplied with the release you download.

### Windows

The developers provide a standalone Windows installer through their [software page](https://www.mrrc.nl/software), with older versions listed under [GitLab releases](https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake/-/releases). Follow the instructions for the version you select. A standalone package includes the required runtime; a source installation requires Python and the dependencies specified by that release. The old version 1.4 installer is no longer the starting point for this guide.

### Running from source

Download the source from the official repository or clone it:

```bash
git clone https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake.git
```

Install the dependencies listed in that checkout's README. The current repository README starts the program with:

```bash
python3 ssnake/src/ssNake.py
```

The filename is case-sensitive on Linux: `ssNake.py` is different from `ssnake.py`. Follow the downloaded version's instructions if its layout has changed.

## 1. Load the dataset

Choose `File → Open`. Depending on the selected data, ssNake will display either an FID or an already processed spectrum. Bruker datasets can contain both raw and processed data, so check what you have opened before applying a Fourier transform.

For this example, I loaded a $^{29}$Si MAS NMR experiment recorded on a Varian instrument.

![Raw FID after loading the Varian dataset](/images/ssNake-howto/FID_loaded.jpg)

## 2. Adjust the FID length

Using `Matrix → Sizing`, I truncated the FID to 1024 points and then zero-filled it to 2048 points.

Truncation is useful when the later points contain predominantly noise, but cutting off a signal that has not decayed can introduce artifacts. Zero-filling provides more points in the frequency-domain spectrum; it does not add experimental resolution.

![FID after truncation and zero-filling](/images/ssNake-howto/FID_sized.jpg)

## 3. Apply a window function

Choose `Tools → Apodize`. Here, I applied a Gaussian window with a width of approximately 100 Hz. The window is shown in green, and the original FID remains visible in gray.

Apodization changes the balance between signal-to-noise ratio and resolution. Use only as much broadening as the analysis requires, and record the setting when comparing lineshapes.

![Gaussian apodization applied to the FID](/images/ssNake-howto/FID_apodization.jpg)

For this dataset, I also shifted the FID six points to the left using `Matrix → Shift Data`. This is a dataset-specific correction, not a step to apply automatically: removing initial points changes the signal and its phase behavior.

![FID shifted six points to the left](/images/ssNake-howto/FID_leftshift.jpg)

## 4. Fourier-transform the data

Click `Fourier` at the bottom left of the window, use `Ctrl + F`, or choose `Transforms → Fourier Transform`.

![Spectrum after Fourier transformation](/images/ssNake-howto/Spec_raw.jpg)

Use the `Axis` tab to display the frequency axis in ppm if desired. Changing the displayed unit does not establish the chemical-shift reference; check the reference separately.

To navigate the display, drag a box with the left mouse button to zoom, drag with the right button to move the view, and use the mouse wheel to scale the signal. Double-click the right mouse button to reset the view.

## 5. Correct the phase

Choose `Tools → Phasing → Phase`. Adjust the zero- and first-order phase until the signals are as close as possible to absorptive lineshapes. In the illustrated interface, holding `Ctrl` or `Shift` increases the adjustment step by a factor of 10 or 100.

In this example, I used the weak spinning sidebands to help assess the first-order correction, then adjusted the zero-order phase. Check the complete spectral region rather than only the strongest peak.

![Spectrum during interactive phase correction](/images/ssNake-howto/Spec_phase.jpg)

## 6. Correct the baseline

Choose `Tools → Baseline Correction`. The illustrated version fits a polynomial or a sine/cosine function to the selected baseline regions.

Exclude the NMR signals by clicking at the beginning and end of each signal-containing region. These excluded regions appear in red. Choose a low-complexity baseline function first, click `Fit`, and inspect the result before accepting it.

Broad spectral intensity can resemble baseline curvature. Do not increase the fitting order simply to make the baseline look flatter if that removes real signal.

![Baseline correction with signal regions excluded](/images/ssNake-howto/Spec_baselinecorr.jpg)

## 7. Normalize and check the result

Normalization is optional. I find it convenient before fitting because it keeps the numerical scale manageable. Use `Matrix → Normalize` and check the normalization mode; normalization to a maximum and normalization to an integral have different meanings.

![Normalization of the processed spectrum](/images/ssNake-howto/Spec_normalized.jpg)

The final spectrum of this lithium disilicate glass is shown below.

![Final processed silicon-29 MAS NMR spectrum](/images/ssNake-howto/Spec_final.jpg)

Before proceeding, check the chemical-shift reference, phase, baseline, and any artifacts introduced by truncation or shifting. Retain the raw data and record the processing settings so the result can be reproduced.

## Next step

Continue with [NMR data fitting with ssNake]({{ '/posts/2021/08/2023-04-11-ssnake-howto-fit/' | relative_url }}). For quadrupolar spectra of disordered materials, see the working guide to [Czjzek fitting]({{ '/posts/2026/09/ssnake-czjzek-fitting/' | relative_url }}).
