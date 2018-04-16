import csv

import logger
from demand.model import ElementsInflater


class DailyDemand:
    __logger = logger.Logger()
    __elements_kids = list()
    __elements_male = list()
    __elements_female = list()

    __loading_kids = False
    __loading_male = False
    __loading_female = False

    def __init__(self):
        self.__load_elements()
        self.__load_vitamins()
        self.__load_water()
        self.__load_micronutrients()

    def __load_elements(self):

        with open('./input-data/daily-demand/elements.csv', newline='') as csv_file:
            elements = csv.reader(csv_file, delimiter=',', quotechar='"')
            for index, row in enumerate(elements):
                if index == 0:
                    continue  # header
                if row[0] in ('Infants', 'Children'):
                    self.__logger.info("Loading elements for kids")
                    self.__loading_kids = True
                    self.__loading_male = self.__loading_female = False
                    continue
                if row[0] == 'Males':
                    self.__logger.info("Loading elements for males")
                    self.__loading_male = True
                    self.__loading_kids = self.__loading_female = False
                    continue
                if row[0] == 'Females':
                    self.__logger.info("Loading elements for females")
                    self.__loading_female = True
                    self.__loading_kids = self.__loading_male = False
                    continue
                if row[0] == 'Pregnancy':
                    self.__loading_female = self.__loading_kids = self.__loading_male = False
                    continue
                if row[0] == 'Lactation':
                    self.__loading_female = self.__loading_kids = self.__loading_male = False
                    continue

                elements = ElementsInflater.inflate(row)

                if self.__loading_kids:
                    self.__elements_kids.append(elements)
                if self.__loading_male:
                    self.__elements_male.append(elements)
                if self.__loading_female:
                    self.__elements_female.append(elements)

    def __load_vitamins(self):
        pass

    def __load_water(self):
        pass

    def __load_micronutrients(self):
        pass
