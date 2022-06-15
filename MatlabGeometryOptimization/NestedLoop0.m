function Output0 = NestedLoop0(n,n_cell,dx_cell,dx_overall,DIAM,ALPH,w,n_overall,num_points_overall,MainLayerFix)

ResultsAll=[];
%Position loop
if MainLayerFix==true
   nN=n-1; 
else
    nN=n;
end
        parfor i_cell=1:(n_cell+1)^(nN*2)
            if MainLayerFix==true
                Cell_Coords=[0,0,GenCellCoords(i_cell,dx_cell,nN, n_cell)];
            else
                Cell_Coords=GenCellCoords(i_cell,dx_cell,n, n_cell);
            end
            
            [P_goodTot,P_good2,P_badarea,AvTanVel,P_No]=NestedLoop1(dx_overall,DIAM,Cell_Coords,ALPH,w,n_overall,num_points_overall);
            ResultsAll=[ResultsAll; [Cell_Coords,ALPH,DIAM,P_goodTot,P_good2,P_badarea,P_No,AvTanVel]];
        end
        Output0=ResultsAll;
end

