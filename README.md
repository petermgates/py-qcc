# py-qcc
Quality Control Charts in Python. Inspired by the R qcc package.

## Planned features
Tools:
- Reshape data table with value column and subgroup reference column (qcc_groups). 

Charts for continuous variables:
- x-bar for subgroup means.
- R for subgroup ranges.
- *s* for subgroup variance.
- Individuals for single measurements.
- Moving range for single measurements.

Charts for attributes:
- *p* for proportion of nonconforming units.
- *np* for number of nonconforming units.
- *c* for nonconformities per unit.
- *u* for average nonconformities per unit.

Other charts:
- Operating characteristic.
- Process capability.
- Cusum.
- EWMA.
- Pareto.
- Multivariate control charts.

Additional features:
- Calibration data and subsequent new data. 
- Nelson and Western Electric rules.
- Summary statistics.