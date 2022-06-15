function Out = PlotterContour(i,ParName, d,w,Par,D,W,Q,OutputDir)
    %FigNum=3*(i-1)+1;
    F_TA=scatteredInterpolant(d,w,Par);
    TA2=F_TA(D,W);
%     hf(FigNum)=figure(FigNum);
%     surf(D,W,TA2,'EdgeColor','none')
%     colorbar
%     %campos([4401.80925645085   23683.44745915113   25.18900384688])
%     xlabel('X position');ylabel('Y position')
%     title([ParName+' - interpolation factor Q = ' num2str(Q)])
%     ax = gca;
%     exportgraphics(ax,OutputDir+ParName+"Surf.jpg",'Resolution',300)
%     
%     
%     FigNum=FigNum+1;
%     hf(FigNum)=figure(FigNum);
%     hTA_surfc=surfc(D,W,TA2,'EdgeColor','none');
%     colorbar
%     %campos([5578.878486985600   7013.723961265031   21.490607228584])
%     xlabel('X position');ylabel('Y position')
%     title(ParName+' contour projections')
%     ax = gca;
%     exportgraphics(ax,OutputDir+ParName+"Surf_Projections.jpg",'Resolution',300)
    %%%% 005
%FigNum=FigNum+1;

%     x_TA_contours=hTA_surfc(2).XData;
%     y_TA_contours=hTA_surfc(2).YData;
%     z_TA_contours=hTA_surfc(2).ZData;
    FigNum=i;
    hf(FigNum)=figure(FigNum);
    contourf(D,W,TA2)   ;
    colorbar
%     [c,h] = contourm(theCon,theCon,-6000:1500:6000);
%     clegendm(c,h,4,'m')
    xlabel('x_{2} / d{1}');ylabel('y_{2} / d_{1}')
    ax = gca;
    exportgraphics(ax,OutputDir+ParName+"Contour.jpg",'Resolution',300)
    Out="Good"+i
end

