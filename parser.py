import re

def extract_items_and_total(text):

    lines = text.split()

    items = []
    total = None

    # Regex for price (integer or decimal)
    price_pattern = re.compile(r"\d+\.\d+|\d+")

    # Try line-based splitting first
    raw_lines = text.split("\n")

    for line in raw_lines:

        # Look for total
        if "total" in line.lower():
            numbers = price_pattern.findall(line)
            if numbers:
                total = float(numbers[-1])
            continue

        # Look for item + price
        numbers = price_pattern.findall(line)

        if numbers:
            price = float(numbers[-1])

            # Remove price from line to get item name
            item_name = re.sub(price_pattern, "", line).strip()

            if len(item_name) > 2:
                items.append({
                    "name": item_name,
                    "price": price
                })

    return items, total