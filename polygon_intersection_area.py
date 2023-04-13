def do_polygons_intersect(polygon1, polygon2):
    def line_intersect(line1, line2):
        print("line1: ", line1)
        print("line2: ", line2)

        def ccw(x1, y1, x2, y2, x3, y3):
            return (y3-y1)*(x2-x1) > (y2-y1)*(x3-x1)

        x1, y1 = line1[0][0], line1[0][1]
        x2, y2 = line1[1][0], line1[1][1]
        x3, y3 = line2[0][0], line2[0][1]
        x4, y4 = line2[1][0], line2[1][1]
        return ccw(x1, y1, x3, y3, x4, y4) != ccw(x2, y2, x3, y3, x4, y4) and ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4)

    def get_edges(polygon):
        return [(polygon[i], polygon[(i+1)%len(polygon)]) for i in range(len(polygon))]

    edges1 = get_edges(polygon1)
    edges2 = get_edges(polygon2)

    for edge1 in edges1:
        for edge2 in edges2:
            if line_intersect(edge1, edge2):
                return True
    return False


def is_left(A,B,C):
    # returns True if C is on the left of the line AB
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])


def polygon_clip(subjectPolygon, clipPolygon):
    def inside(p):
        # returns True if point p is inside the clip polygon
        return (cp2[0] - cp1[0]) * (p[1] - cp1[1]) > (cp2[1] - cp1[1]) * (p[0] - cp1[0])

    def computeIntersection(s, e):
        # calculates the intersection of line segement subject and line cp1,cp2
        dc = [cp1[0] - cp2[0], cp1[1] - cp2[1]]  # difference between cp1 and cp2
        dp = [s[0] - e[0], s[1] - e[1]]  # difference between s and e
        n1 = cp1[1] * cp2[0] - cp1[0] * cp2[1]  # cross product of dc and cp1,cp2
        n2 = s[1] * e[0] - s[0] * e[1]  # cross product of dp and s,e
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [(n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3]


    def clip(subjectPolygon, clipPolygon):
        outputList = subjectPolygon
        cp1 = clipPolygon[-1]

        for clipVertex in clipPolygon:
            cp2 = clipVertex
            inputList = outputList
            outputList = []
            s = inputList[-1]

            for subjectVertex in inputList:
                e = subjectVertex
                if inside(e):
                    if not inside(s):
                        outputList.append(computeIntersection(s, e))
                    outputList.append(e)
                elif inside(s):
                    outputList.append(computeIntersection(s, e))
                s = e
            cp1 = cp2
        return (outputList)

    # Clip the subject polygon against each edge of the clip polygon
    outputPolygon = subjectPolygon
    cp1 = clipPolygon[-1]  # Define cp1 outside the for loop
    for i in range(len(clipPolygon)):
        cp2 = clipPolygon[i]
        edge = [clipPolygon[i - 1], cp2]
        outputPolygon = clip(outputPolygon, edge)
        cp1 = cp2  # Update cp1 for the next iteration

    # Calculate the area of the clipped polygon
    if len(outputPolygon) < 3:
        # The clipped polygon has less than 3 vertices, so it is not a valid polygon
        return 0
    else:
        # Use the Shoelace formula to calculate the area of the clipped polygon
        area = 0.0
        j = len(outputPolygon) - 1
        for i in range(len(outputPolygon)):
            area += (outputPolygon[j][0] + outputPolygon[i][0]) * (outputPolygon[j][1] - outputPolygon[i][1])
            j = i
        return abs(area / 2.0)


