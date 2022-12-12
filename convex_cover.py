# import matplotlib.pyplot as plt
# from matplotlib.patches import Circle

# v = [[0.573,  0.797],
#      [0.688,  0.402],
#      [0.747,  0.238],
#      [0.802,  0.426],
#      [0.757,  0.796],
#      [0.589,  0.811]]

# c = [(0.7490863467660889, 0.4917635308023209),
#      (0.6814339441396109, 0.6199470305156477),
#      (0.7241617773773865, 0.6982813914515696),
#      (0.6600700275207232, 0.7516911829987891),
#      (0.6315848053622062, 0.7730550996176769),
#      (0.7348437356868305, 0.41342916986639894),
#      (0.7597683050755328, 0.31729154508140384)]

# r = [0, 0, 0.10297280518543134, 0, 0.06374182913818943,
#      0.0684588720095565, 0.07987784828713643]

# x_point,y_point=[],[]
# for p in v:
#     x_point.append(p[0])
#     y_point.append(p[1])

# centers=[]
# for ce in c:
#     centers.append(ce)


# fig=plt.figure()
# ax=fig.add_subplot(111)

# plt.plot(x_point,y_point,'o')

# for i in range(len(centers)):
#     print("1")
#     cir=Circle(centers[i],r[i],color='r',alpha=0.5)
#     ax.add_patch(cir)
# plt.axis('equal')
# plt.show()
import numpy as np


def find_convex_cover(pvertices: list, clist: list) -> list:
    """
    Args:
        pvertices (list): _description_
        clist (list): _description_

    Returns:
        list: _description_
    """
    assert isinstance(pvertices, list) or isinstance(pvertices, np.ndarray)
    assert isinstance(clist, list)

    for point in pvertices:
        assert (isinstance(point, list) or isinstance(pvertices, np.ndarray) )and len(point) == 2
        for p in point:
            assert isinstance(p, int) or isinstance(p, float)

    for point in clist:
        assert isinstance(point, tuple) and len(point) == 2
        for p in point:
            assert isinstance(p, int) or isinstance(p, float)

    pvertices = np.array(pvertices, dtype=np.dtype('float64'))
    clist = np.array(clist, dtype=np.dtype('float64'))

    pvertices = np.expand_dims(pvertices, axis=1)
    r = pvertices - clist

    # the default ord of np.linalg.norm is 2
    all_possible_distance = np.apply_along_axis(np.linalg.norm, -1, r)

    # find the min distance from point to all circle center,return #circle
    cir_ord = np.argmin(all_possible_distance, axis=-1)

    radius = {}

    # if one center is the closet to multiple points, then we should choose the biggest distance to those candidate points.
    # Because it can cover most points one time and the sum(square) of the circle can be small!
    for i,  c in enumerate(cir_ord):
        if c not in radius:
            radius[c] = 0
            radius[c] = max(all_possible_distance[i, c], radius[c])
        else:
            radius[c] = max(all_possible_distance[i, c], radius[c])

    radius_list = []
    for i in range(len(clist)):
        # Some circle center may not be the closet one to any points, so they should not be utilized. so r is 0
        if i not in radius:
            radius_list.append(0)
        else:
            radius_list.append(radius[i])

    return radius_list


if __name__ == "__main__":
    pvertices = np.array([[0.573,  0.797],
                         [0.688,  0.402],
                         [0.747,  0.238],
                         [0.802,  0.426],
                         [0.757,  0.796],
                         [0.589,  0.811]])
    clist = [(0.7490863467660889, 0.4917635308023209),
             (0.6814339441396109, 0.6199470305156477),
             (0.7241617773773865, 0.6982813914515696),
             (0.6600700275207232, 0.7516911829987891),
             (0.6315848053622062, 0.7730550996176769),
             (0.7348437356868305, 0.41342916986639894),
             (0.7597683050755328, 0.31729154508140384)]

    print(find_convex_cover(pvertices=pvertices, clist=clist))
