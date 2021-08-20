class Clock:
   
    def __init__(self, hour, minute):
        hours = minute // 60 + hour
        self._minute = minute % 60
        self._hour = hours % 24
        

    def __repr__(self):
        return f"{self._hour:02}:{self._minute:02}"

    def __eq__(self, other):
        return self._hour==other._hour and self._minute==other._minute     

    def __add__(self, minutes):
        extra_hours, extra_minutes = divmod(minutes, 60)
        self._hour = self._hour + extra_hours
        self._minute = self._minute + extra_minutes
        return Clock(self._hour, self._minute)
        


    def __sub__(self, minutes):
        extra_hours, extra_minutes = divmod(minutes, 60)
        self._hour = self._hour - extra_hours
        self._minute = self._minute - extra_minutes
        return Clock(self._hour, self._minute)
        