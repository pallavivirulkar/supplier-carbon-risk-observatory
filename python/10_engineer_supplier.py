import pandas as pd

df = pd.read_csv("../data/processed_dataco_clean.csv")

CATEGORY_GROUP_MAP = {
    "Children's Clothing": "Apparel & Footwear", "Girls' Apparel": "Apparel & Footwear",
    "Golf Apparel": "Apparel & Footwear", "Men's Clothing": "Apparel & Footwear",
    "Men's Footwear": "Apparel & Footwear", "Women's Apparel": "Apparel & Footwear",
    "Women's Clothing": "Apparel & Footwear",

    "Baseball & Softball": "Sporting Goods & Equipment", "Basketball": "Sporting Goods & Equipment",
    "Boxing & MMA": "Sporting Goods & Equipment", "Camping & Hiking": "Sporting Goods & Equipment",
    "Cardio Equipment": "Sporting Goods & Equipment", "Cleats": "Sporting Goods & Equipment",
    "Fishing": "Sporting Goods & Equipment", "Fitness Accessories": "Sporting Goods & Equipment",
    "Golf Bags & Carts": "Sporting Goods & Equipment", "Golf Balls": "Sporting Goods & Equipment",
    "Golf Gloves": "Sporting Goods & Equipment", "Golf Shoes": "Sporting Goods & Equipment",
    "Hockey": "Sporting Goods & Equipment", "Hunting & Shooting": "Sporting Goods & Equipment",
    "Indoor/Outdoor Games": "Sporting Goods & Equipment", "Kids' Golf Clubs": "Sporting Goods & Equipment",
    "Lacrosse": "Sporting Goods & Equipment", "Men's Golf Clubs": "Sporting Goods & Equipment",
    "Shop By Sport": "Sporting Goods & Equipment", "Soccer": "Sporting Goods & Equipment",
    "Sporting Goods": "Sporting Goods & Equipment", "Strength Training": "Sporting Goods & Equipment",
    "Tennis & Racquet": "Sporting Goods & Equipment", "Water Sports": "Sporting Goods & Equipment",
    "Women's Golf Clubs": "Sporting Goods & Equipment",

    "Cameras ": "Electronics Hardware", "Computers": "Electronics Hardware",
    "Consumer Electronics": "Electronics Hardware", "Electronics": "Electronics Hardware",

    "Books ": "Media & Publishing", "CDs ": "Media & Publishing", "DVDs": "Media & Publishing",
    "Music": "Media & Publishing", "Video Games": "Media & Publishing",

    "Accessories": "Home & Lifestyle", "As Seen on  TV!": "Home & Lifestyle",
    "Baby ": "Home & Lifestyle", "Crafts": "Home & Lifestyle", "Garden": "Home & Lifestyle",
    "Health and Beauty": "Home & Lifestyle", "Pet Supplies": "Home & Lifestyle",
    "Toys": "Home & Lifestyle", "Trade-In": "Home & Lifestyle",
}

SUPPLIER_MAP = {
    "Apparel & Footwear": ("SUP-001", "Vietnam Apparel Co.", "VNM"),
    "Sporting Goods & Equipment": ("SUP-002", "China Sporting Goods Mfg.", "CHN"),
    "Electronics Hardware": ("SUP-003", "China Electronics Mfg.", "CHN"),
    "Media & Publishing": ("SUP-004", "USA Media Distribution", "USA"),
    "Home & Lifestyle": ("SUP-005", "Mexico Home Goods Co.", "MEX"),
}

df["Category Group"] = df["Category Name"].map(CATEGORY_GROUP_MAP)
df["Supplier Id"] = df["Category Group"].map(lambda g: SUPPLIER_MAP[g][0])
df["Supplier Name"] = df["Category Group"].map(lambda g: SUPPLIER_MAP[g][1])
df["Supplier Country ISO3"] = df["Category Group"].map(lambda g: SUPPLIER_MAP[g][2])

print("Unmapped categories:", df["Category Group"].isnull().sum())
print("\nSupplier distribution:")
print(df["Supplier Name"].value_counts())

df.to_csv("../data/processed_dataco_clean.csv", index=False)
print("\nSaved. Final shape:", df.shape)