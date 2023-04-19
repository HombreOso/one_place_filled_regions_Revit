# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from do_polygons_overlap import *

from polygon_intersection_area import *

from chat_gpt_polygon_overlap import *


def ccw(x1, y1, x2, y2, x3, y3):
    return (y3 - y1) * (x2 - x1) > (y2 - y1) * (x3 - x1)


def is_polygon_ccw_then_revert(polygon, polygon_type):
    if len(polygon) > 0:
        polygon_x0 = polygon[0][0]
        polygon_y0 = polygon[0][1]

        polygon_x1 = polygon[1][0]
        polygon_y1 = polygon[1][1]

        polygon_x2 = polygon[2][0]
        polygon_y2 = polygon[2][1]

        if not ccw(polygon_x0, polygon_y0, polygon_x1, polygon_y1, polygon_x2, polygon_y2):
            print('clockwise polygon  ', polygon_type, '  >> reverse', )
            polygon = polygon[::-1]

    return polygon


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def point_obj_transition(polygon):
    return [Point(polyg_tuple[0], polyg_tuple[1]) for polyg_tuple in polygon]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filled_region_polygon = [(20.067389491544439, 27.150589420636614), (20.067389491544404, 5.4970461135499988),
                             (0.38235012146566311, 5.4970461135500628), (-0.27381785753692695, 27.150589420636681)]
    room_polygon = [(20.789174268447326, 12.714893882578878), (30.631693953486689, 12.714893882578847),
                    (44.411221512541829, 12.714893882578803), (49.004397365560187, 12.714893882578789),
                    (49.004397365560209, 26.494421441633943), (20.789174268447351, 26.49442144163401)]

    filled_region_polygon1 = [(20.067389491544439, 27.150589420636614), (20.067389491544404, 5.4970461135499988),
                              (0.38235012146566311, 5.4970461135500628), (-0.27381785753692695, 27.150589420636681)]
    room_polygon2 = [(9.3062346359013812, 12.714893882578915), (20.133006289444701, 12.714893882578881),
                     (20.133006289444726, 26.49442144163401), (9.3062346359014168, 26.494421441634035)]

    room_polygon3 = [(20.789174268447326, 12.714893882578878), (30.631693953486689, 12.714893882578847),
                     (44.411221512541829, 12.714893882578803), (49.004397365560187, 12.714893882578789),
                     (49.004397365560209, 26.494421441633943), (20.789174268447351, 26.49442144163401)]

    room_polygon4 = [(8.6500666568987565, 12.058725903576294), (0.38235012146567332, 12.058725903576319),
                     (0.38235012146566183, 4.9064949324477105), (8.650066656898737, 4.9064949324476848)]

    room_polygon5 = [(20.46109027894601, 12.058725903576255), (9.3062346359013812, 12.05872590357629),
                     (9.3062346359013617, 4.906494932447683), (18.820670331439359, 4.9064949324476528),
                     (18.820670331439342, -5.6578095294945783), (30.303609963985277, -5.6578095294946404),
                     (30.303609963985302, -0.73654968697495704), (30.303609963985373, 12.058725903576224)]

    room_polygon6 = [(44.08313752304052, 12.05872590357618), (30.959777942987998, 12.058725903576221),
                     (30.95977794298793, -0.40846569747364742), (44.083137523040499, -0.40846569747368983)]

    filled_region_polygon2 = [(20.789174268447347, 26.49442144163401), (20.789174268447326, 12.714893882578879),
                              (29.323747405278933, -0.048480572650211023), (44.083137523040492, -0.40846569747368378),
                              (44.739305502043159, 26.494421441633932)]

    polygon1 = [(8, 2), (5, 1), (3, 3), (4, 6), (9, 7), (9, 4)]
    polygon2 = [(8, 11), (8, 6), (13, 6), (13, 11)]
    polygon3 = [(8, 11), (10, 7), (13, 6), (13, 11)]  # (10, 7) changes from polygon2
    polygon4 = [(8, 2), (5, 1), (3, 3), (4, 6), (12, 10), (9, 4)]  # (13, 11) changes from polygon1

    polygon_a = is_polygon_ccw_then_revert(filled_region_polygon1, 'filled region')
    polygon_b = is_polygon_ccw_then_revert(room_polygon4, 'room')

    print('do_polygons_overlap?: ', do_polygons_overlap(polygon_a, polygon_b))

    print_hi('PyCharm')

    # print("Do polygons intersect?: ", do_polygons_intersect(filled_region_polygon1, room_polygon2))
    # if do_polygons_overlap(polygon_a, polygon_b):
    #     intersec_area = polygon_clip(polygon_a, polygon_b)
    # else:
    #     intersec_area = 0

    # print("intersection area: ", intersec_area)

    PolygonA = Polygon(point_obj_transition(polygon_a))
    PolygonB = Polygon(point_obj_transition(polygon_b))


    print("do polygons intersect?.... :", PolygonA.intersects(PolygonB))
    print("overlap_area_A_B: ", overlap_area(PolygonA, PolygonB))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
