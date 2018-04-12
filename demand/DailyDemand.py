import csv

import logger


class DailyDemand:
    __logger = logger.Logger()
    __elements_kids = ()
    __elements_male = ()
    __elements_female = ()

    def __init__(self):
        self.__load_elements()

    def __load_elements(self):
        loading_kids = False
        loading_male = False
        loading_female = False

        with open('./input-data/daily-demand/elements.csv', newline='') as csv_file:
            elements = csv.reader(csv_file, delimiter=',', quotechar='"')
            for index, row in enumerate(elements):
                if index == 0:
                    continue  # header
                if row[0] in ('Infants', 'Children'):
                    self.__logger.info("Loading elements for kids")
                    loading_kids = True
                    loading_male = loading_female = False
                    continue
                if row[0] == 'Males':
                    self.__logger.info("Loading elements for males")
                    loading_male = True
                    loading_kids = loading_female = False
                    continue
                if row[0] == 'Females':
                    self.__logger.info("Loading elements for females")
                    loading_female = True
                    loading_kids = loading_male = False
                    continue
                if row[0] == 'Pregnancy':
                    loading_female = loading_kids = loading_male = False
                    continue
                if row[0] == 'Lactation':
                    loading_female = loading_kids = loading_male = False
                    continue

                months_range = self.__unify_to_months(row[0])


                if loading_kids:
                    pass
                if loading_male:
                    pass
                if loading_female:
                    pass

    def __unify_to_months(self, raw_value):
        if raw_value.startswith('>'):
            raw_range = raw_value.split(' ')[1]
            unit = raw_value.split(' ')[2]
            range_from = int(raw_range.split('>')[0])
            range_to = 100
            pass
        else:
            raw_range = raw_value.split(' ')[0]
            unit = raw_value.split(' ')[1]
            range_from = int(raw_range.split('–')[0])  # It is not a pause char!
            range_to = int(raw_range.split('–')[1])  # It is not a pause char!

        if unit == 'y':
            range_from = range_from * 12
            range_to = range_to * 12 + 11

        self.__logger.debug("Unifying range to months. Result: from={}, to={}".format(range_from, range_to))
        return range_from, range_to
