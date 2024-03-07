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

  iso_27e_sspc_rawfit_params = {
    "25": [
      [50.0,           9.6, 1.19627, 2.01344,   5.26398, 25.02105,   52.77311, 0.02041],
      [75.0,     5964810.3, 0.94980, 3.93801,  85.74702, 13.66994,   90.88372, 0.02234],
      [100.0,   13701063.0, 1.06943, 4.36319,  65.18541, 16.59563,  114.03538, 0.12805],
      [125.0,        272.3, 0.72577, 0.30405,  22.20698, 20.36472,  219.19906, 0.06651],
      [150.0,  158589997.5, 1.07588, 4.57093,  85.36255, 14.31150,  158.24714, 0.07434],
      [175.0,  187829057.2, 1.09428, 4.55053,  83.97471, 14.53719,  197.36357, 0.06487],
      [200.0,  336739516.9, 1.19624, 4.65956,  90.05244, 13.74541,  194.62026, 0.13355],
      [250.0,  310976159.3, 1.00766, 4.25710, 105.45130, 11.41199,  307.24682, 0.12779],
      [300.0,   43361113.0, 1.01561, 3.80258,  79.21006, 14.04741,  363.22880, 0.07771],
      [350.0,  222931699.9, 1.13113, 4.15593,  99.21305, 12.28634,  374.43521, 0.09721],
      [400.0,  158872884.4, 1.09244, 3.97721,  97.74169, 12.23576,  441.55959, 0.07426],
      [500.0,   32629211.4, 1.01739, 3.47222,  79.49699, 13.64547,  574.93160, 0.09288],
      [600.0,   31787631.7, 0.94600, 3.24038,  79.01364, 13.21799,  773.07188, 0.12051],
      [700.0,   20279643.6, 0.95255, 3.10219,  72.08445, 13.95032,  844.05160, 0.13282],
      [800.0,   31493197.8, 0.93737, 3.08663,  76.58056, 13.34792, 1017.67514, 0.13056],
      [900.0,   21688368.0, 0.93249, 2.95150,  71.24267, 13.89465, 1075.93078, 0.16097],
      [1000.0,  23146154.8, 0.95075, 2.95739,  74.40731, 13.43294, 1112.49319, 0.19243],
      [1200.0,  14568582.1, 1.00433, 2.88082,  73.01736, 13.48146, 1546.25557, 0.20575],
      [1400.0,   9381598.7, 1.07725, 2.80763,  73.07428, 13.20622, 1557.32978, 0.19764],
      [1600.0,   7515917.0, 1.06711, 2.70137,  68.82487, 13.74428, 1820.42961, 0.23427],
      [1800.0,   6652556.8, 1.05192, 2.61592,  65.93493, 14.10803, 2094.96887, 0.29504],
      [2000.0,   6066816.2, 1.07353, 2.57476,  66.74995, 13.73543, 2132.13375, 0.31715],
      [2400.0,   6683006.6, 1.08149, 2.53196,  67.16715, 13.57768, 2659.52144, 0.35521],
      [2800.0,   5602825.9, 1.10010, 2.45661,  64.59587, 13.84117, 2962.77203, 0.47852],
      [3200.0,   5737121.1, 1.09529, 2.41149,  63.32187, 14.05024, 3477.13510, 0.68396],
      [3600.0,   5359256.1, 1.12872, 2.37782,  63.26882, 13.80593, 3627.98215, 0.67940],
      [4000.0,   4924891.7, 1.13705, 2.33150,  61.34594, 14.01181, 3909.05322, 0.82047]
    ],
    "30": [
      [  50.0,    1277581.1, 1.21909, 4.37243,  20.39951, 20.96531,   54.46637, 0.00711],
      [  75.0,   15451544.2, 1.17681, 4.38997,  45.85026, 17.43455,   80.97483, 0.01616],
      [ 100.0,   56432245.9, 1.18335, 4.46946,  52.98749, 16.85352,  106.07036, 0.05263],
      [ 125.0,  136606310.7, 1.06140, 4.29389,  76.32098, 13.49168,  142.89529, 0.06039],
      [ 150.0,  681359390.6, 1.08675, 4.53887,  90.90258, 12.46004,  171.38854, 0.05757],
      [ 175.0,  731482470.8, 1.01521, 4.34022, 100.16084, 11.11724,  220.46944, 0.04861],
      [ 200.0,  267883176.4, 0.98798, 4.01112,  91.85711, 11.83792,  259.77975, 0.05823],
      [ 250.0, 3698636905.2, 1.15023, 4.58690, 127.70796,  8.99089,  269.30204, 0.05472],
      [ 300.0,  240202637.4, 1.07106, 3.89891,  95.32575, 11.40375,  340.44720, 0.08250],
      [ 350.0, 1132141382.3, 1.16160, 4.18765, 118.98355,  9.33951,  368.03568, 0.04457],
      [ 400.0,  369399941.7, 1.05523, 3.81179, 106.92193,  9.95863,  453.43287, 0.07836],
      [ 500.0,  118542676.9, 0.96277, 3.34723,  92.86951, 10.85138,  639.80572, 0.09278],
      [ 600.0,   85061073.4, 0.93824, 3.14905,  87.37404, 11.25567,  778.73556, 0.07773],
      [ 700.0,   67423626.6, 0.93581, 3.03340,  84.30226, 11.49649,  883.62463, 0.08897],
      [ 800.0,   68448451.4, 0.90314, 2.88684,  81.89913, 11.46651, 1057.27771, 0.16780],
      [ 900.0,   77675139.7, 0.89090, 2.82152,  81.02242, 11.47651, 1232.94313, 0.14134],
      [1000.0,   80418941.1, 0.87419, 2.71655,  79.47148, 11.55893, 1372.08562, 0.18941],
      [1200.0,   76621633.7, 1.01290, 2.97935,  95.76575,  9.76724, 1572.54730, 0.17628],
      [1400.0,   39350613.7, 1.05977, 2.84828,  90.01724, 10.33445, 1643.76802, 0.16514],
      [1600.0,   33158817.1, 1.08629, 2.78415,  90.58491, 10.08491, 1755.03828, 0.20910],
      [1800.0,   28073883.2, 1.07509, 2.70390,  87.30595, 10.30595, 2029.13701, 0.23170],
      [2000.0,   23825322.1, 1.06947, 2.63070,  85.05837, 10.48991, 2222.51933, 0.26193],
      [2400.0,   22959065.1, 1.06842, 2.56284,  83.07360, 10.59550, 2618.30009, 0.29036],
      [2800.0,   20579978.0, 1.08049, 2.50196,  81.84792, 10.59995, 3030.28297, 0.45703],
      [3200.0,   19301024.1, 1.09887, 2.46173,  81.10258, 10.53068, 3335.96995, 0.49694],
      [3600.0,   19742910.9, 1.12117, 2.44189,  82.00825, 10.35223, 3596.50195, 0.58635],
      [4000.0,   15855483.9, 1.12924, 2.37789,  76.16968, 11.32452, 3909.05323, 0.62102]
    ],
    "35": [
      [  50.0,    5388821.1, 1.22906, 4.59354,  10.28783, 22.62551,   56.03489, 0.04952],
      [  75.0,   33503987.6, 1.18145, 4.36479,  42.31609, 16.00507,   81.68281, 0.04163],
      [ 100.0,   46198302.9, 1.08295, 4.00342,  62.09768, 13.47482,  113.56727, 0.09252],
      [ 125.0,  215435823.2, 1.10819, 4.21562,  80.81029, 11.32805,  140.40504, 0.03974],
      [ 150.0,  145551289.5, 1.03376, 3.91985,  85.47338, 10.26847,  184.19733, 0.03621],
      [ 175.0, 3032636759.3, 1.13318, 4.55377, 123.07171,  7.33420,  195.62714, 0.08259],
      [ 200.0, 4363347168.5, 1.17409, 4.57737, 132.52747,  6.33024,  214.75192, 0.04088],
      [ 250.0, 1201104988.1, 1.09565, 4.13510, 123.95592,  6.45862,  286.46614, 0.03599],
      [ 300.0, 7397788462.0, 1.14976, 4.41105, 161.76182,  3.43764,  327.46830, 0.06588],
      [ 350.0,  770941462.8, 1.06330, 3.84415, 126.83254,  5.81910,  403.64986, 0.07622],
      [ 400.0, 7759640918.4, 1.18180, 4.29140, 172.99587,  2.20552,  417.15087, 0.09048],
      [ 500.0,  158988301.1, 0.90258, 3.08683, 101.47264,  7.11027,  759.69839, 0.11113],
      [ 600.0,  192452555.5, 0.94776, 3.16263, 110.66271,  6.21972,  764.95960, 0.11336],
      [ 700.0,  107658010.8, 0.88657, 2.81813,  94.88011,  7.55008,  985.45985, 0.11755],
      [ 800.0,   99773209.5, 0.86953, 2.68827,  89.50207,  7.97277, 1173.62735, 0.13935],
      [ 900.0,  111792600.0, 0.89222, 2.74778,  95.95298,  7.15913, 1187.86917, 0.14980],
      [1000.0,  136628076.3, 0.84945, 2.56029,  89.90076,  7.68416, 1483.94757, 0.14319],
      [1200.0,  161474491.7, 0.98107, 2.92867, 116.88612,  4.69901, 1598.09654, 0.26509],
      [1400.0,  124200216.7, 1.09679, 2.95225, 124.42157,  3.78170, 1536.64182, 0.23233],
      [1600.0,   79191439.4, 1.02855, 2.76084, 111.38838,  5.08570, 1926.73422, 0.20393],
      [1800.0,   57659305.3, 1.05041, 2.69036, 107.71257,  5.22194, 2050.00881, 0.28718],
      [2000.0,   51406798.1, 1.03702, 2.62435, 102.67275,  5.89206, 2355.96084, 0.20616],
      [2400.0,   46796348.0, 1.04337, 2.55548, 101.45272,  5.90112, 2757.70257, 0.32878],
      [2800.0,   43605799.5, 1.06566, 2.51590, 102.50482,  5.43261, 2988.21276, 0.46909],
      [3200.0,   43137111.1, 1.06001, 2.46903, 101.53746,  5.34269, 3540.46331, 0.53276],
      [3600.0,   45685279.4, 1.07699, 2.45745, 103.29617,  5.09386, 3909.51024, 0.51137],
      [4000.0,   39131666.7, 1.08723, 2.40858, 100.73738,  5.11250, 4265.79714, 0.81004]
    ],
    "40": [
      [  50.0,   351479051.3, 0.66850, 3.52740,    4.10729,   25.02931,  131.90307, 0.37051],
      [  75.0,   228574377.2, 0.65604, 0.53941, 1807.39536, -109.68386,  132.51714, 0.35266],
      [ 100.0,   902442210.3, 1.26250, 4.71488,   82.83185,    9.22610,  104.58960, 0.25215],
      [ 125.0,   388855672.6, 1.21185, 4.24318,  112.94431,    3.78511,  129.75792, 0.29548],
      [ 150.0,      994599.7, 0.88335, 2.40884,   46.51666,   11.36345,  236.20547, 0.18159],
      [ 175.0,      592995.9, 0.76360, 1.61365,   29.74022,   14.52663,  371.88390, 0.34390],
      [ 200.0,  1520338119.8, 1.09408, 4.15449,  138.48859,    2.68182,  226.78380, 0.18928],
      [ 250.0, 12571173442.1, 1.17321, 4.50170,  184.22059,   -1.31702,  266.77818, 0.25348],
      [ 300.0,  1951563097.8, 1.05546, 3.94329,  161.51856,   -0.42173,  340.84048, 0.25055],
      [ 350.0,  2238183727.1, 1.01067, 3.83901,  169.11152,   -1.40959,  440.21271, 0.36217],
      [ 400.0, 33178242123.6, 1.10808, 4.36109,  236.64589,   -6.12546,  421.70800, 0.38976],
      [ 500.0,   105371159.1, 0.86499, 2.77141,  101.04297,    3.84578,  806.42591, 0.35529],
      [ 600.0,    25269203.2, 0.84148, 2.31704,   76.83662,    6.46249,  862.08818, 0.84063],
      [ 700.0,   109164894.7, 0.94847, 2.89228,  118.60324,    1.39785,  759.29592, 0.98851],
      [ 800.0,   368578770.2, 0.91019, 2.96026,  138.43238,   -0.57056,  995.56939, 0.78943],
      [ 900.0,  3881957724.6, 0.72052, 1.84416,   68.90256,    6.84792, 2728.82412, 1.10985],
      [1000.0,   251297894.9, 0.98541, 3.00059,  129.72795,    1.51198,  988.36322, 1.09488],
      [1200.0,  1793618922.5, 0.81878, 2.64940,  120.00227,    1.04824, 3372.18498, 1.39674],
      [1400.0,   759704816.8, 0.85373, 2.64277,  137.76429,   -2.97260, 3018.36332, 2.11468],
      [1600.0,   138430296.1, 0.87909, 2.43467,  101.79117,    2.47132, 2932.23603, 1.98467],
      [1800.0,    60717278.1, 0.98920, 2.55615,  107.80762,    2.36814, 2131.92979, 2.10287],
      [2000.0,   139251560.4, 1.06317, 2.74156,  143.37325,   -2.61422, 2194.87527, 1.68799],
      [2400.0,   146958239.9, 1.08712, 2.71083,  150.45635,   -3.94462, 2370.96000, 2.26125],
      [2800.0,   101741233.5, 0.99009, 2.50643,  122.05659,   -0.75440, 3535.59004, 3.32061],
      [3200.0,    84142522.5, 1.02520, 2.48090,  124.07938,   -1.30007, 3813.26164, 3.01929],
      [3600.0,    88118964.3, 1.07886, 2.50576,  133.70307,   -2.87750, 3736.86667, 2.93089],
      [4000.0,    97442944.9, 1.04794, 2.46852,  131.12059,   -2.59383, 4602.83700, 3.50190]
    ]
  }
  
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
    self.src_spec_err = np.ones(self.size, dtype="float") * -1         #error in summed source spectrum
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
  def brl_rebin(oldVals, oldBins, newBins, flux=False):
    n = oldBins.size
    m = newBins.size
    
    if (n < 2 or m < 2):
      print("length(s) violation: {}, {}".format(n, m))
      result = np.zeros((m-1), dtype=float)
      oldLo = oldBins[0]
      oldHi = oldBins[1]
      newLo = newBins[0]
      newHi = newBins[1]
      newIndex = 0
      oldIndex = 0
      total = 0.

    while (1):
    #DEBUG****print,oldIndex,oldLo,oldHi,newIndex,newLo,newHi,total
      if (oldHi < newLo):
        oldIndex += 1
        if (oldIndex > n-1):
          return result
        oldLo = oldHi
        oldHi = oldBins[oldIndex+1]
        continue
    
      if (newHi < oldLo):
        result[newIndex] = (total/(newHi-newLo)) if flux else (total/(oldHi-oldLo))
        total = 0.
        newIndex += 1
        if (newIndex > m-1):
          return result
        newLo = newHi
        newHi = newBins[newIndex+1]
        continue
    
      if (newHi < oldHi):
        total += (newHi-(oldLo>newLo))*oldVals[oldIndex]
        result[newIndex] = (total/(newHi-newLo)) if flux else (total/(oldHi-oldLo))
        total = 0.
        newIndex += 1
        if (newIndex > m-1):
          return result
        newLo = newHi
        newHi = newBins[newIndex+1]
        continue
    
      total += (oldHi-(oldLo>newLo))*oldVals[oldIndex]
      oldIndex += 1
      if (oldIndex > n-1):
        result[newIndex] = (total/(newHi-newLo)) if flux else (total/(oldHi-oldLo))
        return result
      oldLo=oldHi
      oldHi=oldBins[oldIndex+1]

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

  def _barrel_sp_drm_interp(self, altitude, ein, loginterpolate=False, pitch='iso', show=False, verbose=False):
    #loginterpolate = 1 : logarithmic interpolation

    if (pitch != "iso" and pitch != "mir"):
      print("Illegal distribution name.  Use iso or mir.")

    if (altitude < 25.):
      print("BARREL_SP_RESPONSE_INTERP Warning: altitude < 25 km, being set to 25 km.")
      altitude = 25.
    
    if (altitude > 40.):
      print,"BARREL_SP_RESPONSE_INTERP Warning: altitude > 40 km, being set to 40 km."
      altitude = 40.

    #For Notebook
    #if (show):
    #  loadct,13
    
    #27 electron energy input curve fitting parms a[0-5]
    if (altitude < 27.5):
      fitparams = SpecData.iso_27e_sspc_rawfit_params["25"]
    elif (altitude < 32.5):
      fitparams = SpecData.iso_27e_sspc_rawfit_params["30"]
    elif (altitude < 37.5):
      fitparams = SpecData.iso_27e_sspc_rawfit_params["35"]
    else:
      fitparams = SpecData.iso_27e_sspc_rawfit_params["40"]

    es = fitparams[:,0]
    if (ein < es[0]) or (ein > 4000.):
      print("Electron energy out of range: {}. Use {}".format(ein, es[0]))
      return 0
    
    #to find the nearest energy and for later interpolation
    for i, es_i in enumerate(es):
      if ((ein == es_i) or (ein == 4000)):
        i1=i
        i2=i
        g1=0.
      elif ((ein > es[i]) and (ein < es[i+1])):
        i1=i
        i2=i+1
        g1= float((ein-es[i])/(es[i+1]-es[i]))

    # here shift/stretch the energy scale so that 
    # ebins range	[24,ein]
    # e1 range 	[24,es[i1]]
    # e2 range	[24,es[i2]]
    # [0,23] is out of fitting range.

    ebins = np.array(range(ein), dtype=float)*(ein-24.)/ein+24.
    e1 = np.array(range(ein), dtype=float)*((es[i1]-24.)/ein)+24.
    e2 = np.array(range(ein), dtype=float)*((es[i2]-24.)/ein)+24.

    curve = np.zeros(ein)
    if (g1 == 0.):
      a = fitparams[i1, 1:7]
      f1 = self._barrel_sp_brem(ebins, a)

      #Fix some blowing up at low energies temporarily:
      f1 = self._barrel_sp_patch_drmrow(f1)

      curve = f1
      #For Notebook
      #if keyword_set(show):
      #  plot,ebins,f1,/xlog,/ylog,color=150,xrange=[10,5000],$
      #    yrange=[0.0001,10000],$
      #    xtitle='X-Ray Energy (KeV)',ytitle='Xray Flux Cts/Kev'
      #else:
      a = fitparams[i1, 1:7]
      f1 = self._barrel_sp_brem(e1,a)
      a = fitparams[i2, 1:7]
      f2 = self._barrel_sp_brem(e2,a)

      #Fix some blowing up at low energies temporarily:
      f1 = self._barrel_sp_patch_drmrow(f1)
      f2 = self._barrel_sp_patch_drmrow(f2)

      if (loginterpolate):
        curve = np.exp(
          (np.log(f1)*(es[i2]-ein) + np.log(f2)*(ein-es[i1]))/
          (es[i2]-es[i1])
        )
      else:
        curve = (f1*(es[i2]-ein) + f2*(ein-es[i1])) / (es[i2]-es[i1])
      
      #For Notebook
      #if keyword_set(show) then begin
      #  plot,e1,f1,/xlog,/ylog,color=150,xrange=[10,10000],$
      #      yrange=[0.0001,10000],linestyle=3, $
      #      xtitle='X-Ray Energy (KeV)',$
      #      ytitle='Xray Flux Cts/Kev'
      #  oplot,e2,f2,color=80,linestyle=2
      #  oplot,ebins,curve
    
    a = np.zeros([ein, 2], dtype=float)
    a[:, 0] = ebins
    a[:, 1] = curve

    return a

  def _barrel_sp_brem(x, a):
    e0 = a[5] #frozen
    f = a[0] * np.exp(-(e0/(e0^a[1]-x^a[1])))/x^a[2]*np.exp(-a[3]/(x-a[4]))
    return f

  def _barrel_sp_patch_drmrow(f):
    #Look for the signature of an upward spike and zero out above that:
    n = f.size
    shift = np.roll(f,1)
    a = f[1:n]
    b = shift[1:n]
    w = np.where(a > b*1000.)[0]
    if w.size > 0:
      f[w[0]:n] = 0
    return f

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
        sp = self._barrel_sp_drm_interp(self.altitude, ein, True, pitch)
        if (sp.size == 1): print("Energy out of range.")
      else:
        if (self.altitude > al[i]) and (self.altitude < al[i+1]):
          sp1 = self._barrel_sp_drm_interp(al[i], ein, True, pitch)
          sp2 = self._barrel_sp_drm_interp(al[i+1], ein, True, pitch)
          n1 = sp1.size
          n2 = sp2.size
          if (sp1.size == 1): print("Energy out of range.")
          
          de = sp2[:, 0]-sp1[:, 0]
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

    row = SpecData.brl_rebin(s1, e1, e2, flux=1)
       
    return row
  
  def _barrel_sp_make_drm(self, angledist=1, whichone=1):
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

  #NAME: barrel_sp_fold.pro
  #DESCRIPTION: BARREL top-level spectral folding routine
  #
  #REQUIRED INPUTS:
  #ss        spectrum structure
  # 
  #OPTIONAL INPUTS:
  #method    1 = single-parameter spectrum, single drm, use "model"
  #          2 = single fixed (file input) spectrum, single drm
  #          3 = double fixed (file input) spectrum, single drm
  #          4 = single-parameter spectrum, dual drm, use "model"
  #          5 = single fixed (file input)) spectrum, dual drm
  #          6 = double fixed (file input)) spectrum, dual drm
  #model     spectral model of electron spectrum (default is exponential)
  #          1 = exponential
  #          2 = monoenergetic
  #fitrange  energy range to use for fitting (regardless of full range
  #          of ebins) (this is a vector [start,end]
  #maxcycles Maximum number of times to try rescaling range for fit parameters
  #quiet     Don't make graphs + screen output
  #verbose   show some debugging info as fits go along
  #modlfile        Filename for inputting a handmade model component
  #secondmodlfile  Filename for inputting a second handmade model component
  #bkg_renorm      match background to source > 3 MeV before subtracting
  #
  #OUTPUTS (written into ss structure):
  #params            best fit parameters
  #param_ranges      ranges on best fit parameters (1 sigma) (2x2 array)
  #chisquare         chi-square (not reduced)
  #dof               degrees of freedom associated with chisquare
  #modvals           values of the fit function at the centers of the energy bins
  #
  #CALLS:
  #edge_products(), (imported from solarsoft), barrel_sp_fold_m1
  #through barrel_sp_fold_m6
  #
  #NOTES: 
  #
  #STATUS: Tested for methods 1&4 on artificial data.
  #
  #TO BE ADDED:
  #     Support for other spectral models
  #     Support for single + summed fixed spectra (from file), varying normalization
  #
  #REVISION HISTORY:
  #Version 1.0 DMS 7/18/12 -- split out from barrel_folding as the new top layer
  #                7/24/12 -- fixed minimum of plot to account for
  #                           possible values << 1 (fixed threshold for minimum
  #                           of plot changed to 1.d-6 instead of 0.5
  #                           when there are real values that are too low)
  #          2.3   8/19/12 -- added support for method 3
  #          2.5   1/5/13 --  rewrite to support new general
  #                           spectroscopy structure ss
  #          2.6   5/29/13 -- adding support for L2 MSPC files (already cts/keV)
  #          2.8   7/8/13  -- remove call to idl_screen_graphics()
  #          3.0   9/9/13  -- set ss.numparams here instead of upstream at barrel_sp_make()
  #          3.2   10/29/13 - Print total, background, and net count
  #                           rates just before proceeding to fit
  #                11/12/13 - plot data before fitting in case fit crashes
  #                11/12/13 - bkg_renorm defaults to zero, not 1.
  def _barrel_sp_fold(self, maxcycles=30, bkg_renorm=False,
      method=1, model=1, fitrange=[110, 2500],
      modlfile = None, secondmodlfile=None, residuals=1):
    
    self.method = method
    self.model = model
    self.fitrange = fitrange
    self.bkg_renorm = bkg_renorm
    self.modlfile = modlfile
    self.secondmodlfile = secondmodlfile

    #CHECK CONSISTENCY OF INPUT PARAMETERS
    if (self.method > 4) and (self.drm2type == -1):
      print('BARREL_SP_FOLD: Method > 3 requires a second response matrix (drm2).')
    if (self.method != 1 and self.method != 4 and self.modlfile == ""):
      print('BARREL_SP_FOLD: This method requires a filename for an input model (modlfile)')
    if (self.method == 3 or self.method == 6 and (self.modlfile == "" or self.secondmodlfile == "")):
      print('BARREL_SP_FOLD: This method requires two filenames for input models (modlfile, secondmodlfile)')

    #Create energy bin centers and widths, find bins to use in fit:
    [ctwidth, ctmean, ctgmean] = SpecData.edge_products(self.ebins)
    [elwidth, elmean, elgmean] = SpecData.edge_products(self.elebins)

    usebins = np.where(ctmean > self.fitrange[0] and ctmean < self.fitrange[1])

    #Subtract background & calculate error bars on subtracted spectrum -- cts/keV:
    src_spec = self.src_spec/self.src_live 
    bkg_spec = self.bkg_spec/self.bkg_live 
    src_spec_err = self.src_spec_err/self.src_live
    bkg_spec_err = self.bkg_spec_err/self.bkg_live
    renorm = 1.
    if (self.bkg_renorm): 
      #normalize bkg so that it matches src at high energies.
      #med.spectra will only go up to 4 MeV, so we are keeping a
      #band at least 750 keV up to that, even though the hardest
      #drep might put a few counts into the bottom of this range.

      w = np.where(ctmean > 3250. and ctmean < 6750.)
      renorm = src_spec[w].sum() / bkg_spec[w].sum()
      print("Background renormalization factor: {}".format(renorm))
      
    bkg_spec = self.bkg_spec * renorm
    subspec = self.src_spec - bkgspec
    subspec_err = sqrt( srcspecerr^2. + (bkgspecerr*renorm)^2 )
    print("Total count rate:      {} c/s".format((srcspec*ctwidth).sum()))
    print("Background count rate: {} c/s".format((bkgspec*ctwidth).sum()))
    print("Net count rate:        {} c/s".format((subspec*ctwidth).sum()))
### Pick up on line 120 of barrel_sp_fold.pro
    return
    