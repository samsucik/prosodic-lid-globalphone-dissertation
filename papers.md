# Literature

## Various (mainly X-vector and BNF)

### [Spoken Language Recognition using X-vectors (Snyder et al., 2018a)](papers/Snyder_et_al_2018.pdf)
X-vectors applied to LID.

### [X-vectors: Robust DNN Embeddings for <abbr title="Speaker Recognition">SRE</abbr> (Snyder et al., 2018b)](papers/Snyder_et_al_2018-1.pdf)
X-vectors applied to SRE, playing with data augmentation. Has corresponding [Kaldi recipe](https://github.com/kaldi-asr/kaldi/tree/master/egs/sre16/v2).

### [Language Recognition using Time Delay Deep Neural Network (Sarma et al., 2018)](papers/Sarma_et_al_2018.pdf)
LID: TDNN trained on mono-lingual ASR used to produce i-vectors, then classified using log-regression. The LRE07/v2 Kaldi recipe.

### [<abbr title="Deep Neural Network">DNN</abbr> Embeddings for Text-Independent <abbr title="Speaker Verification">SV</abbr> (Snyder et al., 2017)](papers/Snyder_et_al_2017.pdf)
X-vectors applied to SV; scoring **pairs** of speakers. Embeddings from 2 different DNN layers.

### [<abbr title="Language Identification">LID</abbr> Using Deep Convolutional <abbr title="Recurrent Neural Networks">RNNs</abbr> (Bartz et al., 2017)](papers/Bartz_et_al_2017.pdf)
CNN->RNN architevture applied to LID, operating on spectrograms. No comparison to existing systems.

### [A <abbr title="time delay neural network">TDNN</abbr> architecture for efficient modeling of <abbr title="long temporal contexts">LTCs</abbr> (Peddinti et al., 2015)](papers/Peddinti_et_al_2015.pdf)
Using TDNNs with subsampling improves speech recognition performance.

### [Automatic <abbr title="Language Identification">LID</abbr> Using <abbr title="Deep Neural Networks">DNNs</abbr> (Lopez-Moreno et al., 2014)](papers/Lopez-Moreno_et_al_2014.pdf)
First DNN application to LID. Averaging across frame-level scores.

### [Neural Network <abbr title="Bottleneck Features">BNFs</abbr> for <abbr title="Language Identification">LID</abbr> (Matejka et al., 2014)](papers/Matejka_et_al_2014.pdf)
**TO-READ** Adding BNFs drastically improves LID from noisy speech.

### [Deep <abbr title="Bottleneck Features">BNFs</abbr> for Spoken <abbr title="Language Identification">LID</abbr> (Jiang et al., 2014)](papers/Jiang_at_al_2014.pdf)
DBNFs improve LID. Frame-level (or window-level) processing. Detailed architecture & training description.

### [A study on <abbr title="Universal Background Model">UBM</abbr> training in <abbr title="Speaker Verification">SV</abbr> (Hasan, 2011)](papers/Hasan_2011.pdf)
Improving GMM-UBM performance: Choosing data smartly to decrease training time.

### [Front-End Factor Analysis for <abbr title="Speaker Verification">SV</abbr> (Dehak et al., 2011)](papers/Dehak_et_al_2011.pdf)
Uses JFA in low-D space, introduces i-vectors. SV.

### [Support vector machines for speaker and language recognition (Campbell et al., 2006)](papers/Campbell_et_al_2006.pdf)
Defines SDCs.

### [Revising Perceptual Linear Prediction (PLP) (Hoenig et al., 2005)](papers/Hoenig_et_al_2005.pdf)
Defines PLPs. Compares MFCC with PLP and creates a new feature by mixing the two, with slightly better WER on an ASR task.

## Prosody-specific

### [A PITCH EXTRACTION ALGORITHM TUNED FOR AUTOMATIC SPEECH RECOGNITION (Ghahremani et al., 2014)](papers/Ghahremani_et_al_2005.pdf)
Kaldi pitch extractor that works even for unvoiced frames.

### [Feature Extraction Methods LPC, PLP and MFCC In <abbr title="Speech Recognition">SRE</abbr> (Dave, 2013)](papers/Dave_2013.pdf)
Brief description of LPC, PLP, MFCC and other acoustic features.

### [Prosodic Features and Formant Modeling for an I-vector-based <abbr title="Language Recognition">LRE</abbr> System (Martinez et al., 2013)](papers/Martinez_et_al_2013.pdf)
LID: For voiced frames, pitch contour and formant contours (all parametrised by Legendre polynomials), duration and energy are used as features for an i-Vector system. The system performs quite well on its own, and significantly improves an acoustic system (using SDCs) when fused together.

### [I-vector-based Prosodic System for <abbr title="Language Identification">LID</abbr> (Martinez et al., 2012)](papers/Martinez_et_al_2012.pdf)

### [A COMPARISON OF APPROACHES FOR MODELING PROSODIC FEATURES IN SPEAKER RECOGNITION (Ferrer et al., 2010)](papers/Ferrer_et_al_2010.pdf)
SRE: GMM and JFA used for modelling _energy valley-based polynomial approximation_ features (EV-PA). Good seed paper.

### [Extraction and representation of prosodic features for <abbr title="language and speaker recognition">L&SRE</abbr> (Mary et al., 2008)](papers/Mary_et_al_2008.pdf)

### [Integrating Acoustic, Prosodic and Phonotactic Features for <abbr title="Spoken Language Identification">SLID</abbr> (Tong et al., 2006)](papers/Tong_et_al_2006.pdf)

### [LANGUAGE IDENTIFICATION USING PITCH CONTOUR INFORMATION (Lin et al., 2005)](papers/Lin_et_al_2005.pdf)
LV: Modelling pitch contour with Legendre polynomials, feeding into GMMs, doing pair-wise decision (verification).