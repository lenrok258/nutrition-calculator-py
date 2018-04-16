class Elements:
    # "Life Stage Group"
    age_months_from = -1
    age_months_to = -1

    # Demand
    calcium = ''
    chromium = ''
    copper = ''
    fluoride = ''
    iodine = ''
    iron = ''
    magnesium = ''
    manganese = ''
    molybdenum = ''
    phosphorus = ''
    selenium = ''
    zinc = ''
    potassium = ''
    sodium = ''
    chloride = ''

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
