# Experiments
Training the TDNN for 7 epochs, on 91100 utterances, 70 archives and 163 iterations.

## Fusion

Evaluating:
- 10s: on 20284 segments (20282 for fusion cases involving pitch as a single feature)

Testing:
- 10s: on 18663 segments (18649 for fusion cases involving pitch as a single feature -- less by 0.075%)
- 3s: on 46202 segments (45801 for fusion cases involving pitch as a single feature -- less by 0.877%)


## MFCC
Training runtime:
23D features
Accuracy:  0.941
C_primary: 0.078

## MFCC + pitch
Training runtime:
23D features
Accuracy:  0.9308
C_primary: 0.0919

## MFCC + energy
Training runtime:
23D features
Accuracy:  0.9387
C_primary: 0.0802

## MFCC + pitch+energy
Training runtime:
23D features
Accuracy:  0.9378
C_primary: 0.0822

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

## MFCC+deltas+energy
Training runtime:
69D features
Accuracy:  0.9454
C_primary: 0.0697

## MFCC+deltas+pitch
Training runtime:
69D features
Accuracy:  0.9397
C_primary: 0.0797

## MFCC+deltas+pitch+energy
Training runtime:
69D features
Accuracy:  0.9451
C_primary: 0.0722

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

