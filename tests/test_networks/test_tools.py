import pytest
import pandas as pd
import numpy as np

from osef.networks import create_edges_from_xy_df
from osef.networks import transfer_nodes_attribute
from osef.networks import transfer_edges_attributes
from osef.networks import create_directed_tree_from_source
from osef.networks import get_leaves


# GRAPH
#
#       +
#       |
#   +---+---+
#           |
#       +---+---+


@pytest.fixture()
def fix_create_df():
    data = np.array([
        [0, 1, 1, 1, 10],
        [1, 2, 1, 1, 10],
        [1, 1, 2, 1, 10],
        [2, 1, 2, 0, 10],
        [1, 0, 2, 0, 10],
        [2, 0, 3, 0, 10]
    ])
    df = pd.DataFrame(data=data, columns=["X0", "Y0", "X1", "Y1", "L"])
    return df


def test_create_edges_from_xy_df_base(fix_create_df):
    df = fix_create_df
    g = create_edges_from_xy_df(df, "X0", "Y0", "X1", "Y1")
    assert len(g.edges) == 6
