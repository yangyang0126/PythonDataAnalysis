# Python数据可视化

## [Plotly](https://plot.ly/python/)

Released: Apr 1, 2020

```
pip install plotly
```

![image-20200403120520213](../../job/upload/image-20200403120520213.png)

![image-20200403120540838](../../job/upload/image-20200403120540838.png)

## [Bokeh](http://bokeh.pydata.org/en/latest/)

Released: Mar 30, 2020

```
pip install bokeh
```

```python
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, factor_cmap

output_file("periodic.html")

periods = ["I", "II", "III", "IV", "V", "VI", "VII"]
groups = [str(x) for x in range(1, 19)]

df = elements.copy()
df["atomic mass"] = df["atomic mass"].astype(str)
df["group"] = df["group"].astype(str)
df["period"] = [periods[x-1] for x in df.period]
df = df[df.group != "-"]
df = df[df.symbol != "Lr"]
df = df[df.symbol != "Lu"]

cmap = {
    "alkali metal"         : "#a6cee3",
    "alkaline earth metal" : "#1f78b4",
    "metal"                : "#d93b43",
    "halogen"              : "#999d9a",
    "metalloid"            : "#e08d49",
    "noble gas"            : "#eaeaea",
    "nonmetal"             : "#f1d4Af",
    "transition metal"     : "#599d7A",
}

TOOLTIPS = [
    ("Name", "@name"),
    ("Atomic number", "@{atomic number}"),
    ("Atomic mass", "@{atomic mass}"),
    ("Type", "@metal"),
    ("CPK color", "$color[hex, swatch]:CPK"),
    ("Electronic configuration", "@{electronic configuration}"),
]

p = figure(title="Periodic Table (omitting LA and AC Series)", plot_width=1000, plot_height=450,
           x_range=groups, y_range=list(reversed(periods)),
           tools="hover", toolbar_location=None, tooltips=TOOLTIPS)

r = p.rect("group", "period", 0.95, 0.95, source=df, fill_alpha=0.6, legend_field="metal",
           color=factor_cmap('metal', palette=list(cmap.values()), factors=list(cmap.keys())))

text_props = {"source": df, "text_align": "left", "text_baseline": "middle"}

x = dodge("group", -0.4, range=p.x_range)

p.text(x=x, y="period", text="symbol", text_font_style="bold", **text_props)

p.text(x=x, y=dodge("period", 0.3, range=p.y_range), text="atomic number",
       text_font_size="11px", **text_props)

p.text(x=x, y=dodge("period", -0.35, range=p.y_range), text="name",
       text_font_size="7px", **text_props)

p.text(x=x, y=dodge("period", -0.2, range=p.y_range), text="atomic mass",
       text_font_size="7px", **text_props)

p.text(x=["3", "3"], y=["VI", "VII"], text=["LA", "AC"], text_align="center", text_baseline="middle")

p.outline_line_color = None
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_standoff = 0
p.legend.orientation = "horizontal"
p.legend.location ="top_center"
p.hover.renderers = [r] # only hover element boxes

show(p)
```



![1559200278332](assets/1559200278332.png)



## [matplotlib](https://matplotlib.org/index.html)

Released: Mar 19, 2020

```
pip install matplotlib
```

![image-20200403120815152](../../job/upload/image-20200403120815152.png)

## [Seaborn](http://seaborn.pydata.org/index.html)

Released: Jan 24, 2020

```
pip install seaborn
```

![](assets/1559198332859.png)

## [missingno](https://github.com/ResidentMario/missingno)

Released: Jul 10, 2019

```
pip install missingno
```

![image-20200403120658930](../../job/upload/image-20200403120658930.png)

## [pygal](http://www.pygal.org/en/stable/)

Released: Jul 5, 2017

```
pip install pygal
```

![image-20200403120306247](../../job/upload/image-20200403120306247.png)



## [Leather](https://leather.readthedocs.io/en/latest/index.html)

Released: Dec 1, 2016

```
pip install leather
```

![img](https://leather.readthedocs.io/en/latest/_images/colorized_dots.svg)



## [ggplot](http://ggplot.yhathq.com/)

Released: Sep 30, 2016

```
pip install ggplot
```

![image-20200403123342296](../../job/upload/image-20200403123342296.png)

## [geoplotlib](https://github.com/andrea-cuttone/geoplotlib)

Released: Jul 27, 2016

```
pip install geoplotlib
```

![image-20200403124105206](../../job/upload/image-20200403124105206.png)

## [Gleam](https://github.com/dgrtwo/gleam)

Released: Apr 10, 2014

pip install gleam

![image-20200403120925766](../../job/upload/image-20200403120925766.png)

