sop_dev
=======

Self-organized Polymer model.

<!-- comments here -->
# Potential Energy Functions
<!-- ![PEF](description_eq/equations/sop/equation_FENE_all.png?raw=true "Optional Title") -->
<!-- ![SOP_PEF](description_eq/equations/sop/equation_FENE_all.png?raw=true "SOP_PEF") -->
![SOP_PEF](description_eq/equations/sop/equation_sop_total.png?raw=true "SOP_PEF")

<!-- ![GitHub Logo](~/ext/research_review/equation_repo/rmsd/equation_rmsd.png) -->
<!-- Format: ![Alt Text](url) -->
<!-- /home/dale/sop_dev/description_eq/equations/sop: -->
<!-- total used in directory 52K available 65932108 -->
<!-- drwxr-xr-x 6 dale users 4.0K Nov  3 17:53 .. -->
<!-- -rwxr-xr-x 1 dale users 1.8K Nov  3 17:52 equation_FENE_all.tex -->
<!-- drwxr-xr-x 2 dale users 4.0K Nov  3 17:52 . -->
<!-- -rwxr-xr-x 1 dale users 7.4K Nov  3 17:52 equation_3cosinesVhelix.png -->
<!-- -rwxr-xr-x 1 dale users  488 Nov  3 17:52 equation_3cosinesVhelix.tex -->
<!-- -rwxr-xr-x 1 dale users  28K Nov  3 17:52 equation_FENE_all.png -->

<!-- /home/dale/sop_dev/description_eq/equations/sop: -->
<!-- -rw-r--r-- 1 dale users  17K Nov  3 18:31 equation_sop_total.png -->
<!-- -rw-r--r-- 1 dale users 5.5K Nov  3 18:30 equation_sop_repulsive.png -->
<!-- -rw-r--r-- 1 dale users 6.7K Nov  3 18:29 equation_sop_attractive.png -->
<!-- -rw-r--r-- 1 dale users 7.1K Nov  3 18:28 equation_sop_FENE.png -->
<!-- -rw-r--r-- 1 dale users 4.3K Nov  3 18:26 equation_sop_generic.png -->

## FENE
![SOP_FENE](description_eq/equations/sop/equation_sop_FENE.png?raw=true "SOP_FENE")

## Noncovalent Interactions: Attractive Lennard-Jones
![SOP_attractive](description_eq/equations/sop/equation_sop_attractive.png?raw=true "SOP_attractive")

## Repulsive part of Lennard-Jones
![SOP_repulsive](description_eq/equations/sop/equation_sop_repulsive.png?raw=true "SOP_repulsive")

# accessible_area
The accessible area software is used to calculate the solvent accessible surface area of the tertiary structure of interest (that which is lost) in a protein before and after the force quench in the force-extension curve for a protein during a steering simulation. The coarse-grained representations steered with the SOP model were reconstructed to full atomistic detail using pulchra (Skolnick).

# biopython

# chi_analysis

# contacts
The get_contacts software uses an 8 $\AA$ cutoff criterion to generate a contact topology. The contact topology is the map of noncovalent interactions implemented between neighboring C-alphas (but not within i-> i+1 or i-> i+2) expected to give coarse-grained representations of proteins similar structural stability as atomistic ones in simulations.

# gsop104

# gsop107

# molecules

# projects_gsop

# sop

# sopnucleo

# tension

<!-- Description of the pulling speed, deltax, nav, and integration time step (h) -->
# Pulling Speed | Integration time step

## zeta
![zeta](description_eq/equations/timespeed/equation_zeta.png?raw=true "zeta")

Zeta should be set to 50, representing the high friction coefficient in the overdamped regime, appropriate for Brownian Dynamics. Eta is the [dynamic viscosity](http://en.wikipedia.org/wiki/Viscosity) for water, 0.1 Pa*s. Alpha is the size of the bead in our simulations, 3.80 angstroms. m\_theta is the mass of the beads/atoms, a coefficient between 3 and 5 for the 20 common amino acids x 10^-22 g. Epsilon\_h is generally 1.25 or parametrized from approximately this value.

[Dynamic viscosity](http://en.wikipedia.org/wiki/Viscosity) μ, has units of pascal-second (Pa·s), (equivalent to (N·s)/m2, or kg/(m·s)).
Water at 20 °C has a viscosity of 0.001002 Pa·s.
The cgs physical unit for dynamic viscosity is the poise (P) sometimes express in centipoise (cP).
Water at 20 °C has a viscosity of 1.0020 cP.

units:
```
50.0 = 6 * pi * (kg/(m*s)) * (m^2) / sqrt( g * kcal/mol)
```

numbers:
```
50.0 = 6 * pi * 0.1 * (3.80E-10)^2 / sqrt((coef x 10^-22) * 1.25)
```

Something isn't quite right! if you only use 3.80E-10 instead of ^2, the viscosity equals 0.1351

<!-- 1 P = 0.1 Pa·s, -->
<!--     1 cP = 1 mPa·s = 0.001 Pa·s = 0.001 N·s·m-2 = 0.001 kg·m-1·s-1. -->

## tau_L
![tau_L](description_eq/equations/timespeed/equation_tau_lf.png?raw=true "tau_L")

tau_{L} = 2.24E-12 s, m_{theta} = 3E-22 g, alpha = 3.80 angstroms^2,
epsilon_{h} = 1.25 kcal/mol, f = 690 angstroms^2 * g s^-1

units:
```
s = sqrt(( g * (m^2)) / (kcal/mol * A^2 * g * s^-1 ))
```

numbers:
```
2.24 E-12 s = sqrt((3E-22 * (3.80*10^-10)^2 / (1.25 * 690))
```

## tau_H
![tau_H](description_eq/equations/timespeed/equation_tau_h.png?raw=true "tau_H")

tau_{H} = 233 ps, zeta = 50 unitless, epsilon_{h} = 1.25 kcal/mol, tau_{L} = 2.24 ps, kBT = 0.6 kcal/mol

units:
```
ps = (50 * (kcal/mol) * ps) / 0.6 kcal/mol
```

numbers:
```
233 = (50 * 1.25 * 2.24) / 0.6
```

## h (integration time step)
![h](description_eq/equations/timespeed/equation_h.png?raw=true "h")

h = 18.64 ps, tau_{H} = 233 ps

## Pulling Speed
![Pulling Speed](description_eq/equations/timespeed/equation_pulling_speed.png?raw=true "pulling speed")

v = 2.68E-8 angstroms/ps | 2.68E-6 m/s | 2.68 micron/s, deltax = 0.0005 angstroms, nav = 1000 unitless, h = 18.67 ps

## typical AFM / LOT
Atomic Force Microscopy (AFM), Laser Optical Tweezers (LOT)
AFM = 0.1 - 10 $\mu$m/s
LOT = 0.001 - 0.1 $\mu$m/s
