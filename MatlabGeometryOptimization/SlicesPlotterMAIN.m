clear;clc;close all
InputDir="TableResults/";
ATVof1=59.7966;
filename=InputDir+"DIAMs.mat";
load(filename);

% DIAMs=0.6:0.1:1;
n=2;
A=[];

for i=1:size(DIAMs,1)
   filename=InputDir+"Diameter_"+(DIAMs(i,1)*100)+"_"+(DIAMs(i,2)*100)+".mat" ;
   load(filename)
%    ResultsAll(:,11)=ResultsAll(:,size(ResultsAll,2))./ATVof1;
   A1=ResultsAll(ResultsAll(:,8)<(1.1),:);
%    A1=ResultsAll(ResultsAll(:,8)<(1.1),:);
   A=[A;A1];
end


ResultsAll=A(:,[3,4,6,8,9,11,12,13]);
ResultsAll=ResultsAll(ResultsAll(:,3)==0 | ResultsAll(:,3)==15  | ResultsAll(:,3)==30 | ResultsAll(:,3)==45,:);
ResultsAll=ResultsAll(ResultsAll(:,4)==0.6 | ResultsAll(:,4)==0.7 | ResultsAll(:,4)==0.8 | ResultsAll(:,4)==0.9 | ResultsAll(:,4)==1,:);

DorA=4;
DorA2=3;

% load ResultsAll.mat
zz=unique(ResultsAll(:,DorA2));
OutputDir="Plots/";

ParName=["High velocity area","Low velocity area","No velocity area","Average tangential velocity"];
ForPlotName=["HighArea","LowArea","NoArea","AvTanVel"];
ColBarTitle=["A_{h}/A","A_{l}/A","A_{n}/A","v'"];

if(DorA==4)
    Zlab="d_{2} / d_{1}";
    OutputName="Diam_";
    ofWhat="_alpha_";
else
    Zlab="\alpha_{2}";
    OutputName="Alpha_";
    ofWhat="_diam_";
end

for Di=1:size(zz,1)
    A=ResultsAll(find(ResultsAll(:,DorA2)>(zz(Di)-0.1) & ResultsAll(:,DorA2)<(zz(Di)+0.1)),:);

    x=unique(A(:,1));
    y=unique(A(:,2));
    z=unique(A(:,DorA));
    
    [X,Y,Z]=meshgrid(x,y,z);
    V=zeros(size(x,1),size(y,1),size(z,1),3);
    for zzi=1:4
%         if(zzi==2)
%            continue 
%         end
        for k=1:size(z,1)
            lookIn1=A(A(:,DorA)==z(k),:);
            for i=1:size(x,1)
                lookIn2=lookIn1(lookIn1(:,1)==x(i),:);
                for j=1:size(y,1)
                    lookIn3=lookIn2(lookIn2(:,2)==y(j),:);
                    V(i,j,k,zzi)=lookIn3(1,zzi+4);
                end
            end
        end
    end

    xslice = [];   
    yslice = [];
    zslice = z;

    for zzi=1:4
%         if(zzi==2)
%            continue 
%         end
        cAxisArr=[max(ResultsAll(:,zzi+4)),min(ResultsAll(:,zzi+4))];
        h=slice(X,Y,Z,V(:,:,:,zzi),xslice,yslice,zslice);
        set(gca,'fontname','times')
%         hold on
%         %%highlight points which are greater then 5
%         [idx1,idx2] = max(A(:,zzi+4));
%         plot3(A(idx2,1),A(idx2,2),A(idx2,DorA),'.r','markersize',10)
        
        set(gca,'FontSize',19)
        
        xlabel('dx');ylabel('dy');zlabel(Zlab)
        set(h,'EdgeColor','none',...
            'FaceColor','interp',...
            'FaceAlpha','interp');
        % set transparency to correlate to the data values.
        alpha('color');
        colormap(jet);
        hcb=colorbar;
        colorTitleHandle = get(hcb,'Title');
        
        titleString = ColBarTitle(zzi);
        caxis([cAxisArr(2), cAxisArr(1)]);
        
        set(colorTitleHandle ,'String',titleString);
        shading interp
        ax = gca;
%         title(ParName(zzi))   
        exportgraphics(ax,OutputDir+OutputName+ForPlotName(zzi)+ofWhat+zz(Di)+".jpg")
%         savefig(OutputDir+OutputName+ForPlotName(zzi)+ofWhat+zz(Di)+".fig")
    end
end


TC1 = topkrows(ResultsAll,20,5,'descend');
TC2 = topkrows(ResultsAll,20,6,'ascend');
TC3 = topkrows(ResultsAll,20,7,'descend');


