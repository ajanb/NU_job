% colsofdf=["dx","dy", "alpha", "d"];
% parsplot=["V", "High velocity region", "Alow","No velocity region"];
% yLabsPlot=["V", "Ah/A", "Al/A", "An/A"];
% Pathis="NewResults/csvsminmax/";
% k=0;
% 
% for coli=1:size(colsofdf,2)
%     colis=colsofdf(coli);
% %     disp(colis)
%     for parii=1:size(parsplot,2)
%         pari=parsplot(parii);
% %         disp(pari)
%         df=csvread(Pathis+colis+"_"+pari+".csv");
%         k=k+1;
% %         figure(k)
%         plot(df(:,1), df(:,2), 'LineWidth',3)
%         hold on;
%         
%         plot(df(:,1), df(:,3), 'LineWidth',3)
%         legend('Max', 'Min')
%         xlabel(colis)
%         ylabel(pari)
%         
%         savefig("NewResults/figplotsminmax/"+colis+"_"+pari+".fig")
%         hold off
%     end
% end
% 1:(n_cell+1)^(nN*2)
n_cell=20;

for i=1:(n_cell+1)^(2)
    disp(i)
    Cell_Coords=[0,0,GenCellCoords(i,1/20/2,1, 20)]

end