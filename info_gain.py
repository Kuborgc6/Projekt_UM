from class_counts import class_counts
import numpy as np

def info_gain(data, left, right):
    """Information Gain.
    """
    # Entropy before partition
    library = class_counts(data)
    all_elem = 0
    for name,dict_ in library.items():
        all_elem = all_elem+dict_

    Entropy = 0

    for name,dict_ in library.items():
        Entropy = Entropy - (dict_/all_elem)*np.log(dict_/all_elem) 

    # Entropy of left after partition
    library_tr_l = class_counts(left)
    all_elem_tr_l = 0
    for name,dict_ in library_tr_l.items():
        all_elem_tr_l = all_elem_tr_l+dict_

    Entropy_tr_l = 0

    for name,dict_ in library_tr_l.items():
        Entropy_tr_l = Entropy_tr_l - (dict_/all_elem_tr_l)*np.log(dict_/all_elem_tr_l) 

    # Entropy of right after partition

    library_tr_r = class_counts(right)
    all_elem_tr_r = 0
    for name,dict_ in library_tr_r.items():
        all_elem_tr_r = all_elem_tr_r+dict_

    Entropy_tr_r = 0

    for name,dict_ in library_tr_r.items():
        Entropy_tr_r = Entropy_tr_r - (dict_/all_elem_tr_r)*np.log(dict_/all_elem_tr_r) 
    if Entropy > 0: #When Entropy is 0 Gain will be allways inf, but in this case spliting is worst than leaving it as it is
        Gain = (Entropy-(Entropy_tr_l+Entropy_tr_r))/Entropy
    else:
        Gain = 0
    return Gain