from django.shortcuts import render
from .models import Bmi

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, LassoSelectTool, WheelZoomTool, PointDrawTool, ColumnDataSource
# Create your views here.
def home(request) :
    context={}
    if request.method=="POST":
        weight_metric=request.POST.get("weight-metric")
        weight_imperial=request.POST.get("weight-imperial")

        if weight_metric:
            weight=float(request.POST.get("weight-metric"))
            height=float(request.POST.get("height-metric"))
        elif weight_imperial:
            weight=float(request.POST.get("weight-metric"))/2.205
            weight=(float(request.POST.get("feet"))*30.48 + float(request.POST.get("inches"))*2.54)/100

        bmi=(weight/(height**2))
        save=request.POST.get("save")
        if save=="on":
            Bmi.objects.create(user=request.user, weight=weight, height=height, bmi=round(bmi))

        if bmi < 16:
            state="Severe Thinness"
        elif bmi>16 and bmi < 17:
            state="Moderate Thinness"
        elif bmi>17 and bmi < 18:
            state="Mild Thinness"
        elif bmi>18 and bmi < 25:
            state="Normal"
        elif bmi>25 and bmi < 30:
            state="Overweight"
        elif bmi>30 and bmi < 35:
            state="Obese class 1"
        elif bmi>35 and bmi < 40:
            state="Obese class 2"
        elif bmi>40:
            state="Obess clss 3"
        context["bmi"]=round(bmi)
        context["state"]=state


        if request.user.is_authenticated:
            dates=[]
            bmis=[]
            dates_queryset=Bmi.objects.all().filter(user, request.user)
            for qr in dates_queryset:
                dates.append(str(qr.date))
                bmis.append(int(qr.bmi))


            plot=figure(x_range=dates, plot_height=600, plot_width=600, title="Bmi Statistics", toolbar_location="right", tools="")
            plot.title.text_font_size="20pt"

            plot.xaxis.major_label_text_font_size="14pt"

            plot.step(dates, bmis, line_width=2)
            plot.legend.label_text_font_size='14pt'


            script, div = components(plot)
            context["script"]=script
            context["div"]=div


    return render(request,"index.html",context)
