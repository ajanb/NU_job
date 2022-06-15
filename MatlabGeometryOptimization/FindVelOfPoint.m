function VelOfPoint = FindVelOfPoint(x,y,DIAM,Cell_Coords,ALPH,w)
    IubVal=zeros(size(DIAM,2),1);
    for i_lu=1:size(DIAM,2)
        IubVal(i_lu,1)=abs(I_uB(x,y,DIAM(i_lu),Cell_Coords((i_lu-1)*2+1),Cell_Coords(i_lu*2),ALPH(i_lu))-1);
    end

    if(max(IubVal)==0)
       VelOfPoint=0; 
    else
        indsToVel=find(IubVal(:,1)==1);

        VelOfPointMax=0;
        for indi=1:size(indsToVel,1)
            indofit=indsToVel(indi,1);

            VelOfPoint=RotVel(x,y,DIAM(indofit),Cell_Coords((indofit-1)*2+1),Cell_Coords(indofit*2),ALPH(indofit),w(indofit));
            if(VelOfPointMax<VelOfPoint)
                VelOfPointMax=VelOfPoint;
            end
        end
        VelOfPoint=VelOfPointMax;
        
    end
end

