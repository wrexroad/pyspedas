import numpy as np
import json

with open('./dbase.json', 'r') as f:
  dbase = json.load(f)
  for key,value in dbase.items():
    dbase[key] = np.array(value)

class SpecData:   
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

  @staticmethod
  def barrel_sp_brem(x, a):
    e0 = a[5] #frozen
    ff = a[0] * np.exp(-(e0/(e0**a[1]-np.power(x,a[1]))))/np.power(x,a[2])*np.exp(-a[3]/(x-a[4]))
    return f
  
  @staticmethod
  def barrel_sp_patch_drmrow(f):
    #Look for the signature of an upward spike and zero out above that:
    n = f.size
    shift = np.roll(f,1)
    a = f[1:]
    b = shift[1:]
    w = np.where(a > b*1000.)[0]
    if w.size > 0:
      f[w[0]:] = 0
    return f

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
      elif ((ein > es_i) and (ein < es[i+1])):
        i1=i
        i2=i+1
        g1= float((ein-es_i)/(es[i+1]-es_i))

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
      f1 = SpecData.barrel_sp_brem(ebins, a)

      #Fix some blowing up at low energies temporarily:
      f1 = SpecData.barrel_sp_patch_drmrow(f1)

      curve = f1
      #For Notebook
      #if keyword_set(show):
      #  plot,ebins,f1,/xlog,/ylog,color=150,xrange=[10,5000],$
      #    yrange=[0.0001,10000],$
      #    xtitle='X-Ray Energy (KeV)',ytitle='Xray Flux Cts/Kev'
      #else:
      a = fitparams[i1, 1:7]
      f1 = SpecData.barrel_sp_brem(e1,a)
      a = fitparams[i2, 1:7]
      f2 = SpecData.barrel_sp_brem(e2,a)

      #Fix some blowing up at low energies temporarily:
      f1 = SpecData.barrel_sp_patch_drmrow(f1)
      f2 = SpecData.barrel_sp_patch_drmrow(f2)

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
    subspec = self.src_spec - self.bkg_spec
    subspec_err = np.sqrt(np.power(self.src_spec_err, 2) + np.power((self.bkg_spec_err * renorm), 2) )
    print("Total count rate:      {} c/s".format((self.src_spec*ctwidth).sum()))
    print("Background count rate: {} c/s".format((self.bkg_spec*ctwidth).sum()))
    print("Net count rate:        {} c/s".format((subspec*ctwidth).sum()))
    
    #plot the data points: MOVE TO NOTEBOOK
    #window,xsize=500,ysize=800
    #loadct2,13
    #!p.multi=[0,1,3]
    #plot,ctmean,srcspec,/xlog,/ylog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],$
    #     yrange=[max([1.d-2,min(srcspec)/1.5]),max(srcspec)*1.5],$
    #     xtitle='Energy, keV',ytitle='counts/keV/s',psym=3,$
    #     position=[0.12,0.65,0.97,0.98],charsize=2
    #oplot,ctmean,bkgspec,col=2
    #if renorm NE 1. then oplot,ctmean,bkgspec/renorm,col=4
    #for i=0, n_elements(subspec)-1 do begin
    #     oplot,[ctmean[i],ctmean[i]],$
    #           [srcspec[i]-srcspecerr[i],srcspec[i]+srcspecerr[i]], psym=0
    #     oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #           [srcspec[i],srcspec[i]], psym=0
    #endfor
    
    
    #Do the actual fitting according to the chosen method:
    if method == 1:
      self._barrel_sp_fold_m1(
        elmean, elwidth, ctwidth, ctmean, usebins, maxcycles,
        params, param_ranges, modvals, chisquare, dof
      )
    elif method == 2:
      self._barrel_sp_fold_m2(
        subspec, subspecerr, modlfile, ss.drm, ss.elebins, elmean, elwidth, ctwidth, usebins, maxcycles,
        params, param_ranges, modvals, chisquare, dof
      )
    elif method == 3:
      self._barrel_sp_fold_m3(
        subspec, subspecerr, modlfile, secondmodlfile, ss.drm, ss.elebins, elmean, elwidth, ctwidth, usebins, maxcycles,
        params, param_ranges, modvals, secondmodvals, chisquare, dof
      )
    elif method == 4:
      self._barrel_sp_fold_m4(
        subspec, subspecerr, model, ss.drm, ss.drm2, elmean, elwidth, ctwidth, usebins, maxcycles,
        params, param_ranges, modvals, chisquare, dof
      )


    #THESE SHOULD ALREADY BE SET 
    #Fill in the fit results in the structure:
    #numparams=params.size
    #self.numparams=numparams
    #ss.params[0:numparams-1] = params
    #ss.param_ranges[0:numparams-1,*] = param_ranges
    #ss.modvals = modvals
    #if (method eq 3 or method eq 6) then ss.secondmodvals=secondmodvals
    #ss.chisq = chisquare
    #ss.chi_dof = dof
    #ss.subspec = subspec
    #ss.subspecerr = subspecerr

    #THIS SHOULD GO TO A NOTEBOOK
    #;Show results and make a plot if requested:
    #if not keyword_set(quiet) then begin
    #    print,'Best normalization and range:          ',params[0],$
    #      '  (',param_ranges[0,0],param_ranges[1,0],')  '
    #    if (method EQ 3 or method EQ 6) then $
    #    print,'Best second normalization and range:          ',params[1],$
    #      '  (',param_ranges[0,1],param_ranges[1,1],')  '
    #    if (method EQ 1 or method EQ 4) then $
    #    print,'Best spectral parameter and range:     ',params[1],$
    #      '  (',param_ranges[0,1],param_ranges[1,1],')  '
    #    if (method EQ 5) then $
    #      print,'Best drm interpolation and range:          ',params[1],$
    #      '  (',param_ranges[0,1],param_ranges[1,1],')  '
    #    if (method EQ 4 or method EQ 6) then $
    #      print,'Best drm interpolation and range:          ',params[2],$
    #      '  (',param_ranges[0,2],param_ranges[1,2],')  '
    #  
    #    print,'Chi-square, DOF, reduced, probability: ',chisquare,dof,chisquare/dof,1.-chisqr_pdf(chisquare,dof)
#
    #    plot,ctmean,subspec,/xlog,/ylog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],$
    #        yrange=[max([1.d-6,min(subspec)/1.5]),max(subspec)*1.5],$
    #        xtitle='Energy, keV',ytitle='counts/keV/s',psym=3,$
    #        position=[0.12,0.3,0.97,0.6],charsize=2    
    #    ;;overplot the model:
    #    if method EQ 3 or method EQ 6 then begin
    #          oplot,ctmean,modvals,color=4,psym=0
    #          oplot,ctmean,secondmodvals,color=3,psym=0
    #          oplot,ctmean,modvals+secondmodvals,color=2,psym=0
    #    endif else   oplot,ctmean,modvals,color=3,psym=0
#
    #    ;;What you will really see is the error bars.
    #    ;;Plot data points that were not used in a different color:
    #    for i=0, n_elements(subspec)-1 do begin
    #      if ctmean[i] GE fitrange[0] and ctmean[i] LE fitrange[1] then col=0 else col=6
    #        oplot,[ctmean[i],ctmean[i]],$
    #              [subspec[i]-subspecerr[i],subspec[i]+subspecerr[i]], psym=0, color=col
    #        oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #              [subspec[i],subspec[i]], psym=0, color=col
    #    endfor
#
    #    ;sum model components if necessary:
    #    if method EQ 3 or method EQ 6 then modv=modvals+secondmodvals else modv=modvals
#
    #    ;Show the residuals in difference format:
#
    #    case residuals of
    #    2: begin  ;Plot ratio with full scale visible
    #      plot,ctmean,subspec/modv,psym=3,/xlog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],$
    #          xtitle='Energy, keV',ytitle='data/model',position=[0.12,0.05,0.97,0.20],charsize=2
#
    #      for i=0, n_elements(subspec)-1 do begin
    #          if ctmean[i] GE fitrange[0] and ctmean[i] LE fitrange[1] then col=0 else col=6
    #            oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #              [subspec[i]/modv[i],subspec[i]/modv[i]], psym=0, color=col
    #      endfor
    #    end
#
    #    3: begin  ;Plot differences on linear scale (usually favors low-energy points)
    #      plot,ctmean,subspec-modv,psym=3,/xlog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],$
    #          xtitle='Energy, keV',ytitle='data-model',position=[0.12,0.05,0.97,0.23],charsize=2    
#
    #      for i=0, n_elements(subspec)-1 do begin
    #          if ctmean[i] GE fitrange[0] and ctmean[i] LE fitrange[1] then col=0 else col=6
    #            mindraw=max( [min(subspec-modv),subspec[i]-modv[i]-subspecerr[i]] )
    #            maxdraw=min( [max(subspec-modv),subspec[i]-modv[i]+subspecerr[i]] )
    #            oplot,[ctmean[i],ctmean[i]],[mindraw,maxdraw], psym=0, color=col
    #            oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #              [subspec[i]-modv[i],subspec[i]-modv[i]], psym=0, color=col
    #      endfor
    #    end
#
    #    4: begin  ;Plot ratio on a large scale for bad situations
    #      plot,ctmean,subspec/modv,psym=3,/xlog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],charsize=2,$
    #          xtitle='Energy, keV',ytitle='data/model',position=[0.12,0.05,0.97,0.23],yrange=[0.33333,3.]
#
    #      for i=0, n_elements(subspec)-1 do begin
    #          if ctmean[i] GE fitrange[0] and ctmean[i] LE fitrange[1] then col=0 else col=6
    #            oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #              [subspec[i]/modv[i],subspec[i]/modv[i]], psym=0, color=col
    #      endfor
    #    end
#
    #    5: begin  ;Plot ratio of subtracted to total (where smallish)
    #      plot,ctmean,subspec/srcspec,psym=3,/xlog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],charsize=2,$
    #          xtitle='Energy, keV',ytitle='subtracted/total',position=[0.12,0.05,0.97,0.23],yrange=[-.5,.5]
#
    #      for i=0, n_elements(subspec)-1 do begin
    #          if ctmean[i] GE fitrange[0] and ctmean[i] LE fitrange[1] then col=0 else col=6
    #            oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #              [subspec[i]/srcspec[i],subspec[i]/srcspec[i]], psym=0, color=col
    #      endfor
    #    end
#
    #    else: begin  ;default is ratio with a limited scale
    #      plot,ctmean,subspec/modv,psym=3,/xlog,xrange=[min(ctmean)/1.5,max(ctmean)*1.5],charsize=2,$
    #          xtitle='Energy, keV',ytitle='data/model',position=[0.12,0.05,0.97,0.23],yrange=[0.8,1.25]
#
    #      for i=0, n_elements(subspec)-1 do begin
    #          if ctmean[i] GE fitrange[0] and ctmean[i] LE fitrange[1] then col=0 else col=6
    #            oplot,[ctmean[i]-ctwidth[i]/2.,ctmean[i]+ctwidth[i]/2.],$
    #              [subspec[i]/modv[i],subspec[i]/modv[i]], psym=0, color=col
    #      endfor
    #    end
#
    #endcase
#
    #endif

    return

  def _barrel_sp_fold_m1(self, phmean, phwidth, ctwidth, ctmean, usebins, maxcycles):
    #Find good starting parameters:
    if (self.model == 1):
      #This formula for approximate e-folding from a count ratio between
      #two bands is empirical from simulations. 
      energies=dbase["guess_efold"]
      ratios=dbase["guess_efold_ratios"]
    elif (self.model == 2):
      energies=dbase["guess_emono"]
      ratios=dbase["guess_emono_ratios"]
    
    w1 = np.where(ctmean > 110 and ctmean < 150.)[0]
    w2 = np.where(ctmean > 200. and ctmean < 250.)[0]
    rat = self.subspec[w2].sum()/self.subspec[w1].sum()
    
    if (rat < ratios.min()):
      startpar = min(energies)
    elif (rat > ratios.max()):
      startpar = max(energies)
    else:
      startpar = np.interp(rat, energies, ratios)
        
    if (self.model == 1):
      tryspec = np.matmul((np.exp(-phmean/startpar)*phwidth), self.drm)
    elif self.model == 2:
      tryspec = phmean*0.
      tryspec[np.where( np.abs(phmean-startpar) == np.abs(phmean-startpar).min())[0][0] ] = 1.
      tryspec = np.matmul(tryspec, self.drm)
    else:
      print('Only exponential or monoenergetic spectrum is currently supported.')

    #Find a starting normalization by scaling area of model and data
    #(this will be the same procedure for every starting model):
    startnorm = (self.subspec[usebins]*ctwidth[usebins] ).sum() / ( tryspec[usebins]*ctwidth[usebins] ).sum()

    #Try a starting range around these trial values.  If the minimum 
    #chi-square is not on the boundary, zoom in.  If it is, zoom out.
    #In either case, recenter.

    points = 10   #always run a 21x21(x21) grid
    scaling = [0.5,0.5]  #[norm,par]: best values +/- 50%

    
    print('iter#', 'startpar','startnorm','bestpar','bestnorm','scalepar','scalenorm','bestchi')    
    #format='(a8,4a11,2a13,a10)'
    
    #Iterate the fit, adjusting the scale dynamically:
    #barrel_sp_fitgrid1, subspec, subspecerr, model, drm, phmean, phwidth, usebins, startpar, $
    #     startnorm, points, scaling, bestpar, bestnorm, bestparn, bestnormn, modvals, $
    #     chiarray, bestchi, pararray, normarray
    for i in range(maxcycles):
      [bestpar, bestnorm, bestparn, bestnormn, modvals, chiarray, bestchi, pararray, normarray] = self._barrel_sp_fitgrid1(
        phmean, phwidth, usebins, startpar, startnorm, points, scaling
      )
      
      #if best value is not on boundary, zoom in or finish.
      #Note that zooming in or out on scalingdrm doesn't do anything if
      #you aren't using two drms.
      if np.abs(bestnormn) != points and scaling[0] >= 0.001:
        scaling[0] /= 2.5
      if np.abs(bestparn) != points and scaling[1] >= 0.001:
        scaling[1] /= 2.5

      #If scaling is now very fine, break.  Note that the last values of the
      #scaling parameters recorded here aren't really the last
      #values used, the last value used could be 2.5 times higher in one or more:
      if scaling[0] < 0.001 and scaling[1] < 0.001:
        break

      if np.abs(bestnormn) == points:
        scaling[0] *= 2.0
      if np.abs(bestparn) == points:
        scaling[1] *= 2.0

      print(i,startpar,startnorm,bestpar,bestnorm,scaling[1],scaling[0],bestchi)
      #format='(i8,4f11.3,2f13.6,f13.4)'

      startpar = bestpar
      startnorm = bestnorm

    #If it never got to the finest scale, break with error:
    if scaling[0] > 0.001 or scaling[1] > 0.001:
      print, 'WARNING: Fit failed to converge in maximum number of cycles.'

    #Set most output variables (either 2 or 3 best-fit params depending on
    #treatment of response matrices:
    params = [bestnorm, bestpar]
    chisquare = bestchi
    dof = usebins.size - 2

    #Only one thing left: the error on the parameters.  This requires more
    #effort.  Here we will wander radially outwards until we find that the
    #whole boundary has chisq > chimin
    #Always center on the best value:
    startpar = bestpar
    startnorm = bestnorm
    points = 10

    #Create masks for the outer boundary of the chi-square space:
    edges1 = np.zeros([2*points+1, 2*points+1])
    edges2 = np.zeros([2*points+1, 2*points+1])
    edges1[:, 0] = 1
    edges1[:, 2*points] = 1
    edges2[0, :] = 1
    edges2[2*points, :] = 1

    #Create initial values for error bar search:
    scaling = [0.1, 0.1]   #first guess
    scaling0 = scaling
    minscaling = scaling
    goingup = [0,0]

    for i in range(maxcycles):      
      [bestpar, bestnorm, bestparn, bestnormn, modvals, chiarray, bestchi, pararray, normarray] = self._barrel_sp_fitgrid1(
        phmean, phwidth, usebins, startpar, startnorm, points, scaling
      )
      #First see if the contour is completely closed:
      #Look for chisq < min_chisq + 1 on boundary:
      w1 = np.where(edges1.astype(bool) and (chiarray <= chisquare + 1))[0]
      w2 = np.where(edges2.astype(bool) and (chiarray <= chisquare + 1))[0]
      nw1 = 0
      for dim in w1: nw1 += dim.size
      nw2 = 0
      for dim in w2: nw2 += dim.size
      nw=[nw1,nw2]

      #If the boundary is entirely outside of the chi-square contour, zoom
      #in by a factor of 2, unless you had already zoomed out, in which 
      #case you've actually identified the right scale:
      if (np.sum(nw) == 0):
        if (np.sum(goingup) == 2):
          break
        if (not goingup[0]): scaling[0] /= 2.0
        if (not goingup[1]): scaling[1] /= 2.0
        continue
    
      #If boundary not entirely clear, take each axis separately, and
      #expand or contract the scaling:
      for j, v in enumerate(nw):
        if (nw[j] > 0):
          goingup[j] = 1
          scaling[j] *= 2.0
        else:
          if (not goingup[j]): scaling[j] /= 2.0 
      
      #Now that we've found the appropriate scaling (within a factor
      #of 2 of the point where the last good fit appears on the boundary), 
      #do one very fine map of chisquare space to find the error bars:

      points = 40

      [bestpar, bestnorm, bestparn, bestnormn, modvals, chiarray, bestchi, pararray, normarray] = self._barrel_sp_fitgrid1(
        phmean, phwidth, usebins, startpar, startnorm, points, scaling
      )

      #Pick out the subset of points within the min(chisquare)+1. contour:
      w = np.where(chiarray < chisquare + 1.)[0]
      if w.size == 0:
        print('Failure in finding error bars.')

      #This makes up the last needed output parameter: ranges of the parameters
      param_ranges = [
        [np.min(normarray[w]), np.max(normarray[w])],
        [np.min(pararray[w]), np.max(pararray[w])]
      ]

    return [params, param_ranges, modvals, chisquare, dof]
  

  def _barrel_sp_fold_m2(self, phebins, phmean, phwidth, ctwidth, usebins, maxcycles):
    subspec = self.subspec
    subspecerr = self.subspec_err
    modlfile = self.modlfile
    drm = self.drm
    
    ### FIX 
    modelspec = barrel_sp_readmodelspec(modlfile, phebins, phmean)

    tryspec = np.matmul(drm, modelspec*phwidth)

    #Find a starting normalization by scaling area of model and data
    #(this will be the same procedure for every starting model):  

    startnorm = np.sum( subspec[usebins]*ctwidth[usebins] ) / np.sum( tryspec[usebins]*ctwidth[usebins] )

    #Try a starting range around these trial values.  If the minimum 
    #chi-square is not on the boundary, zoom in.  If it is, zoom out.
    #In either case, recenter.

    points = 10   #always run a 21x21(x21) grid
    scaling = [0.5]  #[norm]: best value +/- 50%

    
    print('iter#', 'startnorm','bestnorm','scalenorm','bestchi')
    #format='(a8,2a11,a13,a10)'

    #Iterate the fit, adjusting the scale dynamically:
    for i in range(maxcycles):
      [bestnorm, bestnormn, modvals, chiarray, bestchi, normarray] = self._barrel_sp_fitgrid2(
        phmean, phwidth, usebins, startnorm, points, scaling
      )
      
      #if best value is not on boundary, zoom in or finish.
      #Note that zooming in or out on scalingdrm doesn't do anything if
      #you aren't using two drms.

      if (np.abs(bestnormn) != points and scaling[0] >= 0.001):
        scaling[0] /= 2.5
    
      #If scaling is now very fine, break.  Note that the last values of the
      #scaling parameters recorded here aren't really the last
      #values used, the last value used could be 2.5 times higher in one or more:
      if (scaling[0] < 0.001):
        break

      if (np.abs(bestnormn) == points):
        scaling[0] *= 2.0

      print(i,startnorm,bestnorm,scaling[0],bestchi)
      #format='(i8,2f11.3,f13.6,f13.4)'

      startnorm = bestnorm


    #If it never got to the finest scale, break with error:
    if (scaling[0] > 0.001):
        print('Fit failed to converge in maximum number of cycles.')

    #Set most output variables (either 2 or 3 best-fit params depending on
    #treatment of response matrices:
    params = [bestnorm]
    chisquare = bestchi
    dof = usebins.size - 2

    #Only one thing left: the error on the parameters.  This requires more
    #effort.  Here we will wander radially outwards until we find that the
    #whole boundary has chisq > chimin
    #Always center on the best value:
    startnorm = bestnorm
    points = 10

    #Create masks for the outer boundary of the chi-square space:
    edges = np.zeros(2*points+1, dtype=int)
    edges[0] = 1
    edges[2*points] = 1

    #Create initial values for error bar search:
    scaling = [0.1] #first guess
    scaling0 = scaling
    minscaling = scaling
    goingup = 0

    for i in range(maxcycles):
      [bestnorm, bestnormn, modvals, chiarray, bestchi, normarray] = self._barrel_sp_fitgrid2(
        phmean, phwidth, usebins, startnorm, points, scaling
      )

      #First see if the contour is completely closed:
      #Look for chisq < min_chisq + 1 on boundary:
      w1 = np.where(edges.astype(bool) and (chiarray < chisquare + 1.))[0]
      nw = w1.size

      #If the boundary is entirely outside of the chi-square contour, zoom
      #in by a factor of 2, unless you had already zoomed out, in which 
      #case you've actually identified the right scale:
      if (nw == 0):
          if (goingup):
            break
          scaling[0] /= 2.0
          continue
          
      if (nw > 0):
          goingup = 1
          scaling[0] *= 2.0

      #Now that we've found the appropriate scaling (within a factor
      #of 2 of the point where the last good fit appears on the boundary), 
      #do one very fine map of chisquare space to find the error bars:

      points = 40

      [bestnorm, bestnormn, modvals, chiarray, bestchi, normarray] = self._barrel_sp_fitgrid2(
        phmean, phwidth, usebins, startnorm, points, scaling
      )

      #Pick out the subset of points within the min(chisquare)+1. contour:
      w = np.where(chiarray < chisquare + 1.)[0]
      nw = w.size
      if (nw == 0):
        print('Failure in finding error bars.')

      #This makes up the last needed output parameter: ranges of the parameters
      param_ranges = [ [np.min(normarray[w]), np.max(normarray[w])] ]

    return [params, param_ranges, modvals, chisquare, dof]

  def _barrel_sp_fold_m3(self):
    return
  def _barrel_sp_fold_m4(self):
    return
  
  def _barrel_sp_fitgrid1(self, phmean, phwidth, usebins, startpar, startnorm, points, scaling):
    subspec = self.subspec
    subspecerr = self.subspecerr
    model = self.model
    drm = self.drm

    #Set up the vectors of values for parameters and normalizations:
    pts = 2*points + 1
    normvector = [np.array(range(pts))-points]*scaling[0]/points*startnorm + startnorm
    parvector  = [np.array(range(pts))-points]*scaling[1]/points*startpar + startpar
    parrange   = [np.min(parvector),max(parvector)]

    if (model == 2):
      #Reassign minimum/maximum if they are going to force the fit to go
      #out of range (this is particular to the monoenergetic model)
      minpossible = phmean[1]
      w = np.where(parvector <= minpossible)[0]
      nl = w.size
      
      maxpossible = phmean[phmean.size - 2]
      w = np.where(parvector >= maxpossible)[0]
      ng = w.size

      if nl > 0 or ng > 0:
        parstart  = np.max([minpossible, np.min(parvector)])
        parend    = np.min([maxpossible, np.max(parvector)])
        parvector = np.array(range(pts)) * (parend - parstart) / (1 * pts) + parstart
        print('rescaled from ',parrange, ' to ',[min(parvector),max(parvector)])
    
    #Set up the output arrays:
    pararray  = np.zeros([pts,pts])
    normarray = np.zeros([pts,pts])
    chiarray  = np.zeros([pts,pts])

    #Initialize best chi-square as something awful:
    bestchi = 1e10

    #Loop away!

    for j in range(pts):         #over spectral parameter
      #Set up the model, photons/bin:
      if (model == 1):
        vals = np.exp(-phmean/parvector[j])*phwidth
        foldvals = np.matmul(drm, vals)
      elif (model == 2):
        #In order to differentiate between different energies within one input
        #bin, evaluate the bins to either side, fit a quadratic, and
        #interpolate to the exact target energy:
        vals1 = phmean*0.
        vals2 = phmean*0.
        vals3 = phmean*0.
        bin2 = (
          np.where( np.abs(phmean-parvector[j])==np.min(np.abs(phmean-parvector[j])) )[0]
        )[0]
        bin1 = bin2 - 1
        bin3 = bin2 + 1
        if (bin1 < 0 or bin3 > phmean.size-1):
          print('Tried energy out of range.')
        vals1[bin1]=1
        vals2[bin2]=1
        vals3[bin3]=1
        foldvals1 = np.matmul(drm,vals1)
        foldvals2 = np.matmul(drm,vals2)
        foldvals3 = np.matmul(drm,vals3)
        foldvals = foldvals2*0 #QUESTION: What is this doing?
        for i in range(foldvals1.size):
          y = [foldvals1[i], foldvals2[i], foldvals3[i]]
          x = [phmean[bin1], phmean[bin2], phmean[bin3]]
          r = np.polyfit(x,y,2)
          foldvals[i] = r[2] + r[1]*parvector[j] + r[0]*np.power(parvector[j],2)
        
      else:
        print('Only exponential or monoenergetic spectra are currently supported.')

      #Test different normalizations against the data:
      for i in range(pts):
        normarray[i,j] = normvector[i]
        pararray[i,j]  = parvector[j]
        chiarray[i,j]  = np.sum(
          np.power(
            (subspec[usebins] - normvector[i]*foldvals[usebins])/subspecerr[usebins],
            2
          )
        )
   
    #Find the best fit and set output parameters:
    bestchi = np.min(chiarray)
    w = (
      np.where(chiarray == bestchi)[0]
    )[0]
    bestpar = pararray[w]
    bestnorm = normarray[w]
    bestparn = (
      np.where(parvector == bestpar)[0]
    )[0] - points
    bestnormn = (
      np.where(normvector == bestnorm)[0]
    )[0] - points
    
    if (model == 1):
      modvals = bestnorm * np.matmul(drm, (np.exp(-phmean/bestpar)*phwidth))
    elif (model == 2):
      modvals = 0*phmean
      w = (np.where( np.abs(phmean-bestpar) == min(np.abs(phmean-bestpar)))[0])[0]
      modvals[w]= bestnorm
      modvals = np.matmul(drm,modvals)
    
    return [bestpar, bestnorm, bestparn, bestnormn, modvals, chiarray, bestchi, pararray, normarray]
  
  def _barrel_sp_fitgrid2(self, phmean, phwidth, usebins, startnorm, points, scaling):
    subspec = self.subspec
    subspecerr = self.subspecerr
    modelspec = self.modelspec
    drm = self.drm

    pts = 2*points + 1
    normvector = [np.arange(pts)-points]*scaling[0]/points*startnorm + startnorm

    #Set up the output arrays:
    chiarray = np.zeros(pts)

    #Initialize best chi-square as something awful:
    bestchi = 1e10

    #Loop away!

    foldvals = np.matmul(drm, modelspec*phwidth)
    for j in range(pts): #over normalization
      chiarray[j] = np.sum( np.power( (subspec[usebins] - normvector[j]*foldvals[usebins])/subspecerr[usebins], 2) )
    normarray = normvector

    #Find the best fit and set output parameters:

    bestchi = np.min(chiarray)
    w = (np.where(chiarray == bestchi)[0])[0]
    bestnorm = normarray[w]
    bestnormn = (np.where(normvector == bestnorm)[0])[0] - points
    modvals = bestnorm * np.matmul(drm, (modelspec*phwidth) )

    return [bestnorm, bestnormn, modvals, chiarray, bestchi, normarray]

  def _barrel_sp_fitgrid3(self, phmean, phwidth, usebins, startnorm1, startnorm2, points, scaling):
    subspec = self.subspec
    subspecerr = self.subspecerr
    modelspec1 = self.modelspec1
    modelspec2 = self.modelspec2
    drm = self.drm

    #Set up the vectors of values for parameters and normalizations:
    pts = 2*points + 1
    norm1vector = [np.arange(pts)-points]*scaling[0]/points*startnorm1 + startnorm1
    norm2vector = [np.arange(pts)-points]*scaling[1]/points*startnorm2 + startnorm2

    #Set up the output arrays:
    norm1array = np.zeros([pts,pts])
    norm2array = np.zeros([pts,pts])
    chiarray   = np.zeros([pts,pts])

    #Initialize best chi-square as something awful:
    bestchi = 1e10

    #Loop away!

    for j in range(pts): #over normalization 1
      foldvals1 = np.matmul(drm, norm1vector[j]*modelspec1*phwidth)

      for i in range(pts): #over normalization 2
        foldvals2 = np.matmul(drm, norm2vector[i]*modelspec2*phwidth)

        #Test different normalizations against the data:
        norm1array[j,i] = norm1vector[j]
        norm2array[j,i] = norm2vector[i]
        chiarray[j,i] = np.sum( np.power( (subspec[usebins] - (foldvals1[usebins]+foldvals2[usebins])) / subspecerr[usebins] ), 2 )

    #Find the best fit and set output parameters:

    bestchi = np.min(chiarray)
    w = (np.where(chiarray == bestchi)[0])[0]
    bestnorm1 = norm1array[w]
    bestnorm2 = norm2array[w]
    bestnorm1n = (np.where(norm1vector == bestnorm1)[0])[0] - points
    bestnorm2n = (np.where(norm2vector == bestnorm2)[0])[0] - points
    modvals1 = bestnorm1 * np.matmul(drm, (modelspec1*phwidth))
    modvals2 = bestnorm2 * np.matmul(drm, (modelspec2*phwidth))

    return [bestnorm1, bestnorm2, bestnorm1n, bestnorm2n, modvals1, modvals2, chiarray, bestchi, norm1array, norm2array]
  
  def _barrel_sp_fitgrid4(self, phmean, phwidth, usebins, startpar, startnorm, startdrm, points, scaling):
    subspec = self.subspec
    subspecerr = self.subspecerr
    model = self.model
    drm = self.drm
    drm2 = self.drm2

    #Set up the vectors of values for parameters and normalizations:
    pts = 2*points + 1
    normvector = [findgen(pts)-points]*scaling[0]/points*startnorm + startnorm
    parvector  = [findgen(pts)-points]*scaling[1]/points*startpar + startpar
    drmvector  = [findgen(pts)-points]*scaling[2]/points + startdrm

    #Rescale drm vector to omit unphysical regions (< 0, > 1):
    drmlow = np.where(drmvector < 0.)[0]
    nlow = drmlow.size
    drmhigh = np.where(drmvector > 1.)[0]
    nhigh = drmhigh.size
    drmmin = np.min(drmvector)
    drmmax = np.max(drmvector)
    if (nlow > 0):
      drmmin = 0
    if (nhigh > 0):
      drmmax = 1
    if (nlow > 0 or nhigh > 0):
      drmvector = drmmin + (drmmax-drmmin)*np.arange(pts)/(1.*(pts-1.))

    #Set up the output arrays:
    pararray = np.zeros([pts,pts,pts])
    normarray = np.zeros([pts,pts,pts])
    drmarray = np.zeros([pts,pts,pts])
    chiarray = np.zeros([pts,pts,pts])

    #Initialize best chi-square as something awful:
    bestchi = 1.e10

    #Loop away!

    for k in range(pts):  #over drm
      thisdrm = drm*drmvector[k] + drm2*(1.0 - drmvector[k])

      for j in range(pts): #over spectral parameter
        #Set up the model, photons/bin:
        if (model == 1):
          vals = np.exp(-phmean/parvector[j])*phwidth
        else:
          print('BARREL_SP_FITGRID: Only exponential spectrum is currently supported.')

        #Fold through response matrix
        foldvals = np.matmul(thisdrm, vals)

        #Test different normalizations against the data:
        for i in (pts):
          normarray[i,j,k] = normvector[i]
          pararray[i,j,k] = parvector[j]
          drmarray[i,j,k] = drmvector[k]
          chiarray[i,j,k] = np.sum( np.power( (subspec[usebins] - normvector[i]*foldvals[usebins])/subspecerr[usebins], 2) )
      

    #Find the best fit and set output parameters:
    bestchi = np.min(chiarray)
    w = (np.where(chiarray == bestchi)[0])[0]
    bestpar = pararray[w]
    bestnorm = normarray[w]
    bestdrm = drmarray[w]
    bestparn = (np.where(parvector == bestpar)[0])[0] - points
    bestnormn = (np.where(normvector == bestnorm)[0])[0] - points
    bestdrmn = (np.where(drmvector == bestdrm)[0])[0] - points
    drmbest =  drm*bestdrm + drm2*(1.0 - bestdrm)
    
    if (model == 1):
      modvals = bestnorm*np.matmul(drmbest, (np.exp(-phmean/bestpar)*phwidth))

    return [bestpar, bestnorm, bestdrm, bestparn, bestnormn, bestdrmn, modvals, chiarray, bestchi, pararray, normarray, drmarray]