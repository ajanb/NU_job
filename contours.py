import pandas as pd 

# # Contour plots
def ContourPlotter(pari, d, alpha, df):
    x=np.sort(df.dx.unique())
    y=np.sort(df.dy.unique())
    
    X, Y   = np.meshgrid(x, y)
    Z=np.zeros((len(x), len(y)))

    for i in range(len(x)):
        for j in range(len(y)):
            Z[i,j]=float(df.loc[(df['dx']==x[i]) & (df['dy']==y[j]) & (df['alpha']==alpha) & (df['d']==d), [pari]].values)

    minmaxdf=df.loc[(df['alpha']==alpha) & (df['d']==d), ['dx','dy',pari]]
    Max=(minmaxdf.loc[minmaxdf[pari]==np.max(minmaxdf[pari]),['dx','dy',pari]])
    Min=(minmaxdf.loc[minmaxdf[pari]==np.min(minmaxdf[pari]),['dx','dy',pari]])

    fig = plt.figure(figsize=(3, 2.3))
    # Add axes object to our figure that takes up entire figure
    ax = fig.add_axes([0, 0, 1, 1])

    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.linewidth'] = 0.2

    levels=np.linspace(Z.min(), Z.max(), 100)
    ax.contourf(X, Y,Z, levels=levels, cmap="RdBu_r")
    fig.colorbar(cntr1, ax=ax)

    plt.scatter(Max.dx, Max.dy, s=20,c='red', edgecolor='blue')
    plt.scatter(Min.dx, Min.dy, s=20, c='blue', edgecolor='red')

    plt.savefig(("Contours/FullSize_d"+str(d)+'alpha'+str(alpha)+'_'+pari+".png"), dpi=300, transparent=False, bbox_inches='tight')



# # 4 in 1 contour plots
def Contours4in1(df, pari, ds, alphas):    
    parDict={'V':"v'", 'High velocity region':'$A_{h}$/A', 'Low velocity region':'$A_{l}$/A'}
    minmaxer=df.loc[(df['alpha'].isin(alphas)) & (df['d'].isin(ds)), [pari]]
    vminmax=[np.min(minmaxer), np.max(minmaxer)]
    
    fig, axes = plt.subplots(2, 2, sharex='none', sharey='none')
    i2=0
    for ax in axes.flat:
            d=ds[i2]
            alpha=alphas[i2]
            
            mpl.rcParams['font.family'] = 'Times New Roman'
            plt.rcParams['font.size'] = 10
    
            x=np.sort(df.dx.unique())
            y=np.sort(df.dy.unique())
            X, Y   = np.meshgrid(x, y)
            
            Z=np.zeros((len(x), len(y)))
            
            for k in range(len(x)):
                for m in range(len(y)):
                    Z[k,m]=float(df.loc[(df['dx']==x[k]) & (df['dy']==y[m]) & (df['alpha']==alpha), [pari]].values)

            print(np.max(Z))
            minmaxdf=df.loc[(df['alpha']==alpha) & (df['d']==d), ['dx','dy',pari]]
            Max=(minmaxdf.loc[minmaxdf[pari]==np.max(minmaxdf[pari]),['dx','dy',pari]])
            Min=(minmaxdf.loc[minmaxdf[pari]==np.min(minmaxdf[pari]),['dx','dy',pari]])
            
            levels=np.linspace(Z.min(), Z.max(), 100)
            
            im = ax.contourf(X, Y, Z, levels=levels, cmap="RdBu_r")

            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="3%", pad=0.03)
            kwargs = {'format': '%.4f'}
            clb=plt.colorbar(im, cax=cax,**kwargs)
            clb.ax.set_title(parDict[pari],fontsize=11)
            
            #ax.scatter(Max.dx, Max.dy, s=20,c='red', edgecolor='#D0D3D4')
            #ax.scatter(Min.dx, Min.dy, s=20, c='#336EFF', edgecolor='#D0D3D4')
            
            if (i2==0):
                ax.text(-0.24, 1, 'a)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
            elif (i2==1):
                ax.text(-0.24, 1, 'b)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
            elif (i2==2):
                ax.text(-0.24, 1, 'c)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
                
            elif (i2==3):
                ax.text(-0.24, 1, 'd)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
            
            i2+=1
                
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.6, 
                    hspace=0.5)

    plt.savefig(('Contours/'+pari+"4in1.png"), dpi=300, transparent=False, bbox_inches='tight')

