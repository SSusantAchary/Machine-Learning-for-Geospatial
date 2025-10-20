#!/usr/bin/env python3
"""
Compute zonal statistics for raster tiles defined by a grid GeoJSON.

Usage:
    python raster_tile_stats.py --raster data/ndvi.tif --grid data/tiles.geojson --out stats.csv
"""

import argparse
import json
from pathlib import Path

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask


def zonal_stats(raster_path: Path, grid_path: Path) -> gpd.GeoDataFrame:
    """Return mean, min, max for each tile geometry."""
    grid = gpd.read_file(grid_path)
    with rasterio.open(raster_path) as src:
        stats = []
        for feature in grid.itertuples():
            geometry = json.loads(feature.geometry.to_json())
            data, _ = mask(src, [geometry], crop=True, filled=False)
            flat = data[0].compressed()
            if flat.size == 0:
                stats.append({"mean": np.nan, "min": np.nan, "max": np.nan})
            else:
                stats.append(
                    {"mean": float(flat.mean()), "min": float(flat.min()), "max": float(flat.max())}
                )

    return grid.join(gpd.GeoDataFrame(stats))


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute raster tile statistics.")
    parser.add_argument("--raster", type=Path, required=True, help="Input raster (GeoTIFF).")
    parser.add_argument("--grid", type=Path, required=True, help="Tile polygons (GeoJSON/GeoPackage).")
    parser.add_argument("--out", type=Path, required=True, help="Output CSV path.")
    args = parser.parse_args()

    result = zonal_stats(args.raster, args.grid)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.out, index=False)
    print(f"Saved stats to {args.out.resolve()}")


if __name__ == "__main__":
    main()
