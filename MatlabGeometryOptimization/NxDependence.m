clc
clear
tic;


%Sides of the rectangular area:
Ax=3;%m
Ay=3;%m
X=[];

ncase=1;
dimrand=0.5+rand(ncase,1)*0.5;
posrand=[rand(ncase,1)*0.5,rand(ncase,1)*0.5];
anglerand=rand(ncase,1)*45;



X1=[];
X2=[];
X3=[];
X4=[];
X5=[];

% Ax=1;%m
% Ay=1;%m


for ni=50:400
    
    dx_overall=Ax/ni;
    n_overall=[ni, ni];
    num_points_overall=n_overall(1)*n_overall(2);
    
    
    
    
    PGT=[];
    PG=[];
    PB=[];
    ATV=[];
    Ano=[];
    for dimi=1:1
%         for posi=1:size(posrand,1)
%             for anglei=1:size(anglerand,1)
                
            [PGT1,PGof1,PBof1,ATVof1,nonono]=NestedLoop1(dx_overall,1,[0,0],0,1,n_overall,num_points_overall);
            
            PGT=[PGT, PGT1];
            PG=[PG, PGof1];
            PB=[PB, PBof1];
            ATV=[ATV, ATVof1];
            Ano=[Ano, nonono];

            
            
%             end
%         end
    end
%     X(:,:,1)=[X(:,:,1), PGT1];
%     X(:,:,2)=[X(:,:,2), PGof1];
%     X(:,:,3)=[X(:,:,3), PBof1];
%     X(:,:,4)=[X(:,:,4), ATVof1];
%     X(:,:,5)=[X(:,:,5), nonono];

    X1=[X1; [ni, PGT]];
    X2=[X2; [ni, PG]];
    X3=[X3; [ni, PB]];
    X4=[X4; [ni, ATV]];
    X5=[X5; [ni, Ano]];
 
end
% 
% % 
% plot(X(:,1), X(:,2), 'DisplayName', 'A_{h}', 'LineWidth',2)
% hold on
% % plot(X(:,1), X(:,3), 'DisplayName', 'R10','LineWidth',2)
% % hold on
% plot(X(:,1), X(:,4), 'DisplayName', 'A_{l}','LineWidth',2)
% hold on
% plot(X(:,1), X(:,5), 'DisplayName', 'V','LineWidth',2)
% hold on
% plot(X(:,1), X(:,6), 'DisplayName', 'A_{no}','LineWidth',2)
% xlabel('N');ylabel('Y');
% legend
% 

labss=['A_{h}/A', 'A_{ov}/A', 'A_{l}/A', "v'", 'A_{no}/A'];
labss2=['A_hA', 'A_ovA', 'A_lA', "v'", 'A_noA'];
X=[X1, X2, X3, X4, X5];
for i=1:5
    figure
    set(gca,'fontname','times') 
%     set(gca,'DefaultTextFontSize',25)
    
    plot(X(:,1), smoothdata(X(:, ((i-1)*(ncase+1)+2):((ncase+1)*i)),1))
    xline(100,'red')
    legend('Case 1','Case 2','Case 3','LineWidth',1.5)%, 'FontSize', 24)
    ax = gca;  
    ax.FontSize = 19; 
    xlabel('N')%, 'FontSize', 24);
    ylabel(labss(i))%, 'FontSize', 24)
    exportgraphics(ax,labss2(i)+".jpg")
    

end

save('NewResults/nXDependent.mat','X')
% figure
% set(gca,'fontname','times') 
% 
% plot(X(:,1), (abs(0.3018-X(:,6))))
% legend('Case 1','LineWidth',1.5)%, 'FontSize', 24)
% ax = gca;  
% ax.FontSize = 22; 
% xlabel('N')%, 'FontSize', 24);
% ylabel(labss(3))%, 'FontSize', 24)
% % exportgraphics(ax,labss2(i)+".jpg")

% save('PGT.mat','X1')
% save('PG.mat','X2')
% save('PB.mat','X3')
% save('ATV.mat','X4')
% save('Ano.mat','X5')