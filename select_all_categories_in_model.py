import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager

doc = __revit__.ActiveUIDocument.Document

cats = doc.Settings.Categories

used_cat = []
unused_cat = []
count_error = 0
for cat in cats:
	#if cat.CategoryType == CategoryType.Model or cat.CategoryType == CategoryType.Annotation:
    # print(cat.Id.IntegerValue)
    try:
        cate = Revit.Elements.Category.ById(cat.Id.IntegerValue)
        count = FilteredElementCollector(doc).OfCategoryId(cat.Id).WhereElementIsNotElementType().GetElementCount();
        if count>0:
	        used_cat.append(cate)
        else:
            unused_cat.append(cate)
    except IndentationError:
        print "Indentation"
    except:
    	print("Error Category Id is", cat.Id.IntegerValue)
    	count_error = count_error + 1
print("number of errors: ", count_error)

OUT = used_cat, unused_cat