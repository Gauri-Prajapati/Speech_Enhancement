
results = 'results_clean_enhanced.txt' # clean_(noisy/enhanced)_pair_file.scp
sm = 0.0
with open(results) as r:
    for files in r:
        files = files.strip()
        # print(files)
        files = files.split(' ')
        score = files[2]
        sm += float(score)
avg_score = float(sm/824)
print(sm)
print('averaged score is ', avg_score)        







