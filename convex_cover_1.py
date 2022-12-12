import numpy as np
import collections

def find_convex_cover(pvertices, clist):
    """
    Finds the optimum radius of circles such that all vertices are contained
    :param pvertices:
    :param clist:
    :return:
    """

    assert isinstance(clist, list)
    for elem in clist:
        assert isinstance(elem, tuple)
        assert len(elem) == 2
        for num in elem:
            assert isinstance(num, (float, int))

    for elem in pvertices:
        assert len(elem) == 2
        for num in elem:
            assert isinstance(num, (float, int))

    pvertices = np.array(pvertices)
    clist = np.array(clist)

    p_expand=np.expand_dims(pvertices,axis=1)
    r = p_expand - clist
    #r = pvertices[:, None] - clist
    print("r is :",r.shape)
    print(pvertices[:,None].shape,pvertices[:,None])
    print("ccc",clist.shape)
    #print(r)
    D = np.apply_along_axis(np.linalg.norm, -1, r)
    print(D)
    argmins = np.argmin(D, axis=-1)
    print(argmins)
    radii = collections.defaultdict(int)

    for i, argmin in enumerate(argmins):
        radii[argmin] = max(D[i, argmin], radii[argmin])
    print(len(radii),radii)
    return [radii[i] for i in range(len(clist))]


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
    
    print(find_convex_cover(pvertices=pvertices,clist=clist))
