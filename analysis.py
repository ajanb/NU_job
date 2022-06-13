import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re
import matplotlib as mpl
from pylab import cm
import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1 import make_axes_locatable


os.chdir('/Users/bekzatajan/Job_NU/Matlab/ThreeRegions/NewResults/')
filesindir=os.listdir('csvs/')
meanss=[]
stdd=[]
newdf=pd.DataFrame()
good=[x for x in filesindir if 'csv' in x]
for goody in good:
    df=pd.read_csv(('csvs/'+goody),header=None)
#     df=df[:,[]]
    df.rename(columns={12:'Av. tangential velocity'}, inplace=True)
    df.rename(columns={2:'x_pos',3:'y_pos',5:'Angle',7:'Diameter',8:'High velocity region',
                      9:'Overlapping region', 10:'Low velocity region', 11:'No velocity region'}, inplace=True)
    df['Coords']=[(df['x_pos'][ii],df['y_pos'][ii]) for ii in range(df.shape[0])]
    meanss.append(np.mean(df['Av. tangential velocity']))
    stdd.append(np.std(df['Av. tangential velocity']))
    #df['Diameters']=int(re.findall('\d+(?=\.)', goody)[0])
    newdf=newdf.append(df)

newdf.drop(['Coords',0,1,4,6],axis=1,inplace=True)
newdf2=newdf.rename(columns={'Av. tangential velocity':"V", 'x_pos':'dx', 'y_pos':'dy', 'Diameter':'d', 'Angle':'alpha'})
newdf2['Alow']=newdf2['Low velocity region']-newdf2['No velocity region']
newdf2 = newdf2[newdf2['d']==1.]

colsofdf=['dx','dy', 'alpha', 'd']
parsplot=['V', 'High velocity region', 'Low velocity region']
xLabsPlot=['dx','dy', '\u03B1', '$d_{2}/d_{1}$']
yLabsPlot=["v'", '$A_{h}/A$', '$A_{l}/A$']


parDict={'V':{'col':7, 'Lab':"v'"}, 'High velocity region':{'col':1, 'Lab':'$A_{h}$/A'}, 'Low velocity region':{'col':5, 'Lab':'$A_{l}$/A'}}    
parDict['V']



# # Mesh sensitivity plots
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth


def plotmeshsense(subData):
    
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
        ax.axvline(x=200, color='green', ls=':', lw=1, label='Optimal $N_{x}, N_{y}$')
        #if i2==0:
        #    ax.legend(bbox_to_anchor=(1.36, 1), loc=1, frameon=False, fontsize=11)
        
        ax.text(-0.17, 1, textLabs[i2], fontsize=12, ha='center', va='center', transform=ax.transAxes)
        
        # Add the x and y-axis labels
        ax.set_xlabel('$N_{x}, N_{y}$', labelpad=5)
        ax.set_ylabel(yLabis, labelpad=5)
        i2+=1 
    
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.65)
    
    plt.savefig(("meshSense/AllParams3in1.png"), dpi=300, transparent=False, bbox_inches='tight')
    


meshdf=pd.read_csv(('meshSense/nXDependent.csv'),header=None)
plotmeshsense(meshdf)
plt.show()
# # Plot function for Min&Max lines for 4 in 1

    
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
                ax.text(-0.17, 1, 'a)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
#                ax.legend(bbox_to_anchor=(1.75, 1), loc=1, frameon=False, fontsize=11)
            
            elif (i2==1):
                ax.text(-0.17, 1, 'b)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
            
            elif (i2==2):
                ax.text(-0.17, 1, 'c)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
            
            
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




colsofdf=['dx','dy', 'alpha']

parsplot=['V', 'High velocity region', 'Low velocity region']

xLabsPlot=['dx','dy', '\u03B1', '$d_{2}/d_{1}$']
yLabsPlot=["v'", '$A_{h}/A$', '$A_{l}/A$']

subData={'dx':{}, 'dy':{}, 'alpha':{}, 'd':{}}

for colis in colsofdf:
    gg=newdf2.groupby(colis)
    dffmax=gg.apply(lambda grp: grp.max())
    dffmin=gg.apply(lambda grp: grp.min())
    X=dffmin[colis].values
    
    for pari in parsplot:
        Max=dffmax[pari].values
        Min=dffmin[pari].values
        
        subData[colis][pari]=[X, Max, Min]


for pari in parsplot:
    plotminmax2(subData, colsofdf, pari, xLabsPlot, yLabsPlot)





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
            coli=colsofdf[i2]
            
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
                    Z[k,m]=float(df.loc[(df['dx']==x[k]) & (df['dy']==y[m]) & (df['alpha']==alpha) & (df['d']==d), [pari]].values)

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
            
            ax.scatter(Max.dx, Max.dy, s=20,c='red', edgecolor='#D0D3D4')
            ax.scatter(Min.dx, Min.dy, s=20, c='#336EFF', edgecolor='#D0D3D4')
            
            if (i2==0):
                ax.text(-0.17, 1, 'a)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
            elif (i2==1):
                ax.text(-0.1, 1, 'b)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
            elif (i2==2):
                ax.text(-0.17, 1, 'c)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
                
            elif (i2==3):
                ax.text(-0.1, 1, 'd)', fontsize=12, ha='center', va='center', transform=ax.transAxes)
                
            
            i2+=1
                
    plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.5, 
                    hspace=0.5)

    plt.savefig(('Contours/'+pari+"4in1.png"), dpi=300, transparent=False, bbox_inches='tight')


# # Sclice plots (not complete but somehow working)


x=np.sort(newdf2.dx.unique())
y=np.sort(newdf2.dy.unique())
Ds=[0.7, .9, 1.]
X, Y   = np.meshgrid(x, y)


Z=np.zeros((len(x), len(y), len(Ds)))
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(Ds)):
            Z[i,j,k]=float(newdf2.loc[(newdf2['dx']==x[i]) & (newdf2['dy']==y[j]) & (newdf2['alpha']==0) & (newdf2['d']==Ds[k]), ['Low velocity region']].values)
#             print(i,j,k)

Max=np.squeeze(newdf2.loc[newdf2['Low velocity region']==np.max(newdf2['Low velocity region']),['dx','dy','V']].values)
Min=np.squeeze(newdf2.loc[newdf2['Low velocity region']==np.min(newdf2['Low velocity region']),['dx','dy','V']].values)

Z1 = Z[:,:,0]
Z2 = Z[:,:,1]
Z3 = Z[:,:,2]

fig    = plt.figure()
ax     = fig.gca(projection='3d')


mpl.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.linewidth'] = 0.2


levels=np.linspace(Z1.min(), Z1.max(), 1000)
ax.contourf(X, Y,Z1, levels=levels, zdir='z', offset=Ds[0], cmap=plt.get_cmap('rainbow'))

levels=np.linspace(Z2.min(), Z2.max(), 100)
ax.contourf(X, Y,Z2, levels=levels, zdir='z', offset=Ds[1], cmap=plt.get_cmap('rainbow'))


# ax1.plot(Max[0], Min[1], 'ko', size=5)
# plt.plot(Max[0], Max[1], marker="h", markersize=10, markeredgecolor="red", markerfacecolor="red")
# plt.plot(Min[0], Min[1], marker="h", markersize=10, markeredgecolor="red", markerfacecolor="blue")


levels=np.linspace(Z3.min(), Z3.max(), 1000)
ax.contourf(X, Y,Z3, levels=levels, zdir='z', offset=Ds[2], cmap=plt.get_cmap('rainbow'))

fig.colorbar(cntr1, ax=ax)

ax.set_xlim(-0.02, 0.52)
ax.set_ylim(-0.02, 0.52)
ax.set_zlim3d(Ds[0], Ds[2])

# plt.show()

plt.savefig(("Exxxx.png"), dpi=300, transparent=False, bbox_inches='tight')


# -

Contours4in1(newdf2, 'High velocity region', [0.7, 1., 3., 0.9], [45, 0., 0., 15])
# ContourPlotter('V', 1., 45, newdf2)

# +
# g = sns.stripplot(data = newdf, 
#                   x = "Diameter", 
#                   y = "Av. tangential velocity", 
#                   color = 'red')
boxcolor='#13294B'
linecolor='#E84A27'
def boxplotter(i,xl,yl,boxcol,medcol,labnames,leglab):
    sns.set()
    sns.set_style("whitegrid")
    sns.set_style({'font.family':'serif', 'font.serif':'Times New Roman'})
#     b=sns.boxplot(data = newdf,
#                 y = xl, 
#                 x = yl,
#                 orient='h',
#                 #y = "Av. tangential velocity", 
#                 color = boxcol,
#                 #showfliers = False,
#                 medianprops=dict(color=medcol, alpha=0.7),
#                 flierprops = dict(markerfacecolor = '0.50', markersize = 2))
#     b=sns.displot(yl['Av. tangential velocity'])
    b = sns.displot(newdf, y=yl, hue=xl, palette="Set1",kind='kde')

    b.set_axis_labels("Density", labnames,fontsize=18)

    b._legend.set_title(title=leglab)
    b.set(xlim=(0, None))
#     plt.legend(loc="upper right", frameon=True, fontsize=20)

    plt.savefig((yl+xl+".png"), dpi=300,bbox_inches='tight') 
    
plotcolnames=['Av. tangential velocity','Low velocity region','High velocity region','Overlapping region']
plotcolnames2=['\u03C5\'','$A_{l}/A$','$A_{h}/A$','$P_{ov}$','\u03C5\'','$A_{l}/A$','$A_{h}/A$','$P_{ov}$']
i=0
for each in plotcolnames:
    i+=1
    boxplotter(i,'Diameter',each,boxcolor,linecolor,plotcolnames2[i-1],'$d_{2}/d_{1}$')
for each in plotcolnames:
    i+=1
    boxplotter(i,'Angle',each,boxcolor,linecolor,plotcolnames2[i-1],'$\u03B1_{2}$')

# +
sns.boxplot(data = newdf,
            x = "Angle", 
            y = "Av. tangential velocity", 
            color = 'lightblue',
            showfliers = False,
            flierprops = dict(markerfacecolor = '0.50', markersize = 2))

plt.savefig("boxAngle.png", dpi=300) 

# +
print(good)
print('\n')
print('High vel: '+str(np.corrcoef(df['High velocity region'],df['Av. tangential velocity'])[0,1]))
print('Low vel: ' + str(np.corrcoef(df['Low velocity region'],df['Av. tangential velocity'])[0,1]))
print('Overlap: '+ str(np.corrcoef(df['Overlapping region'],df['Av. tangential velocity'])[0,1]))
print('Diameter: ' + str(np.corrcoef(df['Diameter'],df['Av. tangential velocity'])[0,1]))
print('Angle: ' + str(np.corrcoef(df['Angle'],df['Av. tangential velocity'])[0,1])+'\n')
for i in range(len(meanss)):
    print('Means: '+str(meanss[i]))
print('\n')
for i in range(len(meanss)):
    print('STD: '+str(stdd[i]))

print('\nmean: '+str(np.mean(meanss))+'; std: '+ str(np.mean(stdd)))
# -

fig=sns.displot(newdf, x="Av. tangential velocity", hue="Diameter", element="step",bins=60)
# fig = myplt.get_figure()
# plt.savefig("out.png", dpi=300)
plt.show()

fig=sns.displot(newdf, x="Av. tangential velocity", hue="Angle", element="step",bins=60)
# fig = myplt.get_figure()
# plt.savefig("outangless.png", dpi=300) 
plt.show()

# # Draft

# +

angleplotcorr=[]
for group, frame in newdf.groupby('Angle'):
#     print(str(group)+': '+str(np.corrcoef(frame['High velocity region'],frame['Av. tangential velocity'])[0,1]))
    angleplotcorr.append([group, np.corrcoef(frame['Diameter'],frame['Av. tangential velocity'])[0,1]])
angleplotcorr=pd.DataFrame(angleplotcorr,columns=['Angle','Corr'])
angleplotcorr
sns.set_style('whitegrid')
sns.lineplot(data=angleplotcorr,x='Angle',y='Corr')


# +

angleplotcorr=[]
for group, frame in newdf.groupby('Diameter'):
#     print(str(group)+': '+str(np.corrcoef(frame['High velocity region'],frame['Av. tangential velocity'])[0,1]))
    angleplotcorr.append([group, np.corrcoef(frame['Angle'],frame['Av. tangential velocity'])[0,1]])
angleplotcorr=pd.DataFrame(angleplotcorr,columns=['Diameter','Corr'])
angleplotcorr
sns.set_style('whitegrid')
sns.scatterplot(data=angleplotcorr,x='Diameter',y='Corr')


# +
diamcorrs=[]
for group, frame in newdf.groupby('Diameter'):
    diamcorrs.append([group, np.corrcoef(frame['Angle'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['High velocity region'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['Low velocity region'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['Overlapping region'],frame['Av. tangential velocity'])[0,1]])

diamcorrs=pd.DataFrame(diamcorrs, columns=['Diameter','Angle','High velocity region','Low velocity region','Overlapping region'])
#ax=diamcorrs.plot(kind='scatter',x='Diameter',y='Angle',color='Pink', label='Angle');
ax=diamcorrs.plot(kind='scatter',x='Diameter',y='Angle',color='Blue', label='$\u03B1_{2}$')
# ax=
diamcorrs.plot(kind='scatter',x='Diameter',y='Low velocity region',color='DarkGreen', label='$A_{l}/A$',ax=ax);
diamcorrs.plot(kind='scatter',x='Diameter',y='High velocity region',color='Orange', label='$A_{h}/A$',ax=ax);
# ax=diamcorrs.plot(kind='scatter',x='Diameter',y='Low velocity region',color='DarkGreen', label='Low velocity');
# diamcorrs.plot(kind='scatter',x='Diameter',y='Overlapping region',color='DarkRed', label='$P_{ov}$',ax=ax);
ax.set_xlabel('$d_{2}/d_{1}$',fontsize=14)
ax.set_ylabel('Correlation',fontsize=14)
ax.tick_params(labelsize=14)
# diamcorrs
plt.savefig("CorrPlotDiam.png", dpi=300,bbox_inches='tight') 
    
    


# +
anglecorrs=[]
for group, frame in newdf.groupby('Angle'):
    anglecorrs.append([group, np.corrcoef(frame['Diameter'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['High velocity region'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['Low velocity region'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['Overlapping region'],frame['Av. tangential velocity'])[0,1]])

anglecorrs=pd.DataFrame(anglecorrs, columns=['Angle','Diameter','High velocity region','Low velocity region','Overlapping region'])
# ax=anglecorrs.plot(kind='scatter',x='Angle',y='High velocity region',color='DarkBlue', label='High velocity');

ax=anglecorrs.plot(kind='scatter',x='Angle',y='Diameter',color='Blue', label='$d_2/d_1$');
anglecorrs.plot(kind='scatter',x='Angle',y='High velocity region',color='Orange', label='$A_{h}/A$',ax=ax);
anglecorrs.plot(kind='scatter',x='Angle',y='Low velocity region',color='DarkGreen', label='$A_{l}/A$',ax=ax);
# anglecorrs.plot(kind='scatter',x='Angle',y='Overlapping region',color='DarkRed', label='$P_{ov}$',ax=ax);
ax.set_xlabel('$\u03B1_{2}$',fontsize=14)
ax.set_ylabel('Correlation',fontsize=14)
ax.tick_params(labelsize=14)
plt.savefig("CorrPlotAngle.png", dpi=300,bbox_inches='tight')  


# +
anglecorrs=[]
for group, frame in newdf.groupby('Angle'):
    for group2, frame2 in frame.groupby('Diameter')
    anglecorrs.append([group, np.corrcoef(frame['Diameter'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['High velocity region'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['Low velocity region'],frame['Av. tangential velocity'])[0,1],
                                np.corrcoef(frame['Overlapping region'],frame['Av. tangential velocity'])[0,1]])
   
    


# -

newdf[newdf['Av. tangential velocity']==max(newdf['Av. tangential velocity'])]

newdf[newdf['Low velocity region']==min(newdf['Low velocity region'])]

newdf[newdf['High velocity region']==max(newdf['High velocity region'])]

newdf[newdf['No velocity region']==min(newdf['No velocity region'])]

newdf[newdf['Diameter']<=1.0].sort_values(by=['Av. tangential velocity'],ascending=False).Angle.unique()

newdf.sort_values(by=['Av. tangential velocity'],ascending=False).head(50)



def is_pareto_efficient_dumb(costs):
    """
    Find the pareto-efficient points
    :param costs: An (n_points, n_costs) array
    :return: A (n_points, ) boolean array, indicating whether each point is Pareto efficient
    """
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    for i, c in enumerate(costs):
        is_efficient[i] = np.all(np.any(costs[:i]>c, axis=1)) and np.all(np.any(costs[i+1:]>c, axis=1))
    return is_efficient



pardf=newdf[['High velocity region', 'Low velocity region']]
pardf['Low velocity region']=1/pardf['Low velocity region']
pardf=np.array(pardf)

parres=is_pareto_efficient_dumb(pardf)
np.where(parres==True)

newdf.iloc[8400]


# +
def plot_pareto_frontier(Xs, Ys, maxX=True, maxY=True):
    '''Pareto frontier selection process'''
    sorted_list = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxY)
    pareto_front = [sorted_list[0]]
    for pair in sorted_list[1:]:
        if maxY:
            if pair[1] >= pareto_front[-1][1]:
                pareto_front.append(pair)
        else:
            if pair[1] <= pareto_front[-1][1]:
                pareto_front.append(pair)
    
    '''Plotting process'''
#     plt.scatter(Xs,Ys)
    pf_X = [pair[0] for pair in pareto_front]
    pf_Y = [pair[1] for pair in pareto_front]
    plt.plot(pf_X, pf_Y)
    plt.xlabel("Objective 1")
    plt.ylabel("Objective 2")
    plt.show()

# parpldf=newdf
plot_pareto_frontier(np.array(newdf['High velocity region']),np.array(-newdf['Low velocity region']))
# -


