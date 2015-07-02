#!/usr/bin/python

import threading
import DisplayPie

class Statistic(object):

    def __init__(self, users):
        self.users = users
        self.reset()

    def reset(self):
        self.stat_sex      = {}
        self.stat_language = {}
        self.stat_city     = {}
        self.stat_province = {}
        self.stat_country  = {}
        self.statistic = {
                           'sex'      : self.stat_sex,
                           'language' : self.stat_language,
                           'city'     : self.stat_city,
                           'province' : self.stat_province,
                           'country'  : self.stat_country,
                         }

    def doStatistic(self):

        for i in self.users.values():

            if i.sex in self.stat_sex:
                self.stat_sex[i.sex] += 1
            else:
                self.stat_sex[i.sex] = 1

            if i.language in self.stat_language:
                self.stat_language[i.language] += 1
            else:
                self.stat_language[i.language] = 1

            if i.city in self.stat_city:
                self.stat_city[i.city] += 1
            else:
                self.stat_city[i.city] = 1

            if i.province in self.stat_province:
                self.stat_province[i.province] += 1
            else:
                self.stat_province[i.province] = 1

            if i.country in self.stat_country:
                self.stat_country[i.country] += 1
            else:
                self.stat_country[i.country] = 1

    def showPieChart(self, option):

        if option in self.statistic:

            data  = self.statistic[option].values()
            label = self.statistic[option].keys()
            title_msg = 'Distribution scale for %s' %(option)

            DisplayPie.displayPie(label, data, title_msg)

            #t = threading.Thread(target = DisplayPie.displayPie, args = (data, label, title_msg,))
            #t.start()

            #patches = pie(data, labels = label, autopct='%1.2f%%', shadow=True, startangle=90)
            #title(title_msg)
            #show()

        #if option == 'sex':
        #    pie(self.stat_sex.values(), labels = self.stat_sex.keys(),
        #        autopct='%1.2f%%', shadow=True, startangle=90)
        #    title('Scale for sex distribution')
        #    show()

        #if option == 'language':
        #    pie(self.stat_language.values(), labels = self.stat_language.keys(),
        #        autopct='%1.2f%%', shadow=True, startangle=90)
        #    title('Scale for language distribution')
        #    show()

        #if option == 'city':
        #    pie(self.stat_city.values(), labels = self.stat_city.keys(),
        #        autopct='%1.2f%%', shadow=True, startangle=90)
        #    title('Scale for city distribution')
        #    show()

        #if option == 'province':
        #    pie(self.stat_province.values(), labels = self.stat_province.keys(),
        #        autopct='%1.2f%%', shadow=True, startangle=90)
        #    title('Scale for province distribution')
        #    show()

        #if option == 'country':
        #    pie(self.stat_country.values(), labels = self.stat_country.keys(),
        #        autopct='%1.2f%%', shadow=True, startangle=90)
        #    title('Scale for country distribution')
        #    show()


