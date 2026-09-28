"""Transparent two-period DiD baseline, not an identification proof."""
from math import isfinite

def difference_in_differences(treated_before,treated_after,control_before,control_after):
    """Contrast group-period means. No variance estimate is supplied.

    Causal interpretation requires parallel untreated trends, no anticipation
    or spillovers, and stable group composition. Two periods cannot test
    parallel trends. This estimator does not handle staggered adoption.
    """
    if not all(isfinite(x) for x in [treated_before,treated_after,control_before,control_after]):
        raise ValueError("Group-period means must be finite")
    return (treated_after-treated_before)-(control_after-control_before)
