import pyspedas, pytplot
from datetime import datetime
import numpy as np
from scipy.interpolate import interp1d
from .dbase import dbase

class spec:

  @staticmethod
  def create_timestamp_mask(ts, start, end, dur=0):
    #convert start and end times to seconds since epoch
    epoch = datetime(1970, 1, 1)
    start_seconds = (datetime.strptime(start, "%Y-%m-%d/%H:%M:%S") - epoch).total_seconds()
    end_seconds = (datetime.strptime(end, "%Y-%m-%d/%H:%M:%S") - epoch).total_seconds()

    #add a section of valid timestamps to the boolean mask
    return ((ts >= start_seconds) & (ts+dur <= end_seconds))

  @staticmethod
  def ave_spec(ts, cnts, periods):
    if isinstance(periods, tuple):
      periods = [periods]
      
    mask = False
    for (start, end) in periods:
      mask = mask | spec.create_timestamp_mask(ts, start, end)

    #use the mask to select just the counts that we are interested in and take their average
    selected = cnts[mask]
    return np.mean(selected, axis=0)
    
  @staticmethod
  def average_event_spectrum(ts, cnts, nrg, bkg_periods, evt_periods):
    ave_bkg = spec.ave_spec(ts, cnts, bkg_periods)
    ave_evt = spec.ave_spec(ts, cnts, evt_periods)

    return ave_evt-ave_bkg

  @staticmethod
  def background_subtracted_spectrogram(ts, cnts, nrg, bkg_periods):
    ave_bkg = spec.ave_spec(ts, cnts, bkg_periods)
    
    return cnts-ave_bkg

  @staticmethod
  def barrel_sp_make(tplot_var, event_periods=[], background_periods=[]):
    is_slow = tplot_var.endswith("_SSPC")
    payload = tplot_var[3:-5]
    event_periods =  [event_periods] if isinstance(event_periods, tuple) else event_periods
    background_periods =  [background_periods] if isinstance(background_periods, tuple) else background_periods

    size = 256 if is_slow else 48
    drm_size = 256 if is_slow else 184

    return {
      'payload': payload,                                   # Two-character payload ID (e.g. 1F)
      'tplot_var': tplot_var,
      'trange': event_periods,
      'bkgtrange': background_periods,
      'req_date': "",                                       # Requested start time
      'req_duration': "",                                   # Requested duration in hours
      'num_src': len(event_periods),                        # of source spectrum time intervals (default 1)
      'num_bkg': len(background_periods),                   # of background spectrum time intervals (default 1) 
      'is_slow': is_slow,                                   # slow spectrum (256 bins) or medium spectrum (48 bins) 
      'size': size,                                         # number of bins in spectrum 
      'altitude': -1,                                       # altitude in km
      'maglat': -1,                                         # magnetic latitude in degrees
      'bkg_method': 1,                                      # 1 = from data stream, 2 =from model
      'src_spec': np.ones(size, dtype="float") * -1,        # summed source spectrum, deadtime corrected       
      'src_spec_err': np.ones(size, dtype="float") * -1,    # error in summed source spectrum
      'bkg_spec': np.ones(size, dtype="float") * -1,        # summed background spectrum, deadtime corrected        
      'bkg_spec_err': np.ones(size, dtype="float") * -1,    # error in summed background spectrum
      'src_time': -1,                                       # source spectrum accum. time in seconds
      'bkg_time': -1,                                       # background spectrum accum. time in seconds
      'src_live': -1,                                       # source spectrum livetime, seconds (approx.)
      'bkg_live': -1,                                       # background spectrum livetime, seconds (approx.)
      'bkg_renorm': -1,                                     # switch to renormalize bkg to match source > 3 MeV
      'subspec': np.ones(size) * -1,                        # background subtracted spectrum, deadtime corrected
      'subspec_err': np.ones(size) * -1,                    # error in background subtracted spectrum
      'drm_size': drm_size,                                 # number of drm rows (electron side)
      'e_bins': spec.make_standard_energies(is_slow),      # energy channel boundaries (keV)
      'ele_bins': spec.make_standard_electron_energies(is_slow),   # energy boundaries on electron side (ct side is fixed)
      'drm': np.ones((size, drm_size), dtype="float"),      # response matrix
      'drm_type': -1,                                       # 1 =downward isotropic, 2 =mirroring, 3 =other
      'drm2': np.ones((size, drm_size), dtype="float")*-1,  # second response matrix 
      'drm2_type': -1,                                      # 1 =downward isotropic, 2 =mirroring, 3 =other
      'method': -1,                                         # fitting method (1-6)
      'model': -1,                                          # fitting model (1-2)  = exponential, monoenergetic
      'fitrange': np.ones(2, dtype="float") * -1,           # fitting range of energies
      'numparams': -1,                                      # number of fit parameters
      'params': np.ones(10, dtype="float") * -1,            # fit parameters
      'param_ranges': np.ones([10,2], dtype="float") * -1,  # 1-sigma ranges on fit parameters
      'chisq': -1,                                          # chi-square of fit (unreduced)
      'chi_dof': -1,                                        # degrees of freedom for chi-square of fit
      'modvals': np.ones(size, dtype="float") * -1,         # values of model fit at center of each bin
      'secondmodvals': np.ones(size, dtype="float") * -1   # values of 2nd component at center of each bin 
    } 
  
  @staticmethod
  def make_standard_energies(is_slow):
    d = dbase.calib_sspc if is_slow else dbase.calib_mspc
    return d[:,1]
  
  @staticmethod
  def make_standard_electron_energies(is_slow):
    #get sspc standard energies
    e0 = spec.make_standard_energies(is_slow)
    
    if is_slow:
      e = e0
    else:
      #if we are using mspc, we need to interpolate 
      max_index = e0.size - 1
      scale_factor = np.arange(3)/3
      e = np.zeros((max_index)*3 + 1 + 40)
      
      #the new array `e` will have 2 new elements added between each element of `e0`, scaled linearly
      for i in range(max_index):
        e[3*i : (3*i)+3] = e0[i] + (e0[i+1] - e0[i]) * scale_factor 
      
      #add the last value of `e0` to `e`
      e[max_index*3] = e0[max_index]

      #add an extra 40 energy levels in steps of 100 starting at the highest energy of `e0`
      e[e.size-40:e.size] = [num*100 for num in range(1,41)] + e0[max_index]
    return e

  @staticmethod
  def edge_products(edges):
    if isinstance(edges, list):
      edges = np.array(edges)

    if not isinstance(edges, np.ndarray):
      raise ValueError("Input must be a list or a NumPy array")

    #Set up defaults for degenerate case of single value
    width = 0.0
    mean = edges
    gmean = edges
    edges_2 = edges
    edges_1 = edges
    
    if edges.size == 1:
      return [width, mean, gmean]

    dims = edges.shape
    
    if len(dims) > 1 and dims[1] == 2:
        edges_2 = edges
        edges_1 = np.concatenate([edges_2[:,1],[edges_2[:,0][-1]]])
    else:
        edges_2 = np.array([edges[0:-1], edges[1:]]).transpose()
        edges_1 = edges

    mean = edges_2.sum(0)/2
    gmean = np.sqrt((edges_2[:,0]*edges_2[:, 1]))
    width = np.abs(edges_2[:,1]-edges_2[:,0])

    return [width, mean, gmean]
  
  @staticmethod
  def barrel_sp_collect_spectra(ss, altitude=None, maglat=None):
    if altitude is None:
      pyspedas.barrel.ephm(ss["trange"][0], ss["payload"])
      ts, alt = pytplot.get_data('brl'+ss["payload"]+'_GPS_Alt')
      ss["altitude"] = altitude if altitude else alt[int(alt.size/2)]
      print(ss["altitude"])

    if maglat is None and ss["bkg_method"]==2:
      print("Please supply magnetic latitude")
      return
    
    width, mean, gmean = spec.edge_products(ss["e_bins"]) 
    
    for (start, end) in ss["trange"]:
      (spectrum, livetime, rawtime) = spec.barrel_sp_collect_one_spectrum(ss, start, end)
      if livetime == -1 and rawtime == 1:
        #this is the first run, overwrite the fill values
        ss["src_spec"] = spectrum
        ss["src_live"] = livetime
        ss["src_time"] = rawtime
      else:
        ss["src_spec"] += spectrum
        ss["src_live"] += livetime
        ss["src_time"] += rawtime
      
      #Revert to cts/bin instead of cts/keV to calculate errors:
      raw = ss["src_spec"]*(width*ss["src_live"]/ss["src_time"])
      #Average of upper and lower limits from Gehrels 1986:
      ss["src_spec_err"] = ( np.sqrt(raw-0.25) + np.sqrt(raw+0.75) + 1. ) / 2.
      #Return to /keV for the error:
      ss["src_spec_err"] /= (width*ss["src_live"]/ss["src_time"])
  
    if ss["bkg_method"] == 1:
      for (start, end) in ss["bkgtrange"]:
        (spectrum, livetime, rawtime) = spec.barrel_sp_collect_one_spectrum(ss, start, end)
        if livetime == -1 and rawtime == 1:
          #this is the first run, overwrite the fill values
          ss["bkg_spec"] = spectrum
          ss["bkg_live"] = livetime
          ss["bkg_time"] = rawtime
        else:
          ss["bkg_spec"] += spectrum
          ss["bkg_live"] += livetime
          ss["bkg_time"] += rawtime
      
      #Revert to cts/bin instead of cts/keV to calculate errors:
      raw = ss["bkg_spec"]*(width*ss["bkg_live"]/ss["bkg_time"])
      #Average of upper and lower limits from Gehrels 1986:
      ss["bkg_spec_err"] = (np.sqrt(raw-0.25) + np.sqrt(raw+0.75) + 1. ) / 2.
      #Return to /keV for the error:
      ss["bkg_spec_err"] /= (width*ss["bkg_live"]/ss["bkg_time"])
    #else:
      #***STILL NEED TO FINISH PORTING BACKGROUND METHOD 2**
      ##Generate background model in 5 keV bins and rebin:
      #fine_ebins = findgen(1400)*5.+20.
      #edge_products, fine_ebins, mean=fmean, width=fwidth
      #bkgfine = barrel_make_model_bkg( fmean, ss.altitude, ss.maglat )
      #bkgnormal = brl_rebin(bkgfine,fine_ebins,ss.ebins,flux=1)
      #ss["bkg_spec"] = bkgnormal
      #ss["bkg_live"] = 1.
      #ss["bkg_time"] = 1.
      ##Take somewhat arbitrary 5% error bars, even though not really uncorrelated:
      #ss["bkg_spec_err"] = 0.05*ss["bkg_spec"]

  @staticmethod
  def barrel_sp_collect_one_spectrum(ss, start, end):
    dur = 32 if ss["is_slow"] else 4

    spect = pytplot.get_data(ss["tplot_var"])
    spectots = spect.y.sum(1)
    goodspect = spectots >= 0.1

    # Get a list of timestamps for spectra that are contained entirely within the start/end times
    w = spec.create_timestamp_mask(spect.times, start, end, dur)
    # combine with goodspect to get a list of all good spectra within the time bounds
    w = w & goodspect
    spect_cnts = spect.y[w]
    spect_time = spect.times[w]

    #Load IRQ data from the RCNT CDF file
    pyspedas.barrel.rcnt((start, end), ss["payload"])
    irq = pytplot.get_data("brl"+ss["payload"]+"_Interrupt")
    goodirq = irq.y >= 0

    #To calculate livetime, use the IRQ rate. Still use "dur" even 
    #though IRQ is available at 0.25 Hz so that the boundaries match:
    wl = spec.create_timestamp_mask(irq.times, start, end, dur)
    # mask out any bad IRQ values
    wl = wl & goodirq
    rate_irq = irq.y[wl] / 4 #NOT dur here; units must match
    irq_time = irq.times[wl]

    #Calculate the rate in the spectrum
    width, mean, gmean = spec.edge_products(ss["e_bins"])
    rate_spect = []
    spectrum = np.zeros(width.size)
    livetime = 0
    rawtime = 0

    #sum up, calculating livetime using nearest IRQ measurement to each
    #spectrum as you go along:
    #spect.y is /s/keV.
    for (accum, ts) in zip(spect_cnts, spect_time):
      rate_spect.append(np.sum(accum*width))
      dts = np.abs(irq_time-ts)
      nearest_irq = rate_irq[np.argmin(dts)]

      #set units to counts/keV & we will divide by live seconds later:
      spectrum += dur*accum/(1. - nearest_irq*8.0e-6)
      livetime += dur*(1.- nearest_irq*8.0e-6)
      rawtime += dur
    
    return (spectrum, livetime, rawtime)
    


 