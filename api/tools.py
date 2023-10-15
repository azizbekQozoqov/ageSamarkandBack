import mapnik #type: ignore
import math

def rule(start: int , end: int, davr: tuple, color: str):
    r = mapnik.Rule()
    f = mapnik.Filter(f"([date] > {start}) and ([date] <= {end}) and ([date] > {davr[0]} and [date] <= {davr[-1]})")
    polygon_symbolizer = mapnik.PolygonSymbolizer()
    polygon_symbolizer.fill = mapnik.Color(color)
    r.filter = f
    r.symbols.append(polygon_symbolizer)
    return r

def colorize(start: int = 1000, end: int = 2023):
    s = mapnik.Style()
    s.rules.extend([
        rule(-10, 10, (-start, end), '#cfd1d1'),
        rule(1000, 1878, (start, end), '#f5fe95'),
        rule(1878, 1917, (start, end), '#ffb301'),
        rule(1917, 1958, (start, end), '#ff7801'),
        rule(1958, 1966, (start, end), '#ff0109'),
        rule(1966, 1984, (start, end), '#ff017c'),
        rule(1984, 1991, (start, end), '#0066fe'),
        rule(1991, 2000, (start, end), '#0066fe'),
        rule(2000, 2008, (start, end), '#0066fe'),
        rule(2008, 2016, (start, end), '#0066fe'),
        rule(2016, 2022, (start, end), '#0066fe'),
        rule(2022, 9000, (start, end), '#7d7d7d')
    ])
    return s

def calculate_bbox(z, x, y):
    minx, miny = tile_to_lonlat(x, y, z)
    maxx, maxy = tile_to_lonlat(x + 1, y + 1, z)
    return mapnik.Box2d(minx=minx, miny=miny, maxx=maxx, maxy=maxy)

def tile_to_lonlat(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return lon_deg, lat_deg