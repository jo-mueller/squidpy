"""The plotting module."""
from squidpy.pl._graph import (
    ripley,
    co_occurrence,
    nhood_enrichment,
    centrality_scores,
    interaction_matrix,
)
from squidpy.pl._utils import extract
from squidpy.pl._ligrec import ligrec
from squidpy.pl._spatial import (
    spatial_plot,
    spatial_point,
    spatial_shape,
    spatial_segment,
)
from squidpy.pl._interactive import Interactive  # type: ignore[attr-defined]
