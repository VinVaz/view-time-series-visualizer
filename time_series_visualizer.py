import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as ticker
import matplotlib.dates as mpl_dates
from pandas.plotting import register_matplotlib_converters



register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', )
df = df.set_index(['date'])

df.index = pd.to_datetime(df.index,format='%Y-%m-%d')

# Clean data:
# Page views that were in the top 2.5% of the dataset
df = df[df['value'] <= df['value'].quantile(97.5/100)]

# Page views that were in the bottom 2.5% of the dataset.
df = df[df['value'] >= df['value'].quantile(2.5/100)]

sns.set_style('white')

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    
    fig.set_figheight(5.61)
    fig.set_figwidth(18)
    ax.plot_date(df.index,
                 df['value'], 
                 color='#d62728',
                 linestyle='solid',
                 linewidth = 1.8,
                 marker=None)
             
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019',fontsize=14.1 )
    ax.set_xlabel('Date', fontsize=12.7)
    ax.set_ylabel('Page Views', fontsize=12.7)
    ax.tick_params(axis='both', which='major', labelsize=12.7)    
 
    ax.xaxis.set_major_locator(ticker.MultipleLocator(6*29))
    
    # format strings of axis "x"
    date_format = mpl_dates.DateFormatter('%Y-%m')
    ax.xaxis.set_major_formatter(date_format)    
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['month'] = df.index.strftime('%B')
    df_bar['year'] = df.index.strftime('%Y')
    
    df_bar = df_bar.groupby(['year', 'month']).mean()
    df_bar = df_bar.unstack('month')
    
    df_bar.columns = df_bar.columns.map(lambda x: x[1])
    df_bar.columns.name = 'Months'
    new_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar.reindex(new_order, axis=1)
    
    # Draw bar plot
    plot = df_bar.plot(kind='bar')
    plot.set_xlabel('Years')
    plot.set_ylabel('Average Page Views')    
    fig = plot.get_figure()
    
    # The legend should show month labels and have a title of "Months".


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
