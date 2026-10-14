---
title: 'Fitting Czjzek distributions with ssNake'
modified: 2026-09-09
excerpt: 'Working guide to Czjzek fitting; example data, screenshots, and numerical validation are still in preparation.'
date: 2026-09-08
permalink: /posts/2026/09/ssnake-czjzek-fitting/
tags:
  - NMR
  - ssNake
  - fitting
  - quadrupolar NMR
  - Czjzek
---

**Working draft:** Example data, screenshots, and final fit parameters are still in preparation. This workflow has not yet been checked against a specific ssNake release.

Quadrupolar spectra of glasses often reflect distributions of local environments rather than a single quadrupolar coupling constant, $C_Q$, and asymmetry parameter, $\eta_Q$. This guide introduces Czjzek fitting in [ssNake](https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake), starting from a processed spectrum. For earlier steps, see [data processing]({{ '/posts/2021/08/2021-06-28-ssnake-howto-processing/' | relative_url }}) and [basic fitting]({{ '/posts/2021/08/2023-04-11-ssnake-howto-fit/' | relative_url }}).

## Choose the model

The **standard Czjzek model** describes a statistical distribution of electric-field-gradient tensors with no fixed, nonzero tensor contribution. Its width parameter, $\sigma$, controls the spread of quadrupolar interactions.

The **extended model** adds a fixed local contribution described by $C_Q^0$ and $\eta_Q^0$. It can represent disorder around a nonzero underlying interaction. Use it when both the spectrum and structural knowledge justify the additional parameters; a smaller residual alone is not sufficient.

## 1. Prepare the spectrum

Open your processed spectrum with `File → Open`. The planned example uses `Czjzek_example`, which is not yet supplied here.

If needed, apply `Tools → Baseline Correction`, excluding all signal-containing regions. Broad quadrupolar intensity can resemble baseline curvature, so check that the correction does not remove real signal. Optional normalization through `Matrix → Normalize` keeps fitted integrals at a convenient scale. Set the axis to ppm if desired.

Before simulation, verify the observed nucleus, spin, Larmor frequency, static or MAS conditions, spinning frequency, and transitions to include. Incorrect settings can produce plausible-looking fits with misleading parameters.

## 2. Open the fitting panel

Choose `Fitting → Czjzek`. The panel contains simulation, fitting, library, and export controls alongside the component parameters.

**Checked boxes fix parameters; unchecked boxes allow them to vary during fitting.**

| Parameter | Meaning and starting choice |
| --- | --- |
| `Pos` | Isotropic chemical shift; it need not coincide with the observed peak maximum |
| `Integral` | Component scale; adjust to the experimental intensity |
| $\sigma$ | Distribution width; estimate by simulation before optimization |
| `Lorentz` / `Gauss` | Additional broadening; keep small initially |
| $C_Q^0$ | Fixed local contribution in the extended model; use a physically motivated starting value |
| $\eta_Q^0$ | Asymmetry of that contribution, between 0 and 1 |

## 3. Generate the quadrupolar library

ssNake first calculates powder patterns on a $C_Q$–$\eta_Q$ grid. It then combines them with Czjzek weights during fitting, avoiding repeated calculation of every pattern.

Open `Library`, check the experimental settings, and define the grid. Match the static or MAS treatment to the experiment and include the relevant transitions and sidebands. A central-transition-only spectrum can be either static or MAS; transition selection does not determine the spinning treatment.

A finer, wider grid costs more time and memory, but an inadequate grid can bias the fit. Choose limits that contain the distribution throughout the parameter range you expect to explore. For the extended model, account for both the distribution width and the fixed local contribution.

Use `Show` to inspect the weights. They should decay before reaching the upper $C_Q$ boundary. Increase the range if they are cut off, then click `Generate`. Later, repeat the calculation with a wider or finer grid to check that the fitted result is stable.

## 4. Simulate before fitting

Set approximate values of `Pos`, `Integral`, and $\sigma$, then click `Sim`. Adjust one parameter at a time: position for alignment, width for the quadrupolar distribution, and integral for intensity. Add only the extra broadening needed beyond the quadrupolar model.

Aim for a physically reasonable starting spectrum. If you increase $\sigma$ substantially, inspect the library weights again; the original grid may no longer cover the distribution.

## 5. Refine the standard model

Initially, vary `Pos`, `Integral`, and $\sigma$ while keeping additional broadening fixed. Click `Fit` and inspect the residual. Release broadening parameters in a later round if needed; varying everything at once can create strong correlations.

Look for systematic errors at edges, shoulders, and sidebands rather than relying only on RMSD. Repeat the fit from different starting values to assess whether the solution is stable.

## 6. Consider the extended model

If a nonzero underlying interaction is physically expected and the standard model is inadequate, change `Type` to the extended model. Choose $C_Q^0$ and $\eta_Q^0$ from a related material or another justified estimate. Keep $\eta_Q^0$ fixed initially if the data cannot constrain it independently.

Simulate before optimizing. You may need to reduce $\sigma$ because part of the spectral width is now described by the fixed local contribution. Recheck the library coverage after this change. Extended-model calculations can take longer, so refine the starting parameters in small steps.

## 7. Validate and export

Before reporting the result, check:

- **Residual:** does it resemble noise, or contain a missing spectral feature?
- **Library:** do wider limits and a finer grid leave the result essentially unchanged?
- **Stability:** do different starting values lead to similar parameters?
- **Interpretation:** are all components and broadening terms necessary and physically plausible?

Component integrals are quantitative only when excitation and detection efficiencies are comparable. This is not guaranteed for broad quadrupolar spectra.

Save parameters through `Export/Import`. Use `Curves to Workspace` to gather the experiment, components, total fit, and residual, then export with `File → Export → ASCII` or `CSV`. For a figure, use `File → Export → Figure`.

Report the model, experimental conditions, library settings, and fitted parameters with the result. Further examples are available in the developers’ [tutorial collection](https://github.com/smeerten/ssnake_tutorials/tree/master/CzjzekFitting); the fitting software is described in the [ssNake paper](https://doi.org/10.1016/j.jmr.2019.02.006).

<!-- SCREENSHOT 01: Optional schematic or ssNake comparison showing a single quadrupolar pattern, a standard Czjzek distribution, and an extended Czjzek distribution. -->

<!-- SCREENSHOT 02: The loaded and baseline-corrected Czjzek_example spectrum. Show the dataset name and ppm axis. Suggested filename: /images/ssNake-czjzek/Czjzek-spectrum-prepared.jpg -->

<!-- SCREENSHOT 03: Czjzek selected in the Fitting menu and the complete fitting panel visible. Suggested filename: /images/ssNake-czjzek/Czjzek-fitting-window.jpg -->

<!-- SCREENSHOT 04: Library-generation window with the experimental settings and CQ/eta grid highlighted. Suggested filename: /images/ssNake-czjzek/Czjzek-library-settings.jpg -->

<!-- SCREENSHOT 05: A Czjzek weight distribution that fits comfortably inside the selected grid. Suggested filename: /images/ssNake-czjzek/Czjzek-library-valid.jpg -->

<!-- SCREENSHOT 06: Optional comparison showing a distribution cut off by an inadequate CQ range. This would make the warning much easier to understand. Suggested filename: /images/ssNake-czjzek/Czjzek-library-truncated.jpg -->

<!-- SCREENSHOT 07: First trial simulation overlaid with the experimental spectrum. Suggested filename: /images/ssNake-czjzek/Czjzek-first-simulation.jpg -->

<!-- SCREENSHOT 08: Result of the standard Czjzek fit, including experimental spectrum, total fit, component, and residual. Suggested filename: /images/ssNake-czjzek/Czjzek-standard-fit.jpg -->

<!-- SCREENSHOT 09: Extended Czjzek controls with CQ0 and etaQ0 highlighted. Suggested filename: /images/ssNake-czjzek/Czjzek-extended-parameters.jpg -->

<!-- SCREENSHOT 10: Final extended Czjzek fit and residual. Suggested filename: /images/ssNake-czjzek/Czjzek-extended-fit.jpg -->

<!-- SCREENSHOT 11: Curves-to-Workspace or final figure-export window. Suggested filename: /images/ssNake-czjzek/Czjzek-export.jpg -->

<!-- EDITORIAL NOTE (remove before publication): Replace every SCREENSHOT comment with the corresponding image once the workflow has been repeated with Czjzek_example. Add the actual nucleus, field, MAS rate, library limits, grid density, and final fitted parameters wherever useful. -->
