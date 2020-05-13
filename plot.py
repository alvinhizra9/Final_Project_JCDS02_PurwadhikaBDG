from data import data_clean
import plotly
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas
import numpy
import json

def barplot(col='Province'):
    df = data_clean()
    cat=df[col].unique()
    fig1 = go.Figure(data=[
    go.Bar(name='Not Default', x=cat, 
        y=[df[(df[col]==i) & (df['Status']=='Not Default')][col].count() 
            for i in df[col].unique()],
        text=[df[(df[col]==i) & (df['Status']=='Not Default')][col].count() 
            for i in df[col].unique()],
            hovertemplate = 'Province: %{x}<extra></extra>'+'<br><b>Count</b>: %{y}<br>'),
    go.Bar(name='Default', x=cat, 
        y=[df[(df[col]==i) & (df['Status']=='Default')][col].count() 
            for i in df[col].unique()],
        text=[df[(df[col]==i) & (df['Status']=='Default')][col].count() 
            for i in df[col].unique()],
            hovertemplate = 'Province: %{x}<extra></extra>'+'<br><b>Count</b>: %{y}<br>')
    ])
    fig1 = fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    fig1 = fig1.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig1 = fig1.update_layout(barmode='stack')
    fig1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return fig1

def heatmap():
    z = [[149998.75347168, 137972.44034091, 146588.02379421,
        148730.89841737, 143841.18965517, 139194.24362606,
        144654.05357143],
        [151117.72834937, 145744.40915888, 146511.74582405,
        147239.7073058 , 166768.98221344, 137944.29436239,
        111214.5       ],
        [143769.65436788, 145873.16439942, 154258.84943182,
        162740.46232277, 142873.9088423 , 162431.35563581,
        144222.78080158]]

    z_text = [['O', 'P', 'Q', 'R', 'S', 'T', 'U'],
        ['H', 'I', 'J', 'K', 'L', 'M', 'N'],
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']]

    fig2 = ff.create_annotated_heatmap(z, annotation_text=z_text, colorscale='Viridis', 
    showscale = True,text=z_text,hovertemplate = 'Province: %{text}<extra></extra>'+
    '<br><b>Loan Amount</b>: %{z}<br>')
    fig2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return fig2

def distplot1():
    df = data_clean()
    fig3 = go.Figure()
    fig3 = fig3.add_trace(go.Histogram(name='Not Default',x=df[df['Status']=='Not Default']['Age'],
                            hovertemplate = 'Age: %{x:.2f}<extra></extra>'+'<br><b>Dist</b>: %{y}<br>'))
    fig3 = fig3.add_trace(go.Histogram(name='Default',x=df[df['Status']=='Default']['Age'],
                           hovertemplate = 'Age: %{x:.2f}<extra></extra>'+'<br><b>Dist</b>: %{y}<br>'))

    # Overlay both histograms
    fig3 = fig3.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    fig3 = fig3.update_traces(opacity=0.75)
    fig3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return fig3

def distplot2():
    df = data_clean()
    fig4 = go.Figure()
    fig4 =fig4.add_trace(go.Histogram(name='Not Default',x=df[df['Status']=='Not Default']['Loan Amount'],nbinsx=50,
                            hovertemplate = 'Loan Amount: %{x:.2f}<extra></extra>'+'<br><b>Dist</b>: %{y}<br>'))
    fig4 =fig4.add_trace(go.Histogram(name='Default',x=df[df['Status']=='Default']['Loan Amount'],nbinsx=50,
                            hovertemplate = 'Loan Amount: %{x:.2f}<extra></extra>'+'<br><b>Dist</b>: %{y}<br>'))

    # Overlay both histograms
    fig4 =fig4.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    fig4 =fig4.update_traces(opacity=0.75)
    fig4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)
    return fig4