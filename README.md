# Speech_Enhancement
Speech enhancement (SE) algorithm is used to remove noise from the noisy speech signal. There are various signal processing and deep learning-based methods available for SE. Here, signal processing-based methods are considered. No need of training for signal processing approaches. The methods were implemented on 8 kHz sampling frequency. However, it will work on any sampling frequency.
This folder contains a main file and two folders, namely algorithms and eval_scripts.

# Contents: -
    • main.m contains code to test the enhancement approach on test set of the dataset (i.e., in our case, Noisy Speech database [1]).
    • The wav files can be resampled using resampled_wavs.m file.
• ‘algorithm’ folder contains various speech enhancement algorithms listed below.

    1. spectral_subtraction.m     Spectral subtraction algorithm [2]
    2. spec_sub_noise.m     (with ‘adaptive’ method)   Weighted spectral average algorithm [3]
       spec_sub_noise.m     (with ‘i_mcra’ method)   Improved minimum controlled recursive average algorithm [4]
    3. wiener_aprior.m   Wiener filter with a priori estimation [5]
    4. log_mmse.m   Log amplitude MMSE estimator [6]
    5. CycleGAN-based SE (A folder containing samples of clean, noisy, and enhanced speech signals)
• ‘eval_scripts’ folder contains python scripts to evaluate enhanced wav files using PESQ scores.

    • make_clean_noise_pair.py: To make pairs of clean and corresponding noisy (or enhanced) wav files.
         Inputs: noisy_scp (noisy_wavlist.txt), clean_scp (clean_wavlist.txt)
         Output: new_scp (clean_enhanced_pair_file.scp)
         Example content of output file: 
          '\home\clean\p232_029.wav  \home\noisy\p232_029.wav'

    • make_pesq.py: To find PESQ scores of each individual pair of clean and enhanced wav file and store them in a text file along with the wav files location.
        Input: wav_scp (clean_enhanced_pair_file.scp)
        Output: new_scp (results_clean_enhanced.txt)
        Example content of output file: 
         '\home\clean\p232_029.wav  \home\noisy\p232_029.wav   2.243516'

    • avg_score.py: To average PESQ scores from 824 test speech signal for evaluation.
        Input: results (results_clean_enhanced.txt)
        Output: Printing the average score. (i.e., “averaged score is 2.454456”)
# References
[1] Valentini-Botinhao, Cassia. (2017). Noisy speech database for training speech enhancement algorithms and TTS models, 2016 [sound]. University of Edinburgh. School of Informatics. Centre for Speech Technology Research (CSTR). https://doi.org/10.7488/ds/2117.

[2] Berouti, M., Schwartz, M., and Makhoul, J. (1979). Enhancement of speech 
corrupted by acoustic noise. Proc. IEEE Int. Conf. Acoust., Speech, Signal Processing, 208-211.

[3] Hirsch, H. and Ehrlicher, C. (1995). Noise estimation techniques for robust speech recognition. Proc. IEEE Int. Conf. Acoust. , Speech, Signal Processing, 153-156.

[4] Cohen, I. (2003). Noise spectrum estimation in adverse environments:
Improved minima controlled recursive averaging. IEEE Transactions on Speech and Audio Processing, 11(5), 466-475.

[5] Ephraim, Y. and Malah, D. (1984). Speech enhancement using a minimum mean-square error short-time spectral amplitude estimator. IEEE Trans. Acoust.,Speech, Signal Process., ASSP-32(6), 1109-1121.

[6] Ephraim, Y. and Malah, D. (1985). Speech enhancement using a minimum mean-square error log-spectral amplitude estimator. IEEE Trans. Acoust., Speech, Signal Process., ASSP-23(2), 443-445.

     


