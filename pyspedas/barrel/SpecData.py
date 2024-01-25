import numpy as np

class SpecData: 
  calib_sspc = np.array([
    [0.0010,      0.00,    1.000000],
    [2.4414,      2.44,    1.000000],
    [4.8828,      4.88,    1.000000],
    [7.3242,      7.32,    1.000000],
    [9.7656,      9.77,    1.000000],
    [12.2070,     12.21,   1.000000],
    [14.6484,     14.65,   1.000000],
    [17.0898,     17.09,   1.000000],
    [19.5312,     19.53,   1.000000],
    [21.9727,     21.97,   1.000000],
    [24.4141,     24.41,   1.000000],
    [26.8555,     26.86,   1.000000],
    [29.2969,     29.30,   1.000000],
    [31.7383,     31.74,   1.000000],
    [34.1797,     34.18,   1.000000],
    [36.6211,     36.62,   1.000000],
    [39.0625,     39.06,   1.000000],
    [41.5039,     41.50,   1.000000],
    [43.9453,     43.95,   1.000000],
    [46.3867,     46.39,   1.000000],
    [48.8281,     48.83,   1.000000],
    [51.2695,     51.27,   1.000000],
    [53.7109,     53.71,   1.000000],
    [56.1523,     56.15,   1.000000],
    [58.5938,     58.59,   1.000000],
    [61.0352,     61.04,   1.000000],
    [63.4766,     63.48,   1.000000],
    [65.9180,     65.92,   1.000000],
    [68.3594,     68.36,   1.000000],
    [70.8008,     70.80,   1.000000],
    [73.2422,     73.24,   1.000000],
    [75.6836,     75.68,   1.000000],
    [78.1250,     78.12,   1.000000],
    [80.5664,     80.57,   1.000000],
    [83.0078,     83.01,   1.000000],
    [85.4492,     85.45,   1.000000],
    [87.8906,     87.89,   1.000000],
    [90.3320,     90.33,   1.000000],
    [92.7734,     92.77,   1.000000],
    [95.2148,     95.21,   1.000000],
    [97.6562,     97.66,   1.000000],
    [100.0977,    100.10,   1.000000],
    [102.5391,    102.54,   1.000000],
    [104.9805,    104.98,   1.000000],
    [107.4219,    107.42,   1.000000],
    [109.8633,    109.86,   1.000000],
    [112.3047,    112.30,   1.000000],
    [114.7461,    114.75,   1.000000],
    [117.1875,    117.19,   1.000000],
    [119.6289,    119.63,   1.000000],
    [122.0703,    122.07,   1.000000],
    [124.5117,    124.51,   1.000000],
    [126.9531,    126.95,   1.000000],
    [129.3945,    129.39,   1.000000],
    [131.8359,    131.84,   1.000000],
    [134.2773,    134.28,   1.000000],
    [136.7188,    136.72,   1.000000],
    [139.1602,    139.16,   1.000000],
    [141.6016,    141.60,   1.000000],
    [144.0430,    144.04,   1.000000],
    [146.4844,    146.48,   1.000000],
    [148.9258,    148.93,   1.000000],
    [151.3672,    151.37,   1.000000],
    [153.8086,    153.81,   1.000000],
    [156.2500,    156.25,   0.500000],
    [161.1328,    161.13,   0.500000],
    [166.0156,    166.02,   0.500000],
    [170.8984,    170.90,   0.500000],
    [175.7812,    175.78,   0.500000],
    [180.6641,    180.66,   0.500000],
    [185.5469,    185.55,   0.500000],
    [190.4297,    190.43,   0.500000],
    [195.3125,    195.31,   0.500000],
    [200.1953,    200.20,   0.500000],
    [205.0781,    205.08,   0.500000],
    [209.9609,    209.96,   0.500000],
    [214.8438,    214.84,   0.500000],
    [219.7266,    219.73,   0.500000],
    [224.6094,    224.61,   0.500000],
    [229.4922,    229.49,   0.500000],
    [234.3750,    234.38,   0.500000],
    [239.2578,    239.26,   0.500000],
    [244.1406,    244.14,   0.500000],
    [249.0234,    249.02,   0.500000],
    [253.9062,    253.91,   0.500000],
    [258.7891,    258.79,   0.500000],
    [263.6719,    263.67,   0.500000],
    [268.5547,    268.55,   0.500000],
    [273.4375,    273.44,   0.500000],
    [278.3203,    278.32,   0.500000],
    [283.2031,    283.20,   0.500000],
    [288.0859,    288.09,   0.500000],
    [292.9688,    292.97,   0.500000],
    [297.8516,    297.85,   0.500000],
    [302.7344,    302.73,   0.500000],
    [307.6172,    307.62,   0.500000],
    [312.5000,    312.50,   0.250000],
    [322.2656,    322.27,   0.250000],
    [332.0312,    332.03,   0.250000],
    [341.7969,    341.80,   0.250000],
    [351.5625,    351.56,   0.250000],
    [361.3281,    361.33,   0.250000],
    [371.0938,    371.09,   0.250000],
    [380.8594,    380.86,   0.250000],
    [390.6250,    390.62,   0.250000],
    [400.3906,    400.39,   0.250000],
    [410.1562,    410.16,   0.250000],
    [419.9219,    419.92,   0.250000],
    [429.6875,    429.69,   0.250000],
    [439.4531,    439.45,   0.250000],
    [449.2188,    449.22,   0.250000],
    [458.9844,    458.98,   0.250000],
    [468.7500,    468.75,   0.250000],
    [478.5156,    478.52,   0.250000],
    [488.2812,    488.28,   0.250000],
    [498.0469,    498.05,   0.250000],
    [507.8125,    507.81,   0.250000],
    [517.5781,    517.58,   0.250000],
    [527.3438,    527.34,   0.250000],
    [537.1094,    537.11,   0.250000],
    [546.8750,    546.88,   0.250000],
    [556.6406,    556.64,   0.250000],
    [566.4062,    566.41,   0.250000],
    [576.1719,    576.17,   0.250000],
    [585.9375,    585.94,   0.250000],
    [595.7031,    595.70,   0.250000],
    [605.4688,    605.47,   0.250000],
    [615.2344,    615.23,   0.250000],
    [625.0000,    625.00,   0.125000],
    [644.5312,    644.53,   0.125000],
    [664.0625,    664.06,   0.125000],
    [683.5938,    683.59,   0.125000],
    [703.1250,    703.12,   0.125000],
    [722.6562,    722.66,   0.125000],
    [742.1875,    742.19,   0.125000],
    [761.7188,    761.72,   0.125000],
    [781.2500,    781.25,   0.125000],
    [800.7812,    800.78,   0.125000],
    [820.3125,    820.31,   0.125000],
    [839.8438,    839.84,   0.125000],
    [859.3750,    859.38,   0.125000],
    [878.9062,    878.91,   0.125000],
    [898.4375,    898.44,   0.125000],
    [917.9688,    917.97,   0.125000],
    [937.5000,    937.50,   0.125000],
    [957.0312,    957.03,   0.125000],
    [976.5625,    976.56,   0.125000],
    [996.0938,    996.09,   0.125000],
    [1015.6250,   1015.62,  0.125000],
    [1035.1562,   1035.16,  0.125000],
    [1054.6875,   1054.69,  0.125000],
    [1074.2188,   1074.22,  0.125000],
    [1093.7500,   1093.75,  0.125000],
    [1113.2812,   1113.28,  0.125000],
    [1132.8125,   1132.81,  0.125000],
    [1152.3438,   1152.34,  0.125000],
    [1171.8750,   1171.88,  0.125000],
    [1191.4062,   1191.41,  0.125000],
    [1210.9375,   1210.94,  0.125000],
    [1230.4688,   1230.47,  0.125000],
    [1250.0000,   1250.00,  0.062500],
    [1289.0625,   1289.06,  0.062500],
    [1328.1250,   1328.12,  0.062500],
    [1367.1875,   1367.19,  0.062500],
    [1406.2500,   1406.25,  0.062500],
    [1445.3125,   1445.31,  0.062500],
    [1484.3750,   1484.38,  0.062500],
    [1523.4375,   1523.44,  0.062500],
    [1562.5000,   1562.50,  0.062500],
    [1601.5625,   1601.56,  0.062500],
    [1640.6250,   1640.62,  0.062500],
    [1679.6875,   1679.69,  0.062500],
    [1718.7500,   1718.75,  0.062500],
    [1757.8125,   1757.81,  0.062500],
    [1796.8750,   1796.88,  0.062500],
    [1835.9375,   1835.94,  0.062500],
    [1875.0000,   1875.00,  0.062500],
    [1914.0625,   1914.06,  0.062500],
    [1953.1250,   1953.12,  0.062500],
    [1992.1875,   1992.19,  0.062500],
    [2031.2500,   2031.25,  0.062500],
    [2070.3125,   2070.31,  0.062500],
    [2109.3750,   2109.38,  0.062500],
    [2148.4375,   2148.44,  0.062500],
    [2187.5000,   2187.50,  0.062500],
    [2226.5625,   2226.56,  0.062500],
    [2265.6250,   2265.62,  0.062500],
    [2304.6875,   2304.69,  0.062500],
    [2343.7500,   2343.75,  0.062500],
    [2382.8125,   2382.81,  0.062500],
    [2421.8750,   2421.88,  0.062500],
    [2460.9375,   2460.94,  0.062500],
    [2500.0000,   2500.00,  0.031250],
    [2578.1250,   2578.12,  0.031250],
    [2656.2500,   2656.25,  0.031250],
    [2734.3750,   2734.38,  0.031250],
    [2812.5000,   2812.50,  0.031250],
    [2890.6250,   2890.62,  0.031250],
    [2968.7500,   2968.75,  0.031250],
    [3046.8750,   3046.88,  0.031250],
    [3125.0000,   3125.00,  0.031250],
    [3203.1250,   3203.12,  0.031250],
    [3281.2500,   3281.25,  0.031250],
    [3359.3750,   3359.38,  0.031250],
    [3437.5000,   3437.50,  0.031250],
    [3515.6250,   3515.62,  0.031250],
    [3593.7500,   3593.75,  0.031250],
    [3671.8750,   3671.88,  0.031250],
    [3750.0000,   3750.00,  0.031250],
    [3828.1250,   3828.12,  0.031250],
    [3906.2500,   3906.25,  0.031250],
    [3984.3750,   3984.38,  0.031250],
    [4062.5000,   4062.50,  0.031250],
    [4140.6250,   4140.62,  0.031250],
    [4218.7500,   4218.75,  0.031250],
    [4296.8750,   4296.88,  0.031250],
    [4375.0000,   4375.00,  0.031250],
    [4453.1250,   4453.12,  0.031250],
    [4531.2500,   4531.25,  0.031250],
    [4609.3750,   4609.38,  0.031250],
    [4687.5000,   4687.50,  0.031250],
    [4765.6250,   4765.62,  0.031250],
    [4843.7500,   4843.75,  0.031250],
    [4921.8750,   4921.88,  0.031250],
    [5000.0000,   5000.00,  0.015625],
    [5156.2500,   5156.25,  0.015625],
    [5312.5000,   5312.50,  0.015625],
    [5468.7500,   5468.75,  0.015625],
    [5625.0000,   5625.00,  0.015625],
    [5781.2500,   5781.25,  0.015625],
    [5937.5000,   5937.50,  0.015625],
    [6093.7500,   6093.75,  0.015625],
    [6250.0000,   6250.00,  0.015625],
    [6406.2500,   6406.25,  0.015625],
    [6562.5000,   6562.50,  0.015625],
    [6718.7500,   6718.75,  0.015625],
    [6875.0000,   6875.00,  0.015625],
    [7031.2500,   7031.25,  0.015625],
    [7187.5000,   7187.50,  0.015625],
    [7343.7500,   7343.75,  0.015625],
    [7500.0000,   7500.00,  0.015625],
    [7656.2500,   7656.25,  0.015625],
    [7812.5000,   7812.50,  0.015625],
    [7968.7500,   7968.75,  0.015625],
    [8125.0000,   8125.00,  0.015625],
    [8281.2500,   8281.25,  0.015625],
    [8437.5000,   8437.50,  0.015625],
    [8593.7500,   8593.75,  0.015625],
    [8750.0000,   8750.00,  0.015625],
    [8906.2500,   8906.25,  0.015625],
    [9062.5000,   9062.50,  0.015625],
    [9218.7500,   9218.75,  0.015625],
    [9375.0000,   9375.00,  0.015625],
    [9531.2500,   9531.25,  0.015625],
    [9687.5000,   9687.50,  0.015625],
    [9843.7500,   9843.75,  0.015625],
    [9999.9900,  9999.990,  0.015625]
  ])

  calib_mspc = np.array([
    [102.5391,  25.63,  0.814584, 1.00000],
    [112.3047,  28.08,  0.798828, 1.00000],
    [122.0703,  30.52,  0.783377, 1.33333],
    [129.3945,  32.35,  0.771986, 1.00000],
    [139.1602,  34.79,  0.757054, 1.33333],
    [146.4844,  36.62,  0.746045, 1.00000],
    [156.2500,  39.06,  0.731616, 0.66667],
    [170.8984,  42.72,  0.710492, 0.50000],
    [190.4297,  47.61,  0.683274, 0.66667],
    [205.0781,  51.27,  0.663547, 0.50000],
    [224.6094,  56.15,  0.638126, 0.50000],
    [244.1406,  61.04,  0.613680, 0.66667],
    [258.7891,  64.70,  0.595962, 0.50000],
    [278.3203,  69.58,  0.573131, 0.66667],
    [292.9688,  73.24,  0.556584, 0.50000],
    [312.5000,  78.12,  0.535261, 0.33333],
    [341.7969,  85.45,  0.504800, 0.25000],
    [380.8594,  95.21,  0.466863, 0.33333],
    [410.1562, 102.54,  0.440294, 0.25000],
    [449.2188, 112.30,  0.407205, 0.25000],
    [488.2812, 122.07,  0.376603, 0.33333],
    [517.5781, 129.39,  0.355171, 0.25000],
    [556.6406, 139.16,  0.328479, 0.33333],
    [585.9375, 146.48,  0.309786, 0.25000],
    [625.0000, 156.25,  0.286505, 0.16667],
    [683.5938, 170.90,  0.254823, 0.12500],
    [761.7188, 190.43,  0.217961, 0.16667],
    [820.3125, 205.08,  0.193859, 0.12500],
    [898.4375, 224.61,  0.165816, 0.12500],
    [976.5625, 244.14,  0.141830, 0.16667],
    [035.1562, 258.79,  0.126146, 0.12500],
    [113.2812, 278.32,  0.107899, 0.16667],
    [171.8750, 292.97,  0.095967, 0.12500],
    [250.0000, 312.50,  0.082085, 0.08333],
    [367.1875, 341.80,  0.064935, 0.06250],
    [523.4375, 380.86,  0.047507, 0.08333],
    [640.6250, 410.16,  0.037581, 0.06250],
    [796.8750, 449.22,  0.027495, 0.06250],
    [953.1250, 488.28,  0.020116, 0.08333],
    [070.3125, 517.58,  0.015913, 0.06250],
    [226.5625, 556.64,  0.011642, 0.08333],
    [343.7500, 585.94,  0.009210, 0.06250],
    [500.0000, 625.00,  0.006738, 0.04167],
    [734.3750, 683.59,  0.004216, 0.03125],
    [046.8750, 761.72,  0.002257, 0.04167],
    [281.2500, 820.31,  0.001412, 0.03125],
    [593.7500, 898.44,  0.000756, 0.03125],
    [906.2500, 976.56,  0.000405, 0.06250],
    [999.9900, 1000.00, 0.000335, 0.03125]
  ])
  
  def __init__(self, payload, background_intervals=[], event_intervals=[], is_slow=True):
    self.payload = payload
    self.background_intervals = background_intervals 
    self.event_intervals= event_intervals
    self.is_slow = is_slow
    self.size = 256 if self.is_slow else 48
    self.altitude = -1 
    self.maglat = -1
    self.bkg_method = -1                                              #1 =from data stream, 2 =from model
    self.src_spec = np.ones(self.size, dtype="float") * -1            #summed source spectrum, deadtime corrected       
    self.src_specerr = np.ones(self.size, dtype="float") * -1         #error in summed source spectrum
    self.bkg_spec = np.ones(self.size, dtype="float") * -1            #summed background spectrum, deadtime corrected        
    self.bkg_spec_err = np.ones(self.size, dtype="float") * -1        #error in summed background spectrum
    self.src_time = -1                                                #source spectrum accum. time in seconds
    self.bkg_time = -1                                                #background spectrum accum. time in seconds
    self.src_live = -1                                                #source spectrum livetime, seconds (approx.)
    self.bkg_live = -1                                                #background spectrum livetime, seconds (approx.)
    self.bkg_renorm = -1                                              #switch to renormalize bkg to match source > 3 MeV
    self.subspec = np.ones(self.size) * -1                            #background subtracted spectrum, deadtime corrected
    self.subspec_err = np.ones(self.size) * -1                        #error in background subtracted spectrum
    self.drm_size = 256 if self.is_slow else 184                      #number of drm rows (electron side)
    self.e_bins = np.ones(self.size + 1, dtype="float") * -1          #energy channel boundaries (keV)
    self.ele_bins = np.ones(self.drm_size + 1, dtype="float")-1       #energy boundaries on electron side (ct side is fixed)
    self.drm = np.ones((self.size, self.drm_size), dtype="float")     #response matrix
    self.drm_type = -1                                                #1 =downward isotropic, 2 =mirroring, 3 =other
    self.drm2 = np.ones((self.size, self.drm_size), dtype="float")*-1 #second response matrix 
    self.drm2_type = -1                                               #1 =downward isotropic, 2 =mirroring, 3 =other
    self.method = -1                                                  #fitting method (1-6)
    self.model = -1                                                   #fitting model (1-2)  = exponential, monoenergetic
    self.fitrange = np.ones(2, dtype="float") * -1                    #fitting range of energies
    self.numparams = -1                                               #number of fit parameters
    self.params = np.ones(10, dtype="float") * -1                     #fit parameters
    self.param_ranges = np.ones([10,2], dtype="float") * -1             #1-sigma ranges on fit parameters
    self.chisq = -1                                                   #chi-square of fit (unreduced)
    self.chi_dof = -1                                                 #degrees of freedom for chi-square of fit
    self.modvals = np.ones(self.size, dtype="float") * -1             #values of model fit at center of each bin
    self.secondmodvals = np.ones(self.size, dtype="float") * -1       #values of 2nd component at center of each bin 
    self.ebins = self._make_standard_energies()
    self.elebins = self._make_standard_electron_energies()

  @staticmethod
  def edge_products(edges):

    if isinstance(edges, list):
      array_version = np.array(input_array)

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
    if dims[1] == 2:
        edges_2 = edges
        edges_1 = np.concatenate([edges_2[:,1],[edges_2[:,0][-1]]])
    else:
        edges_2 = np.array([edges[0:-1], edges[1]]).transpose()
        edges_1 = edges

    mean = edges_2.sum(1)/2
    gmean = np.sqrt((edges_2[:,0]*edges_2[:, 1]))
    width = np.abs(edges_2[:,1]-edges_2[:,0])

    return [width, mean, gmean]

  @staticmethod  
  def brl_rebin(oldBins, newBins, oldVals, flux):
    return


  def _make_standard_energies(self):
    d = SpecData.calib_sspc if self.is_slow else SpecData.calib_mspc
    return d[:,1]
  
  def _make_standard_electron_energies(self):
    #get sspc standard energies
    e0 = self._make_standard_energies()
    
    if self.is_slow:
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

  def _get_altitude(self):
    return
  
  def _get_maglat(self):
    return

  def _barrel_sp_drm_interp(self, ein, loginterpolate=False, pitch='iso', show=False, verbose=False)
    return

  def _barrel_sp_drm_row(self, ein, ctbins, pitch="iso"):
    if pitch != 'iso' and pitch != 'mir':
      raise ValueError('Illegal distribution name.  Use iso or mir.')
    
    if self.altitude < 25:
      print("BARREL_SP_RESPONSE_INTERP Warning:\n\taltitude < 25 km, being set to 25 km.")
      self.altitude = 25

    if self.altitude > 40:
      print("BARREL_SP_RESPONSE_INTERP Warning:\n\taltitude > 40 km, being set to 40 km.")
      self.altitude = 40
  
    al = np.array([25, 30, 35, 40])

    if ein < 50 or ein > 4000:
      return np.zeros(ctbins.size-1)

    for i in np.arange(2):
      if (self.altitude == al[i]) or (self.altitude == 40):
        sp = self._barrel_sp_drm_interp(ein, True, pitch)
        if (sp.size == 1): print("Energy out of range.")
      else:
        if (self.altitude > al[i]) and (self.altitude < al[i+1]):
          sp1 = self._barrel_sp_drm_interp(al[i], ein, True, pitch)
          sp2 = self._barrel_sp_drm_interp(al[i+1], ein, True, pitch)
          n1 = sp1.size
          n2 = sp2.size
          if (sp1.size == 1): print("Energy out of range.")
          
          de = sp2[0,*]-sp1[0,*]
          ga = (self.altitude - al[i])/5.
          sp = np.zeros([sp2[:, 1].size, 2])
          sp[:, 0] = sp2[:, 0]
          sp[:, 1] = sp1[:, 1] + ga*(sp2[:, 1] - sp1[:, 1])

#MOVE TO NOTEBOOK
#          if keyword_set(show):
#            plot,sp1[:, 0],sp1[:, 1],/xlog,/ylog,xrange=[10,10000],$
#              yrange=[0.01,10000],psym=5,symsize=0.5,$
#              xtitle='X-Ray Energy (KeV)',ytitle='Xray Flux Cts/Kev',$
#              title='Altitude: '+strtrim(self.altitude,2)+' km; Energy: '+strtrim(ein,2)+' keV'
#            oplot,sp2[0,*],sp2[1,*],psym=4,symsize=0.4		
#            oplot,sp[0,*],sp[1,*]

    #rebin to desired energy bins:
    s1 = sp[:, 1]
    e1 = np.concatenate((sp[:, 0] - 0.5, [sp[-1, 0] + 1.0]))
    e2 = ctbins

    row = self._brl_rebin(s1, e1, e2, flux=1)
       
    return row
    

  def _make_drm(self, angledist=1, whichone=1):
    if angledist == 1:
      pitch = 'iso'
    elif angledist == 2:
      pitch = 'mir'
    else:
      raise ValueError('Invalid value for angular distribution index.')

    if whichone != 1 and whichone != 2:
      raise ValueError('Bad response matrix ID number.')
    
    #Set up the response matrix
    ctbins = self.ebins
    elebins = self.elebins
    nct = ctbins.size
    nel = elebins.size
    #[ctwidth, ctmean, gmean] = SpecData.edge_products(ctbins)
    [elwidth, elmean, gmean] = SpecData.edge_products(elebins)
    
    drm = np.ones([nct-1, nel-1], dtype="float")

    #Build the DRM row by row:
    for i in np.arrange(nel-2):
      row = self._barrel_sp_drm_row(elmean[i], ctbins, pitch)
      drm[:, i] = row

    #Normalization factor derived from GEANT simulations:
    #100000000. input e- / (!pi*120.cm^2) = 2210.49 electrons/cm2.
    drm = drm/2210.49

    if whichone == 1:
       self.drm = drm 
       self.drmtype = angledist
    else:
       self.drm2 = drm
       self.drm2type = angledist
