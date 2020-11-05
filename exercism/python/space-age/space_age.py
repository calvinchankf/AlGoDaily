class SpaceAge:

    # years to days
    __on_earth_seconds = 86400
    __on_earth = 365.25
    __on_mercury = (__on_earth * 0.2408467) * __on_earth_seconds
    __on_venus = (__on_earth * 0.61519726) * __on_earth_seconds
    __on_mars = (__on_earth * 1.8808158) * __on_earth_seconds
    __on_jupiter = (__on_earth * 11.862615) * __on_earth_seconds
    __on_saturn = (__on_earth * 29.447498) * __on_earth_seconds
    __on_uranus = (__on_earth * 84.016846) * __on_earth_seconds
    __on_neptune = (__on_earth * 164.79132) * __on_earth_seconds

    _fraction_number = 2
    def __init__(self, seconds):

        self.seconds = seconds

    def on_earth(self):

        return round((self.seconds / self.__on_earth_seconds) / self.__on_earth, self._fraction_number)

    def on_mercury(self):

        return round(self.seconds / self.__on_mercury, self._fraction_number)

    def on_venus(self):

        return round(self.seconds / self.__on_venus, self._fraction_number)

    def on_mars(self):

        return round(self.seconds / self.__on_mars, self._fraction_number)

    def on_jupiter(self):

        return round(self.seconds / self.__on_jupiter, self._fraction_number)

    def on_saturn(self):

        return round(self.seconds / self.__on_saturn, self._fraction_number)

    def on_uranus(self):

        return round(self.seconds / self.__on_uranus, self._fraction_number)

    def on_neptune(self):

        return round(self.seconds / self.__on_neptune, self._fraction_number)


if __name__ == "__main__":
    print(SpaceAge(1000000000).on_earth())