from SensorPackages.InfineonSensor import InfineonSensor
import validation


def createObj(sensor_type):
    implemented = ["Infineon"]
    validation.mustBeMember(sensor_type, implemented)

    if sensor_type == "Infineon":
        return InfineonSensor()
