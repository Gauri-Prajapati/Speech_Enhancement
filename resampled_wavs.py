import librosa
outdir = 'noisy_wav_8k/' # folder where resampled speech signals wiil be stored
file_list = '48kdata/noisy_wavlist.txt' # text file containg filepaths to 48 kHz wavefiles (to be resampled)
with open(file_list) as f:  # 
    for files in f:
        files = files.strip()
        files = files.split(' ')
        filepath = files[1]
        filename = files[0]
        # print(filename)
        out_filepath = outdir + filename + '.wav'
        x,fs = librosa.load(filepath,sr=8000)
        librosa.output.write_wav(out_filepath,x,fs)
# x,fs= librosa.load('48kdata/clean_testset_wav/p232_001.wav',sr=8000)
# librosa.output.write_wav('resampled.wav',x,8000)
        print(filepath) 