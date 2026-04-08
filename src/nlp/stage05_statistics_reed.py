import logging

import polars as pl

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

df = pl.read_csv("data/processed/reed_processed.csv")

logger.info("column means:")
print(df.mean())

logger.info("column medians:")
print(df.median())
