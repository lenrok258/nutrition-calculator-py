import demand.model.InflaterUtils as Utils
from demand.model.Elements import Elements


def inflate(row):
    months_range = Utils.unify_to_months(row[0])
    elements = Elements()
    elements.age_months_from = months_range[0]
    elements.age_months_to = months_range[1]
    elements.calcium = row[1]
    elements.chromium = row[2]
    elements.copper = row[3]
    # TODO: Fill in rest

    return elements
