DirFiles="TableResultsNew/Diameter_";
load("TableResultsNew/DIAMs");
% DIAMs=0.6:0.1:1;
% n=2;
% GoodTotal=zeros(10*size(DIAMs,2),(n*2+n+n+4));
% BadArea=zeros(10*size(DIAMs,2),(n*2+n+n+4));
% GoodArea=zeros(10*size(DIAMs,2),(n*2+n+n+4));
% MaxVel=zeros(10*size(DIAMs,2),(n*2+n+n+4));
% AllGood=zeros(10*size(DIAMs,2),(n*2+n+n+4));
for i=1:size(DIAMs,1)
   filename=DirFiles+(DIAMs(i,1)*100)+"_"+(DIAMs(i,2)*100)+".mat" ;
   filename2=DirFiles+(DIAMs(i,1)*100)+"_"+(DIAMs(i,2)*100)+".csv";
   load(filename)
%    save(filename2,'ResultsAll')

   ResultsAllout=ResultsAll(ResultsAll(:,4)<=ResultsAll(:,3),:);
   writematrix(ResultsAllout,filename2)
%    
%    ResultsAll=sortrows(ResultsAll,(5+2*n));
%    GoodTotal(((i-1)*10+1):10*i,:)=ResultsAll(1:10,:);
%    
%    ResultsAll=sortrows(ResultsAll,(7+2*n));
%    BadArea(((i-1)*10+1):10*i,:)=ResultsAll(1:10,:);
%    ResultsAll=sortrows(ResultsAll,(6+2*n),'descend');
%    GoodArea(((i-1)*10+1):10*i,:)=ResultsAll(1:10,:);
%    ResultsAll=sortrows(ResultsAll,(8+2*n),'descend');
%    MaxVel(((i-1)*10+1):10*i,:)=ResultsAll(1:10,:);
%    
%    ResultsAll=sortrows(ResultsAll,[-(5+2*n),6+2*n,-(7+2*n)]);
%    AllGood=ResultsAll(1:10,:);
end
% GoodTotal=sortrows(GoodTotal,(5+2*n),'descend');
% BadArea=sortrows(BadArea,(7+2*n));
% GoodArea=sortrows(GoodArea,(6+2*n),'descend');
% MaxVel=sortrows(MaxVel,(8+2*n),'descend');
% AllGood=sortrows(AllGood,[-(5+2*n),6+2*n,-(7+2*n)]);
% save('TableResults/BadArea.mat', 'BadArea');
% save('TableResults/GoodArea.mat', 'GoodArea');
% save('TableResults/MaxVel.mat', 'MaxVel');