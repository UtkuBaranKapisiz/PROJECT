import pandas as pd
import numpy as np
import geopy as gpy


def find_distance(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5


main = pd.read_csv("earthquake.csv")

df = pd.DataFrame({
    "id": (i for i in range(1, 24008)),
    "date": main.date,
    "lat": main.lat,
    "long": main.long,
    "dir": main.direction,
    "dist": main.dist,
    "depth": main.depth,
    "max": main.xm,
    "time_dep": main.md,
    "richter": main.richter,
    "moment": main.mw,
    "surface": main.ms,
    "body": main.mb,
    "tier1_dist": 0,
    "tier2_dist": 0,
    "tier3_dist": 0
})
# Fill null values with 0's
df = df.fillna(0)

# Numpy array of "fay noktaları"
points = np.array(
    [[40.73269, 29.8526], [41.11868, 34.20044], [38.76265, 41.14105], [36.88841, 36.5062], [39.3258, 27.79541], [37.83148, 27.24884], [37.55329, 29.11926], [38.41486, 39.46838], [37.9377, 37.63641], [40.40304, 27.04834]])

point_coord = points[0]
location_coord = df.iloc[0][["lat", "long"]].to_numpy()

print(find_distance(point_coord, location_coord))
print(df)
