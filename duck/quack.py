import os

import duckdb
import geojson


def bounding_box(gpx_file_path: str) -> str:
    # return bounding box
    with duckdb.connect("data/database.db") as con:
        con.install_extension("spatial")
        con.load_extension("spatial")
        bbox = con.sql(
            f"""SELECT ST_AsGeoJSON(ST_Extent(geom)) FROM ST_Read('{gpx_file_path}', layer='tracks');"""
        ).fetchone()
    BOX_2D = geojson.loads(bbox[0])
    BOX_2D_COORDS = list(geojson.utils.coords(BOX_2D))
    return f"{BOX_2D_COORDS[0][1]}, {BOX_2D_COORDS[0][0]}, {BOX_2D_COORDS[2][1]}, {BOX_2D_COORDS[2][0]}"  # latitude of the southern edge, longitude of the western edge, latitude of the northern edge, longitude of the eastern edge,


def get_geojson(gpx_file_path: str) -> str:
    with duckdb.connect("data/database.db") as con:
        con.install_extension("spatial")
        con.load_extension("spatial")
        geojson = con.sql(
            f"""SELECT ST_AsGeoJSON(geom) FROM ST_Read('{gpx_file_path}', layer='tracks');"""
        ).fetchone()[0]
    return geojson


def main():
    return


if __name__ == "__main__":
    main()
