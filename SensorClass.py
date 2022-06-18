from abc import ABC, abstractmethod
import sys

sys.path.insert(1, '/home/ivar/Repos/Sensor project/')
import smbus2
import ByteTools
import validation


class SensorClassAbstract(ABC):
    def __init__(self, identifier, addresses, states, scale_factors, bus):
        self.identifier = identifier
        self.addresses = addresses
        self.scale_factors = scale_factors
        self.bus = bus
        self.states = states

    @property
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def setState(self):
        pass

    def getAddress(self, address_type):
        return self.addresses[address_type]



