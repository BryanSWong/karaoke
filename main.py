from interface import Power, Interface

power_on = Power('main')
start = Interface(power_on)
start.start()
