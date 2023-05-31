import math

def calculate_midpoint(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Calculate the differences between the coordinates
    dlon = lon2_rad - lon1_rad

    # Calculate the midpoint latitude
    Bx = math.cos(lat2_rad) * math.cos(dlon)
    By = math.cos(lat2_rad) * math.sin(dlon)
    lat3_rad = math.atan2(math.sin(lat1_rad) + math.sin(lat2_rad), math.sqrt((math.cos(lat1_rad) + Bx) ** 2 + By ** 2))

    # Calculate the midpoint longitude
    lon3_rad = lon1_rad + math.atan2(By, math.cos(lat1_rad) + Bx)

    # Convert the midpoint latitude and longitude back to degrees
    lat3 = math.degrees(lat3_rad)
    lon3 = math.degrees(lon3_rad)

    return lat3, lon3

# Example usage
lat1 = 40.7128  # Latitude of Place 1
lon1 = -74.0060  # Longitude of Place 1

lat2 = 34.0522  # Latitude of Place 2
lon2 = -118.2437  # Longitude of Place 2

midpoint_lat, midpoint_lon = calculate_midpoint(lat1, lon1, lat2, lon2)

print("Midpoint Coordinates:")
print(f"Latitude: {midpoint_lat}")
print(f"Longitude: {midpoint_lon}")
