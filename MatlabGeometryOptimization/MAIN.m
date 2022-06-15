clc
clear
tic;
%Create folders for the outputs:
YourWD=pwd;
if ~exist('TableResultsNew', 'dir')
       mkdir('TableResultsNew')
end
if ~exist('Plots', 'dir')
       mkdir('Plots')
end
TableDir=YourWD+"/TableResultsNew/";
PlotDir=YourWD+"/Plots/";

MainLayerFix=true;
%Material properties
UltSigma=420*10^6;%Pa
rho=8050;%kg/m3
SpecSigma=sqrt(UltSigma/rho);
%Sides of the rectangular area:
Ax=3;%m
Ay=3;%m
n=2;%Number of layers
%Angular velocity
w=zeros(n,1);


%Diameter of the placed layer (You can put an array if you want to run through some)
DIAMs=0.7:0.1:3;
% DIAMs=[nchoosek(DIAMs,n);(DIAMs.*ones(n,size(DIAMs,2)))'];
DIAMs=[ones(size(DIAMs,2),1),DIAMs'];
%Angles to loop through:
ALPHs=0:1:45;
% ALPHs=[nchoosek(ALPHs,n);(ALPHs.*ones(n,size(ALPHs,2)))'];
ALPHs=[zeros(size(ALPHs,2),1),ALPHs'];
%Number of elements in both x and y direction in space coordinates:
n_overall=200;
%Number of elements in both x and y direction in position coordinates for the placed grid:
n_cell=20;


%Evaluate the step sizes for space and position coordinates:

[dx_overall,indmin]=min([Ax/n_overall,Ay/n_overall]);
if Ax~=Ay
    if indmin==1
       n_overall=[n_overall,(fix(Ay/dx_overall)+1)];
    else
       n_overall=[(fix(Ax/dx_overall)+1),n_overall];
    end
else
    n_overall=[n_overall,n_overall];
end



%Find overall points number to find the probability later:
num_points_overall=n_overall(1)*n_overall(2);


wof1=SpecSigma/DIAMs(1);
[PGT,PGof1,PBof1,ATVof1,nonono]=NestedLoop1(dx_overall,1,[0,0],0,wof1,n_overall,num_points_overall);


    
%Diameter loop
for di=1:size(DIAMs,1)
    kk=0;
%     ResultsAll=zeros((n_cell^(2*n)),(n*2+n+n+3));
    ResultsAll=[];
    %Get the Diameter of the upper layer grid
    DIAM=DIAMs(di,:);
    w=SpecSigma./DIAM;
    
    dx_cell=max(DIAM)*0.5/n_cell;
    fprintf('d=%6.2f;\n',DIAM(1,:))
    %Alpha loop
    parfor ali=1:size(ALPHs,1)
        %Get alpha    
        ALPH=ALPHs(ali,:);
    
        ResultsAll=[ResultsAll;NestedLoop0(n,n_cell,dx_cell,dx_overall,DIAM,ALPH,w,n_overall,num_points_overall,MainLayerFix)];
    end
%     ResultsAll(:,size(ResultsAll,2))=ResultsAll(:,size(ResultsAll,2))./ATVof1;
    filename="TableResultsNew/Diameter_";
    for fi=1:(size(DIAM,2)-1)
        filename=filename+(100*DIAM(fi))+"_";
    end
%     ResultsAll(:,end)=ResultsAll(:,end)/wof1;
    filename=filename+(100*DIAM(size(DIAM,2)))+".mat";
    save(filename, 'ResultsAll');
    
%     ResultsAll=sortrows(ResultsAll,6);
%     ResultsAll1=[ResultsAll1;ResultsAll(1:10,:)];
%     
%     ResultsAll=sortrows(ResultsAll,5,'descend');
%     ResultsAll2=[ResultsAll2;ResultsAll(1:10,:)];
%     
%     ResultsAll=sortrows(ResultsAll,7,'descend');
%     ResultsAll3=[ResultsAll3;ResultsAll(1:10,:)];

end
timeElapsed = toc;
save('TableResultsNew/DIAMs.mat','DIAMs')
