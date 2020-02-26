import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
DataFrame1 = arcpy.GetParameterAsText(0)
df = arcpy.mapping.ListDataFrames(mxd, DataFrame1)[0]
source_layer =  arcpy.mapping.Layer(r"D:\LiDAR_2019\d16414.lyr")
for lyr in arcpy.mapping.ListLayers(mxd):
    x = lyr.name
    image = x[0]
    if image == "d":

        arcpy.mapping.UpdateLayer(df, lyr, source_layer, True)
del lyr, mxd
      
        
   
