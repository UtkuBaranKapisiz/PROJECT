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
    [[40.73269, 29.8526], [41.11868, 34.20044], [38.76265, 41.14105],
     [36.88841, 36.5062], [39.3258, 27.79541], [37.83148, 27.24884],
     [37.55329, 29.11926], [38.41486, 39.46838], [37.9377, 37.63641],
     [40.40304, 27.04834], [40.64522, 31.33026], [40.92596, 32.75299],
     [40.84914, 35.88135], [40.4135, 36.79596], [40.20825, 38.29834],
     [39.70719, 39.2981], [38.62975, 40.20996], [39.27904, 40.13855],
     [38.88676, 41.59973], [40.20903, 28.98743], [37.79242, 28.78418],
     [36.72568, 28.90503], [38.16911, 26.57043], [38.52883, 27.41364],
     [39.17266, 26.7984], [38.82687, 29.32251], [38.32011, 31.30554]
     ])

point_coord = points[0]
location_coord = df.iloc[0][["id", "lat", "long"]].to_numpy()

#####################


def tier_list(x, y):

    for j in depremler:
        tier_arr = [0, 0, 0]
        for k in bizimkiler:
            distance = find_distance(j, k)

            if distance <= 30:
                tier_arr[0] += 1
            elif distance <= 50:
                tier_arr[1] += 1
            elif distance <= 70:
                tier_arr[2] += 1
        # tier_arr to dataset
        df.tier1_dist = tier_arr[0]
        df.tier2_dist = tier_arr[1]
        df.tier3_dist = tier_arr[2]
    return tier_arr


#####################
print(find_distance(point_coord, location_coord))
print(df)
