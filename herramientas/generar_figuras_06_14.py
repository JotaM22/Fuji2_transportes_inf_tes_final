#!/usr/bin/env python3
"""Genera los nueve PNG de resultados (figuras 6 a 14) en figuras/.

Datos: Base_Simbal_2026_Unificada_Contraste_Hipotesis.xlsx, hojas
Base por sector, Vecindad W, MSR 9999 y Contrastes H1-H4.
Los datos sectoriales, los recuentos de 50 intervalos de las distribuciones
nulas y los cuatro contrastes están incorporados para generar figuras
reproducibles sin requerir el libro Excel durante la ejecución.
No genera el PDF de la tesis.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

OUT = Path(__file__).resolve().parents[1] / "figuras"
OUT.mkdir(exist_ok=True)

# Unidad, tramo, X local (m), Y local (m), CL (%), CT (%), PCI, IRI (m/km)
FILAS = [
    ("SIM-01",1,39.06,16.03,74.201087,78.636364,78.495435,4.6175),
    ("SIM-02",1,150.66,60.54,83.465,78.354978,83.3904,2.3875),
    ("SIM-03",1,274.35,104.72,67.92,79.850746,60.9336,3.8025),
    ("SIM-04",1,411.99,143.49,89.185,66.437414,80.4464,2.2225),
    ("SIM-05",1,568.23,171.13,83.505,84.40208,82.013,1.92),
    ("SIM-06",1,745.86,182.04,74.725,70.39031,73.8488,2.5625),
    ("SIM-07",1,938.37,177.4,92.905,78.426052,79.863,3.0875),
    ("SIM-08",1,1100.19,171.09,90.92,87.101449,64.4848,2.1575),
    ("SIM-09",1,1288.05,174.54,70.705,72.426471,72.487,4.0675),
    ("SIM-10",1,1473.12,199.55,74.945,65.73913,60.0552,2.6575),
    ("SIM-11",1,1669.35,252.85,63.89,77.195467,71.9526,2.6775),
    ("SIM-12",1,1843.26,317.79,70.035,84.645669,62.9856,2.785),
    ("SIM-13",1,2069.25,409.28,63.775,91.263941,64.3083,4.145),
    ("SIM-14",1,2303.61,486.9,55.875576,71.935484,50.255154,4.2525),
    ("SIM-15",2,560.25,110.69,42.496454,74.657534,67.450638,3.26),
    ("SIM-16",2,579.0,180.44,49.5601,69.544741,65.90132,3.0825),
    ("SIM-17",3,1296.25,195.45,38.5,61.705426,51.348,4.7175),
    ("SIM-18",3,1338.75,353.55,88.595,83.296214,75.8612,3.12),
    ("SIM-19",4,2028.5,441.62,76.017857,85.786802,64.958095,3.1425),
    ("SIM-20",4,2065.5,579.26,70.253091,67.189953,62.412526,3.9025),
]
codigos = [r[0] for r in FILAS]
tramos = np.array([r[1] for r in FILAS], dtype=int)
xy = np.array([[r[2],r[3]] for r in FILAS], dtype=float)
cl, ct, pci, iri = [np.array([r[i] for r in FILAS], dtype=float)
                    for i in (4,5,6,7)]
PALETA = {1:"#286b93",2:"#b87438",3:"#2e8569",4:"#8554a1"}
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":10.5})

def estilo(ax):
    ax.grid(color="#e3e8ed", linewidth=0.85)
    ax.set_axisbelow(True)
    for lado in ("top", "right"): ax.spines[lado].set_visible(False)

def guardar(fig, nombre):
    ruta = OUT / nombre
    fig.savefig(ruta, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("Creada:",ruta)

def dos_cajas(datos, nombres, ylabel, limites, rics, archivo):
    fig, axes = plt.subplots(1,2, figsize=(11.6,5.8), dpi=180,
                            sharey=(limites[0]==limites[1]))
    for idx,(ax,valores,nombre,color,rango) in enumerate(zip(
        axes, datos, nombres, ("#2476a3","#bc7941"), rics)):
        ax.boxplot([valores], positions=[1], widths=0.32, patch_artist=True,
                   boxprops={"facecolor":color,"edgecolor":"#26313d",
                             "alpha":0.24,"linewidth":1.5},
                   medianprops={"color":"#1b2733","linewidth":2.7},
                   whiskerprops={"color":"#354350","linewidth":1.5},
                   capprops={"color":"#354350","linewidth":1.5},
                   flierprops={"marker":"D","markerfacecolor":color,
                               "markeredgecolor":"#29333d","markersize":5})
        dx = np.linspace(-0.12,0.12,20)
        np.random.default_rng(6+idx).shuffle(dx)
        ax.scatter(np.ones(20)+dx,valores,s=34,c=color,edgecolors="white",
                   linewidths=0.7,alpha=0.85,zorder=5)
        ax.set_xlim(.55,1.45);ax.set_ylim(*limites[idx])
        ax.set_xticks([1], ["20 unidades estructura–sector"])
        ax.set_title(nombre,fontsize=12.3,weight="semibold",pad=16)
        ax.set_ylabel(ylabel[idx])
        ax.grid(axis="y",color="#e3e8ec",linewidth=.85)
        ax.set_axisbelow(True)
        for side in ("top","right"): ax.spines[side].set_visible(False)
        mediana = np.median(valores)
        ax.text(.5,-.17,f"Mediana: {mediana:.2f}{rango[0]}   |   "
                f"RIC: {np.percentile(valores,75)-np.percentile(valores,25):.2f}{rango[1]}",
                transform=ax.transAxes,ha="center",fontweight="semibold",
                fontsize=10)
    fig.subplots_adjust(top=.87,bottom=.24,left=.085,right=.985,wspace=.22)
    guardar(fig,archivo)

dos_cajas([cl,ct],["A. Continuidad longitudinal libre (CL)",
                   "B. Abertura transversal libre (CT)"],
          ["Valor del indicador (%)",""],[(0,100),(0,100)],
          [(" %"," pp"),(" %"," pp")],
          "Figura_06_CL_CT_sin_titulo_ni_nota.png")

dos_cajas([pci,iri],["A. Índice de condición del pavimento (PCI)",
                    "B. Índice internacional de rugosidad (IRI)"],
          ["PCI (0–100)","IRI (m/km)"],[(0,100),(0,6)],
          [("",""),(" m/km"," m/km")],
          "Figura_07_Distribucion_PCI_IRI_Simbal_2026.png")

def dispersion(x, y, variable_x, variable_y, filename, xlim, ylim, ytick):
    rho, _ = spearmanr(x,y)
    fig,ax=plt.subplots(figsize=(10.8,6.7),dpi=180)
    for tramo in range(1,5):
        m=tramos==tramo
        ax.scatter(x[m],y[m],s=88,c=PALETA[tramo],
                   edgecolors="white",linewidths=1.2,alpha=.95,
                   label=f"Tramo {tramo} (n = {m.sum()})",zorder=4)
    for i,codigo in enumerate(codigos):
        dx,dy=(7,6) if i%2==0 else (7,-17)
        ax.annotate(codigo[-2:],(x[i],y[i]),xytext=(dx,dy),
                    textcoords="offset points",fontsize=8.6,color="#35424d")
    ax.text(.035,.965,f"ρ de Spearman = {rho:.3f}\nn = 20",
            transform=ax.transAxes,va="top",ha="left",fontsize=12,
            color="#253644",bbox={"facecolor":"white",
            "edgecolor":"#cbd5de","boxstyle":"round,pad=0.55","alpha":.96})
    ax.set_xlabel(variable_x,fontsize=12)
    ax.set_ylabel(variable_y,fontsize=12)
    ax.set_xlim(*xlim);ax.set_ylim(*ylim)
    ax.set_yticks(np.arange(*ytick))
    estilo(ax)
    ax.legend(loc="lower left" if ylim[1]>10 else "upper right",
              frameon=True,edgecolor="#cbd5de",fontsize=10)
    fig.tight_layout(pad=2)
    guardar(fig,filename)

dispersion(cl,pci,"Continuidad longitudinal libre, CL (%)",
           "Índice de condición del pavimento, PCI (0–100)",
           "Figura_08_Asociacion_CL_PCI_Simbal_2026.png",
           (30,100),(40,95),(40,96,5))
dispersion(cl,iri,"Continuidad longitudinal libre, CL (%)",
           "Índice internacional de rugosidad, IRI (m/km)",
           "Figura_09_Asociacion_CL_IRI_Simbal_2026.png",
           (30,100),(1.5,5.1),(1.5,5.1,.5))
dispersion(ct,pci,"Abertura transversal libre, CT (%)",
           "Índice de condición del pavimento, PCI (0–100)",
           "Figura_10_Asociacion_CT_PCI_Simbal_2026.png",
           (55,95),(40,95),(40,96,5))
dispersion(ct,iri,"Abertura transversal libre, CT (%)",
           "Índice internacional de rugosidad, IRI (m/km)",
           "Figura_11_Asociacion_CT_IRI_Simbal_2026.png",
           (55,95),(1.5,5.1),(1.5,5.1,.5))

# Matriz binaria simétrica: cada unidad enlazada con sus dos vecinos
# euclidianos más próximos en el sistema XY local.
d = np.linalg.norm(xy[:,None,:]-xy[None,:,:],axis=2)
np.fill_diagonal(d,np.inf)
W=np.zeros((20,20),dtype=int)
for i in range(20): W[i,np.argsort(d[i])[:2]]=1
W=np.maximum(W,W.T)
assert np.all(W==W.T) and np.trace(W)==0
assert np.triu(W,1).sum()==26

fig,ax=plt.subplots(figsize=(12.5,6.8),dpi=180)
for i,j in np.argwhere(np.triu(W,1)):
    ax.plot(xy[[i,j],0],xy[[i,j],1],color="#a8b1bb",
            linewidth=1.55,alpha=.77,zorder=1)
for tramo in range(1,5):
    m=tramos==tramo
    ax.scatter(xy[m,0],xy[m,1],s=112,c=PALETA[tramo],
               edgecolors="white",linewidths=1.4,
               label=f"Tramo {tramo} (n = {sum(m)})",zorder=3)
for i,codigo in enumerate(codigos):
    dx,dy = (-42,-15) if i%4==0 else (8,12 if i%2==0 else -18)
    ax.annotate(codigo,xy[i],xytext=(dx,dy),textcoords="offset points",
                fontsize=8.8,color="#263440",zorder=5,
                bbox={"boxstyle":"round,pad=0.12","facecolor":"white",
                      "alpha":.83,"edgecolor":"none"})
ax.set_xlabel("Coordenada local X (m)",fontsize=12)
ax.set_ylabel("Coordenada local Y (m)",fontsize=12)
ax.set_xlim(-110,2410);ax.set_ylim(-65,690)
ax.set_aspect("equal",adjustable="box");estilo(ax)
ax.legend(loc="upper left",frameon=True,edgecolor="#d2dae1",fontsize=10)
fig.tight_layout(pad=1.5)
guardar(fig,"Figura_12_Red_vecindad_espacial_Simbal_2026.png")

# Recuentos exactos del histograma de las 9999 realizaciones de MSR por H.
# Los centros y anchos corresponden a 50 intervalos equiespaciados [-1, 1].
FRECUENCIAS = [
[0,0,0,0,0,0,0,0,1,13,22,42,74,93,168,212,239,325,376,450,488,597,610,654,676,640,622,578,555,557,452,389,315,250,199,133,103,91,42,25,8,0,0,0,0,0,0,0,0,0],
[0,0,0,0,2,13,20,22,45,62,86,106,164,173,243,232,343,317,361,407,425,461,495,545,469,517,489,468,449,407,427,390,380,298,249,248,168,149,126,93,49,51,23,16,10,1,0,0,0,0],
[0,0,0,0,0,0,0,5,11,48,51,78,97,134,149,224,298,348,357,407,477,549,594,558,566,592,596,655,537,472,420,376,317,278,253,156,120,96,70,52,37,17,4,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,3,12,44,106,199,299,426,541,609,644,666,738,722,667,688,667,628,635,542,446,315,221,121,45,14,1,0,0,0,0,0,0,0,0,0,0,0,0],
]
OBS = [.5772579022316113,-.5892703941148457,.2892750449916851,-.13999709302388263]
PESP=[.0045,.0356,.2675,.5217]
PHOLM=[.0180,.1068,.5350,.5350]
assert all(sum(f)==9999 for f in FRECUENCIAS)
fig,axs=plt.subplots(2,2,figsize=(11.7,8),dpi=175,sharex=True,sharey=True)
edges=np.linspace(-1,1,51);centers=(edges[:-1]+edges[1:])/2
for i,ax in enumerate(axs.flat):
    heights=np.array(FRECUENCIAS[i])/(9999*(edges[1]-edges[0]))
    ax.bar(centers,heights,width=edges[1]-edges[0],
           color=["#276d96","#b67b41","#398c70","#8b66a9"][i],
           edgecolor="white",linewidth=.48,alpha=.76)
    ax.axvline(OBS[i],color="#1c2833",linewidth=2.25,linestyle="--",
               label="Estadístico observado")
    ax.set_title(["H1: CL–PCI","H2: CL–IRI","H3: CT–PCI","H4: CT–IRI"][i],
                 fontsize=12.5,fontweight="semibold",pad=12)
    ax.text(.98,.97,f"T observado = {OBS[i]:+.3f}\np espacial = {PESP[i]:.4f}",
            ha="right",va="top",transform=ax.transAxes,fontsize=10,
            bbox={"facecolor":"white","alpha":.96,"edgecolor":"#c9d3dc",
                  "boxstyle":"round,pad=0.42"})
    estilo(ax);ax.set_xlim(-1,1)
    ax.legend(loc="upper left",fontsize=8.8,frameon=False)
for ax in axs[1,:]:
    ax.set_xlabel("Correlación residualizada bajo la hipótesis nula (T*)")
for ax in axs[:,0]:ax.set_ylabel("Densidad")
fig.subplots_adjust(left=.09,right=.985,top=.955,bottom=.09,hspace=.24,wspace=.16)
guardar(fig,"Figura_13_Distribuciones_nulas_Moran_H1_H4_Simbal_2026.png")

fig,ax=plt.subplots(figsize=(10.5,5.8),dpi=180)
pos=np.arange(4)
bars=ax.bar(pos,PHOLM,width=.55,
            color=["#357e9b" if v<.05 else "#a3aebb" for v in PHOLM],
            edgecolor="#354553",linewidth=.8,zorder=3)
ax.axhline(.05,color="#b34f42",linestyle="--",linewidth=2,
           label="Umbral de significancia (α = 0,05)",zorder=4)
for bar,v in zip(bars,PHOLM):
    ax.text(bar.get_x()+bar.get_width()/2,v+.012,f"{v:.4f}",
            ha="center",va="bottom",fontsize=12,fontweight="semibold",color="#263542")
ax.set_xticks(pos,["H1\nCL–PCI","H2\nCL–IRI","H3\nCT–PCI","H4\nCT–IRI"])
ax.set_ylabel("Valor p ajustado por Holm",fontsize=12)
ax.set_ylim(0,.63);ax.set_yticks(np.arange(0,.61,.1))
estilo(ax);ax.legend(loc="upper left",frameon=True,edgecolor="#ccd5df",fontsize=10.5)
fig.subplots_adjust(left=.12,right=.985,bottom=.19,top=.94)
guardar(fig,"Figura_14_Valores_p_Holm_Simbal_2026.png")

print("Total:",len(list(OUT.glob("Figura_*.png"))))
