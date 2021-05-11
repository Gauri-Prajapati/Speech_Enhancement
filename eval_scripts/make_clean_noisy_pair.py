new_scp = 'clean_enhanced_pair_file.scp' # clean_(noisy/enhanced)_pair_file.scp
clean_scp = 'clean_wavlist.txt' # clean only
noisy_scp = 'enhanced_wavlist.txt' # noisy / enhanced

f = open(new_scp,'w')
with open(clean_scp) as cl:
    for file_clean in cl:
        file_clean = file_clean.strip()
        clean_path = file_clean.split(' ')[1]
        file_name = file_clean.split(' ')[0]

        with open(noisy_scp) as no:
            for file_noisy in no:
                file_noisy = file_noisy.strip()
                noisy_path = file_noisy.split(' ')[1]
                noisy_name = file_noisy.split(' ')[0]

                if file_name==noisy_name:
                    pair_path = clean_path + ' ' + noisy_path + '\n'
                    f.write(pair_path)
                    print(pair_path)
                