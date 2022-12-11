import cartopy.crs as ccrs

def update(k, fig_title):
    plt.cla()
    ax = plt.axes(projection=ccrs.Orthographic(central_longitude=(-k),central_latitude=0))
    ax.coastlines()
    plt.title(fig_title)