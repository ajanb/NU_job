function [outputArg0,outputArg1,outputArg2,outputArg3,outputArg4] = NestedLoop1(dx_overall,DIAM,Cell_Coords,ALPH,w,n_overall,num_points_overall)    
    NumIn=0;
    NumBad=0;
    SumVel=0;
    GoodAreaTot=0;
    NumNo=0;
    %Space coordinates loop
    parfor i_overall=1:n_overall(1)
        %Space X
        x=i_overall*dx_overall;
        [O12,A12,B12,C12,D12]=NestedLoop2(dx_overall,x,DIAM,Cell_Coords,ALPH,w,n_overall);
        
        GoodAreaTot=GoodAreaTot+O12;
        SumVel=SumVel+A12;
        NumIn=NumIn+B12;
        NumBad=NumBad+C12;
        NumNo=NumNo+D12;

    end



    %Collect the values into ResultsAll
    outputArg0=GoodAreaTot/num_points_overall;
    outputArg1=NumIn/num_points_overall;
    outputArg2=NumBad/num_points_overall;
    outputArg3=SumVel/num_points_overall;
    outputArg4=NumNo/num_points_overall;
    
end