import subprocess
from re import findall
from time import sleep

CPU_MAX_FREQ = 1800000
CPU_MIN_FREQ =  600000

def measure_util_time():
    out=subprocess.run(["cat","/proc/stat"],capture_output=True)
    tvals = [eval(entry) for entry in findall("\d+",str(out.stdout))]
    t_total = sum(tvals[0:8])
    t_active = t_total - tvals[3] - tvals[4]
    return t_total, t_active

def util_ratio(dt=1):
    tt0,ta0 = measure_util_time()
    sleep(dt)
    tt1,ta1 = measure_util_time()
    return (ta1-ta0) / (tt1-tt0)

def set_freq(freq):
    with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed",mode="w") as setspeed:
        setspeed.write(str(freq))

def get_freq():
    out=subprocess.run(["sudo","cat","/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq"],capture_output=True)
    return eval(out.stdout)

def next_freq(util):
    freq = 1.25 * CPU_MAX_FREQ * util
    if freq < CPU_MIN_FREQ:
        freq = CPU_MIN_FREQ
    elif freq > CPU_MAX_FREQ:
        freq = CPU_MAX_FREQ
    else:
        freq = int(freq-freq%100000)
    return freq

# main -----------------------------------------------------

if __name__ == "__main__":

    governor = subprocess.run(["sudo","cat","/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"], capture_output=True).stdout[:-1].decode()
    assert governor=='userspace', f"Must change governor to userspace. Current governor is '{governor}'"

    try:
        while True:
            util = util_ratio(0.5)
            new_freq = next_freq(util)
            print("util: %8.4f%%\t\tcurrent: %7d\tnext: %7d" % (100*util, get_freq(), new_freq))
            set_freq(new_freq)
    except KeyboardInterrupt:
        print("\nkbi exit\n")