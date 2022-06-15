function [outputArg0,outputArg1,outputArg2,outputArg3, outputArg4] = NestedLoop2(dx_overall,x,DIAM,Cell_Coords,ALPH,w,n_overall)
    outputArg0=0;
    outputArg1=0;
    outputArg2=0;
    outputArg3=0;
    outputArg4=0;
    
    parfor j_overall=1:n_overall(2)
        %Space Y
        y=j_overall*dx_overall;

        outputArg1=outputArg1+FindVelOfPoint(x,y,DIAM,Cell_Coords,ALPH,w) ;


        %Count the points in the intersection area of
        %center/empty and edge regions: 
        %prodIs=1;
        IDvalues=zeros(2,size(DIAM,2));
        for i_lu=1:size(DIAM,2)
            IDvalues(1,i_lu)=I_U(1,x,y,DIAM(i_lu),Cell_Coords((i_lu-1)*2+1),Cell_Coords(i_lu*2),ALPH(i_lu));
            IDvalues(2,i_lu)=I_U(2,x,y,DIAM(i_lu),Cell_Coords((i_lu-1)*2+1),Cell_Coords(i_lu*2),ALPH(i_lu));
        end

        prodIs=0;
        if(max(IDvalues(1,:))==1 && max(IDvalues(2,:))==1)
            prodIs=1; 
        end
        outputArg2=outputArg2+prodIs;
        
        %Count good area total
        prodIs=0;
        if(max(IDvalues(1,:))==1)
            prodIs=1; 
        end
        outputArg0=outputArg0+prodIs;
        


        %Count the points in the center/bad region:
        prodIs=1;
        for i_lu=1:size(DIAM,2)
            prodIs=prodIs*I_U(2,x,y,DIAM(i_lu),Cell_Coords((i_lu-1)*2+1),Cell_Coords(i_lu*2),ALPH(i_lu));
        end
        outputArg3=outputArg3+prodIs;
        %Count No region:
        prodIs=1;
        for i_lu=1:size(DIAM,2)
            prodIs=prodIs*I_U(3,x,y,DIAM(i_lu),Cell_Coords((i_lu-1)*2+1),Cell_Coords(i_lu*2),ALPH(i_lu));
        end
        outputArg4=outputArg4+prodIs;
        
    end

end

