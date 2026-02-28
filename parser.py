def reconstruct_lines(df):
    lines = []

    grouped = df.groupby("line_num")

    for _, group in grouped:
        words = group.sort_values("left")["text"].astype(str)
        line_text = " ".join(words)
        lines.append(line_text.strip())

    return lines

import re

def extract_items(lines):

    items = []

    for i in range(len(lines)):

        line = lines[i]
        numbers = re.findall(r"\d+\.\d+", line)

        # Detect structured item row (many numbers in line)
        if len(numbers) >= 2:

            price = float(numbers[-1])

            # Look at next line for item description
            if i + 1 < len(lines):
                next_line = lines[i + 1]

                # If next line has no numbers, assume it's description
                if not re.search(r"\d", next_line):

                    name = next_line.strip()

                    items.append({
                        "name": name,
                        "price": price
                    })

    return items

def extract_total(lines):

    totals = []

    for line in lines:
        lower = line.lower()

        if "total invoice" in lower or "gross total" in lower:
            numbers = re.findall(r"\d+\.\d+|\d+", line)
            if numbers:
                return float(numbers[-1])

        if "total" in lower and "qty" not in lower:
            numbers = re.findall(r"\d+\.\d+|\d+", line)
            if numbers:
                totals.append(float(numbers[-1]))

    # Fallback: choose largest value in receipt
    all_numbers = []

    for line in lines:
        nums = re.findall(r"\d+\.\d+|\d+", line)
        for n in nums:
            all_numbers.append(float(n))

    if all_numbers:
        return max(all_numbers)

    return None

def lines_to_text(lines):
    return " ".join(lines)