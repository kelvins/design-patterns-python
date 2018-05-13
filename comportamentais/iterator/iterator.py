#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class RadioStation(object):

    def __init__(self, frequency):
        self.__frequency = frequency

    @property
    def frequency(self):
        return self.__frequency


class StationList(object):

    def __init__(self):
        self.__stations = []
        self.__counter = 0

    def add_station(self, radio_station):
        self.__stations.append(radio_station)

    def remove_station(self, frequency):
        for index in range(0, len(self.__stations)):
            if self.__stations[index].frequency == frequency:
                self.__stations.pop(index)
                break
        else:
            print 'Radio station not found'

    def count(self):
        return len(self.__stations)

    def current(self):
        return self.__stations[self.__counter].frequency

    def key(self):
        return self.__counter

    def next(self):
        self.__counter += 1

    def rewind(self):
        self.__counter = 0


if __name__ == '__main__':
    station_list = StationList()

    station_list.add_station(RadioStation(89))
    station_list.add_station(RadioStation(101))
    station_list.add_station(RadioStation(102))
    station_list.add_station(RadioStation(103.2))

    print 'Stations: {}'.format(station_list.count())
    station_list.remove_station(89)
    print 'Stations: {}'.format(station_list.count())

    print 'Current Station: {}'.format(station_list.current())
    station_list.next()
    print 'Current Station: {}'.format(station_list.current())
