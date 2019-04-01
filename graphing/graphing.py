import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.cm import ScalarMappable
from matplotlib.ticker import MaxNLocator
import numpy as np
import seaborn as sns
import pandas as pd

font_size = 15
matplotlib.rc('axes', edgecolor='black')
sns.set(font_scale=font_size/10)

def save_fig(fig, name):
    fig.savefig("../img/{}.pdf".format(name))
    fig.savefig("../img/{}.png".format(name))

def style_axis(ax):
    # Black border
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_color('black')
    
    # White background
    ax.set_facecolor('#FFFFFF')
    
    return ax

def plot_linear(line_data, x_label=None, y_label=None, stats_interval=1, 
                legend_loc=0, mark_maxima=False, axis_scales="normal", start=0, figsize=(8, 4),
                ymin=None, ymax=None, use_legend=True, linewidth=1.2, title=None, fig=None, ax=None, 
                markersize=12, drawLegendLines=True, tight_layout=True, int_ticklabels="none", show_ticks="none"):
    """
    line data consists of dicts like:
        values (column)
        xs (optional)
        err_bars (optional)
        label
        colour
        symbol
    """
    
    if fig is None:
        fig = plt.figure(figsize=figsize, frameon=True)
    if ax is None:
        ax = fig.add_subplot(111)
        
    for line in line_data:
        x = line["xs"][start:] \
            if "xs" in line.keys() \
            else \
            np.arange(start, line["values"][start:].shape[0]+start) * stats_interval
        
        params = {
            "label": line["label"], 
            "c": line["colour"],
            "linewidth": linewidth,
            "linestyle": line["linestyle"] if "linestyle" in line.keys() else '-',
            "marker": line["symbol"] if "symbol" in line.keys() else None,
            "markersize": markersize
        }
        y = line["values"][start:]
        if axis_scales == "logx":
            ax.semilogx(x, y, **params)
        elif axis_scales == "logy":
            ax.semilogy(x, y, **params)
        elif axis_scales == "log":
            ax.loglog(x, y, **params)
        else:
            ax.plot(x, y, **params)
            if "err_bars" in line.keys():
                ax.errorbar(x, y, yerr=line["err_bars"], xerr=None, fmt='none', 
                            ecolor=line["colour"], capsize=3, elinewidth=1)
        
        if mark_maxima:
            max_x = x[np.argmax(y)]
            max_y = np.amax(y)
            params = {
                "c": line["colour"],
                "markersize": 10
            }
            if axis_scales == "logx":
                ax.semilogx(max_x, max_y, "x", **params)
            elif axis_scales == "logy":
                ax.semilogy(max_x, max_y, "x", **params)
            elif axis_scales == "log":
                ax.loglog(max_x, max_y, "x", **params)
            else:
                ax.plot(max_x, max_y, "x", **params)

    ax.tick_params(axis='both', which='both', size=6, labelcolor='black', color='black', labelsize=font_size)
    if int_ticklabels == "x":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    elif int_ticklabels == "y":
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    elif int_ticklabels == "both":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    if show_ticks == "x":
        ax.xaxis.set_ticks_position('bottom')
    elif show_ticks == "y":
        ax.yaxis.set_ticks_position('left')
    elif show_ticks == "both":
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
    
    if ymin is not None:
        ax.set_ylim(bottom=ymin)
    if ymax is not None:
        ax.set_ylim(top=ymax)
    
    handlelength = None if drawLegendLines else 0
    handletextpad = None if drawLegendLines else 0
    if use_legend:
        legend = ax.legend(loc=legend_loc, handlelength=handlelength, handletextpad=handletextpad,
                           frameon=1, prop={'size': font_size})
        frame = legend.get_frame()
        frame.set_facecolor('white')
        frame.set_edgecolor('black')
    
        for legobj in legend.legendHandles:
            legobj.set_linewidth(2.0)
            if not drawLegendLines: legobj.set_visible(False)
    
    ax.set_xlabel(x_label, fontsize=font_size, color='black')
    ax.set_ylabel(y_label, fontsize=font_size,  color='black')
    ax.set_title(title)
    
    ax = style_axis(ax)

    if tight_layout: plt.tight_layout()
    
    return fig

def plot_heatmap(values, xs, ys, x_label, y_label, height=None, width=None, cmap=None, logColourbar=False, 
                 scale_label=None, scale_format="%.3f", fmt=".3g", min_v=None, max_v=None, 
                 title=None):
    if cmap is None:
        cmap = 'seismic'
    if logColourbar:
        norm = LogNorm(vmin=np.amax(values), vmax=np.amin(values))
    else:
        norm = None
    if width is None:
        width = 1.0*len(xs) + 3
    if height is None:
        height = (width - 6)*(len(ys)*1.0/(len(xs)*1.0))
    cbar_kws = {
        "pad": 0.01,
        "format": scale_format
    }
    if scale_label is not None:
        cbar_kws["label"] = scale_label
        
    fig = plt.figure(figsize=(width, height), frameon=True, edgecolor='blue')
    ax = fig.add_subplot(111)
    ax = sns.heatmap(values, vmin=min_v, vmax=max_v, cmap=cmap, center=None, robust=True, 
                annot=True, fmt=fmt, annot_kws={"fontsize": font_size}, linewidths=0, linecolor='black', 
                cbar=True, cbar_kws=cbar_kws, cbar_ax=None, square=False, 
                xticklabels=xs, yticklabels=ys, mask=None, ax=ax,
                norm=norm)
    
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_color('black')
    
    ax.tick_params(axis='both', which='both', size=6, labelcolor='black', color='black', labelsize=font_size)   
    ax.set_xlabel(x_label, fontsize=font_size, color='black')
    ax.set_ylabel(y_label, fontsize=font_size,  color='black')
    ax.set_title(title)
    ax.set_facecolor('#FFFFFF')
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    return fig

def plot_cat(x, y, hue, data, legend_descs=None, order=None, hue_order=None, palette=None,
             legend_title=None, title=None, ylabel=None, xlabel=None, xticks=None, figsize=(9,7)):
    plt.figure(figsize=figsize)
    ax = plt.gca()
    ax = style_axis(ax)
    f = sns.catplot(x=x, y=y, hue=hue, data=data, height=6, kind="bar", ax=ax, 
                    order=order, hue_order=hue_order, palette=palette)
    leg = ax.legend()
    for i, desc in enumerate(legend_descs):
        leg.get_texts()[i].set_text(desc)
    leg.set_title(legend_title)

    plt.close(f.fig)

    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_xticklabels(xticks)
    ax.set_title(title)
    fig = plt.gcf()
    plt.tight_layout()
    plt.show()
    return fig

# Taking an existing axis, produce another one within the same figure
# but perhaps positioned and scaled differently -- relative to the
# source axis.
def insert_axis(ax_src, fig, rect=[0.0,0.0,1.0,1.0]):
    box = ax_src.get_position()
    width = box.width
    height = box.height
    inax_position = ax_src.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)    
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[3]
    ax = fig.add_axes([x,y,width,height])
    return ax
