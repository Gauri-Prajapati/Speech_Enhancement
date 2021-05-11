%% File to resample the audio file to fs=8000 Hz.
clc
clear all
close all
% noisy_data_list / clean_data_list ----> is a list containing paths of the speech files needed to be resampled
noisy_data_list = '/home/speech_enhancement_DS/noisy_wavlist.txt';
clean_data_list = '/home/speech_enhancement_DS/clean_wavlist.txt';
% clean_new / noisy_new ----> Path of the directory where the resampled files will be dumped
clean_new = '/home/speech_enhancement_DS/clean_wav/';
noisy_new = '/home/speech_enhancement_DS/noisy_wav/';

if ~exist(clean_new, 'dir')
    mkdir(clean_new)
end
if ~exist(noisy_new, 'dir')
    mkdir(noisy_new)
end
%%

fileID = fopen(clean_data_list);
protocol = textscan(fileID,'%s %s','delimiter',' ');
fclose(fileID);
filename = protocol{1};
filepath= protocol{2};


%% algorithm

for i=1:length(filepath)
    save_path = strcat(clean_new,char(filename(i)),'.wav');
    [x, fs] = audioread(filepath{i,1});
    audiowrite(save_path,x,8000);
end
