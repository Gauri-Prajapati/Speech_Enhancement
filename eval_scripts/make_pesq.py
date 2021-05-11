from scipy.io import wavfile
from pesq import pesq

new_scp = 'esults_clean_enhanced_2.txt' # clean_(noisy/enhanced)_pair_file.scp
wav_scp = 'clean_enhanced_pair_file_2.scp'

f = open(new_scp,'w')
with open(wav_scp) as n:
    for files in n:
        files = files.strip()
        clean_path = files.split(' ')[0]
        noisy_path = files.split(' ')[1]
        rate, ref = wavfile.read(clean_path)
        rate, deg = wavfile.read(noisy_path)

        score = pesq(rate, ref, deg, 'nb')

        write_line = clean_path + ' ' + noisy_path + ' ' + str(score) + '\n'

        f.write(write_line)


