import pandas as pd 
# # Mesh sensitivity plots
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


def plotmeshsense(subData,vertX, figname):
    
    parsplot=['V', 'High velocity region', 'Low velocity region']
    parDict={'V':{'col':7, 'Lab':"v'"}, 'High velocity region':{'col':1, 'Lab':'$A_{h}$/A'}, 'Low velocity region':{'col':5, 'Lab':'$A_{l}$/A'}}    
    xlimsAll={'dx':[-0.04, 0.54],'dy':[-0.04, 0.54], 'd': [0.5, 3.1], 'alpha':[-2, 47]}
    ylimsAll={'V':[.0, 1.19],'Low velocity region':[-0.02, 0.35],'High velocity region':[0.35, 0.85]}
    xlocatorsAll={'dx': [0.1, 0.05],'dy': [0.1, 0.05],'d':[0.5, 0.25],'alpha': [5, 2.5]}
    ylocatorsAll={'V': [0.2, 0.1], 'Low velocity region':[0.1, 0.05],'High velocity region':[0.1, 0.05]}
    
    textLabs=['a)', 'b)', 'c)']
    
    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.linewidth'] = 1
    colors = cm.get_cmap('tab10', 2)
    
    fig, axes = plt.subplots(3, 1, sharex=False, sharey=False)
    i2=0
    for ax in axes.flat:
        mpl.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['font.size'] = 10
        pari=parsplot[i2]
        colsofdf=parDict[pari]['col']
        yLabis=parDict[pari]['Lab']
        
        X=subData.iloc[:,0]
        Case1=subData.iloc[:,colsofdf]
        
        ax.xaxis.set_tick_params(which='major', size=6, width=1, direction='in', top='on')
        ax.xaxis.set_tick_params(which='minor', size=3, width=1, direction='in', top='on')
        ax.yaxis.set_tick_params(which='major', size=6, width=1, direction='in', right='on')
        ax.yaxis.set_tick_params(which='minor', size=3, width=1, direction='in', right='on')                
        
        ax.plot(X, Case1, linewidth=1, color=colors(0), label='Parameter value')

        ax.axvline(x=vertX, color='green', ls=':', lw=1, label='Optimal $N_{x}, N_{y}$')
        #if i2==0:
        #    ax.legend(bbox_to_anchor=(1.36, 1), loc=1, frameon=False, fontsize=11)
        
        ax.text(-0.17, 1, textLabs[i2], fontsize=12, ha='center', va='center', transform=ax.transAxes)
        
        # Add the x and y-axis labels
        ax.set_xlabel('$N_{t}$', labelpad=5)
        ax.set_ylabel(yLabis, labelpad=5)
        i2+=1 
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.65)
    
    plt.savefig(("meshSense/"+figname+".png"), dpi=300, transparent=False, bbox_inches='tight')
    

def plotminmax2(subData, colsofdf, pari, XLabel, YLabel):
    xlimsAll={'dx':[-0.04, 0.54],'dy':[-0.04, 0.54], 'd': [0.5, 3.1], 'alpha':[-2, 47]}
    ylimsAll={'V':[.2, .4],'Low velocity region':[-0.02, 0.35],'High velocity region':[0.35, 0.85]}
    xlocatorsAll={'dx': [0.1, 0.05],'dy': [0.1, 0.05],'d':[0.5, 0.25],'alpha': [5, 2.5]}
    ylocatorsAll={'V': [0.1, 0.05], 'Low velocity region':[0.1, 0.05],'High velocity region':[0.1, 0.05]}
    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.linewidth'] = 1
    colors = cm.get_cmap('tab10', 2)
    fig, axes = plt.subplots(3,1, sharex=False, sharey=False)
    i2=0
    for ax in axes.flat:
            coli=colsofdf[i2]
            xlims=xlimsAll[coli]
            ylims=ylimsAll[pari]
            xlocators=xlocatorsAll[coli]
            ylocators=ylocatorsAll[pari]
            X=subData[coli][pari][0]
            Max=subData[coli][pari][1]
            Min=subData[coli][pari][2]
            ax.xaxis.set_tick_params(which='major', size=6, width=1, direction='in', top='on')
            ax.xaxis.set_tick_params(which='minor', size=3, width=1, direction='in', top='on')
            ax.yaxis.set_tick_params(which='major', size=6, width=1, direction='in', right='on')
            ax.yaxis.set_tick_params(which='minor', size=3, width=1, direction='in', right='on')                
            # Edit the major and minor ticks of the x and y axes
            ax.plot(X, Max, linewidth=2, color=colors(1), label='Max', zorder=1)    
            ax.plot(X, Min, linewidth=2, color=colors(0), label='Min', zorder=1)
            ax.scatter(X[Max==np.max(Max)], Max[Max==np.max(Max)], s=20, c='red', edgecolor='#D0D3D4', zorder=2)
            ax.scatter(X[Min==np.min(Min)], Min[Min==np.min(Min)], s=20, c='blue', edgecolor='#D0D3D4', zorder=2)

            #ax.axvline(x=X[np.argmax(Max)], color='red', ls=':', lw=1, label='Max')
            #ax.axvline(x=X[np.argmin(Min)], color='blue', ls=':', lw=1, label='Min')            
            if (i2==0):
                ax.text(-0.15, 1, 'a)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
#                ax.legend(bbox_to_anchor=(1.75, 1), loc=1, frameon=False, fontsize=11)
            
            elif (i2==1):
                ax.text(-0.15, 1, 'b)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
            
            elif (i2==2):
                ax.text(-0.15, 1, 'c)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
            
            
            # Set the axis limits
            ax.set_xlim(xlims[0], xlims[1])
            ax.set_ylim(ylims[0], ylims[1])
            ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(xlocators[0]))
            ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(xlocators[1]))
            ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(ylocators[0]))
            ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(ylocators[1]))
            # Add the x and y-axis labels
            ax.set_xlabel(XLabel[colsofdf.index(coli)], labelpad=5)
            ax.set_ylabel(YLabel[parsplot.index(pari)], labelpad=5)
            i2+=1
         
    
    plt.savefig(('plotsminmax/'+pari+"4in1.png"), dpi=300, transparent=False, bbox_inches='tight')


# # Plot function for Min&Max

def plotminmax(X, Min, Max, coli, pari, XLabel, YLabel):
    xlimsAll={'dx':[-0.04, 0.54],'dy':[-0.04, 0.54], 'd': [0.5, 3.1], 'alpha':[-2, 47]}
    ylimsAll={'V':[.0, 1.19],'Low velocity region':[-0.02, 0.35],'High velocity region':[0.35, 0.85]}
    xlocatorsAll={'dx': [0.1, 0.05],'dy': [0.1, 0.05],'d':[0.5, 0.25],'alpha': [5, 2.5]}
    ylocatorsAll={'V': [0.2, 0.1], 'Low velocity region':[0.1, 0.05],'High velocity region':[0.1, 0.05]}
        
    xlims=xlimsAll[coli]
    ylims=ylimsAll[pari]
    xlocators=xlocatorsAll[coli]
    ylocators=ylocatorsAll[pari]
    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.linewidth'] = 2
    colors = cm.get_cmap('tab10', 2)
    # Create figure object and store it in a variable called 'fig'
    fig = plt.figure(figsize=(2.2, 2))
    # Add axes object to our figure that takes up entire figure
    ax = fig.add_axes([0, 0, 1, 1])
    # Edit the major and minor ticks of the x and y axes
    ax.xaxis.set_tick_params(which='major', size=6, width=1, direction='in', top='on')
    ax.xaxis.set_tick_params(which='minor', size=3, width=1, direction='in', top='on')
    ax.yaxis.set_tick_params(which='major', size=6, width=1, direction='in', right='on')
    ax.yaxis.set_tick_params(which='minor', size=3, width=1, direction='in', right='on')
    ax.plot(X, Min, linewidth=2, color=colors(0), label='Min')
    ax.plot(X, Max, linewidth=2, color=colors(1), label='Max')
    # Set the axis limits
    ax.set_xlim(xlims[0], xlims[1])
    ax.set_ylim(ylims[0], ylims[1])
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(xlocators[0]))
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(xlocators[1]))
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(ylocators[0]))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(ylocators[1]))
    # Add the x and y-axis labels
    ax.set_xlabel(XLabel, labelpad=10)
    ax.set_ylabel(YLabel, labelpad=10)
    # Add legend to plot
    ax.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=11)
    # Save figure
    plt.savefig(('plotsminmax/'+colis+"_"+pari+".png"), dpi=300, transparent=False, bbox_inches='tight')



