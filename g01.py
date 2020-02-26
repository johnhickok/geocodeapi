# easiest way to log in
import arcpy, os

from arcgis import GIS
from arcgis.geocoding import get_geocoders, batch_geocode

# from arcpy import env

arcpy.env.workspace = os.getcwd()
# this_folder = os.getcwd()

cursor = arcpy.da.SearchCursor("MyProject.gdb\\dcfs", ['office', 'phone', 'street', 'city', 'st', 'zip'])
for row in cursor:
  #x = dict('Address = {}, City = {}, Region = {}, Postal = {}'.format(row[2], row[3], row[4], row[5]))
  s = ('Address = "{}", City = "{}", Region = "{}", Postal = "{}"'.format(row[2], row[3], row[4], row[5]))
  x = dict(s)
  print(x)

x = dict(Address = 20151 Nordhoff Street, City = Chatsworth, Region = CA, Postal = 91311)


print('{} has a population of {}'.format(row[0], row[1]))

x = dict('Address = {}, City = {}, Region = {}, Postal = {}'.format(row[3], row[4], row[5], row[1]))


# log in via users credentials stored in ArcGIS Pro
gis = GIS("pro")

geocoder = get_geocoders(gis)[0]

"""
https://pro.arcgis.com/en/pro-app/arcpy/get-started/data-access-using-cursors.htm

OFFICE: String (8000.0)
PHONE: String (8000.0)
street: String (8000.0)
city: String (8000.0)
st: String (8000.0)
zip: String (255.0)






addresses= [{
                "Address": "380 New York St.",
                "City": "Redlands",
                "Region": "CA",
                "Postal": "92373"
            },{
                "Address": "1 World Way",
                "City": "Los Angeles",
                "Region": "CA",
                "Postal": "90045"
            }]


reader = csv.DictReader(open('myfile.csv'))
for row in reader:
    # profit !
https://gis.stackexchange.com/questions/97209/is-it-a-bad-idea-to-convert-a-file-geodatabase-table-to-a-dictionary

def make_attribute_dict(fc, key_field, attr_list=['*']):
    ''' Create a dictionary of feature class/table attributes.
        Default of ['*'] for attr_list (instead of actual attribute names)
        will create a dictionary of all attributes. '''
    attr_dict = {}
    fc_field_objects = arcpy.ListFields(fc)
    fc_fields = [field.name for field in fc_field_objects if field.type != 'Geometry']
    if attr_list == ['*']:
        valid_fields = fc_fields
    else:
        valid_fields = [field for field in attr_list if field in fc_fields]
    # Ensure that key_field is always the first field in the field list
    cursor_fields = [key_field] + list(set(valid_fields) - set([key_field]))
    with arcpy.da.SearchCursor(fc, cursor_fields) as cursor:
        for row in cursor:
            attr_dict[row[0]] = dict(zip(cursor.fields, row))
    return attr_dict


x = dict(name = "John", age = 36, country = "Norway")


"""

























print("MaxBatchSize : " + str(geocoder.properties.locatorProperties.MaxBatchSize))
print("SuggestedBatchSize : " + str(geocoder.properties.locatorProperties.SuggestedBatchSize))

