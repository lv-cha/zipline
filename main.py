# __author__ = zhaoxi
# __datetime__ = 2020/12/28 15:30
from datetime import datetime

from zipline import run_algorithm
import pandas as pd


def initialize():
    print("intialize")


if __name__ == "__main__":
    run_algorithm(
        start=pd.Timestamp(datetime(year=2019, month=11, day=1)),
        end=pd.Timestamp(datetime(year=2019, month=11, day=2)),
        initialize=initialize,
        capital_base=1000000
    )