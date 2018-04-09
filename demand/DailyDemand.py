import csv

import logger


class DailyDemand:
    __logger = logger.Logger()
    __elements_kids = {}
    __elements_male = {}
    __elements_female = {}

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
                if row[0] == 'Males':
                    self.__logger.info("Loading elements for males")
                    loading_male = True
                    loading_kids = loading_female = False
                if row[0] == 'Females':
                    self.__logger.info("Loading elements for females")
                    loading_female = True
                    loading_kids = loading_male = False
                # TODO: Actual loading
