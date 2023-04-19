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
cat_types = []
count_error = 0
for cat in cats:
    # if cat.CategoryType == CategoryType.Model or cat.CategoryType == CategoryType.Annotation:
    # print(cat.Id.IntegerValue)
    try:
        cate = cat
        count = FilteredElementCollector(doc).OfCategoryId(cat.Id).WhereElementIsNotElementType().GetElementCount();
        if count > 0:
            used_cat.append(cate)
        else:
            unused_cat.append(cate)
    except IndentationError:
        print
        "Indentation"
    except:
        print("Error Category Id is", cat.Name)

        count_error = count_error + 1
        cat_types.append(cat.CategoryType)
print("number of errors: ", count_error)
print("invalid cat types", list(set(cat_types)))

OUT = used_cat, unused_cat

print(len(used_cat))
used_cat_names = [ct.Name for ct in used_cat]
print(used_cat_names)