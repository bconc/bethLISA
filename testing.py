# imports
from gwpy.timeseries import TimeSeriesDict
import numpy as np

def read_out_whitened_data(h5_path):
    """read out whitened data from a .h5 file"""
    obs_tdi = (TimeSeriesDict.read(h5_path))
    return obs_tdi

# false_dict[chs[i]] = get_amplitude(false_list[i], obs)

def get_amplitude(times, tdi_list):
    """return the amplitude of the TDI (timeseries) channel at the given times
    times: List
    tdi: Time series
    """
    full_dict = {}
    for k in times.keys():
        time_info = times[k]
        trigger_time = time_info['time trigg']
        channel = time_info['channels']
        i, amplitude_dict = 0, {}
        for tdi in tdi_list:
            trigger_idx = np.argmin(np.abs(tdi.times.value - trigger_time))
            trigger_amplitude = tdi[trigger_idx]
            amplitude_dict[channel[i]] = trigger_amplitude
            i += 1
        full_dict[k] = {'time trigg': trigger_time, 'channels': channel, 'amplitudes': amplitude_dict}

    return full_dict