% Main file of Speech Enhancement

clc
clear all
close all

% noisy_data_list ------> is a list contain the paths of all noisy speech files needed to be enhanced
noisy_data_list = '/home/speech_enhancement_DS/noisy_wavlist.txt';
% out_dir ------> is the path of directory where enhanced speech files will be dumped
out_dir = '/home/speech_enhancement_DS/spect_sub_using_noise/conn_freq_wavs/';

if ~exist(out_dir, 'dir')
    mkdir(out_dir)
end

%%

fileID = fopen(noisy_data_list);
protocol = textscan(fileID,'%s %s','delimiter',' ');
fclose(fileID);
filename = protocol{1}; % wav file names
filepath= protocol{2}; % full wavefile paths

%%

for i=1:length(filepath)
    save_path = strcat(out_dir,char(filename(i)),'.wav');
    % Just uncomment the algorithm that you want to adopt and comment the remaining ones

    spectral_subtraction(filepath{i,1},save_path); % spectral substraction method
    % spec_sub_noise(filepath{i,1},'adaptive',save_path) % 'adaptive' method for noise estimation along with spectral subtraction
    % log_mmse(filepath{i,1},save_path) % for log mmse algorithm
    % wiener_aprior(filepath{i,1},save_path) % Wiener filtering algorithm based on a priori SNR estimation
    % improved_mcra_est(filepath{i,1},'i_mcra',save_path) % improved Minimum controlled recursive average algorithm 

    disp(save_path)
end
