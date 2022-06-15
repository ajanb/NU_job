clear;clc;close all

load 'OverallVel.mat'

% 
% L=A(:,1);                         % reading distances
% N=2;
% L=1/10^N*floor(L*10^N);      % taking only 2 decimals
% [D,ni,na]=unique(L);             % checking whether the grid is uniform or not
% 
% ni(1)=0 ;  % correction for 1st row because spreadsheet 1st row contains var names only, not numerical data
% 
% nD=[diff(ni); numel(L)-ni(end)+1] ; % amount of measurements at different depths, on same distance
% 
% % coordinates D: Distance W: Depth
% d=A(:,1);
% w=A(:,2);
% 
% % acquiring measurements
% T         =  A(:,3)/max(A(:,3));      %P bad area
% 
% 
% % example plot without interpolation, on same distance
% k=3;
% hf(1)=figure(1);
% plot(w(ni(k):1:ni(k+1)-1)',T(ni(k):1:ni(k+1)-1)')
% xlabel('W:depth');ylabel('T(ºC)')
% title(['Temperature measurements at distance d = ' num2str(d(ni(k)))]);
% grid on
% % 000-1
% 
% 
% % non-uniform grid of 2D reference points
% 
% hf(2)=figure(2);plot(d,w,'ro');grid on;grid minor
% xlabel('D:distance');ylabel('W:depth')
% % 000-2
% 
% % Temperature interpolation
% Q=1;  % interpolation factor ;
% d_uniform_range=linspace(min(d),max(d),Q*numel(nD)-1);
% w_uniform_range=linspace(min(w),max(w),Q*numel(nD)-1);
% [D,W]=meshgrid(d_uniform_range,w_uniform_range);
% % 
% L=A(:,1);                         % reading distances
% N=2;
% L=1/10^N*floor(L*10^N);      % taking only 2 decimals
% [D,ni,na]=unique(L);             % checking whether the grid is uniform or not
% 
% ni(1)=0 ;  % correction for 1st row because spreadsheet 1st row contains var names only, not numerical data
% 
% nD=[diff(ni); numel(L)-ni(end)+1] ; % amount of measurements at different depths, on same distance
% 
% % coordinates D: Distance W: Depth
% d=A(:,1);
% w=A(:,2);
% 
% % acquiring measurements
% T         =  A(:,3)/max(A(:,3));      %P bad area
% 
% 
% % example plot without interpolation, on same distance
% k=3;
% hf(1)=figure(1);
% plot(w(ni(k):1:ni(k+1)-1)',T(ni(k):1:ni(k+1)-1)')
% xlabel('W:depth');ylabel('T(ºC)')
% title(['Temperature measurements at distance d = ' num2str(d(ni(k)))]);
% grid on
% % 000-1
% 
% 
% % non-uniform grid of 2D reference points
% 
% hf(2)=figure(2);plot(d,w,'ro');grid on;grid minor
% xlabel('D:distance');ylabel('W:depth')
% % 000-2
% 
% % Temperature interpolation
% Q=1;  % interpolation factor ;
% d_uniform_range=linspace(min(d),max(d),Q*numel(nD)-1);
% w_uniform_range=linspace(min(w),max(w),Q*numel(nD)-1);
% [D,W]=meshgrid(d_uniform_range,w_uniform_range);
% 


% PlotterContour(1,"OverallVel", d,w,T,D,W,Q)

A=OverallVel;
OutputDir="Plots/";

x_cell=A(:,1);
y_cell=A(:,2);
Rvel=A(:,3);
[X_cell,Y_cell]=meshgrid(unique(x_cell),unique(y_cell));
PlotterContour(4,"", x_cell,y_cell,Rvel,X_cell,Y_cell,1,OutputDir)

% save('Excel_TSal_et_al_variables.mat')    % load with : load(''Excel_TSal_et_al_variables.mat'')
% savefig(hf,'AllFigures.fig')                       % load with : openfig('AllFigures.fig')


