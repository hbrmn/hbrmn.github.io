---
title: 'Fitting Czjzek distributions with ssNake'
date: 2026-09-08
permalink: /posts/2026/09/ssnake-czjzek-fitting/
tags:
  - NMR
  - ssNake
  - fitting
  - quadrupolar NMR
  - Czjzek
---

Quadrupolar NMR spectra of glasses and other disordered solids often cannot be described by a single set of quadrupolar parameters. Instead, the local environment varies from one nucleus to another, producing distributions of the quadrupolar coupling constant, $C_Q$, and the asymmetry parameter, $\eta_Q$. In this tutorial, I will show how such spectra can be fitted in [ssNake](https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake) using the Czjzek model.

The tutorial starts from an already processed spectrum. If your data still require Fourier transformation, phasing, or other basic processing, first see my tutorial on [NMR data processing with ssNake](/posts/2021/08/2021-06-28-ssnake-howto-processing/).

## What does a Czjzek fit describe?

A conventional quadrupolar simulation assigns one $C_Q$ and one $\eta_Q$ value to each site. This is often suitable for a well-defined crystallographic environment but is usually too restrictive for a disordered material.

The standard Czjzek model instead describes a statistical distribution of electric-field-gradient tensors around an environment that would be symmetric before disorder is introduced. Its principal adjustable parameter is $\sigma$, which controls the width of the distribution. A larger $\sigma$ generally produces a broader distribution of $C_Q$ values.

The extended Czjzek model adds a non-zero, locally ordered contribution described by $C_Q^0$ and $\eta_Q^0$. It is therefore useful when the underlying site is already asymmetric and structural disorder produces an additional distribution around that environment.

This distinction matters: the standard and extended models are not merely two different mathematical lineshapes. They represent different assumptions about the local structure, and the more complicated model should only be used when it is justified by the data and by chemical knowledge of the sample.

<!-- SCREENSHOT 01: Optional schematic or ssNake comparison showing a single quadrupolar pattern, a standard Czjzek distribution, and an extended Czjzek distribution. -->

## Load and prepare the spectrum

Open the dataset `Czjzek_example` using `File --> Open`. Since this example has already been processed in TopSpin, only a few preparatory steps are required.

First, apply a baseline correction using `Tools --> Baseline Correction`. Exclude the signal-containing regions from the baseline fit and check that the correction does not remove broad spectral intensity. This is particularly important for disordered quadrupolar spectra, because a slowly varying part of the true lineshape can easily be mistaken for baseline curvature.

Next, normalize the spectrum using `Matrix --> Normalize`. Normalization is not required by the Czjzek model, but it keeps the component integrals at manageable values and makes it easier to compare different trial fits. Finally, set the horizontal axis to ppm in the `Axis` tab if it is not already displayed in ppm.

<!-- SCREENSHOT 02: The loaded and baseline-corrected Czjzek_example spectrum. Show the dataset name and ppm axis. Suggested filename: /images/ssNake-czjzek/Czjzek-spectrum-prepared.jpg -->

Before fitting, note the experimental conditions that determine the simulated lineshape:

- the observed nucleus and its spin quantum number;
- the magnetic field or Larmor frequency;
- whether the experiment was static or recorded under MAS;
- the MAS frequency;
- whether satellite transitions and spinning sidebands must be included.

Most of this information is normally read from the dataset, but it is worth checking before generating a library. An incorrect field or MAS frequency may still produce a visually plausible fit with physically incorrect parameters.

## Open the Czjzek fitting panel

Choose `Fitting --> Czjzek`. The fitting panel appears below the spectrum. As in the other ssNake fitting routines, the left side contains the simulation, fitting, preference, exclusion, and export controls. The right side contains the parameters of the current fit component.

Remember that a checked box fixes the corresponding parameter, whereas an unchecked box allows it to vary during fitting. This is easy to overlook and is one of the most common reasons for an apparently unresponsive fit.

<!-- SCREENSHOT 03: Czjzek selected in the Fitting menu and the complete fitting panel visible. Suggested filename: /images/ssNake-czjzek/Czjzek-fitting-window.jpg -->

The most important component parameters are:

| Parameter | Meaning | Practical starting point |
| --- | --- | --- |
| `Pos` | Isotropic chemical-shift position of the site | Place it near the expected isotropic shift, not necessarily at the observed maximum of a second-order quadrupolar lineshape |
| `Integral` | Scale or area of the component | Use a value comparable to the normalized experimental intensity and refine it during fitting |
| $\sigma$ | Width of the Czjzek distribution | Start with a moderate value and adjust it by simulation before fitting |
| `Lorentz` / `Gauss` | Additional homogeneous or inhomogeneous broadening | Keep small initially; excessive broadening can conceal an unsuitable quadrupolar distribution |
| $C_Q^0$ | Ordered quadrupolar contribution in the extended model | Use a chemically reasonable value from a related crystalline or less-disordered material |
| $\eta_Q^0$ | Asymmetry of the ordered contribution in the extended model | Restrict it to the physical interval from 0 to 1 |

## Generate the quadrupolar library

Czjzek fitting requires an additional step that is not needed for a simple Lorentzian or Gaussian fit. ssNake first calculates a library of quadrupolar powder patterns over a grid of $C_Q$ and $\eta_Q$ values. During simulation and fitting, these patterns are combined with weights defined by the selected Czjzek distribution. Pre-calculating the library makes the iterative fit much faster.

Click `Library` in the fitting panel. In the library window, check the experimental settings and define the $C_Q$–$\eta_Q$ grid. For an MAS spectrum, choose the finite-MAS option, enter the experimental spinning frequency, and include enough spinning sidebands to cover all sidebands visible in the experimental spectral window. A static spectrum or a spectrum containing only the central transition requires different settings.

<!-- SCREENSHOT 04: Library-generation window with the experimental settings and CQ/eta grid highlighted. Suggested filename: /images/ssNake-czjzek/Czjzek-library-settings.jpg -->

There is a trade-off when choosing the grid. A broad and finely spaced grid is more flexible and accurate, but requires more time and memory. A grid that is too narrow truncates the distribution and can bias the fitted value of $\sigma$. As a useful rule of thumb, the maximum $C_Q$ should reach approximately $4\sigma$ for the largest distribution width that the fit is likely to explore. This is a starting criterion rather than a substitute for inspecting the distribution.

Click `Show` to display the distribution weights on the current $C_Q$–$\eta_Q$ grid. The intensity should decay well before it reaches the upper $C_Q$ boundary. If the contours are cut off at the edge, increase the maximum $C_Q$ and generate the library again.

<!-- SCREENSHOT 05: A Czjzek weight distribution that fits comfortably inside the selected grid. Suggested filename: /images/ssNake-czjzek/Czjzek-library-valid.jpg -->

<!-- SCREENSHOT 06: Optional comparison showing a distribution cut off by an inadequate CQ range. This would make the warning much easier to understand. Suggested filename: /images/ssNake-czjzek/Czjzek-library-truncated.jpg -->

Once the experimental settings and grid are satisfactory, click `Generate`. Library generation may take some time. When it is complete, close the library window and return to the fitting panel.

## Simulate before fitting

It is tempting to click `Fit` immediately, but first obtaining a reasonable manual simulation makes the optimization faster and more reliable. Set an approximate `Pos`, `Integral`, and $\sigma$, and then click `Sim`.

Adjust one parameter at a time and simulate again:

- use `Pos` mainly to align the calculated and experimental spectra;
- use $\sigma$ to adjust the extent and character of the quadrupolar distribution;
- use `Integral` to match the overall intensity;
- add only as much Lorentzian or Gaussian broadening as is needed to reproduce broadening not already described by the quadrupolar model.

The goal at this stage is not a perfect match. It is to place the optimizer in a physically sensible region of parameter space.

<!-- SCREENSHOT 07: First trial simulation overlaid with the experimental spectrum. Suggested filename: /images/ssNake-czjzek/Czjzek-first-simulation.jpg -->

If you substantially increase $\sigma$, return to the `Library` window and click `Show` again. The library that was suitable for the starting value may no longer cover the distribution. If necessary, widen the $C_Q$ range and regenerate it before fitting.

## Fit with the standard Czjzek model

Decide which parameters should be optimized and uncheck their boxes. In a first round, it is usually sensible to vary only `Pos`, `Integral`, and $\sigma$, while keeping less important broadening parameters fixed. Click `Fit` and inspect the fitted spectrum and residual.

If the fit is stable, the broadening terms can be released in a later round. This staged approach reduces correlations between $\sigma$, Gaussian broadening, and Lorentzian broadening. Allowing all parameters to vary from the beginning may improve the numerical residual while making the physical interpretation less reliable.

<!-- SCREENSHOT 08: Result of the standard Czjzek fit, including experimental spectrum, total fit, component, and residual. Suggested filename: /images/ssNake-czjzek/Czjzek-standard-fit.jpg -->

Do not judge the result from the RMSD alone. Look for systematic deviations in the central-transition edges, shoulders, and spinning sidebands. A residual with a clear lineshape indicates that the model is missing something, even when its numerical value appears small.

## When should the extended Czjzek model be used?

If the standard Czjzek distribution cannot reproduce the characteristic edges or sideband shapes, and there is a structural reason to expect an already asymmetric underlying environment, change `Type` from the standard to the extended Czjzek model. This activates $C_Q^0$ and $\eta_Q^0$.

Choose physically motivated starting values. Parameters obtained for a related crystalline phase, an ordered analogue, or a less-disordered sample are often more useful than arbitrary guesses. Start by fixing $\eta_Q^0$ if there is not enough information to determine it independently, and release $C_Q^0$ only after a satisfactory manual simulation has been obtained.

Because the extended distribution adds parameters and is computationally more demanding, click `Sim` after each substantial change. A calculation with $\eta_Q^0 \ne 0$ can be particularly slow.

<!-- SCREENSHOT 09: Extended Czjzek controls with CQ0 and etaQ0 highlighted. Suggested filename: /images/ssNake-czjzek/Czjzek-extended-parameters.jpg -->

After changing from the standard to the extended model, $\sigma$ may need to be reduced considerably: part of the width previously assigned to disorder may now be described by the non-zero ordered quadrupolar interaction. Check the distribution in the `Library` window once more, then click `Fit`.

<!-- SCREENSHOT 10: Final extended Czjzek fit and residual. Suggested filename: /images/ssNake-czjzek/Czjzek-extended-fit.jpg -->

## Check that the result is meaningful

Before reporting the fitted parameters, I recommend the following checks:

1. **Inspect the residual.** It should resemble noise rather than a missing spectral component.
2. **Recheck the library limits.** The fitted distribution must not be truncated at the maximum $C_Q$ value.
3. **Repeat the fit from different starting values.** Convergence to similar parameters provides more confidence that the result is not a local minimum.
4. **Test whether all broadening terms are necessary.** Strong correlations between $\sigma$, Gaussian width, and Lorentzian width can make the solution non-unique.
5. **Compare with chemical expectations.** Values of `Pos`, $C_Q^0$, $\eta_Q^0$, and $\sigma$ should remain physically plausible.
6. **Prefer the simpler model when it is sufficient.** An improved residual does not by itself justify the additional parameters of an extended Czjzek distribution or a second site.

The fitted integrals should also be interpreted carefully. They are directly quantitative only if the experimental excitation and detection efficiencies are equivalent for the components being compared. This is not automatically guaranteed for broad quadrupolar spectra.

## Export the fit

Use `Export/Import` to save the fitted parameters. To export the experimental spectrum, individual components, total fit, and residual together, choose `Curves to Workspace`. In the newly created workspace, set the axis to ppm and use `File --> Export --> ASCII` or `CSV`.

For a publication-ready image, use `File --> Export --> Figure`. I normally show the experimental spectrum, total fit, individual components, and residual, while stating in the caption whether the standard or extended Czjzek model was used.

<!-- SCREENSHOT 11: Curves-to-Workspace or final figure-export window. Suggested filename: /images/ssNake-czjzek/Czjzek-export.jpg -->

## Summary

The essential steps are:

1. baseline-correct and normalize the processed spectrum;
2. open `Fitting --> Czjzek`;
3. generate a quadrupolar library using the correct field and MAS settings;
4. verify that the $C_Q$–$\eta_Q$ grid contains the complete distribution;
5. obtain a reasonable manual simulation before fitting;
6. fit the standard Czjzek model first;
7. use the extended model only when the spectrum and structural context justify it;
8. validate the residual, library limits, parameter stability, and physical plausibility before exporting the result.

Further examples are available in the official [ssNake tutorial collection](https://github.com/smeerten/ssnake_tutorials/tree/master/CzjzekFitting). The underlying fitting approach is described in the [ssNake software paper](https://doi.org/10.1016/j.jmr.2019.02.006).

<!-- EDITORIAL NOTE (remove before publication): Replace every SCREENSHOT comment with the corresponding image once the workflow has been repeated with Czjzek_example. Add the actual nucleus, field, MAS rate, library limits, grid density, and final fitted parameters wherever useful. -->
