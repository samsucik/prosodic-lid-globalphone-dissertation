# Experiments
Training the TDNN for 7 epochs, on 91100 utterances, 70 archives and 163 iterations.
Evaluating on 20349 utterances.

## MFCC
Training runtime:
23D features
Accuracy:  0.941
C_primary: 0.078

## MFCC + energy
Training runtime:
23D features
Accuracy:  0.9387
C_primary: 0.0802

## SDC
Training runtime:
72D features
Accuracy:  0.945
C_primary: 0.070

## SDC + pitch+energy
Training runtime:
77D features
Accuracy: 0.943
C_primary: 0.071

## SDC + pitch
Training runtime:
76D features
Accuracy: 0.945 
C_primary: 0.072

## SDC + energy
Training runtime:
76D features
Accuracy: 0.945 
C_primary: 0.069

## MFCC+deltas
Training runtime:
69D features
Accuracy:  0.944 
C_primary: 0.074

## Pitch+energy
Training runtime: 
5D features
Accuracy:  0.860
C_primary: 0.177

## Pitch
Training runtime:
4D features
Accuracy:  0.695
C_primary: 0.385 

## Energy
Training runtime:
1D features
Accuracy:  0.720
C_primary: 0.359

