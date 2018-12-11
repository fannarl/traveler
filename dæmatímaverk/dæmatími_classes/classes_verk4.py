class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return '{} hours, {} minutes and {} seconds'.format(self.hours, self.minutes, self.seconds)        


    def str_update(self, hhmmss):
        self.hhmmss = hhmmss
        hh, mm, ss = hhmmss.split(":")
        self.hours = int(hh)
        self.minutes = int(mm)
        self.seconds = int(ss)


    def add_clocks(self, clock_time):
        self.clock_time = clock_time
        hh2, mm2, ss2 = str(clock_time).split(':')
        hh3 = int(hh2) + int(self.hours)
        mm3 = int(mm2) + int(self.minutes)
        ss3 = int(ss2) + int(self.seconds)
        
        mins = divmod(ss3, 60)
        hour = divmod(mm3, 60)
        day = divmod(hh3, 24)

        ss3 = int(mins[-1])
        mm3 = int(mins[0]) + int(hour[-1])
        hh3 = int(hour[0]) + int(day[-1])
        
        self.hour = str(hh3)
        self.minutes = str(mm3)
        self.seconds = str(ss3)

        print(self.seconds)
        print(self.minutes)
        print(self.hours)

clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
#assert str(clock1) == "0 hours, 0 minutes and 0 seconds"

clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
# #assert str(clock2) == "5 hours, 45 minutes and 52 seconds"

clock3 = clock1.add_clocks(clock2)
print(clock3)
# #assert str(clock3) == "9 hours, 7 minutes and 26 seconds"