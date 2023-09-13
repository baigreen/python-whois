import re
import sys

from typing import (
    Dict,
    List,
    Callable,
)

COM_LIST: List[str] = [
    r"\nRegistrar",
    r"\nRegistrant",
    r"\nTech",
    r"\nAdmin",
    r"\nDomain",
    r"\nName Server:",
]


def groupFromList(list: List[str]) -> Callable[[str], Dict[str, str]]:
    def xgroupFromList(
        whoisStr: str,
        verbose: bool = False,
    ) -> Dict[str, str]:
        result: Dict[str, str] = {}
        # iterate over the lines of whoisStr
        #   for key each item in the list
        #       create a empty list
        #       store the list under key
        #       see if there is a match ans append matched lines to the list
        what = r"\n\n"
        return result

    return xgroupFromList
