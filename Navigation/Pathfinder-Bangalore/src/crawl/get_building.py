import logging
from pathlib import Path
import osmnx as ox
from shapely.geometry import MultiPolygon
import pandas as pd
from typing import Optional

# Constants and Configurations
DEFAULT_EPSG_CODE = "EPSG:4326"
DEFAULT_OUTPUT_DIR = Path(r"D:\Work\experiments_here\Github_codes\Navigation\Pathfinder-Bangalore")
DEFAULT_PLACE_NAME = "Bangalore, India"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def fetch_building_data(place_name: str) -> Optional[pd.DataFrame]:
    """
    Fetch building data from OpenStreetMap for a given place.
    
    Args:
        place_name (str): The name of the place to fetch data for.
    
    Returns:
        pd.DataFrame | None: A DataFrame with building data or None if an error occurs.
    """
    try:
        logger.info(f"Fetching building data for {place_name}...")
        building_data = ox.features_from_place(place_name, tags={"building": True})
        logger.info(f"Successfully fetched {len(building_data)} building entries.")
        return building_data
    except Exception as e:
        logger.error(f"Error fetching building data: {e}")
        return None

def process_building_data(building_data: pd.DataFrame, epsg_code: str) -> Optional[pd.DataFrame]:
    """
    Process building data by converting geometries and calculating centroids.
    
    Args:
        building_data (pd.DataFrame): The raw building data DataFrame.
        epsg_code (str): The EPSG code for coordinate reference system.
    
    Returns:
        pd.DataFrame: The processed DataFrame with centroid and latitude/longitude columns.
    """
    try:
        logger.info("Preprocessing building data...")

        # Convert geometries to MultiPolygon if needed
        building_data["geometry"] = building_data["geometry"].apply(
            lambda x: MultiPolygon([x]) if x.geom_type == "Polygon" else x
        )

        # Calculate centroids
        building_data["centroid"] = building_data["geometry"].centroid

        # Extract latitude and longitude
        building_data["latitude"] = building_data["centroid"].y
        building_data["longitude"] = building_data["centroid"].x

        # Reproject data to the desired CRS
        building_data = building_data.set_crs(epsg_code, allow_override=True)

        # Select relevant columns
        selected_cols = ["amenity", "building", "name", "geometry", "latitude", "longitude"]
        building_data = building_data[selected_cols]

        # Drop rows with missing values
        building_data.dropna(subset=["latitude", "longitude"], inplace=True)

        # Remove duplicates
        building_data.drop_duplicates(subset=["latitude", "longitude"], inplace=True)

        logger.info("Preprocessing completed.")
        return building_data
    except Exception as e:
        logger.error(f"Error in preprocessing building data: {e}")
        return None

def validate_data(building_data: pd.DataFrame) -> bool:
    """
    Validate the integrity and quality of the processed data.

    Args:
        building_data (pd.DataFrame): Processed building data.

    Returns:
        bool: True if validation passes, False otherwise.
    """
    try:
        logger.info("Validating data...")
        if building_data.isnull().sum().any():
            logger.warning("Data contains missing values.")
        if building_data.duplicated(subset=["latitude", "longitude"]).any():
            logger.warning("Data contains duplicate entries.")
        invalid_geometries = building_data[~building_data["geometry"].is_valid]
        if not invalid_geometries.empty:
            logger.warning(f"Found {len(invalid_geometries)} invalid geometries.")
        logger.info("Validation completed.")
        return True
    except Exception as e:
        logger.error(f"Error in data validation: {e}")
        return False

def save_data(building_data: pd.DataFrame, output_dir: Path, file_name: str) -> None:
    """
    Save the processed building data to a CSV file.
    
    Args:
        building_data (pd.DataFrame): The processed building data.
        output_dir (Path): The directory where the CSV file will be saved.
        file_name (str): The name of the output CSV file.
    """
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / file_name
        building_data.to_csv(output_path, index=False)
        logger.info(f"Data saved to {output_path}")
    except Exception as e:
        logger.error(f"Error saving data: {e}")

def crawl_buildings_data(
    place_name: str = DEFAULT_PLACE_NAME,
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    epsg_code: str = DEFAULT_EPSG_CODE,
) -> None:
    """
    Main function to crawl building data, process it, and save it to files.
    
    Args:
        place_name (str): The place name for which to fetch data.
        output_dir (Path): Directory to save the processed data.
        epsg_code (str): The EPSG code for coordinate reference system.
    """
    # Step 1: Fetch the data
    building_data = fetch_building_data(place_name)
    if building_data is None:
        logger.error("Failed to fetch building data. Exiting.")
        return

    # Step 2: Process the data
    building_data = process_building_data(building_data, epsg_code)
    if building_data is None:
        logger.error("Failed to process building data. Exiting.")
        return

    # Step 3: Validate the data
    if not validate_data(building_data):
        logger.error("Data validation failed. Exiting.")
        return

    # Step 4: Save the processed data
    save_data(building_data, output_dir, "bangalore_buildings.csv")
    save_data(building_data[building_data["name"].notnull()], output_dir, "potential_landmarks.csv")

if __name__ == "__main__":
    crawl_buildings_data()
