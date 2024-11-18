

<details class="code-fold">
<summary>Code</summary>

``` python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
```

</details>

<details class="code-fold">
<summary>Code</summary>

``` python
np.random.seed(42069)


def plot_scatter(ax, prng, nb_samples: int = 100):
    for mu, sigma, marker in [(-0.5, 0.75, "o"), (0.75, 1.5, "s")]:
        x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
        ax.plot(x, y, ls="none", marker=marker)
    ax.set_xlabel("X-label")
    ax.set_title("Axes titel")
    return ax


def plot_colored_lines(ax):
    """Plot lines w/ colors following the style color cycle."""
    _t = np.linspace(-10, 10, 100)

    def sigmoid(_t, _t0):
        return 1 / (1 + np.exp(-(_t - _t0)))

    nb_colors = len(plt.rcParams["axes.prop_cycle"])
    shifts = np.linspace(-5, 5, nb_colors)
    amplitudes = np.linspace(1, 1.5, nb_colors)
    for _t0, a in zip(shifts, amplitudes):
        ax.plot(_t, a * sigmoid(_t, _t0), "-")
    ax.set_xlim(-10, 10)
    return ax


def plot_bargraph(ax, prng, min_val: int = 5, max_val: int = 25, nb_samples: int = 5):
    """Plot 2 bar graphs side by side, w/ letters as x-tick labels."""
    _x = np.arange(nb_samples)
    _ya, _yb = prng.randint(min_val, max_val, size=(2, nb_samples))
    width = 0.25
    ax.bar(_x, _ya, width)
    ax.bar(_x + width, _yb, width, color="C2")
    ax.set_xticks(_x + width, labels=["a", "b", "c", "d", "e"])
    return ax


def plot_circles(ax, prng, nb_samples: int = 15):
    """
    Plot circle patches.

    NB: draws a fixed amt of samples, rather tahn using the len of the color cycle, bc diff
    styles may hae diff numbers of colors.
    """
    for sty_dict, j in zip(plt.rcParams["axes.prop_cycle"](), range(nb_samples)):
        ax.add_patch(
            plt.Circle(
                prng.normal(scale=3, size=2), radius=1.0, color=sty_dict["color"]
            )
        )

    ax.grid(visible=True)

    # add title for enabling grid
    plt.title("ax.grid(True)", family="monospace", fontsize="small")

    ax.set_xlim([-4, 8])
    ax.set_ylim([-5, 6])
    ax.set_aspect("equal", adjustable="box")  # to plot circles as circles
    return ax


def plot_img_and_patch(ax, prng, size=(20, 20)):
    """Plot an image with random values and superimpose a circular patch."""
    vals = prng.random_sample(size=size)
    ax.imshow(vals, interpolation="none")
    _c = plt.Circle((5, 5), radius=5, label="patch")
    ax.add_patch(_c)
    # remove ticks
    ax.set_xticks([])
    ax.set_yticks([])


def plot_histogram(ax, prng, nb_samples: int = 10_000):
    """Plot 4 histograms and text annotations."""
    _params = ((10, 10), (4, 12), (50, 12), (6, 55))
    for _a, _b in _params:
        vals = prng.beta(_a, _b, size=nb_samples)
        ax.hist(vals, histtype="stepfilled", bins=30, alpha=0.8, density=True)

    # add small annotation.
    ax.annotate(
        "Annotation",
        xy=(0.25, 4.25),
        xytext=(0.9, 0.9),
        textcoords=ax.transAxes,
        va="top",
        ha="right",
        bbox=dict(boxstyle="round", alpha=0.2),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=-95,angleB=35,rad=10"
        ),
    )
    return ax


def plot_figure(style_label: str = ""):
    """Setup & plot the demonstration figure w/ given style."""
    # Use dedicated RandomState instance to draw the same "random" values across different figures.
    prng = np.random.RandomState(96917002)

    fig, axs = plt.subplots(
        ncols=6, nrows=1, num=style_label, figsize=(14.8, 2.8), squeeze=True
    )

    # make a subtitle, in the same style for all subfigures.
    # except those w/ dark backgrounds, which get a lighter color:
    background_color = mcolors.rgb_to_hsv(
        mcolors.to_rgb(plt.rcParams["figure.facecolor"])
    )[2]
    if background_color < 0.5:
        title_color = [0.8, 0.8, 1]
    else:
        title_color = np.array([19, 6, 84]) / 256
    fig.suptitle(
        style_label,
        x=0.01,
        ha="left",
        color=title_color,
        fontsize=14,
        fontfamily="DejaVu Sans",
        fontweight="normal",
    )

    plot_scatter(axs[0], prng)
    plot_img_and_patch(axs[1], prng)
    plot_bargraph(axs[2], prng)
    plot_colored_lines(axs[3], prng)
    plot_histogram(axs[4], prng)
    plot_circles(axs[5], prng)

    rec = Rectangle((1 + 0.025, -2), 0.05, 16, clip_on=False, color="gray")
    axs[4].add_artist(rec)
```

</details>

<details class="code-fold">
<summary>Code</summary>

``` python
plt.style.use("./light_pastel.mplstyle")
plot_figure(style_label="Quanty Pastel")
plt.savefig("quant_pastel_example.png")
```

</details>

    TypeError: plot_colored_lines() takes 1 positional argument but 2 were given
    [1;31m---------------------------------------------------------------------------[0m
    [1;31mTypeError[0m                                 Traceback (most recent call last)
    Cell [1;32mIn[11], line 2[0m
    [0;32m      1[0m plt[38;5;241m.[39mstyle[38;5;241m.[39muse([38;5;124m"[39m[38;5;124m./light_pastel.mplstyle[39m[38;5;124m"[39m)
    [1;32m----> 2[0m [43mplot_figure[49m[43m([49m[43mstyle_label[49m[38;5;241;43m=[39;49m[38;5;124;43m"[39;49m[38;5;124;43mQuanty Pastel[39;49m[38;5;124;43m"[39;49m[43m)[49m
    [0;32m      3[0m plt[38;5;241m.[39msavefig([38;5;124m"[39m[38;5;124mquant_pastel_example.png[39m[38;5;124m"[39m)

    Cell [1;32mIn[9], line 130[0m, in [0;36mplot_figure[1;34m(style_label)[0m
    [0;32m    128[0m plot_img_and_patch(axs[[38;5;241m1[39m], prng)
    [0;32m    129[0m plot_bargraph(axs[[38;5;241m2[39m], prng)
    [1;32m--> 130[0m [43mplot_colored_lines[49m[43m([49m[43maxs[49m[43m[[49m[38;5;241;43m3[39;49m[43m][49m[43m,[49m[43m [49m[43mprng[49m[43m)[49m
    [0;32m    131[0m plot_histogram(axs[[38;5;241m4[39m], prng)
    [0;32m    132[0m plot_circles(axs[[38;5;241m5[39m], prng)

    [1;31mTypeError[0m: plot_colored_lines() takes 1 positional argument but 2 were given

    Error in callback <function _draw_all_if_interactive at 0x00000204E82537E0> (for post_execute), with arguments args (),kwargs {}:

    RuntimeError: latex was not able to process the following string:
    b'lp'

    Here is the full command invocation and its output:

    latex -interaction=nonstopmode --halt-on-error --output-directory=tmp5f577ce3 03c6366f7a4e307ef0b23ee8720251c2.tex

    This is pdfTeX, Version 3.141592653-2.6-1.40.25 (MiKTeX 24.1 Portable) (preloaded format=latex.fmt)
     restricted \write18 enabled.
    entering extended mode
    (03c6366f7a4e307ef0b23ee8720251c2.tex
    LaTeX2e <2023-11-01> patch level 1
    L3 programming layer <2024-01-04>

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\article.
    cls
    Document Class: article 2023/05/17 v1.4n Standard LaTeX document class

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\size10.c
    lo))

    ! LaTeX Error: File `type1cm.sty' not found.

    Type X to quit or <RETURN> to proceed,
    or enter new name. (Default extension: sty)

    Enter file name: 
    ! Emergency stop.
    <read *> 
             
    l.8 \usepackage
                   {type1ec}^^M
    No pages of output.
    Transcript written on C:\Users\eo\.matplotlib\tex.cache\03\c6\tmp5f577ce3\03c63
    66f7a4e307ef0b23ee8720251c2.log.
    latex: major issue: So far, you have not checked for MiKTeX updates.



    [1;31m---------------------------------------------------------------------------[0m
    [1;31mRuntimeError[0m                              Traceback (most recent call last)
    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\pyplot.py:268[0m, in [0;36m_draw_all_if_interactive[1;34m()[0m
    [0;32m    266[0m [38;5;28;01mdef[39;00m [38;5;21m_draw_all_if_interactive[39m() [38;5;241m-[39m[38;5;241m>[39m [38;5;28;01mNone[39;00m:
    [0;32m    267[0m     [38;5;28;01mif[39;00m matplotlib[38;5;241m.[39mis_interactive():
    [1;32m--> 268[0m         [43mdraw_all[49m[43m([49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\_pylab_helpers.py:131[0m, in [0;36mGcf.draw_all[1;34m(cls, force)[0m
    [0;32m    129[0m [38;5;28;01mfor[39;00m manager [38;5;129;01min[39;00m [38;5;28mcls[39m[38;5;241m.[39mget_all_fig_managers():
    [0;32m    130[0m     [38;5;28;01mif[39;00m force [38;5;129;01mor[39;00m manager[38;5;241m.[39mcanvas[38;5;241m.[39mfigure[38;5;241m.[39mstale:
    [1;32m--> 131[0m         [43mmanager[49m[38;5;241;43m.[39;49m[43mcanvas[49m[38;5;241;43m.[39;49m[43mdraw_idle[49m[43m([49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backend_bases.py:1905[0m, in [0;36mFigureCanvasBase.draw_idle[1;34m(self, *args, **kwargs)[0m
    [0;32m   1903[0m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m[38;5;241m.[39m_is_idle_drawing:
    [0;32m   1904[0m     [38;5;28;01mwith[39;00m [38;5;28mself[39m[38;5;241m.[39m_idle_draw_cntx():
    [1;32m-> 1905[0m         [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mdraw[49m[43m([49m[38;5;241;43m*[39;49m[43margs[49m[43m,[49m[43m [49m[38;5;241;43m*[39;49m[38;5;241;43m*[39;49m[43mkwargs[49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backends\backend_agg.py:387[0m, in [0;36mFigureCanvasAgg.draw[1;34m(self)[0m
    [0;32m    384[0m [38;5;66;03m# Acquire a lock on the shared font cache.[39;00m
    [0;32m    385[0m [38;5;28;01mwith[39;00m ([38;5;28mself[39m[38;5;241m.[39mtoolbar[38;5;241m.[39m_wait_cursor_for_draw_cm() [38;5;28;01mif[39;00m [38;5;28mself[39m[38;5;241m.[39mtoolbar
    [0;32m    386[0m       [38;5;28;01melse[39;00m nullcontext()):
    [1;32m--> 387[0m     [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mfigure[49m[38;5;241;43m.[39;49m[43mdraw[49m[43m([49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mrenderer[49m[43m)[49m
    [0;32m    388[0m     [38;5;66;03m# A GUI class may be need to update a window using this draw, so[39;00m
    [0;32m    389[0m     [38;5;66;03m# don't forget to call the superclass.[39;00m
    [0;32m    390[0m     [38;5;28msuper[39m()[38;5;241m.[39mdraw()

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\artist.py:95[0m, in [0;36m_finalize_rasterization.<locals>.draw_wrapper[1;34m(artist, renderer, *args, **kwargs)[0m
    [0;32m     93[0m [38;5;129m@wraps[39m(draw)
    [0;32m     94[0m [38;5;28;01mdef[39;00m [38;5;21mdraw_wrapper[39m(artist, renderer, [38;5;241m*[39margs, [38;5;241m*[39m[38;5;241m*[39mkwargs):
    [1;32m---> 95[0m     result [38;5;241m=[39m [43mdraw[49m[43m([49m[43martist[49m[43m,[49m[43m [49m[43mrenderer[49m[43m,[49m[43m [49m[38;5;241;43m*[39;49m[43margs[49m[43m,[49m[43m [49m[38;5;241;43m*[39;49m[38;5;241;43m*[39;49m[43mkwargs[49m[43m)[49m
    [0;32m     96[0m     [38;5;28;01mif[39;00m renderer[38;5;241m.[39m_rasterizing:
    [0;32m     97[0m         renderer[38;5;241m.[39mstop_rasterizing()

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\artist.py:72[0m, in [0;36mallow_rasterization.<locals>.draw_wrapper[1;34m(artist, renderer)[0m
    [0;32m     69[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
    [0;32m     70[0m         renderer[38;5;241m.[39mstart_filter()
    [1;32m---> 72[0m     [38;5;28;01mreturn[39;00m [43mdraw[49m[43m([49m[43martist[49m[43m,[49m[43m [49m[43mrenderer[49m[43m)[49m
    [0;32m     73[0m [38;5;28;01mfinally[39;00m:
    [0;32m     74[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\figure.py:3162[0m, in [0;36mFigure.draw[1;34m(self, renderer)[0m
    [0;32m   3159[0m             [38;5;66;03m# ValueError can occur when resizing a window.[39;00m
    [0;32m   3161[0m     [38;5;28mself[39m[38;5;241m.[39mpatch[38;5;241m.[39mdraw(renderer)
    [1;32m-> 3162[0m     [43mmimage[49m[38;5;241;43m.[39;49m[43m_draw_list_compositing_images[49m[43m([49m
    [0;32m   3163[0m [43m        [49m[43mrenderer[49m[43m,[49m[43m [49m[38;5;28;43mself[39;49m[43m,[49m[43m [49m[43martists[49m[43m,[49m[43m [49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43msuppressComposite[49m[43m)[49m
    [0;32m   3165[0m     renderer[38;5;241m.[39mclose_group([38;5;124m'[39m[38;5;124mfigure[39m[38;5;124m'[39m)
    [0;32m   3166[0m [38;5;28;01mfinally[39;00m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\image.py:132[0m, in [0;36m_draw_list_compositing_images[1;34m(renderer, parent, artists, suppress_composite)[0m
    [0;32m    130[0m [38;5;28;01mif[39;00m not_composite [38;5;129;01mor[39;00m [38;5;129;01mnot[39;00m has_images:
    [0;32m    131[0m     [38;5;28;01mfor[39;00m a [38;5;129;01min[39;00m artists:
    [1;32m--> 132[0m         [43ma[49m[38;5;241;43m.[39;49m[43mdraw[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m    133[0m [38;5;28;01melse[39;00m:
    [0;32m    134[0m     [38;5;66;03m# Composite any adjacent images together[39;00m
    [0;32m    135[0m     image_group [38;5;241m=[39m []

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\artist.py:72[0m, in [0;36mallow_rasterization.<locals>.draw_wrapper[1;34m(artist, renderer)[0m
    [0;32m     69[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
    [0;32m     70[0m         renderer[38;5;241m.[39mstart_filter()
    [1;32m---> 72[0m     [38;5;28;01mreturn[39;00m [43mdraw[49m[43m([49m[43martist[49m[43m,[49m[43m [49m[43mrenderer[49m[43m)[49m
    [0;32m     73[0m [38;5;28;01mfinally[39;00m:
    [0;32m     74[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axes\_base.py:3101[0m, in [0;36m_AxesBase.draw[1;34m(self, renderer)[0m
    [0;32m   3098[0m     [38;5;28;01mfor[39;00m spine [38;5;129;01min[39;00m [38;5;28mself[39m[38;5;241m.[39mspines[38;5;241m.[39mvalues():
    [0;32m   3099[0m         artists[38;5;241m.[39mremove(spine)
    [1;32m-> 3101[0m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_update_title_position[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   3103[0m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m[38;5;241m.[39maxison:
    [0;32m   3104[0m     [38;5;28;01mfor[39;00m _axis [38;5;129;01min[39;00m [38;5;28mself[39m[38;5;241m.[39m_axis_map[38;5;241m.[39mvalues():

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axes\_base.py:3045[0m, in [0;36m_AxesBase._update_title_position[1;34m(self, renderer)[0m
    [0;32m   3043[0m top [38;5;241m=[39m [38;5;28mmax[39m(top, bb[38;5;241m.[39mymax)
    [0;32m   3044[0m [38;5;28;01mif[39;00m title[38;5;241m.[39mget_text():
    [1;32m-> 3045[0m     [43max[49m[38;5;241;43m.[39;49m[43myaxis[49m[38;5;241;43m.[39;49m[43mget_tightbbox[49m[43m([49m[43mrenderer[49m[43m)[49m  [38;5;66;03m# update offsetText[39;00m
    [0;32m   3046[0m     [38;5;28;01mif[39;00m ax[38;5;241m.[39myaxis[38;5;241m.[39moffsetText[38;5;241m.[39mget_text():
    [0;32m   3047[0m         bb [38;5;241m=[39m ax[38;5;241m.[39myaxis[38;5;241m.[39moffsetText[38;5;241m.[39mget_tightbbox(renderer)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:1372[0m, in [0;36mAxis.get_tightbbox[1;34m(self, renderer, for_layout_only)[0m
    [0;32m   1369[0m     renderer [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mfigure[38;5;241m.[39m_get_renderer()
    [0;32m   1370[0m ticks_to_draw [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39m_update_ticks()
    [1;32m-> 1372[0m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_update_label_position[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   1374[0m [38;5;66;03m# go back to just this axis's tick labels[39;00m
    [0;32m   1375[0m tlb1, tlb2 [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39m_get_ticklabel_bboxes(ticks_to_draw, renderer)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:2654[0m, in [0;36mYAxis._update_label_position[1;34m(self, renderer)[0m
    [0;32m   2650[0m     [38;5;28;01mreturn[39;00m
    [0;32m   2652[0m [38;5;66;03m# get bounding boxes for this axis and any siblings[39;00m
    [0;32m   2653[0m [38;5;66;03m# that have been set by `fig.align_ylabels()`[39;00m
    [1;32m-> 2654[0m bboxes, bboxes2 [38;5;241m=[39m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_get_tick_boxes_siblings[49m[43m([49m[43mrenderer[49m[38;5;241;43m=[39;49m[43mrenderer[49m[43m)[49m
    [0;32m   2655[0m x, y [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mlabel[38;5;241m.[39mget_position()
    [0;32m   2656[0m [38;5;28;01mif[39;00m [38;5;28mself[39m[38;5;241m.[39mlabel_position [38;5;241m==[39m [38;5;124m'[39m[38;5;124mleft[39m[38;5;124m'[39m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:2206[0m, in [0;36mAxis._get_tick_boxes_siblings[1;34m(self, renderer)[0m
    [0;32m   2204[0m axis [38;5;241m=[39m ax[38;5;241m.[39m_axis_map[name]
    [0;32m   2205[0m ticks_to_draw [38;5;241m=[39m axis[38;5;241m.[39m_update_ticks()
    [1;32m-> 2206[0m tlb, tlb2 [38;5;241m=[39m [43maxis[49m[38;5;241;43m.[39;49m[43m_get_ticklabel_bboxes[49m[43m([49m[43mticks_to_draw[49m[43m,[49m[43m [49m[43mrenderer[49m[43m)[49m
    [0;32m   2207[0m bboxes[38;5;241m.[39mextend(tlb)
    [0;32m   2208[0m bboxes2[38;5;241m.[39mextend(tlb2)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:1351[0m, in [0;36mAxis._get_ticklabel_bboxes[1;34m(self, ticks, renderer)[0m
    [0;32m   1349[0m [38;5;28;01mif[39;00m renderer [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
    [0;32m   1350[0m     renderer [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mfigure[38;5;241m.[39m_get_renderer()
    [1;32m-> 1351[0m [38;5;28;01mreturn[39;00m ([[43mtick[49m[38;5;241;43m.[39;49m[43mlabel1[49m[38;5;241;43m.[39;49m[43mget_window_extent[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   1352[0m          [38;5;28;01mfor[39;00m tick [38;5;129;01min[39;00m ticks [38;5;28;01mif[39;00m tick[38;5;241m.[39mlabel1[38;5;241m.[39mget_visible()],
    [0;32m   1353[0m         [tick[38;5;241m.[39mlabel2[38;5;241m.[39mget_window_extent(renderer)
    [0;32m   1354[0m          [38;5;28;01mfor[39;00m tick [38;5;129;01min[39;00m ticks [38;5;28;01mif[39;00m tick[38;5;241m.[39mlabel2[38;5;241m.[39mget_visible()])

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:959[0m, in [0;36mText.get_window_extent[1;34m(self, renderer, dpi)[0m
    [0;32m    954[0m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(
    [0;32m    955[0m         [38;5;124m"[39m[38;5;124mCannot get window extent of text w/o renderer. You likely [39m[38;5;124m"[39m
    [0;32m    956[0m         [38;5;124m"[39m[38;5;124mwant to call [39m[38;5;124m'[39m[38;5;124mfigure.draw_without_rendering()[39m[38;5;124m'[39m[38;5;124m first.[39m[38;5;124m"[39m)
    [0;32m    958[0m [38;5;28;01mwith[39;00m cbook[38;5;241m.[39m_setattr_cm([38;5;28mself[39m[38;5;241m.[39mfigure, dpi[38;5;241m=[39mdpi):
    [1;32m--> 959[0m     bbox, info, descent [38;5;241m=[39m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_get_layout[49m[43m([49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_renderer[49m[43m)[49m
    [0;32m    960[0m     x, y [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mget_unitless_position()
    [0;32m    961[0m     x, y [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mget_transform()[38;5;241m.[39mtransform((x, y))

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:373[0m, in [0;36mText._get_layout[1;34m(self, renderer)[0m
    [0;32m    370[0m ys [38;5;241m=[39m []
    [0;32m    372[0m [38;5;66;03m# Full vertical extent of font, including ascenders and descenders:[39;00m
    [1;32m--> 373[0m _, lp_h, lp_d [38;5;241m=[39m [43m_get_text_metrics_with_cache[49m[43m([49m
    [0;32m    374[0m [43m    [49m[43mrenderer[49m[43m,[49m[43m [49m[38;5;124;43m"[39;49m[38;5;124;43mlp[39;49m[38;5;124;43m"[39;49m[43m,[49m[43m [49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_fontproperties[49m[43m,[49m
    [0;32m    375[0m [43m    [49m[43mismath[49m[38;5;241;43m=[39;49m[38;5;124;43m"[39;49m[38;5;124;43mTeX[39;49m[38;5;124;43m"[39;49m[43m [49m[38;5;28;43;01mif[39;49;00m[43m [49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mget_usetex[49m[43m([49m[43m)[49m[43m [49m[38;5;28;43;01melse[39;49;00m[43m [49m[38;5;28;43;01mFalse[39;49;00m[43m,[49m[43m [49m[43mdpi[49m[38;5;241;43m=[39;49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mfigure[49m[38;5;241;43m.[39;49m[43mdpi[49m[43m)[49m
    [0;32m    376[0m min_dy [38;5;241m=[39m (lp_h [38;5;241m-[39m lp_d) [38;5;241m*[39m [38;5;28mself[39m[38;5;241m.[39m_linespacing
    [0;32m    378[0m [38;5;28;01mfor[39;00m i, line [38;5;129;01min[39;00m [38;5;28menumerate[39m(lines):

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:69[0m, in [0;36m_get_text_metrics_with_cache[1;34m(renderer, text, fontprop, ismath, dpi)[0m
    [0;32m     66[0m [38;5;250m[39m[38;5;124;03m"""Call ``renderer.get_text_width_height_descent``, caching the results."""[39;00m
    [0;32m     67[0m [38;5;66;03m# Cached based on a copy of fontprop so that later in-place mutations of[39;00m
    [0;32m     68[0m [38;5;66;03m# the passed-in argument do not mess up the cache.[39;00m
    [1;32m---> 69[0m [38;5;28;01mreturn[39;00m [43m_get_text_metrics_with_cache_impl[49m[43m([49m
    [0;32m     70[0m [43m    [49m[43mweakref[49m[38;5;241;43m.[39;49m[43mref[49m[43m([49m[43mrenderer[49m[43m)[49m[43m,[49m[43m [49m[43mtext[49m[43m,[49m[43m [49m[43mfontprop[49m[38;5;241;43m.[39;49m[43mcopy[49m[43m([49m[43m)[49m[43m,[49m[43m [49m[43mismath[49m[43m,[49m[43m [49m[43mdpi[49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:77[0m, in [0;36m_get_text_metrics_with_cache_impl[1;34m(renderer_ref, text, fontprop, ismath, dpi)[0m
    [0;32m     73[0m [38;5;129m@functools[39m[38;5;241m.[39mlru_cache([38;5;241m4096[39m)
    [0;32m     74[0m [38;5;28;01mdef[39;00m [38;5;21m_get_text_metrics_with_cache_impl[39m(
    [0;32m     75[0m         renderer_ref, text, fontprop, ismath, dpi):
    [0;32m     76[0m     [38;5;66;03m# dpi is unused, but participates in cache invalidation (via the renderer).[39;00m
    [1;32m---> 77[0m     [38;5;28;01mreturn[39;00m [43mrenderer_ref[49m[43m([49m[43m)[49m[38;5;241;43m.[39;49m[43mget_text_width_height_descent[49m[43m([49m[43mtext[49m[43m,[49m[43m [49m[43mfontprop[49m[43m,[49m[43m [49m[43mismath[49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backends\backend_agg.py:212[0m, in [0;36mRendererAgg.get_text_width_height_descent[1;34m(self, s, prop, ismath)[0m
    [0;32m    210[0m _api[38;5;241m.[39mcheck_in_list([[38;5;124m"[39m[38;5;124mTeX[39m[38;5;124m"[39m, [38;5;28;01mTrue[39;00m, [38;5;28;01mFalse[39;00m], ismath[38;5;241m=[39mismath)
    [0;32m    211[0m [38;5;28;01mif[39;00m ismath [38;5;241m==[39m [38;5;124m"[39m[38;5;124mTeX[39m[38;5;124m"[39m:
    [1;32m--> 212[0m     [38;5;28;01mreturn[39;00m [38;5;28;43msuper[39;49m[43m([49m[43m)[49m[38;5;241;43m.[39;49m[43mget_text_width_height_descent[49m[43m([49m[43ms[49m[43m,[49m[43m [49m[43mprop[49m[43m,[49m[43m [49m[43mismath[49m[43m)[49m
    [0;32m    214[0m [38;5;28;01mif[39;00m ismath:
    [0;32m    215[0m     ox, oy, width, height, descent, font_image [38;5;241m=[39m \
    [0;32m    216[0m         [38;5;28mself[39m[38;5;241m.[39mmathtext_parser[38;5;241m.[39mparse(s, [38;5;28mself[39m[38;5;241m.[39mdpi, prop)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backend_bases.py:597[0m, in [0;36mRendererBase.get_text_width_height_descent[1;34m(self, s, prop, ismath)[0m
    [0;32m    593[0m fontsize [38;5;241m=[39m prop[38;5;241m.[39mget_size_in_points()
    [0;32m    595[0m [38;5;28;01mif[39;00m ismath [38;5;241m==[39m [38;5;124m'[39m[38;5;124mTeX[39m[38;5;124m'[39m:
    [0;32m    596[0m     [38;5;66;03m# todo: handle properties[39;00m
    [1;32m--> 597[0m     [38;5;28;01mreturn[39;00m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mget_texmanager[49m[43m([49m[43m)[49m[38;5;241;43m.[39;49m[43mget_text_width_height_descent[49m[43m([49m
    [0;32m    598[0m [43m        [49m[43ms[49m[43m,[49m[43m [49m[43mfontsize[49m[43m,[49m[43m [49m[43mrenderer[49m[38;5;241;43m=[39;49m[38;5;28;43mself[39;49m[43m)[49m
    [0;32m    600[0m dpi [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mpoints_to_pixels([38;5;241m72[39m)
    [0;32m    601[0m [38;5;28;01mif[39;00m ismath:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\texmanager.py:363[0m, in [0;36mTexManager.get_text_width_height_descent[1;34m(cls, tex, fontsize, renderer)[0m
    [0;32m    361[0m [38;5;28;01mif[39;00m tex[38;5;241m.[39mstrip() [38;5;241m==[39m [38;5;124m'[39m[38;5;124m'[39m:
    [0;32m    362[0m     [38;5;28;01mreturn[39;00m [38;5;241m0[39m, [38;5;241m0[39m, [38;5;241m0[39m
    [1;32m--> 363[0m dvifile [38;5;241m=[39m [38;5;28;43mcls[39;49m[38;5;241;43m.[39;49m[43mmake_dvi[49m[43m([49m[43mtex[49m[43m,[49m[43m [49m[43mfontsize[49m[43m)[49m
    [0;32m    364[0m dpi_fraction [38;5;241m=[39m renderer[38;5;241m.[39mpoints_to_pixels([38;5;241m1.[39m) [38;5;28;01mif[39;00m renderer [38;5;28;01melse[39;00m [38;5;241m1[39m
    [0;32m    365[0m [38;5;28;01mwith[39;00m dviread[38;5;241m.[39mDvi(dvifile, [38;5;241m72[39m [38;5;241m*[39m dpi_fraction) [38;5;28;01mas[39;00m dvi:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\texmanager.py:295[0m, in [0;36mTexManager.make_dvi[1;34m(cls, tex, fontsize)[0m
    [0;32m    293[0m     [38;5;28;01mwith[39;00m TemporaryDirectory([38;5;28mdir[39m[38;5;241m=[39mcwd) [38;5;28;01mas[39;00m tmpdir:
    [0;32m    294[0m         tmppath [38;5;241m=[39m Path(tmpdir)
    [1;32m--> 295[0m         [38;5;28;43mcls[39;49m[38;5;241;43m.[39;49m[43m_run_checked_subprocess[49m[43m([49m
    [0;32m    296[0m [43m            [49m[43m[[49m[38;5;124;43m"[39;49m[38;5;124;43mlatex[39;49m[38;5;124;43m"[39;49m[43m,[49m[43m [49m[38;5;124;43m"[39;49m[38;5;124;43m-interaction=nonstopmode[39;49m[38;5;124;43m"[39;49m[43m,[49m[43m [49m[38;5;124;43m"[39;49m[38;5;124;43m--halt-on-error[39;49m[38;5;124;43m"[39;49m[43m,[49m
    [0;32m    297[0m [43m             [49m[38;5;124;43mf[39;49m[38;5;124;43m"[39;49m[38;5;124;43m--output-directory=[39;49m[38;5;132;43;01m{[39;49;00m[43mtmppath[49m[38;5;241;43m.[39;49m[43mname[49m[38;5;132;43;01m}[39;49;00m[38;5;124;43m"[39;49m[43m,[49m
    [0;32m    298[0m [43m             [49m[38;5;124;43mf[39;49m[38;5;124;43m"[39;49m[38;5;132;43;01m{[39;49;00m[43mtexfile[49m[38;5;241;43m.[39;49m[43mname[49m[38;5;132;43;01m}[39;49;00m[38;5;124;43m"[39;49m[43m][49m[43m,[49m[43m [49m[43mtex[49m[43m,[49m[43m [49m[43mcwd[49m[38;5;241;43m=[39;49m[43mcwd[49m[43m)[49m
    [0;32m    299[0m         (tmppath [38;5;241m/[39m Path(dvifile)[38;5;241m.[39mname)[38;5;241m.[39mreplace(dvifile)
    [0;32m    300[0m [38;5;28;01mreturn[39;00m dvifile

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\texmanager.py:258[0m, in [0;36mTexManager._run_checked_subprocess[1;34m(cls, command, tex, cwd)[0m
    [0;32m    254[0m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(
    [0;32m    255[0m         [38;5;124mf[39m[38;5;124m'[39m[38;5;124mFailed to process string with tex because [39m[38;5;132;01m{[39;00mcommand[[38;5;241m0[39m][38;5;132;01m}[39;00m[38;5;124m [39m[38;5;124m'[39m
    [0;32m    256[0m         [38;5;124m'[39m[38;5;124mcould not be found[39m[38;5;124m'[39m) [38;5;28;01mfrom[39;00m [38;5;21;01mexc[39;00m
    [0;32m    257[0m [38;5;28;01mexcept[39;00m subprocess[38;5;241m.[39mCalledProcessError [38;5;28;01mas[39;00m exc:
    [1;32m--> 258[0m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(
    [0;32m    259[0m         [38;5;124m'[39m[38;5;132;01m{prog}[39;00m[38;5;124m was not able to process the following string:[39m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    260[0m         [38;5;124m'[39m[38;5;132;01m{tex!r}[39;00m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    261[0m         [38;5;124m'[39m[38;5;124mHere is the full command invocation and its output:[39m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    262[0m         [38;5;124m'[39m[38;5;132;01m{format_command}[39;00m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    263[0m         [38;5;124m'[39m[38;5;132;01m{exc}[39;00m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m[38;5;241m.[39mformat(
    [0;32m    264[0m             prog[38;5;241m=[39mcommand[[38;5;241m0[39m],
    [0;32m    265[0m             format_command[38;5;241m=[39mcbook[38;5;241m.[39m_pformat_subprocess(command),
    [0;32m    266[0m             tex[38;5;241m=[39mtex[38;5;241m.[39mencode([38;5;124m'[39m[38;5;124municode_escape[39m[38;5;124m'[39m),
    [0;32m    267[0m             exc[38;5;241m=[39mexc[38;5;241m.[39moutput[38;5;241m.[39mdecode([38;5;124m'[39m[38;5;124mutf-8[39m[38;5;124m'[39m, [38;5;124m'[39m[38;5;124mbackslashreplace[39m[38;5;124m'[39m))
    [0;32m    268[0m         ) [38;5;28;01mfrom[39;00m [38;5;28;01mNone[39;00m
    [0;32m    269[0m _log[38;5;241m.[39mdebug(report)
    [0;32m    270[0m [38;5;28;01mreturn[39;00m report

    [1;31mRuntimeError[0m: latex was not able to process the following string:
    b'lp'

    Here is the full command invocation and its output:

    latex -interaction=nonstopmode --halt-on-error --output-directory=tmp5f577ce3 03c6366f7a4e307ef0b23ee8720251c2.tex

    This is pdfTeX, Version 3.141592653-2.6-1.40.25 (MiKTeX 24.1 Portable) (preloaded format=latex.fmt)
     restricted \write18 enabled.
    entering extended mode
    (03c6366f7a4e307ef0b23ee8720251c2.tex
    LaTeX2e <2023-11-01> patch level 1
    L3 programming layer <2024-01-04>

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\article.
    cls
    Document Class: article 2023/05/17 v1.4n Standard LaTeX document class

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\size10.c
    lo))

    ! LaTeX Error: File `type1cm.sty' not found.

    Type X to quit or <RETURN> to proceed,
    or enter new name. (Default extension: sty)

    Enter file name: 
    ! Emergency stop.
    <read *> 
             
    l.8 \usepackage
                   {type1ec}^^M
    No pages of output.
    Transcript written on C:\Users\eo\.matplotlib\tex.cache\03\c6\tmp5f577ce3\03c63
    66f7a4e307ef0b23ee8720251c2.log.
    latex: major issue: So far, you have not checked for MiKTeX updates.

    RuntimeError: latex was not able to process the following string:
    b'lp'

    Here is the full command invocation and its output:

    latex -interaction=nonstopmode --halt-on-error --output-directory=tmpsw2hjri_ 03c6366f7a4e307ef0b23ee8720251c2.tex

    This is pdfTeX, Version 3.141592653-2.6-1.40.25 (MiKTeX 24.1 Portable) (preloaded format=latex.fmt)
     restricted \write18 enabled.
    entering extended mode
    (03c6366f7a4e307ef0b23ee8720251c2.tex
    LaTeX2e <2023-11-01> patch level 1
    L3 programming layer <2024-01-04>

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\article.
    cls
    Document Class: article 2023/05/17 v1.4n Standard LaTeX document class

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\size10.c
    lo))

    ! LaTeX Error: File `type1cm.sty' not found.

    Type X to quit or <RETURN> to proceed,
    or enter new name. (Default extension: sty)

    Enter file name: 
    ! Emergency stop.
    <read *> 
             
    l.8 \usepackage
                   {type1ec}^^M
    No pages of output.
    Transcript written on C:\Users\eo\.matplotlib\tex.cache\03\c6\tmpsw2hjri_\03c63
    66f7a4e307ef0b23ee8720251c2.log.
    latex: major issue: So far, you have not checked for MiKTeX updates.



    [1;31m---------------------------------------------------------------------------[0m
    [1;31mRuntimeError[0m                              Traceback (most recent call last)
    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\IPython\core\formatters.py:343[0m, in [0;36mBaseFormatter.__call__[1;34m(self, obj)[0m
    [0;32m    341[0m     [38;5;28;01mpass[39;00m
    [0;32m    342[0m [38;5;28;01melse[39;00m:
    [1;32m--> 343[0m     [38;5;28;01mreturn[39;00m [43mprinter[49m[43m([49m[43mobj[49m[43m)[49m
    [0;32m    344[0m [38;5;66;03m# Finally look for special method names[39;00m
    [0;32m    345[0m method [38;5;241m=[39m get_real_method(obj, [38;5;28mself[39m[38;5;241m.[39mprint_method)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\IPython\core\pylabtools.py:170[0m, in [0;36mprint_figure[1;34m(fig, fmt, bbox_inches, base64, **kwargs)[0m
    [0;32m    167[0m     [38;5;28;01mfrom[39;00m [38;5;21;01mmatplotlib[39;00m[38;5;21;01m.[39;00m[38;5;21;01mbackend_bases[39;00m [38;5;28;01mimport[39;00m FigureCanvasBase
    [0;32m    168[0m     FigureCanvasBase(fig)
    [1;32m--> 170[0m [43mfig[49m[38;5;241;43m.[39;49m[43mcanvas[49m[38;5;241;43m.[39;49m[43mprint_figure[49m[43m([49m[43mbytes_io[49m[43m,[49m[43m [49m[38;5;241;43m*[39;49m[38;5;241;43m*[39;49m[43mkw[49m[43m)[49m
    [0;32m    171[0m data [38;5;241m=[39m bytes_io[38;5;241m.[39mgetvalue()
    [0;32m    172[0m [38;5;28;01mif[39;00m fmt [38;5;241m==[39m [38;5;124m'[39m[38;5;124msvg[39m[38;5;124m'[39m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backend_bases.py:2175[0m, in [0;36mFigureCanvasBase.print_figure[1;34m(self, filename, dpi, facecolor, edgecolor, orientation, format, bbox_inches, pad_inches, bbox_extra_artists, backend, **kwargs)[0m
    [0;32m   2172[0m     [38;5;66;03m# we do this instead of `self.figure.draw_without_rendering`[39;00m
    [0;32m   2173[0m     [38;5;66;03m# so that we can inject the orientation[39;00m
    [0;32m   2174[0m     [38;5;28;01mwith[39;00m [38;5;28mgetattr[39m(renderer, [38;5;124m"[39m[38;5;124m_draw_disabled[39m[38;5;124m"[39m, nullcontext)():
    [1;32m-> 2175[0m         [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mfigure[49m[38;5;241;43m.[39;49m[43mdraw[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   2176[0m [38;5;28;01mif[39;00m bbox_inches:
    [0;32m   2177[0m     [38;5;28;01mif[39;00m bbox_inches [38;5;241m==[39m [38;5;124m"[39m[38;5;124mtight[39m[38;5;124m"[39m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\artist.py:95[0m, in [0;36m_finalize_rasterization.<locals>.draw_wrapper[1;34m(artist, renderer, *args, **kwargs)[0m
    [0;32m     93[0m [38;5;129m@wraps[39m(draw)
    [0;32m     94[0m [38;5;28;01mdef[39;00m [38;5;21mdraw_wrapper[39m(artist, renderer, [38;5;241m*[39margs, [38;5;241m*[39m[38;5;241m*[39mkwargs):
    [1;32m---> 95[0m     result [38;5;241m=[39m [43mdraw[49m[43m([49m[43martist[49m[43m,[49m[43m [49m[43mrenderer[49m[43m,[49m[43m [49m[38;5;241;43m*[39;49m[43margs[49m[43m,[49m[43m [49m[38;5;241;43m*[39;49m[38;5;241;43m*[39;49m[43mkwargs[49m[43m)[49m
    [0;32m     96[0m     [38;5;28;01mif[39;00m renderer[38;5;241m.[39m_rasterizing:
    [0;32m     97[0m         renderer[38;5;241m.[39mstop_rasterizing()

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\artist.py:72[0m, in [0;36mallow_rasterization.<locals>.draw_wrapper[1;34m(artist, renderer)[0m
    [0;32m     69[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
    [0;32m     70[0m         renderer[38;5;241m.[39mstart_filter()
    [1;32m---> 72[0m     [38;5;28;01mreturn[39;00m [43mdraw[49m[43m([49m[43martist[49m[43m,[49m[43m [49m[43mrenderer[49m[43m)[49m
    [0;32m     73[0m [38;5;28;01mfinally[39;00m:
    [0;32m     74[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\figure.py:3162[0m, in [0;36mFigure.draw[1;34m(self, renderer)[0m
    [0;32m   3159[0m             [38;5;66;03m# ValueError can occur when resizing a window.[39;00m
    [0;32m   3161[0m     [38;5;28mself[39m[38;5;241m.[39mpatch[38;5;241m.[39mdraw(renderer)
    [1;32m-> 3162[0m     [43mmimage[49m[38;5;241;43m.[39;49m[43m_draw_list_compositing_images[49m[43m([49m
    [0;32m   3163[0m [43m        [49m[43mrenderer[49m[43m,[49m[43m [49m[38;5;28;43mself[39;49m[43m,[49m[43m [49m[43martists[49m[43m,[49m[43m [49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43msuppressComposite[49m[43m)[49m
    [0;32m   3165[0m     renderer[38;5;241m.[39mclose_group([38;5;124m'[39m[38;5;124mfigure[39m[38;5;124m'[39m)
    [0;32m   3166[0m [38;5;28;01mfinally[39;00m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\image.py:132[0m, in [0;36m_draw_list_compositing_images[1;34m(renderer, parent, artists, suppress_composite)[0m
    [0;32m    130[0m [38;5;28;01mif[39;00m not_composite [38;5;129;01mor[39;00m [38;5;129;01mnot[39;00m has_images:
    [0;32m    131[0m     [38;5;28;01mfor[39;00m a [38;5;129;01min[39;00m artists:
    [1;32m--> 132[0m         [43ma[49m[38;5;241;43m.[39;49m[43mdraw[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m    133[0m [38;5;28;01melse[39;00m:
    [0;32m    134[0m     [38;5;66;03m# Composite any adjacent images together[39;00m
    [0;32m    135[0m     image_group [38;5;241m=[39m []

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\artist.py:72[0m, in [0;36mallow_rasterization.<locals>.draw_wrapper[1;34m(artist, renderer)[0m
    [0;32m     69[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:
    [0;32m     70[0m         renderer[38;5;241m.[39mstart_filter()
    [1;32m---> 72[0m     [38;5;28;01mreturn[39;00m [43mdraw[49m[43m([49m[43martist[49m[43m,[49m[43m [49m[43mrenderer[49m[43m)[49m
    [0;32m     73[0m [38;5;28;01mfinally[39;00m:
    [0;32m     74[0m     [38;5;28;01mif[39;00m artist[38;5;241m.[39mget_agg_filter() [38;5;129;01mis[39;00m [38;5;129;01mnot[39;00m [38;5;28;01mNone[39;00m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axes\_base.py:3101[0m, in [0;36m_AxesBase.draw[1;34m(self, renderer)[0m
    [0;32m   3098[0m     [38;5;28;01mfor[39;00m spine [38;5;129;01min[39;00m [38;5;28mself[39m[38;5;241m.[39mspines[38;5;241m.[39mvalues():
    [0;32m   3099[0m         artists[38;5;241m.[39mremove(spine)
    [1;32m-> 3101[0m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_update_title_position[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   3103[0m [38;5;28;01mif[39;00m [38;5;129;01mnot[39;00m [38;5;28mself[39m[38;5;241m.[39maxison:
    [0;32m   3104[0m     [38;5;28;01mfor[39;00m _axis [38;5;129;01min[39;00m [38;5;28mself[39m[38;5;241m.[39m_axis_map[38;5;241m.[39mvalues():

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axes\_base.py:3045[0m, in [0;36m_AxesBase._update_title_position[1;34m(self, renderer)[0m
    [0;32m   3043[0m top [38;5;241m=[39m [38;5;28mmax[39m(top, bb[38;5;241m.[39mymax)
    [0;32m   3044[0m [38;5;28;01mif[39;00m title[38;5;241m.[39mget_text():
    [1;32m-> 3045[0m     [43max[49m[38;5;241;43m.[39;49m[43myaxis[49m[38;5;241;43m.[39;49m[43mget_tightbbox[49m[43m([49m[43mrenderer[49m[43m)[49m  [38;5;66;03m# update offsetText[39;00m
    [0;32m   3046[0m     [38;5;28;01mif[39;00m ax[38;5;241m.[39myaxis[38;5;241m.[39moffsetText[38;5;241m.[39mget_text():
    [0;32m   3047[0m         bb [38;5;241m=[39m ax[38;5;241m.[39myaxis[38;5;241m.[39moffsetText[38;5;241m.[39mget_tightbbox(renderer)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:1372[0m, in [0;36mAxis.get_tightbbox[1;34m(self, renderer, for_layout_only)[0m
    [0;32m   1369[0m     renderer [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mfigure[38;5;241m.[39m_get_renderer()
    [0;32m   1370[0m ticks_to_draw [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39m_update_ticks()
    [1;32m-> 1372[0m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_update_label_position[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   1374[0m [38;5;66;03m# go back to just this axis's tick labels[39;00m
    [0;32m   1375[0m tlb1, tlb2 [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39m_get_ticklabel_bboxes(ticks_to_draw, renderer)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:2654[0m, in [0;36mYAxis._update_label_position[1;34m(self, renderer)[0m
    [0;32m   2650[0m     [38;5;28;01mreturn[39;00m
    [0;32m   2652[0m [38;5;66;03m# get bounding boxes for this axis and any siblings[39;00m
    [0;32m   2653[0m [38;5;66;03m# that have been set by `fig.align_ylabels()`[39;00m
    [1;32m-> 2654[0m bboxes, bboxes2 [38;5;241m=[39m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_get_tick_boxes_siblings[49m[43m([49m[43mrenderer[49m[38;5;241;43m=[39;49m[43mrenderer[49m[43m)[49m
    [0;32m   2655[0m x, y [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mlabel[38;5;241m.[39mget_position()
    [0;32m   2656[0m [38;5;28;01mif[39;00m [38;5;28mself[39m[38;5;241m.[39mlabel_position [38;5;241m==[39m [38;5;124m'[39m[38;5;124mleft[39m[38;5;124m'[39m:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:2206[0m, in [0;36mAxis._get_tick_boxes_siblings[1;34m(self, renderer)[0m
    [0;32m   2204[0m axis [38;5;241m=[39m ax[38;5;241m.[39m_axis_map[name]
    [0;32m   2205[0m ticks_to_draw [38;5;241m=[39m axis[38;5;241m.[39m_update_ticks()
    [1;32m-> 2206[0m tlb, tlb2 [38;5;241m=[39m [43maxis[49m[38;5;241;43m.[39;49m[43m_get_ticklabel_bboxes[49m[43m([49m[43mticks_to_draw[49m[43m,[49m[43m [49m[43mrenderer[49m[43m)[49m
    [0;32m   2207[0m bboxes[38;5;241m.[39mextend(tlb)
    [0;32m   2208[0m bboxes2[38;5;241m.[39mextend(tlb2)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\axis.py:1351[0m, in [0;36mAxis._get_ticklabel_bboxes[1;34m(self, ticks, renderer)[0m
    [0;32m   1349[0m [38;5;28;01mif[39;00m renderer [38;5;129;01mis[39;00m [38;5;28;01mNone[39;00m:
    [0;32m   1350[0m     renderer [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mfigure[38;5;241m.[39m_get_renderer()
    [1;32m-> 1351[0m [38;5;28;01mreturn[39;00m ([[43mtick[49m[38;5;241;43m.[39;49m[43mlabel1[49m[38;5;241;43m.[39;49m[43mget_window_extent[49m[43m([49m[43mrenderer[49m[43m)[49m
    [0;32m   1352[0m          [38;5;28;01mfor[39;00m tick [38;5;129;01min[39;00m ticks [38;5;28;01mif[39;00m tick[38;5;241m.[39mlabel1[38;5;241m.[39mget_visible()],
    [0;32m   1353[0m         [tick[38;5;241m.[39mlabel2[38;5;241m.[39mget_window_extent(renderer)
    [0;32m   1354[0m          [38;5;28;01mfor[39;00m tick [38;5;129;01min[39;00m ticks [38;5;28;01mif[39;00m tick[38;5;241m.[39mlabel2[38;5;241m.[39mget_visible()])

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:959[0m, in [0;36mText.get_window_extent[1;34m(self, renderer, dpi)[0m
    [0;32m    954[0m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(
    [0;32m    955[0m         [38;5;124m"[39m[38;5;124mCannot get window extent of text w/o renderer. You likely [39m[38;5;124m"[39m
    [0;32m    956[0m         [38;5;124m"[39m[38;5;124mwant to call [39m[38;5;124m'[39m[38;5;124mfigure.draw_without_rendering()[39m[38;5;124m'[39m[38;5;124m first.[39m[38;5;124m"[39m)
    [0;32m    958[0m [38;5;28;01mwith[39;00m cbook[38;5;241m.[39m_setattr_cm([38;5;28mself[39m[38;5;241m.[39mfigure, dpi[38;5;241m=[39mdpi):
    [1;32m--> 959[0m     bbox, info, descent [38;5;241m=[39m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_get_layout[49m[43m([49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_renderer[49m[43m)[49m
    [0;32m    960[0m     x, y [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mget_unitless_position()
    [0;32m    961[0m     x, y [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mget_transform()[38;5;241m.[39mtransform((x, y))

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:373[0m, in [0;36mText._get_layout[1;34m(self, renderer)[0m
    [0;32m    370[0m ys [38;5;241m=[39m []
    [0;32m    372[0m [38;5;66;03m# Full vertical extent of font, including ascenders and descenders:[39;00m
    [1;32m--> 373[0m _, lp_h, lp_d [38;5;241m=[39m [43m_get_text_metrics_with_cache[49m[43m([49m
    [0;32m    374[0m [43m    [49m[43mrenderer[49m[43m,[49m[43m [49m[38;5;124;43m"[39;49m[38;5;124;43mlp[39;49m[38;5;124;43m"[39;49m[43m,[49m[43m [49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43m_fontproperties[49m[43m,[49m
    [0;32m    375[0m [43m    [49m[43mismath[49m[38;5;241;43m=[39;49m[38;5;124;43m"[39;49m[38;5;124;43mTeX[39;49m[38;5;124;43m"[39;49m[43m [49m[38;5;28;43;01mif[39;49;00m[43m [49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mget_usetex[49m[43m([49m[43m)[49m[43m [49m[38;5;28;43;01melse[39;49;00m[43m [49m[38;5;28;43;01mFalse[39;49;00m[43m,[49m[43m [49m[43mdpi[49m[38;5;241;43m=[39;49m[38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mfigure[49m[38;5;241;43m.[39;49m[43mdpi[49m[43m)[49m
    [0;32m    376[0m min_dy [38;5;241m=[39m (lp_h [38;5;241m-[39m lp_d) [38;5;241m*[39m [38;5;28mself[39m[38;5;241m.[39m_linespacing
    [0;32m    378[0m [38;5;28;01mfor[39;00m i, line [38;5;129;01min[39;00m [38;5;28menumerate[39m(lines):

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:69[0m, in [0;36m_get_text_metrics_with_cache[1;34m(renderer, text, fontprop, ismath, dpi)[0m
    [0;32m     66[0m [38;5;250m[39m[38;5;124;03m"""Call ``renderer.get_text_width_height_descent``, caching the results."""[39;00m
    [0;32m     67[0m [38;5;66;03m# Cached based on a copy of fontprop so that later in-place mutations of[39;00m
    [0;32m     68[0m [38;5;66;03m# the passed-in argument do not mess up the cache.[39;00m
    [1;32m---> 69[0m [38;5;28;01mreturn[39;00m [43m_get_text_metrics_with_cache_impl[49m[43m([49m
    [0;32m     70[0m [43m    [49m[43mweakref[49m[38;5;241;43m.[39;49m[43mref[49m[43m([49m[43mrenderer[49m[43m)[49m[43m,[49m[43m [49m[43mtext[49m[43m,[49m[43m [49m[43mfontprop[49m[38;5;241;43m.[39;49m[43mcopy[49m[43m([49m[43m)[49m[43m,[49m[43m [49m[43mismath[49m[43m,[49m[43m [49m[43mdpi[49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\text.py:77[0m, in [0;36m_get_text_metrics_with_cache_impl[1;34m(renderer_ref, text, fontprop, ismath, dpi)[0m
    [0;32m     73[0m [38;5;129m@functools[39m[38;5;241m.[39mlru_cache([38;5;241m4096[39m)
    [0;32m     74[0m [38;5;28;01mdef[39;00m [38;5;21m_get_text_metrics_with_cache_impl[39m(
    [0;32m     75[0m         renderer_ref, text, fontprop, ismath, dpi):
    [0;32m     76[0m     [38;5;66;03m# dpi is unused, but participates in cache invalidation (via the renderer).[39;00m
    [1;32m---> 77[0m     [38;5;28;01mreturn[39;00m [43mrenderer_ref[49m[43m([49m[43m)[49m[38;5;241;43m.[39;49m[43mget_text_width_height_descent[49m[43m([49m[43mtext[49m[43m,[49m[43m [49m[43mfontprop[49m[43m,[49m[43m [49m[43mismath[49m[43m)[49m

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backends\backend_agg.py:212[0m, in [0;36mRendererAgg.get_text_width_height_descent[1;34m(self, s, prop, ismath)[0m
    [0;32m    210[0m _api[38;5;241m.[39mcheck_in_list([[38;5;124m"[39m[38;5;124mTeX[39m[38;5;124m"[39m, [38;5;28;01mTrue[39;00m, [38;5;28;01mFalse[39;00m], ismath[38;5;241m=[39mismath)
    [0;32m    211[0m [38;5;28;01mif[39;00m ismath [38;5;241m==[39m [38;5;124m"[39m[38;5;124mTeX[39m[38;5;124m"[39m:
    [1;32m--> 212[0m     [38;5;28;01mreturn[39;00m [38;5;28;43msuper[39;49m[43m([49m[43m)[49m[38;5;241;43m.[39;49m[43mget_text_width_height_descent[49m[43m([49m[43ms[49m[43m,[49m[43m [49m[43mprop[49m[43m,[49m[43m [49m[43mismath[49m[43m)[49m
    [0;32m    214[0m [38;5;28;01mif[39;00m ismath:
    [0;32m    215[0m     ox, oy, width, height, descent, font_image [38;5;241m=[39m \
    [0;32m    216[0m         [38;5;28mself[39m[38;5;241m.[39mmathtext_parser[38;5;241m.[39mparse(s, [38;5;28mself[39m[38;5;241m.[39mdpi, prop)

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\backend_bases.py:597[0m, in [0;36mRendererBase.get_text_width_height_descent[1;34m(self, s, prop, ismath)[0m
    [0;32m    593[0m fontsize [38;5;241m=[39m prop[38;5;241m.[39mget_size_in_points()
    [0;32m    595[0m [38;5;28;01mif[39;00m ismath [38;5;241m==[39m [38;5;124m'[39m[38;5;124mTeX[39m[38;5;124m'[39m:
    [0;32m    596[0m     [38;5;66;03m# todo: handle properties[39;00m
    [1;32m--> 597[0m     [38;5;28;01mreturn[39;00m [38;5;28;43mself[39;49m[38;5;241;43m.[39;49m[43mget_texmanager[49m[43m([49m[43m)[49m[38;5;241;43m.[39;49m[43mget_text_width_height_descent[49m[43m([49m
    [0;32m    598[0m [43m        [49m[43ms[49m[43m,[49m[43m [49m[43mfontsize[49m[43m,[49m[43m [49m[43mrenderer[49m[38;5;241;43m=[39;49m[38;5;28;43mself[39;49m[43m)[49m
    [0;32m    600[0m dpi [38;5;241m=[39m [38;5;28mself[39m[38;5;241m.[39mpoints_to_pixels([38;5;241m72[39m)
    [0;32m    601[0m [38;5;28;01mif[39;00m ismath:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\texmanager.py:363[0m, in [0;36mTexManager.get_text_width_height_descent[1;34m(cls, tex, fontsize, renderer)[0m
    [0;32m    361[0m [38;5;28;01mif[39;00m tex[38;5;241m.[39mstrip() [38;5;241m==[39m [38;5;124m'[39m[38;5;124m'[39m:
    [0;32m    362[0m     [38;5;28;01mreturn[39;00m [38;5;241m0[39m, [38;5;241m0[39m, [38;5;241m0[39m
    [1;32m--> 363[0m dvifile [38;5;241m=[39m [38;5;28;43mcls[39;49m[38;5;241;43m.[39;49m[43mmake_dvi[49m[43m([49m[43mtex[49m[43m,[49m[43m [49m[43mfontsize[49m[43m)[49m
    [0;32m    364[0m dpi_fraction [38;5;241m=[39m renderer[38;5;241m.[39mpoints_to_pixels([38;5;241m1.[39m) [38;5;28;01mif[39;00m renderer [38;5;28;01melse[39;00m [38;5;241m1[39m
    [0;32m    365[0m [38;5;28;01mwith[39;00m dviread[38;5;241m.[39mDvi(dvifile, [38;5;241m72[39m [38;5;241m*[39m dpi_fraction) [38;5;28;01mas[39;00m dvi:

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\texmanager.py:295[0m, in [0;36mTexManager.make_dvi[1;34m(cls, tex, fontsize)[0m
    [0;32m    293[0m     [38;5;28;01mwith[39;00m TemporaryDirectory([38;5;28mdir[39m[38;5;241m=[39mcwd) [38;5;28;01mas[39;00m tmpdir:
    [0;32m    294[0m         tmppath [38;5;241m=[39m Path(tmpdir)
    [1;32m--> 295[0m         [38;5;28;43mcls[39;49m[38;5;241;43m.[39;49m[43m_run_checked_subprocess[49m[43m([49m
    [0;32m    296[0m [43m            [49m[43m[[49m[38;5;124;43m"[39;49m[38;5;124;43mlatex[39;49m[38;5;124;43m"[39;49m[43m,[49m[43m [49m[38;5;124;43m"[39;49m[38;5;124;43m-interaction=nonstopmode[39;49m[38;5;124;43m"[39;49m[43m,[49m[43m [49m[38;5;124;43m"[39;49m[38;5;124;43m--halt-on-error[39;49m[38;5;124;43m"[39;49m[43m,[49m
    [0;32m    297[0m [43m             [49m[38;5;124;43mf[39;49m[38;5;124;43m"[39;49m[38;5;124;43m--output-directory=[39;49m[38;5;132;43;01m{[39;49;00m[43mtmppath[49m[38;5;241;43m.[39;49m[43mname[49m[38;5;132;43;01m}[39;49;00m[38;5;124;43m"[39;49m[43m,[49m
    [0;32m    298[0m [43m             [49m[38;5;124;43mf[39;49m[38;5;124;43m"[39;49m[38;5;132;43;01m{[39;49;00m[43mtexfile[49m[38;5;241;43m.[39;49m[43mname[49m[38;5;132;43;01m}[39;49;00m[38;5;124;43m"[39;49m[43m][49m[43m,[49m[43m [49m[43mtex[49m[43m,[49m[43m [49m[43mcwd[49m[38;5;241;43m=[39;49m[43mcwd[49m[43m)[49m
    [0;32m    299[0m         (tmppath [38;5;241m/[39m Path(dvifile)[38;5;241m.[39mname)[38;5;241m.[39mreplace(dvifile)
    [0;32m    300[0m [38;5;28;01mreturn[39;00m dvifile

    File [1;32mc:\Users\eo\.pyenv\pyenv-win\versions\3.12.5\Lib\site-packages\matplotlib\texmanager.py:258[0m, in [0;36mTexManager._run_checked_subprocess[1;34m(cls, command, tex, cwd)[0m
    [0;32m    254[0m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(
    [0;32m    255[0m         [38;5;124mf[39m[38;5;124m'[39m[38;5;124mFailed to process string with tex because [39m[38;5;132;01m{[39;00mcommand[[38;5;241m0[39m][38;5;132;01m}[39;00m[38;5;124m [39m[38;5;124m'[39m
    [0;32m    256[0m         [38;5;124m'[39m[38;5;124mcould not be found[39m[38;5;124m'[39m) [38;5;28;01mfrom[39;00m [38;5;21;01mexc[39;00m
    [0;32m    257[0m [38;5;28;01mexcept[39;00m subprocess[38;5;241m.[39mCalledProcessError [38;5;28;01mas[39;00m exc:
    [1;32m--> 258[0m     [38;5;28;01mraise[39;00m [38;5;167;01mRuntimeError[39;00m(
    [0;32m    259[0m         [38;5;124m'[39m[38;5;132;01m{prog}[39;00m[38;5;124m was not able to process the following string:[39m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    260[0m         [38;5;124m'[39m[38;5;132;01m{tex!r}[39;00m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    261[0m         [38;5;124m'[39m[38;5;124mHere is the full command invocation and its output:[39m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    262[0m         [38;5;124m'[39m[38;5;132;01m{format_command}[39;00m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m
    [0;32m    263[0m         [38;5;124m'[39m[38;5;132;01m{exc}[39;00m[38;5;130;01m\n[39;00m[38;5;130;01m\n[39;00m[38;5;124m'[39m[38;5;241m.[39mformat(
    [0;32m    264[0m             prog[38;5;241m=[39mcommand[[38;5;241m0[39m],
    [0;32m    265[0m             format_command[38;5;241m=[39mcbook[38;5;241m.[39m_pformat_subprocess(command),
    [0;32m    266[0m             tex[38;5;241m=[39mtex[38;5;241m.[39mencode([38;5;124m'[39m[38;5;124municode_escape[39m[38;5;124m'[39m),
    [0;32m    267[0m             exc[38;5;241m=[39mexc[38;5;241m.[39moutput[38;5;241m.[39mdecode([38;5;124m'[39m[38;5;124mutf-8[39m[38;5;124m'[39m, [38;5;124m'[39m[38;5;124mbackslashreplace[39m[38;5;124m'[39m))
    [0;32m    268[0m         ) [38;5;28;01mfrom[39;00m [38;5;28;01mNone[39;00m
    [0;32m    269[0m _log[38;5;241m.[39mdebug(report)
    [0;32m    270[0m [38;5;28;01mreturn[39;00m report

    [1;31mRuntimeError[0m: latex was not able to process the following string:
    b'lp'

    Here is the full command invocation and its output:

    latex -interaction=nonstopmode --halt-on-error --output-directory=tmpsw2hjri_ 03c6366f7a4e307ef0b23ee8720251c2.tex

    This is pdfTeX, Version 3.141592653-2.6-1.40.25 (MiKTeX 24.1 Portable) (preloaded format=latex.fmt)
     restricted \write18 enabled.
    entering extended mode
    (03c6366f7a4e307ef0b23ee8720251c2.tex
    LaTeX2e <2023-11-01> patch level 1
    L3 programming layer <2024-01-04>

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\article.
    cls
    Document Class: article 2023/05/17 v1.4n Standard LaTeX document class

    (C:\ProgramData\scoop\apps\latex\current\texmfs\install\tex/latex/base\size10.c
    lo))

    ! LaTeX Error: File `type1cm.sty' not found.

    Type X to quit or <RETURN> to proceed,
    or enter new name. (Default extension: sty)

    Enter file name: 
    ! Emergency stop.
    <read *> 
             
    l.8 \usepackage
                   {type1ec}^^M
    No pages of output.
    Transcript written on C:\Users\eo\.matplotlib\tex.cache\03\c6\tmpsw2hjri_\03c63
    66f7a4e307ef0b23ee8720251c2.log.
    latex: major issue: So far, you have not checked for MiKTeX updates.

    <Figure size 2960x560 with 6 Axes>
