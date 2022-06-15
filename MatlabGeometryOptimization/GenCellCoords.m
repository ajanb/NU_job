%Get the coordinates for all placed layers positions: 
function Out = GenCellCoords(i,dx,n, Nin)
    N=Nin+1;
    
    %i is between 1 and N^(2*n)
    
    Out=zeros(1,n*2);
    for j=1:n*2
        Out(1,j)=(1+fix((i-1)/N^(j-1))-fix((i-1)/N^(j))*N)*dx-dx;
    end
    
end

