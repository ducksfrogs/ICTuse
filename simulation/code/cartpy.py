import cartpy.crs as ccrs

def update(k, fig_title):
    plt.cla()
    ax = plt.axes(projection=ccrs.Orthrographic(central_longitude))
