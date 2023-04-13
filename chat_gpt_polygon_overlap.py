from do_polygons_overlap import do_polygons_overlap
import math

def angle(c, p):
    return math.atan2(p.y - c.y, p.x - c.x)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Polygon:
    def __init__(self, points):
        self.points = points
        print('self.points:   ', points)

    def contains(self, point):
        # Unpack the point coordinates
        x, y = point.x, point.y

        polygon = self.points

        # Number of vertices in the polygon
        n = len(polygon)

        # Boolean to keep track of whether the point is inside the polygon or not
        inside = False

        # Starting vertex of the current side of the polygon
        p1x, p1y = polygon[0].x, polygon[0].y

        # Loop over all sides of the polygon
        for i in range(n + 1):
            # Ending vertex of the current side of the polygon
            p2x, p2y = polygon[i % n].x, polygon[i % n].y

            # Check if the current side intersects with a horizontal line
            # drawn from the point to the right
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            # Calculate the x-coordinate of the intersection
                            xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xints:
                            # If an intersection is found, flip the inside status
                            inside = not inside
            # Move to the next side of the polygon
            p1x, p1y = p2x, p2y

        # Return the final inside status
        return inside

    def edges(self):
        edges = []
        for i in range(len(self.points)):
            edges.append((self.points[i], self.points[(i+1)%len(self.points)]))
        return edges

    def intersects(self, other):
        print('edges polygon1:  ', [((e1A[0].x, e1A[0].y),(e1A[1].x, e1A[1].y)) for e1A in self.edges()])
        print('edges polygon2:  ', [((e1A[0].x, e1A[0].y),(e1A[1].x, e1A[1].y)) for e1A in other.edges()])
        for e1 in self.edges():
            for e2 in other.edges():
                if intersect_stack_overf(e1, e2):
                    return True
        return False

    def area(self):
        n = len(self.points)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += self.points[i].x * self.points[j].y - self.points[j].x * self.points[i].y
        return abs(area) / 2

def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect_stack_overf(e1, e2):
    A, B = e1
    C, D = e2
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def intersect(e1, e2):
    p1, q1 = e1
    p2, q2 = e2
    dx1 = p1.x - q1.x
    dy1 = p1.y - q1.y
    dx2 = p2.x - q2.x
    dy2 = p2.y - q2.y
    det = dx1 * dy2 - dy1 * dx2
    if det == 0:
        return False  # parallel lines
    else:
        t = (dx1 * (p2.y - p1.y) + dy1 * (p1.x - p2.x)) / det
        u = - (dx2 * (p1.y - p2.y) + dy2 * (p2.x - p1.x)) / det
        if t >= 0 and t <= 1 and u >= 0 and u <= 1:
            return True
        else:
            return False

def overlap_area(p1, p2):
    if not p1.intersects(p2):
        return 0

    # find intersection points
    intersection_points = []
    for e1 in p1.edges():
        for e2 in p2.edges():
            if intersect(e1, e2):
                intersection_points.append(intersection(e1, e2))

    # add polygon vertices that are inside the other polygon
    for p in [p1, p2]:
        for pt in p.points:
            if p == p1 and p2.contains(pt):
                intersection_points.append(pt)
            elif p == p2 and p1.contains(pt):
                intersection_points.append(pt)

    # sort intersection points by angle around centroid
    centroid = Point(sum([p.x for p in intersection_points]) / len(intersection_points),
                      sum([p.y for p in intersection_points]) / len(intersection_points))
    intersection_points.sort(key=lambda p: angle(centroid, p))

    # compute area of intersection polygon
    intersection_points.append(intersection_points[0])  # make polygon circular

    print('intersection points:    ', [(P.x, P.y) for P in intersection_points])
    area = 0
    for i in range(len(intersection_points)-1):
        area += (intersection_points[i].x * intersection_points[i+1].y
                 - intersection_points[i+1].x * intersection_points[i].y)
    return abs(area) / 2

def intersection(e1, e2):
    p1, q1 = e1
    p2, q2 = e2
    dx1 = p1.x - q1.x
    dy1 = p1.y - q1.y
    dx2 = p2.x - q2.x
    dy2 = p2.y - q2.y
    det = dx1 * dy2 - dy1 * dx2
    if det == 0:
        return None  # parallel lines
    else:
        t = (dx1 * (p2.y - p1.y) + dy1 * (p1.x - p2.x)) / det
        u = - (dx2 * (p1.y - p2.y) + dy2 * (p2.x - p1.x)) / det
        if t >= 0 and t <= 1 and u >= 0 and u <= 1:
            # x = p1.x + t * dx1
            # y = p1.y + t * dy1
            # amended formula
            x = ((p1.x*q1.y - p1.y*q1.x)*dx2 - (p2.x*q2.y-p2.y*q2.x)*dx1) / det
            y = ((p1.x*q1.y - p1.y*q1.x)*dy2 - (p2.x*q2.y-p2.y*q2.x)*dy1) / det

            return Point(x, y)
        else:
            return None
