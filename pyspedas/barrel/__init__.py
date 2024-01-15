from .load import load

def sspc(trange=['2013-01-28', '2013-01-29'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Slow Specta (256 channels accumulated over 32 seconds)

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-28', '2013-01-29']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.fspc(trange=['2013-01-17', '2013-01-19'], probe='1D')
        >>> tplot('brl1D_FSPC1')

    """
    return load(datatype='sspc', trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)


def mspc(trange=['2013-01-29','2013-01-30'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Medium Spectra (48 channels accumulated over 4 seconds)

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-29','2013-01-30']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.mspc(trange=['2013-01-29','2013-01-30'], probe='1A')
        >>> tplot('brl1A_MSPC')
    """
    return load(datatype='mspc', trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)


def fspc(trange=['2013-01-29','2013-01-30'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Fast Spectra (4 channels record at 20Hz)

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-29','2013-01-30']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.fspc(trange=['2013-01-17', '2013-01-19'], probe='1D')
        >>> tplot('brl1D_FSPC1')
    """

    return load(datatype='fspc',trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)


def rcnt(trange=['2013-01-29','2013-01-30'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Rate Counters (Scintillating statistics)

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-29','2013-01-30']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.rcnt(trange=['2013-01-29','2013-01-30'], probe='1A')
        >>> tplot('brl1A_LowLevel')
    """
    return load(datatype='rcnt', trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)


def magn(trange=['2013-01-29','2013-01-30'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Magnetometer Data

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-29','2013-01-30']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.magn(trange=['2013-01-29','2013-01-30'], probe='1A')
        >>> tplot('brl1A_Total')
    """
    return load(datatype='magn', trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)


def ephm(trange=['2013-01-29','2013-01-30'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Ephemeris (GPS data and magnetic coordinates)

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-29','2013-01-30']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.ephm(trange=['2013-01-29','2013-01-30'], probe='1A')
        >>> ##TODO
    """
   
    return load(datatype='ephm', trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)


def hkpg(trange=['2013-01-29','2013-01-30'],
        probe='1A',
        downloadonly=False,
        no_update=False,
        time_clip=False):
    """
    This function load data from BARREL Housekeeping (Voltages, currents, temperatures)

    Parameters
    ----------
        trange : list of str
            time range of interest [starttime, endtime] with the format 
            'YYYY-MM-DD','YYYY-MM-DD'] or to specify more or less than a day 
            ['YYYY-MM-DD/hh:mm:ss','YYYY-MM-DD/hh:mm:ss']
            Default: ['2013-01-29','2013-01-30']

        probe: str
            Default: '1A'

        downloadonly: bool
            Set this flag to download the CDF files, but not load them into 
            tplot variables.
            Default: False

        no_update: bool
            If set, only load data from your local cache
            Default: False
        
        time_clip: bool
            Time clip the variables to exactly the range specified in the trange keyword
            Default: False

    Returns
    ----------
        List of tplot variables created.

    Example:
    ----------
        >>> import pyspdedas
        >>> from pytplot import tplot
        >>> pyspedas.barrel.hkpg(trange=['2013-01-29','2013-01-30'], probe='1A')
        >>> tplot('brl1A_V1_Battery')
    """
        
    return load(datatype='hkpg', trange=trange, probe=probe, downloadonly=downloadonly, time_clip=time_clip, no_update=no_update)
