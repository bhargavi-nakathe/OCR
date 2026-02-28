import pandas as pd
import random

categories = {
    "grocery": [
        "milk bread rice wheat sugar oil vegetables fruits supermarket",
        "grocery store bill total amount gst",
        "atta dal rice pulses grocery mart",
        "fresh vegetables onion potato tomato",
        "supermarket invoice grocery items"
    ],
    "restaurant": [
        "pizza burger coke restaurant bill",
        "dinner lunch food invoice service tax",
        "hotel restaurant gst total amount",
        "coffee tea sandwich cafe bill",
        "restaurant food order subtotal tax"
    ],
    "fashion": [
        "zudio trent limited mens tshirt jeans clothing",
        "fashion store apparel bill gst invoice",
        "shirt pant casual wear clothing store",
        "h&m zara lifestyle fashion outlet",
        "mens casual shorts knits apparel"
    ],
    "fuel": [
        "petrol diesel fuel pump liter rate",
        "bharat petroleum fuel bill gst",
        "indian oil petrol invoice total",
        "fuel station diesel receipt",
        "petrol pump transaction slip"
    ],
    "pharmacy": [
        "paracetamol tablet medicine pharmacy bill",
        "apollo pharmacy gst invoice",
        "medical store prescription drugs",
        "medicine bill taxable amount",
        "tablet syrup capsule pharmacy"
    ],
    "electronics": [
        "laptop charger mouse electronics store",
        "mobile phone invoice gst total",
        "croma reliance digital bill",
        "tv fridge washing machine electronics",
        "electronics purchase warranty invoice"
    ]
}

data = []

for category, texts in categories.items():
    for _ in range(100):  # 100 rows per category
        text = random.choice(texts)
        noise = str(random.randint(100, 9999))
        data.append([text + " " + noise, category])

df = pd.DataFrame(data, columns=["receipt_text", "category"])

df.to_csv("dataset.csv", index=False)

print("✅ 600 dataset rows generated successfully.")