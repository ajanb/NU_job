function Outputis=RotAx(x, y, alpha)
    xnew=x*cosd(alpha)+y*sind(alpha);
    ynew=-x*sind(alpha)+y*cosd(alpha);
   Outputis=[xnew,ynew];
end