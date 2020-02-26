import arcpy
from arcpy import env

env.workspace = r'D:\LiDAR_2019\Shp_Countours'


outputFGDB = r"D:\LiDAR_2019\LiDAR_2019_ContoursQL1.gdb"


"""fcs = arcpy.ListFeatureClasses()


for fc in fcs:
    print "converting " + fc 
    arcpy.FeatureClassToFeatureClass_conversion(fc, outputFGDB, fc[:-4])



"""

#env.workspace = outputFGDB

env.overwriteOutput = True

fcs = arcpy.ListFeatureClasses()
dsc = arcpy.Describe(r"D:\CC_2019\test\test3.shp")
coord_sys = dsc.spatialReference




for fc in fcs:
    print "Correcting the projection for " + fc
    arcpy.MakeFeatureLayer_management(fc, 'lyr')
    arcpy.DefineProjection_management('lyr',coord_sys)
