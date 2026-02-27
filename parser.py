import re

def extract_items_and_total(text):

    items = []
    total = None

    # Find total
    total_match = re.search(r"total[^0-9]*(\d+\.\d+)", text.lower())
    if total_match:
        total = float(total_match.group(1))

    # Find all item + price patterns
    # Example match: "Milk 2.50"
    item_pattern = re.findall(r"([A-Za-z ]+)\s+(\d+\.\d+)", text)

    for name, price in item_pattern:

        # Skip total
        if "total" in name.lower():
            continue

        clean_name = name.strip()

        if len(clean_name) > 2:
            items.append({
                "name": clean_name,
                "price": float(price)
            })

    return items, total