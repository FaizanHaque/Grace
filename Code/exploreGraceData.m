fname = "../Data/GRCTellus.JPL.200204_201706.GLO.RL06M.MSCNv01CRIv01.nc";
fname2 = "../Data/JPL_MSCNv01_PLACEMENT.nc";
fname3 = "../Data/LAND_MASK.CRIv01.nc";

Data = ncread(fname);
lat = Data.lat;
lon = Data.lon;