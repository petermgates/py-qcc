# py-qcc
Quality Control Charts in Python. Inspired by the R qcc package.

## Planned features
Tools:
- [x] Reshape data table with value column and subgroup reference column (qcc_groups). 

Charts for continuous variables:
- [ ] x-bar for subgroup means.
- [ ] R (range) for subgroup means.
- [ ] S (standard deviation) for subgroup means.
- [ ] Individuals for single measurments.
- [ ] Moving range for single measurments.

Charts for attributes:
- [ ] p for proportion defective with fixed subgroup size (with and without standard).
- [ ] np for proportion defective with variable subgroup size (with and without standard).
- [ ] c for quantity defective with fixed subgroup size (with and without standard).
- [ ] u for quantity defective per unit

Other charts:
- [ ] Operating characteristic.
- [ ] Process capability.
- [ ] Cusum.
- [ ] EWMA.
- [ ] Pareto.
- [ ] Multivariate control charts.

Additional features:
- [ ] Calibration data and subsequent new data. 
- [ ] Nelson and Western Electric rules.
- [ ] Summary statistics.