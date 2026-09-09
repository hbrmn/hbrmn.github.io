---
title: 'How to set up WCPMG NMR'
date: 2021-06-28
permalink: /posts/2021/08/2021-06-28-WCPMG-howto/
tags:
  - NMR
  - WURST
  - WCPMG
  - how-to
---

**Work in progress:** This page currently contains only the introductory note. The pulse-sequence setup and parameter-selection walkthrough are not yet available.

Here, I will demonstrate how to set up a WCPMG experiment and lay out the usual thought process when deciding which parameters to use.

But first, a quick recap on CPMG experiments:

The Carr-Purcell-Meiboom-Gill (CPMG) experiment extends a simple Hahn echo experiment by recording several echoes within a single experiment, quickly alternating between the pulse gating and signal acquisition. This way, by superimposing all measured free-induction decays (FIDs) and subsequent Fourier transformation (FT), a regular frequency spectrum can be obtained.


