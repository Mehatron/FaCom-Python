#!/usr/bin/env python

import ctypes;
from .error import *;
from .const import *;

class Facom:
    'Class for communicate with Fatek PLC ussing facom C library'

    def __init__(self):
        'Construct object of type Facom, open library for communication'

        self.is_open = False
        try:
            self.facom = ctypes.CDLL('libfacom.so');
        except:
            assert False, 'Can\'t find "libfacom.so" (FaCom library)'

    def __del__(self):
        'Destructor of object of type Facom, close communication'

        self.close();

    def open(self, port, station_number = 0x01):
        'Open communication to Fatek PLC'

        error = self.facom.FACOM_open(port, station_number);
        if error < 0:
            self.is_open = False;
        else:
            self.is_open = True;
        return error;

    def close(self):
        'Close communication with Fatek PLC'

        if self.is_open:
            return self.facom.FACOM_close();
        return ERROR;

    def set_data_bits(self, data_bits):
        'Set number of data bits'

        return self.facom.FACOM_setDataBits(data_bits);

    def set_parity(self, parity):
        'Set parity'

        return self.facom.FACOM_setParity(parity);

    def set_stop_bits(self, stop_bits):
        'Set number of stop bits'

        return self.facom.FACOM_setStopBits(parity);

    def set_baud_rate(self, baud_rate):
        'Set baud rate (speed)'

        return self.facom.FACOM_setBaudRate(baud_rate);

    def start(self):
        'Set PLC run mode to On'

        return self.facom.FACOM_start();

    def stop(self):
        'Set PLC run mode to Off'

        return self.facom.FACOM_stop();

    def set_discrete(self, discrete_type, discrete_number, action):
        'Set discrete'

        return self.facom.FACOM_setDiscrete(discrete_type, discrete_number, action);

    def set_discretes(self, discrete_type,
                            discrete_number,
                            discrete_count,
                            data):
        'Set multiple continous discretes'

        return self.facom.FACOM_setDiscretes(discrete_type,
                                             discrete_number,
                                             discrete_count,
                                             data);

    def get_discretes(self, discrete_type,
                            discrete_number,
                            discrete_count,
                            data):
        'Get multiple continous discretes'

        return self.facom.FACOM_getDiscretes(discrete_type,
                                             discrete_number,
                                             discrete_count,
                                             data);

