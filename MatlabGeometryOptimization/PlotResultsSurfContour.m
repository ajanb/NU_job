clear;clc;close all

load 'ResultsAll.mat'

OutputDir="Plots/";
% coordinates
x_cell=ResultsAll(:,1)/max(ResultsAll(:,1));  
y_cell=ResultsAll(:,2)/max(ResultsAll(:,2));  

% acquiring measurements
PBD         =  ResultsAll(:,7)/max(ResultsAll(:,7));      %P bad area
PGA         =  ResultsAll(:,5)/max(ResultsAll(:,5));      %P good area
PBH         =  ResultsAll(:,6)/max(ResultsAll(:,6));      %P bullet hit prob
Rvel        =  ResultsAll(:,8)/max(ResultsAll(:,8));      %Avg Vel


% % example plot without interpolation, on same distance
% k=3;
% hf(1)=figure(1);
% plot(y_cell',PBD')
% xlabel('X');ylabel('PBA')
% title(['P bad area at distance x = ' num2str(x_cell(ni(k)))]);
% grid on
% % 000-1
% 
% 
% % non-uniform grid of 2D reference points
% 
% hf(2)=figure(2);plot(x_cell,y_cell,'ro');grid on;grid minor
% xlabel('X');ylabel('Y')
% 000-2

%interpolation
Q=4;  % interpolation factor ;
numel=size(unique(x_cell),1);
[X_cell,Y_cell]=meshgrid(unique(x_cell),unique(y_cell));


PlotterContour(1,"Percentage of the center or empty and edge region intersection", x_cell,y_cell,PGA,X_cell,Y_cell,Q,OutputDir)

PlotterContour(2,"Probability of hitting center or empty region", x_cell,y_cell,PBD,X_cell,Y_cell,Q,OutputDir)

PlotterContour(3,"Probability of a bullet hitting empty region", x_cell,y_cell,PBH,X_cell,Y_cell,Q,OutputDir)

PlotterContour(4,"Average velocity", x_cell,y_cell,Rvel,X_cell,Y_cell,Q,OutputDir)

