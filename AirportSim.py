import simpy
import random

# this is the value of lambda
arrival_rate = 50
# Id/Boarding pass checking time (in min) per passenger Mu2 (from the problem)
id_check_rate = 0.75
# minimum personal scanner time
min_p_scan = 0.5
# maximum personal scanner time
max_p_scan = 1
# number of ID checkers
checkers_count = 30
# number of personal scanners
scanners_count = 30

# --------------------Variables to capture avg time per replication--------------------------
avg_check_time = []
avg_scan_time = []
avg_total_time_per_passenger = []


class Metrics(object):
    def __init__(self):
        self.p_count = 0
        self.check_time = []
        self.scan_time = []
        self.total_time_per_passenger = []


class Airport(object):
    def __init__(self, env):
        self.env = env
        # NOTE: remember the hint in the problem - [Hint: model them as one block that has more than one resource]
        # checkers are handled as one block with multiple resources but personal scanners are treated as multiple blocks
        # with one resource and are queue based. Note the difference
        self.checker = simpy.Resource(env, checkers_count)
        self.scanner = []
        for i in range(scanners_count):
            self.scanner.append(simpy.Resource(env, 1))

    # boarding pass check event for each passenger
    def boarding_pass_check(self):
        # NOTE - id_Check_rate is the exponential service time, so in order to use it in a poisson process, we need to take the inverse
        yield self.env.timeout(random.expovariate(1.0 / id_check_rate))

    # personal scanning event for each passenger
    def personal_scan(self):
        yield self.env.timeout(random.uniform(min_p_scan, max_p_scan))


def passenger(env, p_name, airport, metric):
    arrival_time = env.now  # arrival time of passenger
    # this is the ID and Boarding pass check process
    with airport.checker.request() as request:
        yield request
        check_start = env.now
        yield env.process(airport.boarding_pass_check())
        check_end = env.now
        metric.check_time.append(check_end - check_start)

    # this is the personal scanning process
    # first we will need to find the shortest scanner queue to send the passenger to
    temp = []
    for scanner in airport.scanner:
        temp.append(len(scanner.queue))

    min_index = temp.index(min(temp))
    with airport.scanner[min_index].request() as request:
        yield request
        scan_start = env.now
        yield env.process(airport.personal_scan())
        scan_end = env.now
        metric.scan_time.append(scan_end - scan_start)

    depart_time = env.now
    metric.total_time_per_passenger.append(depart_time - arrival_time)
    metric.p_count += 1


def passenger_arrival(env, metric):
    count = 0
    airport = Airport(env)
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        count = count + 1
        # now start the process of ID check and personal scan for the passenger
        env.process(passenger(env, 'Passenger %d' % count, airport, metric))


def start_airport_simulator(replications, run_time):
    for i in range(replications):
        # initialize the metrics object
        metric = Metrics()
        # choose random seed
        random.seed(i)
        # create environment
        env = simpy.Environment()
        # run the simulation
        env.process(passenger_arrival(env, metric))
        env.run(until=run_time)

        # --------------calculate avg times per replication----------------
        avg_check_time.append(sum(metric.check_time[1:metric.p_count]) / metric.p_count)
        avg_scan_time.append(sum(metric.scan_time[1:metric.p_count]) / metric.p_count)
        avg_total_time_per_passenger.append(sum(metric.total_time_per_passenger[1:metric.p_count]) / metric.p_count)
        print(
            'Replication %d: Passenger count was %d: Avg Total time %.2f, Avg ID check time %.2f, Avg Scan time %.2f' % (
            i + 1, metric.p_count, avg_total_time_per_passenger[i], avg_check_time[i], avg_scan_time[i]))


if __name__ == '__main__':
    replications = 50
    run_time = 100
    start_airport_simulator(replications, run_time)
