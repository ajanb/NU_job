function Out = RotVel(x,y,d,x1,y1,alpha,w)
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
    DistToC=sqrt((X-R)*(X-R)+(Y-R)*(Y-R));
    Out=DistToC;

end

