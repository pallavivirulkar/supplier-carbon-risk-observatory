import pandas as pd

cepii = pd.read_excel("../data/raw/cepii/dist_cepii.xls")

all_codes = set(cepii["iso_o"].unique()) | set(cepii["iso_d"].unique())

candidates = ["ROM", "ROU", "ZAR", "COD", "SCG", "YUG", "SRB", "MNE", "SDN", "SSD"]
for code in candidates:
    print(code, "exists in CEPII:", code in all_codes)