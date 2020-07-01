import simpy

class metrics(object):
    def __init__(self):
        self.count= 0

def clock(env, tick,m):
    while True:
        global name
        name = name + "de"
        #print(name, env.now)
        m.count = m.count + 1
        yield env.timeout(tick)

if __name__ == '__main__':
    env = simpy.Environment()
    global name
    name = "KPenugon"
    m = metrics()
    env.process(clock(env,0.5,m))
    env.run(until=5)
    print(m.count)