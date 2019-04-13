# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:35:44 2019

@author: Home
"""
#https://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/
import netCDF4 as nc
from netCDF4 import Dataset
import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np 
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
fname1 = "../Data/GRCTellus.JPL.200204_201706.GLO.RL06M.MSCNv01CRIv01.nc";
fname2 = "../Data/JPL_MSCNv01_PLACEMENT.nc";
fname3 = "../Data/LAND_MASK.CRIv01.nc";

ds1 = Dataset(fname1);
#print(ds1.dimensions.keys());
#print(ds1.variables.keys());
#print(ds1.variables['lwe_thickness']);
lwe_t = ds1.variables['lwe_thickness'][:];
lat= ds1.variables['lat'][:];
lon = ds1.variables['lon'][:];
#fig = ff.create_quiver(lon, lat,lwe_t)
#py.iplot(fig)
lwe_t_units = ds1.variables['lwe_thickness'].units;
ds1.close()
