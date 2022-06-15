function identifier=I_uB(x, y, d, x1,y1,alpha)
    R=d/2;
    
    
    
    
    Coords=RotAx(x,y,alpha);
    X=Coords(1);
    Y=Coords(2);
    Coords=RotAx(x1,y1,alpha);
    x1=Coords(1);
    y1=Coords(2);
    
    X=X-x1;
    Y=Y-y1;
    X=abs(X-fix(X/d)*d);
    Y=abs(Y-fix(Y/d)*d);
    XY=(X-R)*(X-R)+(Y-R)*(Y-R);
    %fprintf('x=%6.2f; X=%6.2f\n',x,X)
    %fprintf('y=%6.2f; Y=%6.2f\n',y,Y)
    %fprintf('R=%6.2f; XY=%6.2f\n',R,XY)
    if (XY>(R)^2) && X<=d && Y<=d
        identifier=1;
    
    else 
        identifier=0;
    end
end