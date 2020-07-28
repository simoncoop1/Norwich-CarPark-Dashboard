import bng
import pyproj

# Define coordinate systems
wgs84=pyproj.CRS("EPSG:4326") # LatLon with WGS84 datum used by GPS units and Google Earth
osgb36=pyproj.CRS("EPSG:27700") # UK Ordnance Survey, 1936 datum

# Transform
#x, y = bng.to_osgb36('NT2755072950')
x , y = 538890, 177320
res = pyproj.transform(osgb36, wgs84, x, y)
# (55.94410954187127, -3.1615548049941133i)
print(res)
