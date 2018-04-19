
class Meter(object):
    """Дескриптор для метра."""

    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Foot(object):
    """Дескриптор для фута."""

    def __get__(self, instance, owner):
        return instance.meter * 3.2808

    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808


class Distance:
    """Класс, описывающий расстояние, содержит два дескриптора для футов и метров."""
    meter = Meter()
    foot = Foot()

