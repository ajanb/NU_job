function identifier=I_U(type,x, y, d, x1,y1,alpha)
    
    R=d/2;
    r=R/3;
    rR=r*2;
    
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
    if(type==1)
        if (XY<=r*r)
            identifier=0;
        elseif (XY>(R)^2) && X<=d && Y<=d
            identifier=0;
        elseif XY<=(R)^2 && XY>rR^2
            identifier=1;
        else 

            identifier=0;

        end
    elseif(type==2)
        if (XY<=r*r)
            identifier=1;
        elseif (XY>(R)^2) && X<=d && Y<=d
            identifier=1;
        elseif XY<=(R)^2 && XY>rR^2
            identifier=0;
        else 
            identifier=0;
        end
     elseif(type==3)
        if (XY>(R)^2) && X<=d && Y<=d
            identifier=1;
        else 
            identifier=0;
        end
    end
end