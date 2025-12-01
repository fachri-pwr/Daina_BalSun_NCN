from __future__ import print_function, absolute_import, division

try:
    from . import _supy_driver
except ImportError:
    try:
        import _supy_driver
    except ImportError:
        raise ImportError("Cannot import _supy_driver")


import f90wrap.runtime
import logging
import numpy

class Suews_Def_Dts(f90wrap.runtime.FortranModule):
    """
    Module suews_def_dts
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
        lines 5-1439
    
    """
    @f90wrap.runtime.register_class("supy_driver.SUEWS_CONFIG")
    class SUEWS_CONFIG(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_config)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 18-38
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Config()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 18-38
            
            
            Returns
            -------
            this : Suews_Config
            	Object to be constructed
            
            
            Automatically generated constructor for suews_config
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_config_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Config
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 18-38
            
            Parameters
            ----------
            this : Suews_Config
            	Object to be destructed
            
            
            Automatically generated destructor for suews_config
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_config_finalise(this=self._handle)
        
        @property
        def diagmethod(self):
            """
            Element diagmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 19
            
            """
            return _supy_driver.f90wrap_suews_config__get__diagmethod(self._handle)
        
        @diagmethod.setter
        def diagmethod(self, diagmethod):
            _supy_driver.f90wrap_suews_config__set__diagmethod(self._handle, diagmethod)
        
        @property
        def emissionsmethod(self):
            """
            Element emissionsmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 20
            
            """
            return _supy_driver.f90wrap_suews_config__get__emissionsmethod(self._handle)
        
        @emissionsmethod.setter
        def emissionsmethod(self, emissionsmethod):
            _supy_driver.f90wrap_suews_config__set__emissionsmethod(self._handle, \
                emissionsmethod)
        
        @property
        def roughlenheatmethod(self):
            """
            Element roughlenheatmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 21
            
            """
            return _supy_driver.f90wrap_suews_config__get__roughlenheatmethod(self._handle)
        
        @roughlenheatmethod.setter
        def roughlenheatmethod(self, roughlenheatmethod):
            _supy_driver.f90wrap_suews_config__set__roughlenheatmethod(self._handle, \
                roughlenheatmethod)
        
        @property
        def roughlenmommethod(self):
            """
            Element roughlenmommethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 22
            
            """
            return _supy_driver.f90wrap_suews_config__get__roughlenmommethod(self._handle)
        
        @roughlenmommethod.setter
        def roughlenmommethod(self, roughlenmommethod):
            _supy_driver.f90wrap_suews_config__set__roughlenmommethod(self._handle, \
                roughlenmommethod)
        
        @property
        def faimethod(self):
            """
            Element faimethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 23
            
            """
            return _supy_driver.f90wrap_suews_config__get__faimethod(self._handle)
        
        @faimethod.setter
        def faimethod(self, faimethod):
            _supy_driver.f90wrap_suews_config__set__faimethod(self._handle, faimethod)
        
        @property
        def smdmethod(self):
            """
            Element smdmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 24
            
            """
            return _supy_driver.f90wrap_suews_config__get__smdmethod(self._handle)
        
        @smdmethod.setter
        def smdmethod(self, smdmethod):
            _supy_driver.f90wrap_suews_config__set__smdmethod(self._handle, smdmethod)
        
        @property
        def waterusemethod(self):
            """
            Element waterusemethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 25
            
            """
            return _supy_driver.f90wrap_suews_config__get__waterusemethod(self._handle)
        
        @waterusemethod.setter
        def waterusemethod(self, waterusemethod):
            _supy_driver.f90wrap_suews_config__set__waterusemethod(self._handle, \
                waterusemethod)
        
        @property
        def netradiationmethod(self):
            """
            Element netradiationmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 26
            
            """
            return _supy_driver.f90wrap_suews_config__get__netradiationmethod(self._handle)
        
        @netradiationmethod.setter
        def netradiationmethod(self, netradiationmethod):
            _supy_driver.f90wrap_suews_config__set__netradiationmethod(self._handle, \
                netradiationmethod)
        
        @property
        def stabilitymethod(self):
            """
            Element stabilitymethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 27
            
            """
            return _supy_driver.f90wrap_suews_config__get__stabilitymethod(self._handle)
        
        @stabilitymethod.setter
        def stabilitymethod(self, stabilitymethod):
            _supy_driver.f90wrap_suews_config__set__stabilitymethod(self._handle, \
                stabilitymethod)
        
        @property
        def storageheatmethod(self):
            """
            Element storageheatmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 28
            
            """
            return _supy_driver.f90wrap_suews_config__get__storageheatmethod(self._handle)
        
        @storageheatmethod.setter
        def storageheatmethod(self, storageheatmethod):
            _supy_driver.f90wrap_suews_config__set__storageheatmethod(self._handle, \
                storageheatmethod)
        
        @property
        def diagnose(self):
            """
            Element diagnose ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 29
            
            """
            return _supy_driver.f90wrap_suews_config__get__diagnose(self._handle)
        
        @diagnose.setter
        def diagnose(self, diagnose):
            _supy_driver.f90wrap_suews_config__set__diagnose(self._handle, diagnose)
        
        @property
        def snowuse(self):
            """
            Element snowuse ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 30
            
            """
            return _supy_driver.f90wrap_suews_config__get__snowuse(self._handle)
        
        @snowuse.setter
        def snowuse(self, snowuse):
            _supy_driver.f90wrap_suews_config__set__snowuse(self._handle, snowuse)
        
        @property
        def use_sw_direct_albedo(self):
            """
            Element use_sw_direct_albedo ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 31
            
            """
            return \
                _supy_driver.f90wrap_suews_config__get__use_sw_direct_albedo(self._handle)
        
        @use_sw_direct_albedo.setter
        def use_sw_direct_albedo(self, use_sw_direct_albedo):
            _supy_driver.f90wrap_suews_config__set__use_sw_direct_albedo(self._handle, \
                use_sw_direct_albedo)
        
        @property
        def ohmincqf(self):
            """
            Element ohmincqf ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 32
            
            """
            return _supy_driver.f90wrap_suews_config__get__ohmincqf(self._handle)
        
        @ohmincqf.setter
        def ohmincqf(self, ohmincqf):
            _supy_driver.f90wrap_suews_config__set__ohmincqf(self._handle, ohmincqf)
        
        @property
        def diagqs(self):
            """
            Element diagqs ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 33
            
            """
            return _supy_driver.f90wrap_suews_config__get__diagqs(self._handle)
        
        @diagqs.setter
        def diagqs(self, diagqs):
            _supy_driver.f90wrap_suews_config__set__diagqs(self._handle, diagqs)
        
        @property
        def evapmethod(self):
            """
            Element evapmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 34
            
            """
            return _supy_driver.f90wrap_suews_config__get__evapmethod(self._handle)
        
        @evapmethod.setter
        def evapmethod(self, evapmethod):
            _supy_driver.f90wrap_suews_config__set__evapmethod(self._handle, evapmethod)
        
        @property
        def laimethod(self):
            """
            Element laimethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 35
            
            """
            return _supy_driver.f90wrap_suews_config__get__laimethod(self._handle)
        
        @laimethod.setter
        def laimethod(self, laimethod):
            _supy_driver.f90wrap_suews_config__set__laimethod(self._handle, laimethod)
        
        @property
        def localclimatemethod(self):
            """
            Element localclimatemethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 36
            
            """
            return _supy_driver.f90wrap_suews_config__get__localclimatemethod(self._handle)
        
        @localclimatemethod.setter
        def localclimatemethod(self, localclimatemethod):
            _supy_driver.f90wrap_suews_config__set__localclimatemethod(self._handle, \
                localclimatemethod)
        
        @property
        def stebbsmethod(self):
            """
            Element stebbsmethod ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 37
            
            """
            return _supy_driver.f90wrap_suews_config__get__stebbsmethod(self._handle)
        
        @stebbsmethod.setter
        def stebbsmethod(self, stebbsmethod):
            _supy_driver.f90wrap_suews_config__set__stebbsmethod(self._handle, stebbsmethod)
        
        @property
        def flag_test(self):
            """
            Element flag_test ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 38
            
            """
            return _supy_driver.f90wrap_suews_config__get__flag_test(self._handle)
        
        @flag_test.setter
        def flag_test(self, flag_test):
            _supy_driver.f90wrap_suews_config__set__flag_test(self._handle, flag_test)
        
        def __str__(self):
            ret = ['<suews_config>{\n']
            ret.append('    diagmethod : ')
            ret.append(repr(self.diagmethod))
            ret.append(',\n    emissionsmethod : ')
            ret.append(repr(self.emissionsmethod))
            ret.append(',\n    roughlenheatmethod : ')
            ret.append(repr(self.roughlenheatmethod))
            ret.append(',\n    roughlenmommethod : ')
            ret.append(repr(self.roughlenmommethod))
            ret.append(',\n    faimethod : ')
            ret.append(repr(self.faimethod))
            ret.append(',\n    smdmethod : ')
            ret.append(repr(self.smdmethod))
            ret.append(',\n    waterusemethod : ')
            ret.append(repr(self.waterusemethod))
            ret.append(',\n    netradiationmethod : ')
            ret.append(repr(self.netradiationmethod))
            ret.append(',\n    stabilitymethod : ')
            ret.append(repr(self.stabilitymethod))
            ret.append(',\n    storageheatmethod : ')
            ret.append(repr(self.storageheatmethod))
            ret.append(',\n    diagnose : ')
            ret.append(repr(self.diagnose))
            ret.append(',\n    snowuse : ')
            ret.append(repr(self.snowuse))
            ret.append(',\n    use_sw_direct_albedo : ')
            ret.append(repr(self.use_sw_direct_albedo))
            ret.append(',\n    ohmincqf : ')
            ret.append(repr(self.ohmincqf))
            ret.append(',\n    diagqs : ')
            ret.append(repr(self.diagqs))
            ret.append(',\n    evapmethod : ')
            ret.append(repr(self.evapmethod))
            ret.append(',\n    laimethod : ')
            ret.append(repr(self.laimethod))
            ret.append(',\n    localclimatemethod : ')
            ret.append(repr(self.localclimatemethod))
            ret.append(',\n    stebbsmethod : ')
            ret.append(repr(self.stebbsmethod))
            ret.append(',\n    flag_test : ')
            ret.append(repr(self.flag_test))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SURF_STORE_PRM")
    class SURF_STORE_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=surf_store_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 40-46
        
        """
        def __init__(self, handle=None):
            """
            self = Surf_Store_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 40-46
            
            
            Returns
            -------
            this : Surf_Store_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for surf_store_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__surf_store_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Surf_Store_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 40-46
            
            Parameters
            ----------
            this : Surf_Store_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for surf_store_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__surf_store_prm_finalise(this=self._handle)
        
        @property
        def store_min(self):
            """
            Element store_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 41
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__store_min(self._handle)
        
        @store_min.setter
        def store_min(self, store_min):
            _supy_driver.f90wrap_surf_store_prm__set__store_min(self._handle, store_min)
        
        @property
        def store_max(self):
            """
            Element store_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 42
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__store_max(self._handle)
        
        @store_max.setter
        def store_max(self, store_max):
            _supy_driver.f90wrap_surf_store_prm__set__store_max(self._handle, store_max)
        
        @property
        def store_cap(self):
            """
            Element store_cap ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 43
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__store_cap(self._handle)
        
        @store_cap.setter
        def store_cap(self, store_cap):
            _supy_driver.f90wrap_surf_store_prm__set__store_cap(self._handle, store_cap)
        
        @property
        def drain_eq(self):
            """
            Element drain_eq ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 44
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__drain_eq(self._handle)
        
        @drain_eq.setter
        def drain_eq(self, drain_eq):
            _supy_driver.f90wrap_surf_store_prm__set__drain_eq(self._handle, drain_eq)
        
        @property
        def drain_coef_1(self):
            """
            Element drain_coef_1 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 45
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__drain_coef_1(self._handle)
        
        @drain_coef_1.setter
        def drain_coef_1(self, drain_coef_1):
            _supy_driver.f90wrap_surf_store_prm__set__drain_coef_1(self._handle, \
                drain_coef_1)
        
        @property
        def drain_coef_2(self):
            """
            Element drain_coef_2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 46
            
            """
            return _supy_driver.f90wrap_surf_store_prm__get__drain_coef_2(self._handle)
        
        @drain_coef_2.setter
        def drain_coef_2(self, drain_coef_2):
            _supy_driver.f90wrap_surf_store_prm__set__drain_coef_2(self._handle, \
                drain_coef_2)
        
        def __str__(self):
            ret = ['<surf_store_prm>{\n']
            ret.append('    store_min : ')
            ret.append(repr(self.store_min))
            ret.append(',\n    store_max : ')
            ret.append(repr(self.store_max))
            ret.append(',\n    store_cap : ')
            ret.append(repr(self.store_cap))
            ret.append(',\n    drain_eq : ')
            ret.append(repr(self.drain_eq))
            ret.append(',\n    drain_coef_1 : ')
            ret.append(repr(self.drain_coef_1))
            ret.append(',\n    drain_coef_2 : ')
            ret.append(repr(self.drain_coef_2))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.WATER_DIST_PRM")
    class WATER_DIST_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=water_dist_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 48-56
        
        """
        def __init__(self, handle=None):
            """
            self = Water_Dist_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 48-56
            
            
            Returns
            -------
            this : Water_Dist_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for water_dist_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__water_dist_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 48-56
            
            Parameters
            ----------
            this : Water_Dist_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for water_dist_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__water_dist_prm_finalise(this=self._handle)
        
        @property
        def to_paved(self):
            """
            Element to_paved ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 49
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_paved(self._handle)
        
        @to_paved.setter
        def to_paved(self, to_paved):
            _supy_driver.f90wrap_water_dist_prm__set__to_paved(self._handle, to_paved)
        
        @property
        def to_bldg(self):
            """
            Element to_bldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 50
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_bldg(self._handle)
        
        @to_bldg.setter
        def to_bldg(self, to_bldg):
            _supy_driver.f90wrap_water_dist_prm__set__to_bldg(self._handle, to_bldg)
        
        @property
        def to_evetr(self):
            """
            Element to_evetr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 51
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_evetr(self._handle)
        
        @to_evetr.setter
        def to_evetr(self, to_evetr):
            _supy_driver.f90wrap_water_dist_prm__set__to_evetr(self._handle, to_evetr)
        
        @property
        def to_dectr(self):
            """
            Element to_dectr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 52
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_dectr(self._handle)
        
        @to_dectr.setter
        def to_dectr(self, to_dectr):
            _supy_driver.f90wrap_water_dist_prm__set__to_dectr(self._handle, to_dectr)
        
        @property
        def to_grass(self):
            """
            Element to_grass ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 53
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_grass(self._handle)
        
        @to_grass.setter
        def to_grass(self, to_grass):
            _supy_driver.f90wrap_water_dist_prm__set__to_grass(self._handle, to_grass)
        
        @property
        def to_bsoil(self):
            """
            Element to_bsoil ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 54
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_bsoil(self._handle)
        
        @to_bsoil.setter
        def to_bsoil(self, to_bsoil):
            _supy_driver.f90wrap_water_dist_prm__set__to_bsoil(self._handle, to_bsoil)
        
        @property
        def to_water(self):
            """
            Element to_water ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 55
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_water(self._handle)
        
        @to_water.setter
        def to_water(self, to_water):
            _supy_driver.f90wrap_water_dist_prm__set__to_water(self._handle, to_water)
        
        @property
        def to_soilstore(self):
            """
            Element to_soilstore ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 56
            
            """
            return _supy_driver.f90wrap_water_dist_prm__get__to_soilstore(self._handle)
        
        @to_soilstore.setter
        def to_soilstore(self, to_soilstore):
            _supy_driver.f90wrap_water_dist_prm__set__to_soilstore(self._handle, \
                to_soilstore)
        
        def __str__(self):
            ret = ['<water_dist_prm>{\n']
            ret.append('    to_paved : ')
            ret.append(repr(self.to_paved))
            ret.append(',\n    to_bldg : ')
            ret.append(repr(self.to_bldg))
            ret.append(',\n    to_evetr : ')
            ret.append(repr(self.to_evetr))
            ret.append(',\n    to_dectr : ')
            ret.append(repr(self.to_dectr))
            ret.append(',\n    to_grass : ')
            ret.append(repr(self.to_grass))
            ret.append(',\n    to_bsoil : ')
            ret.append(repr(self.to_bsoil))
            ret.append(',\n    to_water : ')
            ret.append(repr(self.to_water))
            ret.append(',\n    to_soilstore : ')
            ret.append(repr(self.to_soilstore))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.bioCO2_PRM")
    class bioCO2_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=bioco2_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 58-66
        
        """
        def __init__(self, handle=None):
            """
            self = Bioco2_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 58-66
            
            
            Returns
            -------
            this : Bioco2_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for bioco2_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__bioco2_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Bioco2_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 58-66
            
            Parameters
            ----------
            this : Bioco2_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for bioco2_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__bioco2_prm_finalise(this=self._handle)
        
        @property
        def beta_bioco2(self):
            """
            Element beta_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 59
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__beta_bioco2(self._handle)
        
        @beta_bioco2.setter
        def beta_bioco2(self, beta_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__beta_bioco2(self._handle, beta_bioco2)
        
        @property
        def beta_enh_bioco2(self):
            """
            Element beta_enh_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 60
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__beta_enh_bioco2(self._handle)
        
        @beta_enh_bioco2.setter
        def beta_enh_bioco2(self, beta_enh_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__beta_enh_bioco2(self._handle, \
                beta_enh_bioco2)
        
        @property
        def alpha_bioco2(self):
            """
            Element alpha_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 61
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__alpha_bioco2(self._handle)
        
        @alpha_bioco2.setter
        def alpha_bioco2(self, alpha_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__alpha_bioco2(self._handle, alpha_bioco2)
        
        @property
        def alpha_enh_bioco2(self):
            """
            Element alpha_enh_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 62
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__alpha_enh_bioco2(self._handle)
        
        @alpha_enh_bioco2.setter
        def alpha_enh_bioco2(self, alpha_enh_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__alpha_enh_bioco2(self._handle, \
                alpha_enh_bioco2)
        
        @property
        def resp_a(self):
            """
            Element resp_a ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 63
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__resp_a(self._handle)
        
        @resp_a.setter
        def resp_a(self, resp_a):
            _supy_driver.f90wrap_bioco2_prm__set__resp_a(self._handle, resp_a)
        
        @property
        def resp_b(self):
            """
            Element resp_b ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 64
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__resp_b(self._handle)
        
        @resp_b.setter
        def resp_b(self, resp_b):
            _supy_driver.f90wrap_bioco2_prm__set__resp_b(self._handle, resp_b)
        
        @property
        def theta_bioco2(self):
            """
            Element theta_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 65
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__theta_bioco2(self._handle)
        
        @theta_bioco2.setter
        def theta_bioco2(self, theta_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__theta_bioco2(self._handle, theta_bioco2)
        
        @property
        def min_res_bioco2(self):
            """
            Element min_res_bioco2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 66
            
            """
            return _supy_driver.f90wrap_bioco2_prm__get__min_res_bioco2(self._handle)
        
        @min_res_bioco2.setter
        def min_res_bioco2(self, min_res_bioco2):
            _supy_driver.f90wrap_bioco2_prm__set__min_res_bioco2(self._handle, \
                min_res_bioco2)
        
        def __str__(self):
            ret = ['<bioco2_prm>{\n']
            ret.append('    beta_bioco2 : ')
            ret.append(repr(self.beta_bioco2))
            ret.append(',\n    beta_enh_bioco2 : ')
            ret.append(repr(self.beta_enh_bioco2))
            ret.append(',\n    alpha_bioco2 : ')
            ret.append(repr(self.alpha_bioco2))
            ret.append(',\n    alpha_enh_bioco2 : ')
            ret.append(repr(self.alpha_enh_bioco2))
            ret.append(',\n    resp_a : ')
            ret.append(repr(self.resp_a))
            ret.append(',\n    resp_b : ')
            ret.append(repr(self.resp_b))
            ret.append(',\n    theta_bioco2 : ')
            ret.append(repr(self.theta_bioco2))
            ret.append(',\n    min_res_bioco2 : ')
            ret.append(repr(self.min_res_bioco2))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.CONDUCTANCE_PRM")
    class CONDUCTANCE_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=conductance_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 68-81
        
        """
        def __init__(self, handle=None):
            """
            self = Conductance_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 68-81
            
            
            Returns
            -------
            this : Conductance_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for conductance_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__conductance_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Conductance_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 68-81
            
            Parameters
            ----------
            this : Conductance_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for conductance_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__conductance_prm_finalise(this=self._handle)
        
        @property
        def g_max(self):
            """
            Element g_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 69
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_max(self._handle)
        
        @g_max.setter
        def g_max(self, g_max):
            _supy_driver.f90wrap_conductance_prm__set__g_max(self._handle, g_max)
        
        @property
        def g_k(self):
            """
            Element g_k ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 70
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_k(self._handle)
        
        @g_k.setter
        def g_k(self, g_k):
            _supy_driver.f90wrap_conductance_prm__set__g_k(self._handle, g_k)
        
        @property
        def g_q_base(self):
            """
            Element g_q_base ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 71
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_q_base(self._handle)
        
        @g_q_base.setter
        def g_q_base(self, g_q_base):
            _supy_driver.f90wrap_conductance_prm__set__g_q_base(self._handle, g_q_base)
        
        @property
        def g_q_shape(self):
            """
            Element g_q_shape ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 72
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_q_shape(self._handle)
        
        @g_q_shape.setter
        def g_q_shape(self, g_q_shape):
            _supy_driver.f90wrap_conductance_prm__set__g_q_shape(self._handle, g_q_shape)
        
        @property
        def g_t(self):
            """
            Element g_t ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 73
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_t(self._handle)
        
        @g_t.setter
        def g_t(self, g_t):
            _supy_driver.f90wrap_conductance_prm__set__g_t(self._handle, g_t)
        
        @property
        def g_sm(self):
            """
            Element g_sm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 74
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__g_sm(self._handle)
        
        @g_sm.setter
        def g_sm(self, g_sm):
            _supy_driver.f90wrap_conductance_prm__set__g_sm(self._handle, g_sm)
        
        @property
        def kmax(self):
            """
            Element kmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 75
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__kmax(self._handle)
        
        @kmax.setter
        def kmax(self, kmax):
            _supy_driver.f90wrap_conductance_prm__set__kmax(self._handle, kmax)
        
        @property
        def gsmodel(self):
            """
            Element gsmodel ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 77
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__gsmodel(self._handle)
        
        @gsmodel.setter
        def gsmodel(self, gsmodel):
            _supy_driver.f90wrap_conductance_prm__set__gsmodel(self._handle, gsmodel)
        
        @property
        def s1(self):
            """
            Element s1 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 78
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__s1(self._handle)
        
        @s1.setter
        def s1(self, s1):
            _supy_driver.f90wrap_conductance_prm__set__s1(self._handle, s1)
        
        @property
        def s2(self):
            """
            Element s2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 79
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__s2(self._handle)
        
        @s2.setter
        def s2(self, s2):
            _supy_driver.f90wrap_conductance_prm__set__s2(self._handle, s2)
        
        @property
        def th(self):
            """
            Element th ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 80
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__th(self._handle)
        
        @th.setter
        def th(self, th):
            _supy_driver.f90wrap_conductance_prm__set__th(self._handle, th)
        
        @property
        def tl(self):
            """
            Element tl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 81
            
            """
            return _supy_driver.f90wrap_conductance_prm__get__tl(self._handle)
        
        @tl.setter
        def tl(self, tl):
            _supy_driver.f90wrap_conductance_prm__set__tl(self._handle, tl)
        
        def __str__(self):
            ret = ['<conductance_prm>{\n']
            ret.append('    g_max : ')
            ret.append(repr(self.g_max))
            ret.append(',\n    g_k : ')
            ret.append(repr(self.g_k))
            ret.append(',\n    g_q_base : ')
            ret.append(repr(self.g_q_base))
            ret.append(',\n    g_q_shape : ')
            ret.append(repr(self.g_q_shape))
            ret.append(',\n    g_t : ')
            ret.append(repr(self.g_t))
            ret.append(',\n    g_sm : ')
            ret.append(repr(self.g_sm))
            ret.append(',\n    kmax : ')
            ret.append(repr(self.kmax))
            ret.append(',\n    gsmodel : ')
            ret.append(repr(self.gsmodel))
            ret.append(',\n    s1 : ')
            ret.append(repr(self.s1))
            ret.append(',\n    s2 : ')
            ret.append(repr(self.s2))
            ret.append(',\n    th : ')
            ret.append(repr(self.th))
            ret.append(',\n    tl : ')
            ret.append(repr(self.tl))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LAI_PRM")
    class LAI_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lai_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 83-91
        
        """
        def __init__(self, handle=None):
            """
            self = Lai_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 83-91
            
            
            Returns
            -------
            this : Lai_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lai_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lai_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lai_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 83-91
            
            Parameters
            ----------
            this : Lai_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lai_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lai_prm_finalise(this=self._handle)
        
        @property
        def baset(self):
            """
            Element baset ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 84
            
            """
            return _supy_driver.f90wrap_lai_prm__get__baset(self._handle)
        
        @baset.setter
        def baset(self, baset):
            _supy_driver.f90wrap_lai_prm__set__baset(self._handle, baset)
        
        @property
        def gddfull(self):
            """
            Element gddfull ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 85
            
            """
            return _supy_driver.f90wrap_lai_prm__get__gddfull(self._handle)
        
        @gddfull.setter
        def gddfull(self, gddfull):
            _supy_driver.f90wrap_lai_prm__set__gddfull(self._handle, gddfull)
        
        @property
        def basete(self):
            """
            Element basete ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 86
            
            """
            return _supy_driver.f90wrap_lai_prm__get__basete(self._handle)
        
        @basete.setter
        def basete(self, basete):
            _supy_driver.f90wrap_lai_prm__set__basete(self._handle, basete)
        
        @property
        def sddfull(self):
            """
            Element sddfull ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 87
            
            """
            return _supy_driver.f90wrap_lai_prm__get__sddfull(self._handle)
        
        @sddfull.setter
        def sddfull(self, sddfull):
            _supy_driver.f90wrap_lai_prm__set__sddfull(self._handle, sddfull)
        
        @property
        def laimin(self):
            """
            Element laimin ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 88
            
            """
            return _supy_driver.f90wrap_lai_prm__get__laimin(self._handle)
        
        @laimin.setter
        def laimin(self, laimin):
            _supy_driver.f90wrap_lai_prm__set__laimin(self._handle, laimin)
        
        @property
        def laimax(self):
            """
            Element laimax ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 89
            
            """
            return _supy_driver.f90wrap_lai_prm__get__laimax(self._handle)
        
        @laimax.setter
        def laimax(self, laimax):
            _supy_driver.f90wrap_lai_prm__set__laimax(self._handle, laimax)
        
        @property
        def laipower(self):
            """
            Element laipower ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 90
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_lai_prm__array__laipower(self._handle)
            if array_handle in self._arrays:
                laipower = self._arrays[array_handle]
            else:
                laipower = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_lai_prm__array__laipower)
                self._arrays[array_handle] = laipower
            return laipower
        
        @laipower.setter
        def laipower(self, laipower):
            self.laipower[...] = laipower
        
        @property
        def laitype(self):
            """
            Element laitype ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 91
            
            """
            return _supy_driver.f90wrap_lai_prm__get__laitype(self._handle)
        
        @laitype.setter
        def laitype(self, laitype):
            _supy_driver.f90wrap_lai_prm__set__laitype(self._handle, laitype)
        
        def __str__(self):
            ret = ['<lai_prm>{\n']
            ret.append('    baset : ')
            ret.append(repr(self.baset))
            ret.append(',\n    gddfull : ')
            ret.append(repr(self.gddfull))
            ret.append(',\n    basete : ')
            ret.append(repr(self.basete))
            ret.append(',\n    sddfull : ')
            ret.append(repr(self.sddfull))
            ret.append(',\n    laimin : ')
            ret.append(repr(self.laimin))
            ret.append(',\n    laimax : ')
            ret.append(repr(self.laimax))
            ret.append(',\n    laipower : ')
            ret.append(repr(self.laipower))
            ret.append(',\n    laitype : ')
            ret.append(repr(self.laitype))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.OHM_COEF_LC")
    class OHM_COEF_LC(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_coef_lc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 93-97
        
        """
        def __init__(self, handle=None):
            """
            self = Ohm_Coef_Lc()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 93-97
            
            
            Returns
            -------
            this : Ohm_Coef_Lc
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_coef_lc
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__ohm_coef_lc_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_Coef_Lc
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 93-97
            
            Parameters
            ----------
            this : Ohm_Coef_Lc
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_coef_lc
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__ohm_coef_lc_finalise(this=self._handle)
        
        @property
        def summer_dry(self):
            """
            Element summer_dry ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 94
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__summer_dry(self._handle)
        
        @summer_dry.setter
        def summer_dry(self, summer_dry):
            _supy_driver.f90wrap_ohm_coef_lc__set__summer_dry(self._handle, summer_dry)
        
        @property
        def summer_wet(self):
            """
            Element summer_wet ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 95
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__summer_wet(self._handle)
        
        @summer_wet.setter
        def summer_wet(self, summer_wet):
            _supy_driver.f90wrap_ohm_coef_lc__set__summer_wet(self._handle, summer_wet)
        
        @property
        def winter_dry(self):
            """
            Element winter_dry ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 96
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__winter_dry(self._handle)
        
        @winter_dry.setter
        def winter_dry(self, winter_dry):
            _supy_driver.f90wrap_ohm_coef_lc__set__winter_dry(self._handle, winter_dry)
        
        @property
        def winter_wet(self):
            """
            Element winter_wet ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 97
            
            """
            return _supy_driver.f90wrap_ohm_coef_lc__get__winter_wet(self._handle)
        
        @winter_wet.setter
        def winter_wet(self, winter_wet):
            _supy_driver.f90wrap_ohm_coef_lc__set__winter_wet(self._handle, winter_wet)
        
        def __str__(self):
            ret = ['<ohm_coef_lc>{\n']
            ret.append('    summer_dry : ')
            ret.append(repr(self.summer_dry))
            ret.append(',\n    summer_wet : ')
            ret.append(repr(self.summer_wet))
            ret.append(',\n    winter_dry : ')
            ret.append(repr(self.winter_dry))
            ret.append(',\n    winter_wet : ')
            ret.append(repr(self.winter_wet))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.OHM_PRM")
    class OHM_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 99-105
        
        """
        def __init__(self, handle=None):
            """
            self = Ohm_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 99-105
            
            
            Returns
            -------
            this : Ohm_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__ohm_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 99-105
            
            Parameters
            ----------
            this : Ohm_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__ohm_prm_finalise(this=self._handle)
        
        @property
        def chanohm(self):
            """
            Element chanohm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 100
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__chanohm(self._handle)
        
        @chanohm.setter
        def chanohm(self, chanohm):
            _supy_driver.f90wrap_ohm_prm__set__chanohm(self._handle, chanohm)
        
        @property
        def cpanohm(self):
            """
            Element cpanohm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 101
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__cpanohm(self._handle)
        
        @cpanohm.setter
        def cpanohm(self, cpanohm):
            _supy_driver.f90wrap_ohm_prm__set__cpanohm(self._handle, cpanohm)
        
        @property
        def kkanohm(self):
            """
            Element kkanohm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 102
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__kkanohm(self._handle)
        
        @kkanohm.setter
        def kkanohm(self, kkanohm):
            _supy_driver.f90wrap_ohm_prm__set__kkanohm(self._handle, kkanohm)
        
        @property
        def ohm_threshsw(self):
            """
            Element ohm_threshsw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 103
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__ohm_threshsw(self._handle)
        
        @ohm_threshsw.setter
        def ohm_threshsw(self, ohm_threshsw):
            _supy_driver.f90wrap_ohm_prm__set__ohm_threshsw(self._handle, ohm_threshsw)
        
        @property
        def ohm_threshwd(self):
            """
            Element ohm_threshwd ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 104
            
            """
            return _supy_driver.f90wrap_ohm_prm__get__ohm_threshwd(self._handle)
        
        @ohm_threshwd.setter
        def ohm_threshwd(self, ohm_threshwd):
            _supy_driver.f90wrap_ohm_prm__set__ohm_threshwd(self._handle, ohm_threshwd)
        
        def init_array_ohm_coef_lc(self):
            self.ohm_coef_lc = f90wrap.runtime.FortranDerivedTypeArray(self,
                                            _supy_driver.f90wrap_ohm_prm__array_getitem__ohm_coef_lc,
                                            _supy_driver.f90wrap_ohm_prm__array_setitem__ohm_coef_lc,
                                            _supy_driver.f90wrap_ohm_prm__array_len__ohm_coef_lc,
                                            """
            Element ohm_coef_lc ftype=type(ohm_coef_lc) pytype=Ohm_Coef_Lc
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 105
            
            """, Suews_Def_Dts.OHM_COEF_LC)
            return self.ohm_coef_lc
        
        def __str__(self):
            ret = ['<ohm_prm>{\n']
            ret.append('    chanohm : ')
            ret.append(repr(self.chanohm))
            ret.append(',\n    cpanohm : ')
            ret.append(repr(self.cpanohm))
            ret.append(',\n    kkanohm : ')
            ret.append(repr(self.kkanohm))
            ret.append(',\n    ohm_threshsw : ')
            ret.append(repr(self.ohm_threshsw))
            ret.append(',\n    ohm_threshwd : ')
            ret.append(repr(self.ohm_threshwd))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = [init_array_ohm_coef_lc]
        
    
    @f90wrap.runtime.register_class("supy_driver.SOIL_PRM")
    class SOIL_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=soil_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 107-110
        
        """
        def __init__(self, handle=None):
            """
            self = Soil_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 107-110
            
            
            Returns
            -------
            this : Soil_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for soil_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__soil_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 107-110
            
            Parameters
            ----------
            this : Soil_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for soil_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__soil_prm_finalise(this=self._handle)
        
        @property
        def soildepth(self):
            """
            Element soildepth ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 108
            
            """
            return _supy_driver.f90wrap_soil_prm__get__soildepth(self._handle)
        
        @soildepth.setter
        def soildepth(self, soildepth):
            _supy_driver.f90wrap_soil_prm__set__soildepth(self._handle, soildepth)
        
        @property
        def soilstorecap(self):
            """
            Element soilstorecap ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 109
            
            """
            return _supy_driver.f90wrap_soil_prm__get__soilstorecap(self._handle)
        
        @soilstorecap.setter
        def soilstorecap(self, soilstorecap):
            _supy_driver.f90wrap_soil_prm__set__soilstorecap(self._handle, soilstorecap)
        
        @property
        def sathydraulicconduct(self):
            """
            Element sathydraulicconduct ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 110
            
            """
            return _supy_driver.f90wrap_soil_prm__get__sathydraulicconduct(self._handle)
        
        @sathydraulicconduct.setter
        def sathydraulicconduct(self, sathydraulicconduct):
            _supy_driver.f90wrap_soil_prm__set__sathydraulicconduct(self._handle, \
                sathydraulicconduct)
        
        def __str__(self):
            ret = ['<soil_prm>{\n']
            ret.append('    soildepth : ')
            ret.append(repr(self.soildepth))
            ret.append(',\n    soilstorecap : ')
            ret.append(repr(self.soilstorecap))
            ret.append(',\n    sathydraulicconduct : ')
            ret.append(repr(self.sathydraulicconduct))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.anthroHEAT_PRM")
    class anthroHEAT_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=anthroheat_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 112-137
        
        """
        def __init__(self, handle=None):
            """
            self = Anthroheat_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 112-137
            
            
            Returns
            -------
            this : Anthroheat_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for anthroheat_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__anthroheat_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Anthroheat_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 112-137
            
            Parameters
            ----------
            this : Anthroheat_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for anthroheat_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__anthroheat_prm_finalise(this=self._handle)
        
        @property
        def qf0_beu_working(self):
            """
            Element qf0_beu_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 113
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf0_beu_working(self._handle)
        
        @qf0_beu_working.setter
        def qf0_beu_working(self, qf0_beu_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf0_beu_working(self._handle, \
                qf0_beu_working)
        
        @property
        def qf0_beu_holiday(self):
            """
            Element qf0_beu_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 114
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf0_beu_holiday(self._handle)
        
        @qf0_beu_holiday.setter
        def qf0_beu_holiday(self, qf0_beu_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf0_beu_holiday(self._handle, \
                qf0_beu_holiday)
        
        @property
        def qf_a_working(self):
            """
            Element qf_a_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 115
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_a_working(self._handle)
        
        @qf_a_working.setter
        def qf_a_working(self, qf_a_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_a_working(self._handle, \
                qf_a_working)
        
        @property
        def qf_a_holiday(self):
            """
            Element qf_a_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 116
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_a_holiday(self._handle)
        
        @qf_a_holiday.setter
        def qf_a_holiday(self, qf_a_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_a_holiday(self._handle, \
                qf_a_holiday)
        
        @property
        def qf_b_working(self):
            """
            Element qf_b_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 117
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_b_working(self._handle)
        
        @qf_b_working.setter
        def qf_b_working(self, qf_b_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_b_working(self._handle, \
                qf_b_working)
        
        @property
        def qf_b_holiday(self):
            """
            Element qf_b_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 118
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_b_holiday(self._handle)
        
        @qf_b_holiday.setter
        def qf_b_holiday(self, qf_b_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_b_holiday(self._handle, \
                qf_b_holiday)
        
        @property
        def qf_c_working(self):
            """
            Element qf_c_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 119
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_c_working(self._handle)
        
        @qf_c_working.setter
        def qf_c_working(self, qf_c_working):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_c_working(self._handle, \
                qf_c_working)
        
        @property
        def qf_c_holiday(self):
            """
            Element qf_c_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 120
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__qf_c_holiday(self._handle)
        
        @qf_c_holiday.setter
        def qf_c_holiday(self, qf_c_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__qf_c_holiday(self._handle, \
                qf_c_holiday)
        
        @property
        def baset_cooling_working(self):
            """
            Element baset_cooling_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 121
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_cooling_working(self._handle)
        
        @baset_cooling_working.setter
        def baset_cooling_working(self, baset_cooling_working):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_cooling_working(self._handle, \
                baset_cooling_working)
        
        @property
        def baset_cooling_holiday(self):
            """
            Element baset_cooling_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 122
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_cooling_holiday(self._handle)
        
        @baset_cooling_holiday.setter
        def baset_cooling_holiday(self, baset_cooling_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_cooling_holiday(self._handle, \
                baset_cooling_holiday)
        
        @property
        def baset_heating_working(self):
            """
            Element baset_heating_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 123
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_heating_working(self._handle)
        
        @baset_heating_working.setter
        def baset_heating_working(self, baset_heating_working):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_heating_working(self._handle, \
                baset_heating_working)
        
        @property
        def baset_heating_holiday(self):
            """
            Element baset_heating_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 124
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__baset_heating_holiday(self._handle)
        
        @baset_heating_holiday.setter
        def baset_heating_holiday(self, baset_heating_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__baset_heating_holiday(self._handle, \
                baset_heating_holiday)
        
        @property
        def ah_min_working(self):
            """
            Element ah_min_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 125
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__ah_min_working(self._handle)
        
        @ah_min_working.setter
        def ah_min_working(self, ah_min_working):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_min_working(self._handle, \
                ah_min_working)
        
        @property
        def ah_min_holiday(self):
            """
            Element ah_min_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 126
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__ah_min_holiday(self._handle)
        
        @ah_min_holiday.setter
        def ah_min_holiday(self, ah_min_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_min_holiday(self._handle, \
                ah_min_holiday)
        
        @property
        def ah_slope_cooling_working(self):
            """
            Element ah_slope_cooling_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 127
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_cooling_working(self._handle)
        
        @ah_slope_cooling_working.setter
        def ah_slope_cooling_working(self, ah_slope_cooling_working):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_cooling_working(self._handle, \
                ah_slope_cooling_working)
        
        @property
        def ah_slope_cooling_holiday(self):
            """
            Element ah_slope_cooling_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 128
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_cooling_holiday(self._handle)
        
        @ah_slope_cooling_holiday.setter
        def ah_slope_cooling_holiday(self, ah_slope_cooling_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_cooling_holiday(self._handle, \
                ah_slope_cooling_holiday)
        
        @property
        def ah_slope_heating_working(self):
            """
            Element ah_slope_heating_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 129
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_heating_working(self._handle)
        
        @ah_slope_heating_working.setter
        def ah_slope_heating_working(self, ah_slope_heating_working):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_heating_working(self._handle, \
                ah_slope_heating_working)
        
        @property
        def ah_slope_heating_holiday(self):
            """
            Element ah_slope_heating_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 130
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__ah_slope_heating_holiday(self._handle)
        
        @ah_slope_heating_holiday.setter
        def ah_slope_heating_holiday(self, ah_slope_heating_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__ah_slope_heating_holiday(self._handle, \
                ah_slope_heating_holiday)
        
        @property
        def ahprof_24hr_working(self):
            """
            Element ahprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 131
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                ahprof_24hr_working = self._arrays[array_handle]
            else:
                ahprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_working)
                self._arrays[array_handle] = ahprof_24hr_working
            return ahprof_24hr_working
        
        @ahprof_24hr_working.setter
        def ahprof_24hr_working(self, ahprof_24hr_working):
            self.ahprof_24hr_working[...] = ahprof_24hr_working
        
        @property
        def ahprof_24hr_holiday(self):
            """
            Element ahprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 132
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                ahprof_24hr_holiday = self._arrays[array_handle]
            else:
                ahprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__ahprof_24hr_holiday)
                self._arrays[array_handle] = ahprof_24hr_holiday
            return ahprof_24hr_holiday
        
        @ahprof_24hr_holiday.setter
        def ahprof_24hr_holiday(self, ahprof_24hr_holiday):
            self.ahprof_24hr_holiday[...] = ahprof_24hr_holiday
        
        @property
        def popdensdaytime_working(self):
            """
            Element popdensdaytime_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 133
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__popdensdaytime_working(self._handle)
        
        @popdensdaytime_working.setter
        def popdensdaytime_working(self, popdensdaytime_working):
            _supy_driver.f90wrap_anthroheat_prm__set__popdensdaytime_working(self._handle, \
                popdensdaytime_working)
        
        @property
        def popdensdaytime_holiday(self):
            """
            Element popdensdaytime_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 134
            
            """
            return \
                _supy_driver.f90wrap_anthroheat_prm__get__popdensdaytime_holiday(self._handle)
        
        @popdensdaytime_holiday.setter
        def popdensdaytime_holiday(self, popdensdaytime_holiday):
            _supy_driver.f90wrap_anthroheat_prm__set__popdensdaytime_holiday(self._handle, \
                popdensdaytime_holiday)
        
        @property
        def popdensnighttime(self):
            """
            Element popdensnighttime ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 135
            
            """
            return _supy_driver.f90wrap_anthroheat_prm__get__popdensnighttime(self._handle)
        
        @popdensnighttime.setter
        def popdensnighttime(self, popdensnighttime):
            _supy_driver.f90wrap_anthroheat_prm__set__popdensnighttime(self._handle, \
                popdensnighttime)
        
        @property
        def popprof_24hr_working(self):
            """
            Element popprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 136
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                popprof_24hr_working = self._arrays[array_handle]
            else:
                popprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_working)
                self._arrays[array_handle] = popprof_24hr_working
            return popprof_24hr_working
        
        @popprof_24hr_working.setter
        def popprof_24hr_working(self, popprof_24hr_working):
            self.popprof_24hr_working[...] = popprof_24hr_working
        
        @property
        def popprof_24hr_holiday(self):
            """
            Element popprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 137
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                popprof_24hr_holiday = self._arrays[array_handle]
            else:
                popprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroheat_prm__array__popprof_24hr_holiday)
                self._arrays[array_handle] = popprof_24hr_holiday
            return popprof_24hr_holiday
        
        @popprof_24hr_holiday.setter
        def popprof_24hr_holiday(self, popprof_24hr_holiday):
            self.popprof_24hr_holiday[...] = popprof_24hr_holiday
        
        def __str__(self):
            ret = ['<anthroheat_prm>{\n']
            ret.append('    qf0_beu_working : ')
            ret.append(repr(self.qf0_beu_working))
            ret.append(',\n    qf0_beu_holiday : ')
            ret.append(repr(self.qf0_beu_holiday))
            ret.append(',\n    qf_a_working : ')
            ret.append(repr(self.qf_a_working))
            ret.append(',\n    qf_a_holiday : ')
            ret.append(repr(self.qf_a_holiday))
            ret.append(',\n    qf_b_working : ')
            ret.append(repr(self.qf_b_working))
            ret.append(',\n    qf_b_holiday : ')
            ret.append(repr(self.qf_b_holiday))
            ret.append(',\n    qf_c_working : ')
            ret.append(repr(self.qf_c_working))
            ret.append(',\n    qf_c_holiday : ')
            ret.append(repr(self.qf_c_holiday))
            ret.append(',\n    baset_cooling_working : ')
            ret.append(repr(self.baset_cooling_working))
            ret.append(',\n    baset_cooling_holiday : ')
            ret.append(repr(self.baset_cooling_holiday))
            ret.append(',\n    baset_heating_working : ')
            ret.append(repr(self.baset_heating_working))
            ret.append(',\n    baset_heating_holiday : ')
            ret.append(repr(self.baset_heating_holiday))
            ret.append(',\n    ah_min_working : ')
            ret.append(repr(self.ah_min_working))
            ret.append(',\n    ah_min_holiday : ')
            ret.append(repr(self.ah_min_holiday))
            ret.append(',\n    ah_slope_cooling_working : ')
            ret.append(repr(self.ah_slope_cooling_working))
            ret.append(',\n    ah_slope_cooling_holiday : ')
            ret.append(repr(self.ah_slope_cooling_holiday))
            ret.append(',\n    ah_slope_heating_working : ')
            ret.append(repr(self.ah_slope_heating_working))
            ret.append(',\n    ah_slope_heating_holiday : ')
            ret.append(repr(self.ah_slope_heating_holiday))
            ret.append(',\n    ahprof_24hr_working : ')
            ret.append(repr(self.ahprof_24hr_working))
            ret.append(',\n    ahprof_24hr_holiday : ')
            ret.append(repr(self.ahprof_24hr_holiday))
            ret.append(',\n    popdensdaytime_working : ')
            ret.append(repr(self.popdensdaytime_working))
            ret.append(',\n    popdensdaytime_holiday : ')
            ret.append(repr(self.popdensdaytime_holiday))
            ret.append(',\n    popdensnighttime : ')
            ret.append(repr(self.popdensnighttime))
            ret.append(',\n    popprof_24hr_working : ')
            ret.append(repr(self.popprof_24hr_working))
            ret.append(',\n    popprof_24hr_holiday : ')
            ret.append(repr(self.popprof_24hr_holiday))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.IRRIG_daywater")
    class IRRIG_daywater(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=irrig_daywater)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 139-154
        
        """
        def __init__(self, handle=None):
            """
            self = Irrig_Daywater()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 139-154
            
            
            Returns
            -------
            this : Irrig_Daywater
            	Object to be constructed
            
            
            Automatically generated constructor for irrig_daywater
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__irrig_daywater_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Irrig_Daywater
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 139-154
            
            Parameters
            ----------
            this : Irrig_Daywater
            	Object to be destructed
            
            
            Automatically generated destructor for irrig_daywater
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__irrig_daywater_finalise(this=self._handle)
        
        @property
        def monday_flag(self):
            """
            Element monday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 141
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__monday_flag(self._handle)
        
        @monday_flag.setter
        def monday_flag(self, monday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__monday_flag(self._handle, monday_flag)
        
        @property
        def monday_percent(self):
            """
            Element monday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 142
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__monday_percent(self._handle)
        
        @monday_percent.setter
        def monday_percent(self, monday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__monday_percent(self._handle, \
                monday_percent)
        
        @property
        def tuesday_flag(self):
            """
            Element tuesday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 143
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__tuesday_flag(self._handle)
        
        @tuesday_flag.setter
        def tuesday_flag(self, tuesday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__tuesday_flag(self._handle, \
                tuesday_flag)
        
        @property
        def tuesday_percent(self):
            """
            Element tuesday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 144
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__tuesday_percent(self._handle)
        
        @tuesday_percent.setter
        def tuesday_percent(self, tuesday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__tuesday_percent(self._handle, \
                tuesday_percent)
        
        @property
        def wednesday_flag(self):
            """
            Element wednesday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 145
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__wednesday_flag(self._handle)
        
        @wednesday_flag.setter
        def wednesday_flag(self, wednesday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__wednesday_flag(self._handle, \
                wednesday_flag)
        
        @property
        def wednesday_percent(self):
            """
            Element wednesday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 146
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__wednesday_percent(self._handle)
        
        @wednesday_percent.setter
        def wednesday_percent(self, wednesday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__wednesday_percent(self._handle, \
                wednesday_percent)
        
        @property
        def thursday_flag(self):
            """
            Element thursday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 147
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__thursday_flag(self._handle)
        
        @thursday_flag.setter
        def thursday_flag(self, thursday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__thursday_flag(self._handle, \
                thursday_flag)
        
        @property
        def thursday_percent(self):
            """
            Element thursday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 148
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__thursday_percent(self._handle)
        
        @thursday_percent.setter
        def thursday_percent(self, thursday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__thursday_percent(self._handle, \
                thursday_percent)
        
        @property
        def friday_flag(self):
            """
            Element friday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 149
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__friday_flag(self._handle)
        
        @friday_flag.setter
        def friday_flag(self, friday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__friday_flag(self._handle, friday_flag)
        
        @property
        def friday_percent(self):
            """
            Element friday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 150
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__friday_percent(self._handle)
        
        @friday_percent.setter
        def friday_percent(self, friday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__friday_percent(self._handle, \
                friday_percent)
        
        @property
        def saturday_flag(self):
            """
            Element saturday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 151
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__saturday_flag(self._handle)
        
        @saturday_flag.setter
        def saturday_flag(self, saturday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__saturday_flag(self._handle, \
                saturday_flag)
        
        @property
        def saturday_percent(self):
            """
            Element saturday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 152
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__saturday_percent(self._handle)
        
        @saturday_percent.setter
        def saturday_percent(self, saturday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__saturday_percent(self._handle, \
                saturday_percent)
        
        @property
        def sunday_flag(self):
            """
            Element sunday_flag ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 153
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__sunday_flag(self._handle)
        
        @sunday_flag.setter
        def sunday_flag(self, sunday_flag):
            _supy_driver.f90wrap_irrig_daywater__set__sunday_flag(self._handle, sunday_flag)
        
        @property
        def sunday_percent(self):
            """
            Element sunday_percent ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 154
            
            """
            return _supy_driver.f90wrap_irrig_daywater__get__sunday_percent(self._handle)
        
        @sunday_percent.setter
        def sunday_percent(self, sunday_percent):
            _supy_driver.f90wrap_irrig_daywater__set__sunday_percent(self._handle, \
                sunday_percent)
        
        def __str__(self):
            ret = ['<irrig_daywater>{\n']
            ret.append('    monday_flag : ')
            ret.append(repr(self.monday_flag))
            ret.append(',\n    monday_percent : ')
            ret.append(repr(self.monday_percent))
            ret.append(',\n    tuesday_flag : ')
            ret.append(repr(self.tuesday_flag))
            ret.append(',\n    tuesday_percent : ')
            ret.append(repr(self.tuesday_percent))
            ret.append(',\n    wednesday_flag : ')
            ret.append(repr(self.wednesday_flag))
            ret.append(',\n    wednesday_percent : ')
            ret.append(repr(self.wednesday_percent))
            ret.append(',\n    thursday_flag : ')
            ret.append(repr(self.thursday_flag))
            ret.append(',\n    thursday_percent : ')
            ret.append(repr(self.thursday_percent))
            ret.append(',\n    friday_flag : ')
            ret.append(repr(self.friday_flag))
            ret.append(',\n    friday_percent : ')
            ret.append(repr(self.friday_percent))
            ret.append(',\n    saturday_flag : ')
            ret.append(repr(self.saturday_flag))
            ret.append(',\n    saturday_percent : ')
            ret.append(repr(self.saturday_percent))
            ret.append(',\n    sunday_flag : ')
            ret.append(repr(self.sunday_flag))
            ret.append(',\n    sunday_percent : ')
            ret.append(repr(self.sunday_percent))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.IRRIGATION_PRM")
    class IRRIGATION_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=irrigation_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 156-168
        
        """
        def __init__(self, handle=None):
            """
            self = Irrigation_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 156-168
            
            
            Returns
            -------
            this : Irrigation_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for irrigation_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__irrigation_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Irrigation_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 156-168
            
            Parameters
            ----------
            this : Irrigation_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for irrigation_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__irrigation_prm_finalise(this=self._handle)
        
        @property
        def h_maintain(self):
            """
            Element h_maintain ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 157
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__h_maintain(self._handle)
        
        @h_maintain.setter
        def h_maintain(self, h_maintain):
            _supy_driver.f90wrap_irrigation_prm__set__h_maintain(self._handle, h_maintain)
        
        @property
        def faut(self):
            """
            Element faut ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 158
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__faut(self._handle)
        
        @faut.setter
        def faut(self, faut):
            _supy_driver.f90wrap_irrigation_prm__set__faut(self._handle, faut)
        
        @property
        def ie_a(self):
            """
            Element ie_a ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 159
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__ie_a(self._handle)
            if array_handle in self._arrays:
                ie_a = self._arrays[array_handle]
            else:
                ie_a = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__ie_a)
                self._arrays[array_handle] = ie_a
            return ie_a
        
        @ie_a.setter
        def ie_a(self, ie_a):
            self.ie_a[...] = ie_a
        
        @property
        def ie_m(self):
            """
            Element ie_m ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 160
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__ie_m(self._handle)
            if array_handle in self._arrays:
                ie_m = self._arrays[array_handle]
            else:
                ie_m = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__ie_m)
                self._arrays[array_handle] = ie_m
            return ie_m
        
        @ie_m.setter
        def ie_m(self, ie_m):
            self.ie_m[...] = ie_m
        
        @property
        def ie_start(self):
            """
            Element ie_start ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 161
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__ie_start(self._handle)
        
        @ie_start.setter
        def ie_start(self, ie_start):
            _supy_driver.f90wrap_irrigation_prm__set__ie_start(self._handle, ie_start)
        
        @property
        def ie_end(self):
            """
            Element ie_end ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 162
            
            """
            return _supy_driver.f90wrap_irrigation_prm__get__ie_end(self._handle)
        
        @ie_end.setter
        def ie_end(self, ie_end):
            _supy_driver.f90wrap_irrigation_prm__set__ie_end(self._handle, ie_end)
        
        @property
        def internalwateruse_h(self):
            """
            Element internalwateruse_h ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 163
            
            """
            return \
                _supy_driver.f90wrap_irrigation_prm__get__internalwateruse_h(self._handle)
        
        @internalwateruse_h.setter
        def internalwateruse_h(self, internalwateruse_h):
            _supy_driver.f90wrap_irrigation_prm__set__internalwateruse_h(self._handle, \
                internalwateruse_h)
        
        @property
        def irr_daywater(self):
            """
            Element irr_daywater ftype=type(irrig_daywater) pytype=Irrig_Daywater
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 164
            
            """
            irr_daywater_handle = \
                _supy_driver.f90wrap_irrigation_prm__get__irr_daywater(self._handle)
            if tuple(irr_daywater_handle) in self._objs:
                irr_daywater = self._objs[tuple(irr_daywater_handle)]
            else:
                irr_daywater = suews_def_dts.IRRIG_daywater.from_handle(irr_daywater_handle)
                self._objs[tuple(irr_daywater_handle)] = irr_daywater
            return irr_daywater
        
        @irr_daywater.setter
        def irr_daywater(self, irr_daywater):
            irr_daywater = irr_daywater._handle
            _supy_driver.f90wrap_irrigation_prm__set__irr_daywater(self._handle, \
                irr_daywater)
        
        @property
        def wuprofa_24hr_working(self):
            """
            Element wuprofa_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 165
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_working(self._handle)
            if array_handle in self._arrays:
                wuprofa_24hr_working = self._arrays[array_handle]
            else:
                wuprofa_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_working)
                self._arrays[array_handle] = wuprofa_24hr_working
            return wuprofa_24hr_working
        
        @wuprofa_24hr_working.setter
        def wuprofa_24hr_working(self, wuprofa_24hr_working):
            self.wuprofa_24hr_working[...] = wuprofa_24hr_working
        
        @property
        def wuprofa_24hr_holiday(self):
            """
            Element wuprofa_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 166
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                wuprofa_24hr_holiday = self._arrays[array_handle]
            else:
                wuprofa_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofa_24hr_holiday)
                self._arrays[array_handle] = wuprofa_24hr_holiday
            return wuprofa_24hr_holiday
        
        @wuprofa_24hr_holiday.setter
        def wuprofa_24hr_holiday(self, wuprofa_24hr_holiday):
            self.wuprofa_24hr_holiday[...] = wuprofa_24hr_holiday
        
        @property
        def wuprofm_24hr_working(self):
            """
            Element wuprofm_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 167
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_working(self._handle)
            if array_handle in self._arrays:
                wuprofm_24hr_working = self._arrays[array_handle]
            else:
                wuprofm_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_working)
                self._arrays[array_handle] = wuprofm_24hr_working
            return wuprofm_24hr_working
        
        @wuprofm_24hr_working.setter
        def wuprofm_24hr_working(self, wuprofm_24hr_working):
            self.wuprofm_24hr_working[...] = wuprofm_24hr_working
        
        @property
        def wuprofm_24hr_holiday(self):
            """
            Element wuprofm_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 168
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                wuprofm_24hr_holiday = self._arrays[array_handle]
            else:
                wuprofm_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_irrigation_prm__array__wuprofm_24hr_holiday)
                self._arrays[array_handle] = wuprofm_24hr_holiday
            return wuprofm_24hr_holiday
        
        @wuprofm_24hr_holiday.setter
        def wuprofm_24hr_holiday(self, wuprofm_24hr_holiday):
            self.wuprofm_24hr_holiday[...] = wuprofm_24hr_holiday
        
        def __str__(self):
            ret = ['<irrigation_prm>{\n']
            ret.append('    h_maintain : ')
            ret.append(repr(self.h_maintain))
            ret.append(',\n    faut : ')
            ret.append(repr(self.faut))
            ret.append(',\n    ie_a : ')
            ret.append(repr(self.ie_a))
            ret.append(',\n    ie_m : ')
            ret.append(repr(self.ie_m))
            ret.append(',\n    ie_start : ')
            ret.append(repr(self.ie_start))
            ret.append(',\n    ie_end : ')
            ret.append(repr(self.ie_end))
            ret.append(',\n    internalwateruse_h : ')
            ret.append(repr(self.internalwateruse_h))
            ret.append(',\n    irr_daywater : ')
            ret.append(repr(self.irr_daywater))
            ret.append(',\n    wuprofa_24hr_working : ')
            ret.append(repr(self.wuprofa_24hr_working))
            ret.append(',\n    wuprofa_24hr_holiday : ')
            ret.append(repr(self.wuprofa_24hr_holiday))
            ret.append(',\n    wuprofm_24hr_working : ')
            ret.append(repr(self.wuprofm_24hr_working))
            ret.append(',\n    wuprofm_24hr_holiday : ')
            ret.append(repr(self.wuprofm_24hr_holiday))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.anthroEMIS_PRM")
    class anthroEMIS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=anthroemis_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 170-189
        
        """
        def __init__(self, handle=None):
            """
            self = Anthroemis_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 170-189
            
            
            Returns
            -------
            this : Anthroemis_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for anthroemis_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__anthroemis_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Anthroemis_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 170-189
            
            Parameters
            ----------
            this : Anthroemis_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for anthroemis_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__anthroemis_prm_finalise(this=self._handle)
        
        @property
        def startdls(self):
            """
            Element startdls ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 171
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__startdls(self._handle)
        
        @startdls.setter
        def startdls(self, startdls):
            _supy_driver.f90wrap_anthroemis_prm__set__startdls(self._handle, startdls)
        
        @property
        def enddls(self):
            """
            Element enddls ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 172
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__enddls(self._handle)
        
        @enddls.setter
        def enddls(self, enddls):
            _supy_driver.f90wrap_anthroemis_prm__set__enddls(self._handle, enddls)
        
        @property
        def anthroheat(self):
            """
            Element anthroheat ftype=type(anthroheat_prm) pytype=Anthroheat_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 173
            
            """
            anthroheat_handle = \
                _supy_driver.f90wrap_anthroemis_prm__get__anthroheat(self._handle)
            if tuple(anthroheat_handle) in self._objs:
                anthroheat = self._objs[tuple(anthroheat_handle)]
            else:
                anthroheat = suews_def_dts.anthroHEAT_PRM.from_handle(anthroheat_handle)
                self._objs[tuple(anthroheat_handle)] = anthroheat
            return anthroheat
        
        @anthroheat.setter
        def anthroheat(self, anthroheat):
            anthroheat = anthroheat._handle
            _supy_driver.f90wrap_anthroemis_prm__set__anthroheat(self._handle, anthroheat)
        
        @property
        def ef_umolco2perj(self):
            """
            Element ef_umolco2perj ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 174
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__ef_umolco2perj(self._handle)
        
        @ef_umolco2perj.setter
        def ef_umolco2perj(self, ef_umolco2perj):
            _supy_driver.f90wrap_anthroemis_prm__set__ef_umolco2perj(self._handle, \
                ef_umolco2perj)
        
        @property
        def enef_v_jkm(self):
            """
            Element enef_v_jkm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 175
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__enef_v_jkm(self._handle)
        
        @enef_v_jkm.setter
        def enef_v_jkm(self, enef_v_jkm):
            _supy_driver.f90wrap_anthroemis_prm__set__enef_v_jkm(self._handle, enef_v_jkm)
        
        @property
        def frfossilfuel_heat(self):
            """
            Element frfossilfuel_heat ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 176
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__frfossilfuel_heat(self._handle)
        
        @frfossilfuel_heat.setter
        def frfossilfuel_heat(self, frfossilfuel_heat):
            _supy_driver.f90wrap_anthroemis_prm__set__frfossilfuel_heat(self._handle, \
                frfossilfuel_heat)
        
        @property
        def frfossilfuel_nonheat(self):
            """
            Element frfossilfuel_nonheat ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 177
            
            """
            return \
                _supy_driver.f90wrap_anthroemis_prm__get__frfossilfuel_nonheat(self._handle)
        
        @frfossilfuel_nonheat.setter
        def frfossilfuel_nonheat(self, frfossilfuel_nonheat):
            _supy_driver.f90wrap_anthroemis_prm__set__frfossilfuel_nonheat(self._handle, \
                frfossilfuel_nonheat)
        
        @property
        def fcef_v_kgkm(self):
            """
            Element fcef_v_kgkm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 178
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__fcef_v_kgkm(self._handle)
            if array_handle in self._arrays:
                fcef_v_kgkm = self._arrays[array_handle]
            else:
                fcef_v_kgkm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__fcef_v_kgkm)
                self._arrays[array_handle] = fcef_v_kgkm
            return fcef_v_kgkm
        
        @fcef_v_kgkm.setter
        def fcef_v_kgkm(self, fcef_v_kgkm):
            self.fcef_v_kgkm[...] = fcef_v_kgkm
        
        @property
        def humactivity_24hr_working(self):
            """
            Element humactivity_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 179
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_working(self._handle)
            if array_handle in self._arrays:
                humactivity_24hr_working = self._arrays[array_handle]
            else:
                humactivity_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_working)
                self._arrays[array_handle] = humactivity_24hr_working
            return humactivity_24hr_working
        
        @humactivity_24hr_working.setter
        def humactivity_24hr_working(self, humactivity_24hr_working):
            self.humactivity_24hr_working[...] = humactivity_24hr_working
        
        @property
        def humactivity_24hr_holiday(self):
            """
            Element humactivity_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 180
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                humactivity_24hr_holiday = self._arrays[array_handle]
            else:
                humactivity_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__humactivity_24hr_holiday)
                self._arrays[array_handle] = humactivity_24hr_holiday
            return humactivity_24hr_holiday
        
        @humactivity_24hr_holiday.setter
        def humactivity_24hr_holiday(self, humactivity_24hr_holiday):
            self.humactivity_24hr_holiday[...] = humactivity_24hr_holiday
        
        @property
        def maxfcmetab(self):
            """
            Element maxfcmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 181
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__maxfcmetab(self._handle)
        
        @maxfcmetab.setter
        def maxfcmetab(self, maxfcmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__maxfcmetab(self._handle, maxfcmetab)
        
        @property
        def maxqfmetab(self):
            """
            Element maxqfmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 182
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__maxqfmetab(self._handle)
        
        @maxqfmetab.setter
        def maxqfmetab(self, maxqfmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__maxqfmetab(self._handle, maxqfmetab)
        
        @property
        def minfcmetab(self):
            """
            Element minfcmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 183
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__minfcmetab(self._handle)
        
        @minfcmetab.setter
        def minfcmetab(self, minfcmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__minfcmetab(self._handle, minfcmetab)
        
        @property
        def minqfmetab(self):
            """
            Element minqfmetab ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 184
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__minqfmetab(self._handle)
        
        @minqfmetab.setter
        def minqfmetab(self, minqfmetab):
            _supy_driver.f90wrap_anthroemis_prm__set__minqfmetab(self._handle, minqfmetab)
        
        @property
        def trafficrate_working(self):
            """
            Element trafficrate_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 185
            
            """
            return \
                _supy_driver.f90wrap_anthroemis_prm__get__trafficrate_working(self._handle)
        
        @trafficrate_working.setter
        def trafficrate_working(self, trafficrate_working):
            _supy_driver.f90wrap_anthroemis_prm__set__trafficrate_working(self._handle, \
                trafficrate_working)
        
        @property
        def trafficrate_holiday(self):
            """
            Element trafficrate_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 186
            
            """
            return \
                _supy_driver.f90wrap_anthroemis_prm__get__trafficrate_holiday(self._handle)
        
        @trafficrate_holiday.setter
        def trafficrate_holiday(self, trafficrate_holiday):
            _supy_driver.f90wrap_anthroemis_prm__set__trafficrate_holiday(self._handle, \
                trafficrate_holiday)
        
        @property
        def trafficunits(self):
            """
            Element trafficunits ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 187
            
            """
            return _supy_driver.f90wrap_anthroemis_prm__get__trafficunits(self._handle)
        
        @trafficunits.setter
        def trafficunits(self, trafficunits):
            _supy_driver.f90wrap_anthroemis_prm__set__trafficunits(self._handle, \
                trafficunits)
        
        @property
        def traffprof_24hr_working(self):
            """
            Element traffprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 188
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                traffprof_24hr_working = self._arrays[array_handle]
            else:
                traffprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_working)
                self._arrays[array_handle] = traffprof_24hr_working
            return traffprof_24hr_working
        
        @traffprof_24hr_working.setter
        def traffprof_24hr_working(self, traffprof_24hr_working):
            self.traffprof_24hr_working[...] = traffprof_24hr_working
        
        @property
        def traffprof_24hr_holiday(self):
            """
            Element traffprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 189
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                traffprof_24hr_holiday = self._arrays[array_handle]
            else:
                traffprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_prm__array__traffprof_24hr_holiday)
                self._arrays[array_handle] = traffprof_24hr_holiday
            return traffprof_24hr_holiday
        
        @traffprof_24hr_holiday.setter
        def traffprof_24hr_holiday(self, traffprof_24hr_holiday):
            self.traffprof_24hr_holiday[...] = traffprof_24hr_holiday
        
        def __str__(self):
            ret = ['<anthroemis_prm>{\n']
            ret.append('    startdls : ')
            ret.append(repr(self.startdls))
            ret.append(',\n    enddls : ')
            ret.append(repr(self.enddls))
            ret.append(',\n    anthroheat : ')
            ret.append(repr(self.anthroheat))
            ret.append(',\n    ef_umolco2perj : ')
            ret.append(repr(self.ef_umolco2perj))
            ret.append(',\n    enef_v_jkm : ')
            ret.append(repr(self.enef_v_jkm))
            ret.append(',\n    frfossilfuel_heat : ')
            ret.append(repr(self.frfossilfuel_heat))
            ret.append(',\n    frfossilfuel_nonheat : ')
            ret.append(repr(self.frfossilfuel_nonheat))
            ret.append(',\n    fcef_v_kgkm : ')
            ret.append(repr(self.fcef_v_kgkm))
            ret.append(',\n    humactivity_24hr_working : ')
            ret.append(repr(self.humactivity_24hr_working))
            ret.append(',\n    humactivity_24hr_holiday : ')
            ret.append(repr(self.humactivity_24hr_holiday))
            ret.append(',\n    maxfcmetab : ')
            ret.append(repr(self.maxfcmetab))
            ret.append(',\n    maxqfmetab : ')
            ret.append(repr(self.maxqfmetab))
            ret.append(',\n    minfcmetab : ')
            ret.append(repr(self.minfcmetab))
            ret.append(',\n    minqfmetab : ')
            ret.append(repr(self.minqfmetab))
            ret.append(',\n    trafficrate_working : ')
            ret.append(repr(self.trafficrate_working))
            ret.append(',\n    trafficrate_holiday : ')
            ret.append(repr(self.trafficrate_holiday))
            ret.append(',\n    trafficunits : ')
            ret.append(repr(self.trafficunits))
            ret.append(',\n    traffprof_24hr_working : ')
            ret.append(repr(self.traffprof_24hr_working))
            ret.append(',\n    traffprof_24hr_holiday : ')
            ret.append(repr(self.traffprof_24hr_holiday))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SNOW_PRM")
    class SNOW_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=snow_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 191-210
        
        """
        def __init__(self, handle=None):
            """
            self = Snow_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 191-210
            
            
            Returns
            -------
            this : Snow_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for snow_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__snow_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Snow_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 191-210
            
            Parameters
            ----------
            this : Snow_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for snow_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__snow_prm_finalise(this=self._handle)
        
        @property
        def crwmax(self):
            """
            Element crwmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 192
            
            """
            return _supy_driver.f90wrap_snow_prm__get__crwmax(self._handle)
        
        @crwmax.setter
        def crwmax(self, crwmax):
            _supy_driver.f90wrap_snow_prm__set__crwmax(self._handle, crwmax)
        
        @property
        def crwmin(self):
            """
            Element crwmin ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 193
            
            """
            return _supy_driver.f90wrap_snow_prm__get__crwmin(self._handle)
        
        @crwmin.setter
        def crwmin(self, crwmin):
            _supy_driver.f90wrap_snow_prm__set__crwmin(self._handle, crwmin)
        
        @property
        def narp_emis_snow(self):
            """
            Element narp_emis_snow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 194
            
            """
            return _supy_driver.f90wrap_snow_prm__get__narp_emis_snow(self._handle)
        
        @narp_emis_snow.setter
        def narp_emis_snow(self, narp_emis_snow):
            _supy_driver.f90wrap_snow_prm__set__narp_emis_snow(self._handle, narp_emis_snow)
        
        @property
        def preciplimit(self):
            """
            Element preciplimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 195
            
            """
            return _supy_driver.f90wrap_snow_prm__get__preciplimit(self._handle)
        
        @preciplimit.setter
        def preciplimit(self, preciplimit):
            _supy_driver.f90wrap_snow_prm__set__preciplimit(self._handle, preciplimit)
        
        @property
        def preciplimitalb(self):
            """
            Element preciplimitalb ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 196
            
            """
            return _supy_driver.f90wrap_snow_prm__get__preciplimitalb(self._handle)
        
        @preciplimitalb.setter
        def preciplimitalb(self, preciplimitalb):
            _supy_driver.f90wrap_snow_prm__set__preciplimitalb(self._handle, preciplimitalb)
        
        @property
        def snowalbmax(self):
            """
            Element snowalbmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 197
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowalbmax(self._handle)
        
        @snowalbmax.setter
        def snowalbmax(self, snowalbmax):
            _supy_driver.f90wrap_snow_prm__set__snowalbmax(self._handle, snowalbmax)
        
        @property
        def snowalbmin(self):
            """
            Element snowalbmin ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 198
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowalbmin(self._handle)
        
        @snowalbmin.setter
        def snowalbmin(self, snowalbmin):
            _supy_driver.f90wrap_snow_prm__set__snowalbmin(self._handle, snowalbmin)
        
        @property
        def snowdensmax(self):
            """
            Element snowdensmax ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 199
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowdensmax(self._handle)
        
        @snowdensmax.setter
        def snowdensmax(self, snowdensmax):
            _supy_driver.f90wrap_snow_prm__set__snowdensmax(self._handle, snowdensmax)
        
        @property
        def snowdensmin(self):
            """
            Element snowdensmin ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 200
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowdensmin(self._handle)
        
        @snowdensmin.setter
        def snowdensmin(self, snowdensmin):
            _supy_driver.f90wrap_snow_prm__set__snowdensmin(self._handle, snowdensmin)
        
        @property
        def snowlimbldg(self):
            """
            Element snowlimbldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 201
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowlimbldg(self._handle)
        
        @snowlimbldg.setter
        def snowlimbldg(self, snowlimbldg):
            _supy_driver.f90wrap_snow_prm__set__snowlimbldg(self._handle, snowlimbldg)
        
        @property
        def snowlimpaved(self):
            """
            Element snowlimpaved ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 202
            
            """
            return _supy_driver.f90wrap_snow_prm__get__snowlimpaved(self._handle)
        
        @snowlimpaved.setter
        def snowlimpaved(self, snowlimpaved):
            _supy_driver.f90wrap_snow_prm__set__snowlimpaved(self._handle, snowlimpaved)
        
        @property
        def snowpacklimit(self):
            """
            Element snowpacklimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 203
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_prm__array__snowpacklimit(self._handle)
            if array_handle in self._arrays:
                snowpacklimit = self._arrays[array_handle]
            else:
                snowpacklimit = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_prm__array__snowpacklimit)
                self._arrays[array_handle] = snowpacklimit
            return snowpacklimit
        
        @snowpacklimit.setter
        def snowpacklimit(self, snowpacklimit):
            self.snowpacklimit[...] = snowpacklimit
        
        @property
        def snowprof_24hr_working(self):
            """
            Element snowprof_24hr_working ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 204
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_working(self._handle)
            if array_handle in self._arrays:
                snowprof_24hr_working = self._arrays[array_handle]
            else:
                snowprof_24hr_working = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_working)
                self._arrays[array_handle] = snowprof_24hr_working
            return snowprof_24hr_working
        
        @snowprof_24hr_working.setter
        def snowprof_24hr_working(self, snowprof_24hr_working):
            self.snowprof_24hr_working[...] = snowprof_24hr_working
        
        @property
        def snowprof_24hr_holiday(self):
            """
            Element snowprof_24hr_holiday ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 205
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_holiday(self._handle)
            if array_handle in self._arrays:
                snowprof_24hr_holiday = self._arrays[array_handle]
            else:
                snowprof_24hr_holiday = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_prm__array__snowprof_24hr_holiday)
                self._arrays[array_handle] = snowprof_24hr_holiday
            return snowprof_24hr_holiday
        
        @snowprof_24hr_holiday.setter
        def snowprof_24hr_holiday(self, snowprof_24hr_holiday):
            self.snowprof_24hr_holiday[...] = snowprof_24hr_holiday
        
        @property
        def tau_a(self):
            """
            Element tau_a ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 206
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tau_a(self._handle)
        
        @tau_a.setter
        def tau_a(self, tau_a):
            _supy_driver.f90wrap_snow_prm__set__tau_a(self._handle, tau_a)
        
        @property
        def tau_f(self):
            """
            Element tau_f ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 207
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tau_f(self._handle)
        
        @tau_f.setter
        def tau_f(self, tau_f):
            _supy_driver.f90wrap_snow_prm__set__tau_f(self._handle, tau_f)
        
        @property
        def tau_r(self):
            """
            Element tau_r ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 208
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tau_r(self._handle)
        
        @tau_r.setter
        def tau_r(self, tau_r):
            _supy_driver.f90wrap_snow_prm__set__tau_r(self._handle, tau_r)
        
        @property
        def tempmeltfact(self):
            """
            Element tempmeltfact ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 209
            
            """
            return _supy_driver.f90wrap_snow_prm__get__tempmeltfact(self._handle)
        
        @tempmeltfact.setter
        def tempmeltfact(self, tempmeltfact):
            _supy_driver.f90wrap_snow_prm__set__tempmeltfact(self._handle, tempmeltfact)
        
        @property
        def radmeltfact(self):
            """
            Element radmeltfact ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 210
            
            """
            return _supy_driver.f90wrap_snow_prm__get__radmeltfact(self._handle)
        
        @radmeltfact.setter
        def radmeltfact(self, radmeltfact):
            _supy_driver.f90wrap_snow_prm__set__radmeltfact(self._handle, radmeltfact)
        
        def __str__(self):
            ret = ['<snow_prm>{\n']
            ret.append('    crwmax : ')
            ret.append(repr(self.crwmax))
            ret.append(',\n    crwmin : ')
            ret.append(repr(self.crwmin))
            ret.append(',\n    narp_emis_snow : ')
            ret.append(repr(self.narp_emis_snow))
            ret.append(',\n    preciplimit : ')
            ret.append(repr(self.preciplimit))
            ret.append(',\n    preciplimitalb : ')
            ret.append(repr(self.preciplimitalb))
            ret.append(',\n    snowalbmax : ')
            ret.append(repr(self.snowalbmax))
            ret.append(',\n    snowalbmin : ')
            ret.append(repr(self.snowalbmin))
            ret.append(',\n    snowdensmax : ')
            ret.append(repr(self.snowdensmax))
            ret.append(',\n    snowdensmin : ')
            ret.append(repr(self.snowdensmin))
            ret.append(',\n    snowlimbldg : ')
            ret.append(repr(self.snowlimbldg))
            ret.append(',\n    snowlimpaved : ')
            ret.append(repr(self.snowlimpaved))
            ret.append(',\n    snowpacklimit : ')
            ret.append(repr(self.snowpacklimit))
            ret.append(',\n    snowprof_24hr_working : ')
            ret.append(repr(self.snowprof_24hr_working))
            ret.append(',\n    snowprof_24hr_holiday : ')
            ret.append(repr(self.snowprof_24hr_holiday))
            ret.append(',\n    tau_a : ')
            ret.append(repr(self.tau_a))
            ret.append(',\n    tau_f : ')
            ret.append(repr(self.tau_f))
            ret.append(',\n    tau_r : ')
            ret.append(repr(self.tau_r))
            ret.append(',\n    tempmeltfact : ')
            ret.append(repr(self.tempmeltfact))
            ret.append(',\n    radmeltfact : ')
            ret.append(repr(self.radmeltfact))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SPARTACUS_PRM")
    class SPARTACUS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=spartacus_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 212-227
        
        """
        def __init__(self, handle=None):
            """
            self = Spartacus_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 212-227
            
            
            Returns
            -------
            this : Spartacus_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for spartacus_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__spartacus_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Spartacus_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 212-227
            
            Parameters
            ----------
            this : Spartacus_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for spartacus_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__spartacus_prm_finalise(this=self._handle)
        
        @property
        def air_ext_lw(self):
            """
            Element air_ext_lw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 213
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ext_lw(self._handle)
        
        @air_ext_lw.setter
        def air_ext_lw(self, air_ext_lw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ext_lw(self._handle, air_ext_lw)
        
        @property
        def air_ext_sw(self):
            """
            Element air_ext_sw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 214
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ext_sw(self._handle)
        
        @air_ext_sw.setter
        def air_ext_sw(self, air_ext_sw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ext_sw(self._handle, air_ext_sw)
        
        @property
        def air_ssa_lw(self):
            """
            Element air_ssa_lw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 215
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ssa_lw(self._handle)
        
        @air_ssa_lw.setter
        def air_ssa_lw(self, air_ssa_lw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ssa_lw(self._handle, air_ssa_lw)
        
        @property
        def air_ssa_sw(self):
            """
            Element air_ssa_sw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 216
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__air_ssa_sw(self._handle)
        
        @air_ssa_sw.setter
        def air_ssa_sw(self, air_ssa_sw):
            _supy_driver.f90wrap_spartacus_prm__set__air_ssa_sw(self._handle, air_ssa_sw)
        
        @property
        def height(self):
            """
            Element height ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 217
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_prm__array__height(self._handle)
            if array_handle in self._arrays:
                height = self._arrays[array_handle]
            else:
                height = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_prm__array__height)
                self._arrays[array_handle] = height
            return height
        
        @height.setter
        def height(self, height):
            self.height[...] = height
        
        @property
        def ground_albedo_dir_mult_fact(self):
            """
            Element ground_albedo_dir_mult_fact ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 218
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__ground_albedo_dir_mult_fact(self._handle)
        
        @ground_albedo_dir_mult_fact.setter
        def ground_albedo_dir_mult_fact(self, ground_albedo_dir_mult_fact):
            _supy_driver.f90wrap_spartacus_prm__set__ground_albedo_dir_mult_fact(self._handle, \
                ground_albedo_dir_mult_fact)
        
        @property
        def n_stream_lw_urban(self):
            """
            Element n_stream_lw_urban ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 219
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__n_stream_lw_urban(self._handle)
        
        @n_stream_lw_urban.setter
        def n_stream_lw_urban(self, n_stream_lw_urban):
            _supy_driver.f90wrap_spartacus_prm__set__n_stream_lw_urban(self._handle, \
                n_stream_lw_urban)
        
        @property
        def n_stream_sw_urban(self):
            """
            Element n_stream_sw_urban ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 220
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__n_stream_sw_urban(self._handle)
        
        @n_stream_sw_urban.setter
        def n_stream_sw_urban(self, n_stream_sw_urban):
            _supy_driver.f90wrap_spartacus_prm__set__n_stream_sw_urban(self._handle, \
                n_stream_sw_urban)
        
        @property
        def n_vegetation_region_urban(self):
            """
            Element n_vegetation_region_urban ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 221
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__n_vegetation_region_urban(self._handle)
        
        @n_vegetation_region_urban.setter
        def n_vegetation_region_urban(self, n_vegetation_region_urban):
            _supy_driver.f90wrap_spartacus_prm__set__n_vegetation_region_urban(self._handle, \
                n_vegetation_region_urban)
        
        @property
        def sw_dn_direct_frac(self):
            """
            Element sw_dn_direct_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 222
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__sw_dn_direct_frac(self._handle)
        
        @sw_dn_direct_frac.setter
        def sw_dn_direct_frac(self, sw_dn_direct_frac):
            _supy_driver.f90wrap_spartacus_prm__set__sw_dn_direct_frac(self._handle, \
                sw_dn_direct_frac)
        
        @property
        def use_sw_direct_albedo(self):
            """
            Element use_sw_direct_albedo ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 223
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__use_sw_direct_albedo(self._handle)
        
        @use_sw_direct_albedo.setter
        def use_sw_direct_albedo(self, use_sw_direct_albedo):
            _supy_driver.f90wrap_spartacus_prm__set__use_sw_direct_albedo(self._handle, \
                use_sw_direct_albedo)
        
        @property
        def veg_contact_fraction_const(self):
            """
            Element veg_contact_fraction_const ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 224
            
            """
            return \
                _supy_driver.f90wrap_spartacus_prm__get__veg_contact_fraction_const(self._handle)
        
        @veg_contact_fraction_const.setter
        def veg_contact_fraction_const(self, veg_contact_fraction_const):
            _supy_driver.f90wrap_spartacus_prm__set__veg_contact_fraction_const(self._handle, \
                veg_contact_fraction_const)
        
        @property
        def veg_fsd_const(self):
            """
            Element veg_fsd_const ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 225
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__veg_fsd_const(self._handle)
        
        @veg_fsd_const.setter
        def veg_fsd_const(self, veg_fsd_const):
            _supy_driver.f90wrap_spartacus_prm__set__veg_fsd_const(self._handle, \
                veg_fsd_const)
        
        @property
        def veg_ssa_lw(self):
            """
            Element veg_ssa_lw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 226
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__veg_ssa_lw(self._handle)
        
        @veg_ssa_lw.setter
        def veg_ssa_lw(self, veg_ssa_lw):
            _supy_driver.f90wrap_spartacus_prm__set__veg_ssa_lw(self._handle, veg_ssa_lw)
        
        @property
        def veg_ssa_sw(self):
            """
            Element veg_ssa_sw ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 227
            
            """
            return _supy_driver.f90wrap_spartacus_prm__get__veg_ssa_sw(self._handle)
        
        @veg_ssa_sw.setter
        def veg_ssa_sw(self, veg_ssa_sw):
            _supy_driver.f90wrap_spartacus_prm__set__veg_ssa_sw(self._handle, veg_ssa_sw)
        
        def __str__(self):
            ret = ['<spartacus_prm>{\n']
            ret.append('    air_ext_lw : ')
            ret.append(repr(self.air_ext_lw))
            ret.append(',\n    air_ext_sw : ')
            ret.append(repr(self.air_ext_sw))
            ret.append(',\n    air_ssa_lw : ')
            ret.append(repr(self.air_ssa_lw))
            ret.append(',\n    air_ssa_sw : ')
            ret.append(repr(self.air_ssa_sw))
            ret.append(',\n    height : ')
            ret.append(repr(self.height))
            ret.append(',\n    ground_albedo_dir_mult_fact : ')
            ret.append(repr(self.ground_albedo_dir_mult_fact))
            ret.append(',\n    n_stream_lw_urban : ')
            ret.append(repr(self.n_stream_lw_urban))
            ret.append(',\n    n_stream_sw_urban : ')
            ret.append(repr(self.n_stream_sw_urban))
            ret.append(',\n    n_vegetation_region_urban : ')
            ret.append(repr(self.n_vegetation_region_urban))
            ret.append(',\n    sw_dn_direct_frac : ')
            ret.append(repr(self.sw_dn_direct_frac))
            ret.append(',\n    use_sw_direct_albedo : ')
            ret.append(repr(self.use_sw_direct_albedo))
            ret.append(',\n    veg_contact_fraction_const : ')
            ret.append(repr(self.veg_contact_fraction_const))
            ret.append(',\n    veg_fsd_const : ')
            ret.append(repr(self.veg_fsd_const))
            ret.append(',\n    veg_ssa_lw : ')
            ret.append(repr(self.veg_ssa_lw))
            ret.append(',\n    veg_ssa_sw : ')
            ret.append(repr(self.veg_ssa_sw))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SPARTACUS_LAYER_PRM")
    class SPARTACUS_LAYER_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=spartacus_layer_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 229-242
        
        """
        def __init__(self, handle=None):
            """
            self = Spartacus_Layer_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 229-242
            
            
            Returns
            -------
            this : Spartacus_Layer_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for spartacus_layer_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__spartacus_layer_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Spartacus_Layer_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 229-242
            
            Parameters
            ----------
            this : Spartacus_Layer_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for spartacus_layer_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__spartacus_layer_prm_finalise(this=self._handle)
        
        def allocate(self, nlayer):
            """
            allocate__binding__spartacus_layer_prm(self, nlayer)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1135-1149
            
            Parameters
            ----------
            self : Spartacus_Layer_Prm
            nlayer : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__allocate__binding__spartacus_layer_prm(self=self._handle, \
                nlayer=nlayer)
        
        def deallocate(self):
            """
            deallocate__binding__spartacus_layer_prm(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1151-1163
            
            Parameters
            ----------
            self : Spartacus_Layer_Prm
            
            """
            _supy_driver.f90wrap_suews_def_dts__deallocate__binding__spartacus_layer_prm(self=self._handle)
        
        @property
        def building_frac(self):
            """
            Element building_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 230
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__building_frac(self._handle)
            if array_handle in self._arrays:
                building_frac = self._arrays[array_handle]
            else:
                building_frac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__building_frac)
                self._arrays[array_handle] = building_frac
            return building_frac
        
        @building_frac.setter
        def building_frac(self, building_frac):
            self.building_frac[...] = building_frac
        
        @property
        def building_scale(self):
            """
            Element building_scale ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 231
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__building_scale(self._handle)
            if array_handle in self._arrays:
                building_scale = self._arrays[array_handle]
            else:
                building_scale = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__building_scale)
                self._arrays[array_handle] = building_scale
            return building_scale
        
        @building_scale.setter
        def building_scale(self, building_scale):
            self.building_scale[...] = building_scale
        
        @property
        def veg_frac(self):
            """
            Element veg_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 232
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__veg_frac(self._handle)
            if array_handle in self._arrays:
                veg_frac = self._arrays[array_handle]
            else:
                veg_frac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__veg_frac)
                self._arrays[array_handle] = veg_frac
            return veg_frac
        
        @veg_frac.setter
        def veg_frac(self, veg_frac):
            self.veg_frac[...] = veg_frac
        
        @property
        def veg_scale(self):
            """
            Element veg_scale ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 233
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__veg_scale(self._handle)
            if array_handle in self._arrays:
                veg_scale = self._arrays[array_handle]
            else:
                veg_scale = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__veg_scale)
                self._arrays[array_handle] = veg_scale
            return veg_scale
        
        @veg_scale.setter
        def veg_scale(self, veg_scale):
            self.veg_scale[...] = veg_scale
        
        @property
        def alb_roof(self):
            """
            Element alb_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 234
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__alb_roof(self._handle)
            if array_handle in self._arrays:
                alb_roof = self._arrays[array_handle]
            else:
                alb_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__alb_roof)
                self._arrays[array_handle] = alb_roof
            return alb_roof
        
        @alb_roof.setter
        def alb_roof(self, alb_roof):
            self.alb_roof[...] = alb_roof
        
        @property
        def emis_roof(self):
            """
            Element emis_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 235
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__emis_roof(self._handle)
            if array_handle in self._arrays:
                emis_roof = self._arrays[array_handle]
            else:
                emis_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__emis_roof)
                self._arrays[array_handle] = emis_roof
            return emis_roof
        
        @emis_roof.setter
        def emis_roof(self, emis_roof):
            self.emis_roof[...] = emis_roof
        
        @property
        def alb_wall(self):
            """
            Element alb_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 236
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__alb_wall(self._handle)
            if array_handle in self._arrays:
                alb_wall = self._arrays[array_handle]
            else:
                alb_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__alb_wall)
                self._arrays[array_handle] = alb_wall
            return alb_wall
        
        @alb_wall.setter
        def alb_wall(self, alb_wall):
            self.alb_wall[...] = alb_wall
        
        @property
        def emis_wall(self):
            """
            Element emis_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 237
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__emis_wall(self._handle)
            if array_handle in self._arrays:
                emis_wall = self._arrays[array_handle]
            else:
                emis_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__emis_wall)
                self._arrays[array_handle] = emis_wall
            return emis_wall
        
        @emis_wall.setter
        def emis_wall(self, emis_wall):
            self.emis_wall[...] = emis_wall
        
        @property
        def roof_albedo_dir_mult_fact(self):
            """
            Element roof_albedo_dir_mult_fact ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 238
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__roof_albedo_dir_mult_fact(self._handle)
            if array_handle in self._arrays:
                roof_albedo_dir_mult_fact = self._arrays[array_handle]
            else:
                roof_albedo_dir_mult_fact = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__roof_albedo_dir_mult_fact)
                self._arrays[array_handle] = roof_albedo_dir_mult_fact
            return roof_albedo_dir_mult_fact
        
        @roof_albedo_dir_mult_fact.setter
        def roof_albedo_dir_mult_fact(self, roof_albedo_dir_mult_fact):
            self.roof_albedo_dir_mult_fact[...] = roof_albedo_dir_mult_fact
        
        @property
        def wall_specular_frac(self):
            """
            Element wall_specular_frac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 239
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_spartacus_layer_prm__array__wall_specular_frac(self._handle)
            if array_handle in self._arrays:
                wall_specular_frac = self._arrays[array_handle]
            else:
                wall_specular_frac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_spartacus_layer_prm__array__wall_specular_frac)
                self._arrays[array_handle] = wall_specular_frac
            return wall_specular_frac
        
        @wall_specular_frac.setter
        def wall_specular_frac(self, wall_specular_frac):
            self.wall_specular_frac[...] = wall_specular_frac
        
        def __str__(self):
            ret = ['<spartacus_layer_prm>{\n']
            ret.append('    building_frac : ')
            ret.append(repr(self.building_frac))
            ret.append(',\n    building_scale : ')
            ret.append(repr(self.building_scale))
            ret.append(',\n    veg_frac : ')
            ret.append(repr(self.veg_frac))
            ret.append(',\n    veg_scale : ')
            ret.append(repr(self.veg_scale))
            ret.append(',\n    alb_roof : ')
            ret.append(repr(self.alb_roof))
            ret.append(',\n    emis_roof : ')
            ret.append(repr(self.emis_roof))
            ret.append(',\n    alb_wall : ')
            ret.append(repr(self.alb_wall))
            ret.append(',\n    emis_wall : ')
            ret.append(repr(self.emis_wall))
            ret.append(',\n    roof_albedo_dir_mult_fact : ')
            ret.append(repr(self.roof_albedo_dir_mult_fact))
            ret.append(',\n    wall_specular_frac : ')
            ret.append(repr(self.wall_specular_frac))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LUMPS_PRM")
    class LUMPS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lumps_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 250-254
        
        """
        def __init__(self, handle=None):
            """
            self = Lumps_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 250-254
            
            
            Returns
            -------
            this : Lumps_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lumps_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lumps_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lumps_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 250-254
            
            Parameters
            ----------
            this : Lumps_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lumps_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lumps_prm_finalise(this=self._handle)
        
        @property
        def raincover(self):
            """
            Element raincover ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 251
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__raincover(self._handle)
        
        @raincover.setter
        def raincover(self, raincover):
            _supy_driver.f90wrap_lumps_prm__set__raincover(self._handle, raincover)
        
        @property
        def rainmaxres(self):
            """
            Element rainmaxres ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 252
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__rainmaxres(self._handle)
        
        @rainmaxres.setter
        def rainmaxres(self, rainmaxres):
            _supy_driver.f90wrap_lumps_prm__set__rainmaxres(self._handle, rainmaxres)
        
        @property
        def drainrt(self):
            """
            Element drainrt ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 253
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__drainrt(self._handle)
        
        @drainrt.setter
        def drainrt(self, drainrt):
            _supy_driver.f90wrap_lumps_prm__set__drainrt(self._handle, drainrt)
        
        @property
        def veg_type(self):
            """
            Element veg_type ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 254
            
            """
            return _supy_driver.f90wrap_lumps_prm__get__veg_type(self._handle)
        
        @veg_type.setter
        def veg_type(self, veg_type):
            _supy_driver.f90wrap_lumps_prm__set__veg_type(self._handle, veg_type)
        
        def __str__(self):
            ret = ['<lumps_prm>{\n']
            ret.append('    raincover : ')
            ret.append(repr(self.raincover))
            ret.append(',\n    rainmaxres : ')
            ret.append(repr(self.rainmaxres))
            ret.append(',\n    drainrt : ')
            ret.append(repr(self.drainrt))
            ret.append(',\n    veg_type : ')
            ret.append(repr(self.veg_type))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.EHC_PRM")
    class EHC_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ehc_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 256-277
        
        """
        def __init__(self, handle=None):
            """
            self = Ehc_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 256-277
            
            
            Returns
            -------
            this : Ehc_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for ehc_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__ehc_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ehc_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 256-277
            
            Parameters
            ----------
            this : Ehc_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for ehc_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__ehc_prm_finalise(this=self._handle)
        
        def allocate(self, nlayer, ndepth):
            """
            allocate__binding__ehc_prm(self, nlayer, ndepth)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1246-1268
            
            Parameters
            ----------
            self : Ehc_Prm
            nlayer : int
            ndepth : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__allocate__binding__ehc_prm(self=self._handle, \
                nlayer=nlayer, ndepth=ndepth)
        
        def deallocate(self):
            """
            deallocate__binding__ehc_prm(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1270-1290
            
            Parameters
            ----------
            self : Ehc_Prm
            
            """
            _supy_driver.f90wrap_suews_def_dts__deallocate__binding__ehc_prm(self=self._handle)
        
        @property
        def soil_storecap_roof(self):
            """
            Element soil_storecap_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 257
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__soil_storecap_roof(self._handle)
            if array_handle in self._arrays:
                soil_storecap_roof = self._arrays[array_handle]
            else:
                soil_storecap_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__soil_storecap_roof)
                self._arrays[array_handle] = soil_storecap_roof
            return soil_storecap_roof
        
        @soil_storecap_roof.setter
        def soil_storecap_roof(self, soil_storecap_roof):
            self.soil_storecap_roof[...] = soil_storecap_roof
        
        @property
        def soil_storecap_wall(self):
            """
            Element soil_storecap_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 258
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__soil_storecap_wall(self._handle)
            if array_handle in self._arrays:
                soil_storecap_wall = self._arrays[array_handle]
            else:
                soil_storecap_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__soil_storecap_wall)
                self._arrays[array_handle] = soil_storecap_wall
            return soil_storecap_wall
        
        @soil_storecap_wall.setter
        def soil_storecap_wall(self, soil_storecap_wall):
            self.soil_storecap_wall[...] = soil_storecap_wall
        
        @property
        def state_limit_roof(self):
            """
            Element state_limit_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 259
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__state_limit_roof(self._handle)
            if array_handle in self._arrays:
                state_limit_roof = self._arrays[array_handle]
            else:
                state_limit_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__state_limit_roof)
                self._arrays[array_handle] = state_limit_roof
            return state_limit_roof
        
        @state_limit_roof.setter
        def state_limit_roof(self, state_limit_roof):
            self.state_limit_roof[...] = state_limit_roof
        
        @property
        def state_limit_wall(self):
            """
            Element state_limit_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 260
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__state_limit_wall(self._handle)
            if array_handle in self._arrays:
                state_limit_wall = self._arrays[array_handle]
            else:
                state_limit_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__state_limit_wall)
                self._arrays[array_handle] = state_limit_wall
            return state_limit_wall
        
        @state_limit_wall.setter
        def state_limit_wall(self, state_limit_wall):
            self.state_limit_wall[...] = state_limit_wall
        
        @property
        def wet_thresh_roof(self):
            """
            Element wet_thresh_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 261
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__wet_thresh_roof(self._handle)
            if array_handle in self._arrays:
                wet_thresh_roof = self._arrays[array_handle]
            else:
                wet_thresh_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__wet_thresh_roof)
                self._arrays[array_handle] = wet_thresh_roof
            return wet_thresh_roof
        
        @wet_thresh_roof.setter
        def wet_thresh_roof(self, wet_thresh_roof):
            self.wet_thresh_roof[...] = wet_thresh_roof
        
        @property
        def wet_thresh_wall(self):
            """
            Element wet_thresh_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 262
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__wet_thresh_wall(self._handle)
            if array_handle in self._arrays:
                wet_thresh_wall = self._arrays[array_handle]
            else:
                wet_thresh_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__wet_thresh_wall)
                self._arrays[array_handle] = wet_thresh_wall
            return wet_thresh_wall
        
        @wet_thresh_wall.setter
        def wet_thresh_wall(self, wet_thresh_wall):
            self.wet_thresh_wall[...] = wet_thresh_wall
        
        @property
        def tin_roof(self):
            """
            Element tin_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 263
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__tin_roof(self._handle)
            if array_handle in self._arrays:
                tin_roof = self._arrays[array_handle]
            else:
                tin_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__tin_roof)
                self._arrays[array_handle] = tin_roof
            return tin_roof
        
        @tin_roof.setter
        def tin_roof(self, tin_roof):
            self.tin_roof[...] = tin_roof
        
        @property
        def tin_wall(self):
            """
            Element tin_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 264
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__tin_wall(self._handle)
            if array_handle in self._arrays:
                tin_wall = self._arrays[array_handle]
            else:
                tin_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__tin_wall)
                self._arrays[array_handle] = tin_wall
            return tin_wall
        
        @tin_wall.setter
        def tin_wall(self, tin_wall):
            self.tin_wall[...] = tin_wall
        
        @property
        def tin_surf(self):
            """
            Element tin_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 265
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__tin_surf(self._handle)
            if array_handle in self._arrays:
                tin_surf = self._arrays[array_handle]
            else:
                tin_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__tin_surf)
                self._arrays[array_handle] = tin_surf
            return tin_surf
        
        @tin_surf.setter
        def tin_surf(self, tin_surf):
            self.tin_surf[...] = tin_surf
        
        @property
        def k_roof(self):
            """
            Element k_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 266
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__k_roof(self._handle)
            if array_handle in self._arrays:
                k_roof = self._arrays[array_handle]
            else:
                k_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__k_roof)
                self._arrays[array_handle] = k_roof
            return k_roof
        
        @k_roof.setter
        def k_roof(self, k_roof):
            self.k_roof[...] = k_roof
        
        @property
        def k_wall(self):
            """
            Element k_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 267
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__k_wall(self._handle)
            if array_handle in self._arrays:
                k_wall = self._arrays[array_handle]
            else:
                k_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__k_wall)
                self._arrays[array_handle] = k_wall
            return k_wall
        
        @k_wall.setter
        def k_wall(self, k_wall):
            self.k_wall[...] = k_wall
        
        @property
        def k_surf(self):
            """
            Element k_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 268
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__k_surf(self._handle)
            if array_handle in self._arrays:
                k_surf = self._arrays[array_handle]
            else:
                k_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__k_surf)
                self._arrays[array_handle] = k_surf
            return k_surf
        
        @k_surf.setter
        def k_surf(self, k_surf):
            self.k_surf[...] = k_surf
        
        @property
        def cp_roof(self):
            """
            Element cp_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 269
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__cp_roof(self._handle)
            if array_handle in self._arrays:
                cp_roof = self._arrays[array_handle]
            else:
                cp_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__cp_roof)
                self._arrays[array_handle] = cp_roof
            return cp_roof
        
        @cp_roof.setter
        def cp_roof(self, cp_roof):
            self.cp_roof[...] = cp_roof
        
        @property
        def cp_wall(self):
            """
            Element cp_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 270
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__cp_wall(self._handle)
            if array_handle in self._arrays:
                cp_wall = self._arrays[array_handle]
            else:
                cp_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__cp_wall)
                self._arrays[array_handle] = cp_wall
            return cp_wall
        
        @cp_wall.setter
        def cp_wall(self, cp_wall):
            self.cp_wall[...] = cp_wall
        
        @property
        def cp_surf(self):
            """
            Element cp_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 271
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__cp_surf(self._handle)
            if array_handle in self._arrays:
                cp_surf = self._arrays[array_handle]
            else:
                cp_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__cp_surf)
                self._arrays[array_handle] = cp_surf
            return cp_surf
        
        @cp_surf.setter
        def cp_surf(self, cp_surf):
            self.cp_surf[...] = cp_surf
        
        @property
        def dz_roof(self):
            """
            Element dz_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 272
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__dz_roof(self._handle)
            if array_handle in self._arrays:
                dz_roof = self._arrays[array_handle]
            else:
                dz_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__dz_roof)
                self._arrays[array_handle] = dz_roof
            return dz_roof
        
        @dz_roof.setter
        def dz_roof(self, dz_roof):
            self.dz_roof[...] = dz_roof
        
        @property
        def dz_wall(self):
            """
            Element dz_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 273
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__dz_wall(self._handle)
            if array_handle in self._arrays:
                dz_wall = self._arrays[array_handle]
            else:
                dz_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__dz_wall)
                self._arrays[array_handle] = dz_wall
            return dz_wall
        
        @dz_wall.setter
        def dz_wall(self, dz_wall):
            self.dz_wall[...] = dz_wall
        
        @property
        def dz_surf(self):
            """
            Element dz_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 274
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_ehc_prm__array__dz_surf(self._handle)
            if array_handle in self._arrays:
                dz_surf = self._arrays[array_handle]
            else:
                dz_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_ehc_prm__array__dz_surf)
                self._arrays[array_handle] = dz_surf
            return dz_surf
        
        @dz_surf.setter
        def dz_surf(self, dz_surf):
            self.dz_surf[...] = dz_surf
        
        def __str__(self):
            ret = ['<ehc_prm>{\n']
            ret.append('    soil_storecap_roof : ')
            ret.append(repr(self.soil_storecap_roof))
            ret.append(',\n    soil_storecap_wall : ')
            ret.append(repr(self.soil_storecap_wall))
            ret.append(',\n    state_limit_roof : ')
            ret.append(repr(self.state_limit_roof))
            ret.append(',\n    state_limit_wall : ')
            ret.append(repr(self.state_limit_wall))
            ret.append(',\n    wet_thresh_roof : ')
            ret.append(repr(self.wet_thresh_roof))
            ret.append(',\n    wet_thresh_wall : ')
            ret.append(repr(self.wet_thresh_wall))
            ret.append(',\n    tin_roof : ')
            ret.append(repr(self.tin_roof))
            ret.append(',\n    tin_wall : ')
            ret.append(repr(self.tin_wall))
            ret.append(',\n    tin_surf : ')
            ret.append(repr(self.tin_surf))
            ret.append(',\n    k_roof : ')
            ret.append(repr(self.k_roof))
            ret.append(',\n    k_wall : ')
            ret.append(repr(self.k_wall))
            ret.append(',\n    k_surf : ')
            ret.append(repr(self.k_surf))
            ret.append(',\n    cp_roof : ')
            ret.append(repr(self.cp_roof))
            ret.append(',\n    cp_wall : ')
            ret.append(repr(self.cp_wall))
            ret.append(',\n    cp_surf : ')
            ret.append(repr(self.cp_surf))
            ret.append(',\n    dz_roof : ')
            ret.append(repr(self.dz_roof))
            ret.append(',\n    dz_wall : ')
            ret.append(repr(self.dz_wall))
            ret.append(',\n    dz_surf : ')
            ret.append(repr(self.dz_surf))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_PAVED_PRM")
    class LC_PAVED_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_paved_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 279-289
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Paved_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 279-289
            
            
            Returns
            -------
            this : Lc_Paved_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_paved_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_paved_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Paved_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 279-289
            
            Parameters
            ----------
            this : Lc_Paved_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_paved_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_paved_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 281
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_paved_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 282
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_paved_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 283
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_paved_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_paved_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 284
            
            """
            soil_handle = _supy_driver.f90wrap_lc_paved_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_paved_prm__set__soil(self._handle, soil)
        
        @property
        def state(self):
            """
            Element state ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 285
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__state(self._handle)
        
        @state.setter
        def state(self, state):
            _supy_driver.f90wrap_lc_paved_prm__set__state(self._handle, state)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 286
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_paved_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracpaved(self):
            """
            Element irrfracpaved ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 287
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__irrfracpaved(self._handle)
        
        @irrfracpaved.setter
        def irrfracpaved(self, irrfracpaved):
            _supy_driver.f90wrap_lc_paved_prm__set__irrfracpaved(self._handle, irrfracpaved)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 288
            
            """
            return _supy_driver.f90wrap_lc_paved_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_paved_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 289
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_paved_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_def_dts.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_paved_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_paved_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    state : ')
            ret.append(repr(self.state))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracpaved : ')
            ret.append(repr(self.irrfracpaved))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_BLDG_PRM")
    class LC_BLDG_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_bldg_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 291-303
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Bldg_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 291-303
            
            
            Returns
            -------
            this : Lc_Bldg_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_bldg_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_bldg_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Bldg_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 291-303
            
            Parameters
            ----------
            this : Lc_Bldg_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_bldg_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_bldg_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 293
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_bldg_prm__set__sfr(self._handle, sfr)
        
        @property
        def faibldg(self):
            """
            Element faibldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 294
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__faibldg(self._handle)
        
        @faibldg.setter
        def faibldg(self, faibldg):
            _supy_driver.f90wrap_lc_bldg_prm__set__faibldg(self._handle, faibldg)
        
        @property
        def bldgh(self):
            """
            Element bldgh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 295
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__bldgh(self._handle)
        
        @bldgh.setter
        def bldgh(self, bldgh):
            _supy_driver.f90wrap_lc_bldg_prm__set__bldgh(self._handle, bldgh)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 296
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_bldg_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 297
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_bldg_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_bldg_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 298
            
            """
            soil_handle = _supy_driver.f90wrap_lc_bldg_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_bldg_prm__set__soil(self._handle, soil)
        
        @property
        def state(self):
            """
            Element state ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 299
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__state(self._handle)
        
        @state.setter
        def state(self, state):
            _supy_driver.f90wrap_lc_bldg_prm__set__state(self._handle, state)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 300
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_bldg_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracbldgs(self):
            """
            Element irrfracbldgs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 301
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__irrfracbldgs(self._handle)
        
        @irrfracbldgs.setter
        def irrfracbldgs(self, irrfracbldgs):
            _supy_driver.f90wrap_lc_bldg_prm__set__irrfracbldgs(self._handle, irrfracbldgs)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 302
            
            """
            return _supy_driver.f90wrap_lc_bldg_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_bldg_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 303
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_bldg_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_def_dts.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_bldg_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_bldg_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    faibldg : ')
            ret.append(repr(self.faibldg))
            ret.append(',\n    bldgh : ')
            ret.append(repr(self.bldgh))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    state : ')
            ret.append(repr(self.state))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracbldgs : ')
            ret.append(repr(self.irrfracbldgs))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_DECTR_PRM")
    class LC_DECTR_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_dectr_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 305-326
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Dectr_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 305-326
            
            
            Returns
            -------
            this : Lc_Dectr_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_dectr_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_dectr_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Dectr_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 305-326
            
            Parameters
            ----------
            this : Lc_Dectr_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_dectr_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_dectr_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 307
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_dectr_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 308
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_dectr_prm__set__emis(self._handle, emis)
        
        @property
        def faidectree(self):
            """
            Element faidectree ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 309
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__faidectree(self._handle)
        
        @faidectree.setter
        def faidectree(self, faidectree):
            _supy_driver.f90wrap_lc_dectr_prm__set__faidectree(self._handle, faidectree)
        
        @property
        def dectreeh(self):
            """
            Element dectreeh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 310
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__dectreeh(self._handle)
        
        @dectreeh.setter
        def dectreeh(self, dectreeh):
            _supy_driver.f90wrap_lc_dectr_prm__set__dectreeh(self._handle, dectreeh)
        
        @property
        def pormin_dec(self):
            """
            Element pormin_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 311
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__pormin_dec(self._handle)
        
        @pormin_dec.setter
        def pormin_dec(self, pormin_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__pormin_dec(self._handle, pormin_dec)
        
        @property
        def pormax_dec(self):
            """
            Element pormax_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 312
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__pormax_dec(self._handle)
        
        @pormax_dec.setter
        def pormax_dec(self, pormax_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__pormax_dec(self._handle, pormax_dec)
        
        @property
        def alb_min(self):
            """
            Element alb_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 313
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__alb_min(self._handle)
        
        @alb_min.setter
        def alb_min(self, alb_min):
            _supy_driver.f90wrap_lc_dectr_prm__set__alb_min(self._handle, alb_min)
        
        @property
        def alb_max(self):
            """
            Element alb_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 314
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__alb_max(self._handle)
        
        @alb_max.setter
        def alb_max(self, alb_max):
            _supy_driver.f90wrap_lc_dectr_prm__set__alb_max(self._handle, alb_max)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 315
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_dectr_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 316
            
            """
            soil_handle = _supy_driver.f90wrap_lc_dectr_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 317
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_dectr_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def capmax_dec(self):
            """
            Element capmax_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 318
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__capmax_dec(self._handle)
        
        @capmax_dec.setter
        def capmax_dec(self, capmax_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__capmax_dec(self._handle, capmax_dec)
        
        @property
        def capmin_dec(self):
            """
            Element capmin_dec ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 319
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__capmin_dec(self._handle)
        
        @capmin_dec.setter
        def capmin_dec(self, capmin_dec):
            _supy_driver.f90wrap_lc_dectr_prm__set__capmin_dec(self._handle, capmin_dec)
        
        @property
        def irrfracdectr(self):
            """
            Element irrfracdectr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 320
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__irrfracdectr(self._handle)
        
        @irrfracdectr.setter
        def irrfracdectr(self, irrfracdectr):
            _supy_driver.f90wrap_lc_dectr_prm__set__irrfracdectr(self._handle, irrfracdectr)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 321
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_dectr_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def bioco2(self):
            """
            Element bioco2 ftype=type(bioco2_prm) pytype=Bioco2_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 322
            
            """
            bioco2_handle = _supy_driver.f90wrap_lc_dectr_prm__get__bioco2(self._handle)
            if tuple(bioco2_handle) in self._objs:
                bioco2 = self._objs[tuple(bioco2_handle)]
            else:
                bioco2 = suews_def_dts.bioCO2_PRM.from_handle(bioco2_handle)
                self._objs[tuple(bioco2_handle)] = bioco2
            return bioco2
        
        @bioco2.setter
        def bioco2(self, bioco2):
            bioco2 = bioco2._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__bioco2(self._handle, bioco2)
        
        @property
        def maxconductance(self):
            """
            Element maxconductance ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 323
            
            """
            return _supy_driver.f90wrap_lc_dectr_prm__get__maxconductance(self._handle)
        
        @maxconductance.setter
        def maxconductance(self, maxconductance):
            _supy_driver.f90wrap_lc_dectr_prm__set__maxconductance(self._handle, \
                maxconductance)
        
        @property
        def lai(self):
            """
            Element lai ftype=type(lai_prm) pytype=Lai_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 325
            
            """
            lai_handle = _supy_driver.f90wrap_lc_dectr_prm__get__lai(self._handle)
            if tuple(lai_handle) in self._objs:
                lai = self._objs[tuple(lai_handle)]
            else:
                lai = suews_def_dts.LAI_PRM.from_handle(lai_handle)
                self._objs[tuple(lai_handle)] = lai
            return lai
        
        @lai.setter
        def lai(self, lai):
            lai = lai._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__lai(self._handle, lai)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 326
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_dectr_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_def_dts.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_dectr_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_dectr_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    faidectree : ')
            ret.append(repr(self.faidectree))
            ret.append(',\n    dectreeh : ')
            ret.append(repr(self.dectreeh))
            ret.append(',\n    pormin_dec : ')
            ret.append(repr(self.pormin_dec))
            ret.append(',\n    pormax_dec : ')
            ret.append(repr(self.pormax_dec))
            ret.append(',\n    alb_min : ')
            ret.append(repr(self.alb_min))
            ret.append(',\n    alb_max : ')
            ret.append(repr(self.alb_max))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    capmax_dec : ')
            ret.append(repr(self.capmax_dec))
            ret.append(',\n    capmin_dec : ')
            ret.append(repr(self.capmin_dec))
            ret.append(',\n    irrfracdectr : ')
            ret.append(repr(self.irrfracdectr))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    bioco2 : ')
            ret.append(repr(self.bioco2))
            ret.append(',\n    maxconductance : ')
            ret.append(repr(self.maxconductance))
            ret.append(',\n    lai : ')
            ret.append(repr(self.lai))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_EVETR_PRM")
    class LC_EVETR_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_evetr_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 328-345
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Evetr_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 328-345
            
            
            Returns
            -------
            this : Lc_Evetr_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_evetr_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_evetr_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Evetr_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 328-345
            
            Parameters
            ----------
            this : Lc_Evetr_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_evetr_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_evetr_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 330
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_evetr_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 331
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_evetr_prm__set__emis(self._handle, emis)
        
        @property
        def faievetree(self):
            """
            Element faievetree ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 332
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__faievetree(self._handle)
        
        @faievetree.setter
        def faievetree(self, faievetree):
            _supy_driver.f90wrap_lc_evetr_prm__set__faievetree(self._handle, faievetree)
        
        @property
        def evetreeh(self):
            """
            Element evetreeh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 333
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__evetreeh(self._handle)
        
        @evetreeh.setter
        def evetreeh(self, evetreeh):
            _supy_driver.f90wrap_lc_evetr_prm__set__evetreeh(self._handle, evetreeh)
        
        @property
        def alb_min(self):
            """
            Element alb_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 334
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__alb_min(self._handle)
        
        @alb_min.setter
        def alb_min(self, alb_min):
            _supy_driver.f90wrap_lc_evetr_prm__set__alb_min(self._handle, alb_min)
        
        @property
        def alb_max(self):
            """
            Element alb_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 335
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__alb_max(self._handle)
        
        @alb_max.setter
        def alb_max(self, alb_max):
            _supy_driver.f90wrap_lc_evetr_prm__set__alb_max(self._handle, alb_max)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 336
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_evetr_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 337
            
            """
            soil_handle = _supy_driver.f90wrap_lc_evetr_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 338
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_evetr_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracevetr(self):
            """
            Element irrfracevetr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 339
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__irrfracevetr(self._handle)
        
        @irrfracevetr.setter
        def irrfracevetr(self, irrfracevetr):
            _supy_driver.f90wrap_lc_evetr_prm__set__irrfracevetr(self._handle, irrfracevetr)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 340
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_evetr_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def bioco2(self):
            """
            Element bioco2 ftype=type(bioco2_prm) pytype=Bioco2_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 341
            
            """
            bioco2_handle = _supy_driver.f90wrap_lc_evetr_prm__get__bioco2(self._handle)
            if tuple(bioco2_handle) in self._objs:
                bioco2 = self._objs[tuple(bioco2_handle)]
            else:
                bioco2 = suews_def_dts.bioCO2_PRM.from_handle(bioco2_handle)
                self._objs[tuple(bioco2_handle)] = bioco2
            return bioco2
        
        @bioco2.setter
        def bioco2(self, bioco2):
            bioco2 = bioco2._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__bioco2(self._handle, bioco2)
        
        @property
        def maxconductance(self):
            """
            Element maxconductance ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 343
            
            """
            return _supy_driver.f90wrap_lc_evetr_prm__get__maxconductance(self._handle)
        
        @maxconductance.setter
        def maxconductance(self, maxconductance):
            _supy_driver.f90wrap_lc_evetr_prm__set__maxconductance(self._handle, \
                maxconductance)
        
        @property
        def lai(self):
            """
            Element lai ftype=type(lai_prm) pytype=Lai_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 344
            
            """
            lai_handle = _supy_driver.f90wrap_lc_evetr_prm__get__lai(self._handle)
            if tuple(lai_handle) in self._objs:
                lai = self._objs[tuple(lai_handle)]
            else:
                lai = suews_def_dts.LAI_PRM.from_handle(lai_handle)
                self._objs[tuple(lai_handle)] = lai
            return lai
        
        @lai.setter
        def lai(self, lai):
            lai = lai._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__lai(self._handle, lai)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 345
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_evetr_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_def_dts.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_evetr_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_evetr_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    faievetree : ')
            ret.append(repr(self.faievetree))
            ret.append(',\n    evetreeh : ')
            ret.append(repr(self.evetreeh))
            ret.append(',\n    alb_min : ')
            ret.append(repr(self.alb_min))
            ret.append(',\n    alb_max : ')
            ret.append(repr(self.alb_max))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracevetr : ')
            ret.append(repr(self.irrfracevetr))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    bioco2 : ')
            ret.append(repr(self.bioco2))
            ret.append(',\n    maxconductance : ')
            ret.append(repr(self.maxconductance))
            ret.append(',\n    lai : ')
            ret.append(repr(self.lai))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_GRASS_PRM")
    class LC_GRASS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_grass_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 347-362
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Grass_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 347-362
            
            
            Returns
            -------
            this : Lc_Grass_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_grass_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_grass_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Grass_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 347-362
            
            Parameters
            ----------
            this : Lc_Grass_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_grass_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_grass_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 349
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_grass_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 350
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_grass_prm__set__emis(self._handle, emis)
        
        @property
        def alb_min(self):
            """
            Element alb_min ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 351
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__alb_min(self._handle)
        
        @alb_min.setter
        def alb_min(self, alb_min):
            _supy_driver.f90wrap_lc_grass_prm__set__alb_min(self._handle, alb_min)
        
        @property
        def alb_max(self):
            """
            Element alb_max ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 352
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__alb_max(self._handle)
        
        @alb_max.setter
        def alb_max(self, alb_max):
            _supy_driver.f90wrap_lc_grass_prm__set__alb_max(self._handle, alb_max)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 353
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_grass_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_grass_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 354
            
            """
            soil_handle = _supy_driver.f90wrap_lc_grass_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_grass_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 355
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_grass_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracgrass(self):
            """
            Element irrfracgrass ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 356
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__irrfracgrass(self._handle)
        
        @irrfracgrass.setter
        def irrfracgrass(self, irrfracgrass):
            _supy_driver.f90wrap_lc_grass_prm__set__irrfracgrass(self._handle, irrfracgrass)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 357
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_grass_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def bioco2(self):
            """
            Element bioco2 ftype=type(bioco2_prm) pytype=Bioco2_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 358
            
            """
            bioco2_handle = _supy_driver.f90wrap_lc_grass_prm__get__bioco2(self._handle)
            if tuple(bioco2_handle) in self._objs:
                bioco2 = self._objs[tuple(bioco2_handle)]
            else:
                bioco2 = suews_def_dts.bioCO2_PRM.from_handle(bioco2_handle)
                self._objs[tuple(bioco2_handle)] = bioco2
            return bioco2
        
        @bioco2.setter
        def bioco2(self, bioco2):
            bioco2 = bioco2._handle
            _supy_driver.f90wrap_lc_grass_prm__set__bioco2(self._handle, bioco2)
        
        @property
        def maxconductance(self):
            """
            Element maxconductance ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 360
            
            """
            return _supy_driver.f90wrap_lc_grass_prm__get__maxconductance(self._handle)
        
        @maxconductance.setter
        def maxconductance(self, maxconductance):
            _supy_driver.f90wrap_lc_grass_prm__set__maxconductance(self._handle, \
                maxconductance)
        
        @property
        def lai(self):
            """
            Element lai ftype=type(lai_prm) pytype=Lai_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 361
            
            """
            lai_handle = _supy_driver.f90wrap_lc_grass_prm__get__lai(self._handle)
            if tuple(lai_handle) in self._objs:
                lai = self._objs[tuple(lai_handle)]
            else:
                lai = suews_def_dts.LAI_PRM.from_handle(lai_handle)
                self._objs[tuple(lai_handle)] = lai
            return lai
        
        @lai.setter
        def lai(self, lai):
            lai = lai._handle
            _supy_driver.f90wrap_lc_grass_prm__set__lai(self._handle, lai)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 362
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_grass_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_def_dts.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_grass_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_grass_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    alb_min : ')
            ret.append(repr(self.alb_min))
            ret.append(',\n    alb_max : ')
            ret.append(repr(self.alb_max))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracgrass : ')
            ret.append(repr(self.irrfracgrass))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    bioco2 : ')
            ret.append(repr(self.bioco2))
            ret.append(',\n    maxconductance : ')
            ret.append(repr(self.maxconductance))
            ret.append(',\n    lai : ')
            ret.append(repr(self.lai))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_BSOIL_PRM")
    class LC_BSOIL_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_bsoil_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 364-373
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Bsoil_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 364-373
            
            
            Returns
            -------
            this : Lc_Bsoil_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_bsoil_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_bsoil_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Bsoil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 364-373
            
            Parameters
            ----------
            this : Lc_Bsoil_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_bsoil_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_bsoil_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 366
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_bsoil_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 367
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_bsoil_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 368
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_bsoil_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_bsoil_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 369
            
            """
            soil_handle = _supy_driver.f90wrap_lc_bsoil_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_bsoil_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 370
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_bsoil_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracbsoil(self):
            """
            Element irrfracbsoil ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 371
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__irrfracbsoil(self._handle)
        
        @irrfracbsoil.setter
        def irrfracbsoil(self, irrfracbsoil):
            _supy_driver.f90wrap_lc_bsoil_prm__set__irrfracbsoil(self._handle, irrfracbsoil)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 372
            
            """
            return _supy_driver.f90wrap_lc_bsoil_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_bsoil_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def waterdist(self):
            """
            Element waterdist ftype=type(water_dist_prm) pytype=Water_Dist_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 373
            
            """
            waterdist_handle = \
                _supy_driver.f90wrap_lc_bsoil_prm__get__waterdist(self._handle)
            if tuple(waterdist_handle) in self._objs:
                waterdist = self._objs[tuple(waterdist_handle)]
            else:
                waterdist = suews_def_dts.WATER_DIST_PRM.from_handle(waterdist_handle)
                self._objs[tuple(waterdist_handle)] = waterdist
            return waterdist
        
        @waterdist.setter
        def waterdist(self, waterdist):
            waterdist = waterdist._handle
            _supy_driver.f90wrap_lc_bsoil_prm__set__waterdist(self._handle, waterdist)
        
        def __str__(self):
            ret = ['<lc_bsoil_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracbsoil : ')
            ret.append(repr(self.irrfracbsoil))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    waterdist : ')
            ret.append(repr(self.waterdist))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.LC_WATER_PRM")
    class LC_WATER_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=lc_water_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 375-384
        
        """
        def __init__(self, handle=None):
            """
            self = Lc_Water_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 375-384
            
            
            Returns
            -------
            this : Lc_Water_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for lc_water_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__lc_water_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Lc_Water_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 375-384
            
            Parameters
            ----------
            this : Lc_Water_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for lc_water_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__lc_water_prm_finalise(this=self._handle)
        
        @property
        def sfr(self):
            """
            Element sfr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 377
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__sfr(self._handle)
        
        @sfr.setter
        def sfr(self, sfr):
            _supy_driver.f90wrap_lc_water_prm__set__sfr(self._handle, sfr)
        
        @property
        def emis(self):
            """
            Element emis ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 378
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__emis(self._handle)
        
        @emis.setter
        def emis(self, emis):
            _supy_driver.f90wrap_lc_water_prm__set__emis(self._handle, emis)
        
        @property
        def ohm(self):
            """
            Element ohm ftype=type(ohm_prm) pytype=Ohm_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 379
            
            """
            ohm_handle = _supy_driver.f90wrap_lc_water_prm__get__ohm(self._handle)
            if tuple(ohm_handle) in self._objs:
                ohm = self._objs[tuple(ohm_handle)]
            else:
                ohm = suews_def_dts.OHM_PRM.from_handle(ohm_handle)
                self._objs[tuple(ohm_handle)] = ohm
            return ohm
        
        @ohm.setter
        def ohm(self, ohm):
            ohm = ohm._handle
            _supy_driver.f90wrap_lc_water_prm__set__ohm(self._handle, ohm)
        
        @property
        def soil(self):
            """
            Element soil ftype=type(soil_prm) pytype=Soil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 380
            
            """
            soil_handle = _supy_driver.f90wrap_lc_water_prm__get__soil(self._handle)
            if tuple(soil_handle) in self._objs:
                soil = self._objs[tuple(soil_handle)]
            else:
                soil = suews_def_dts.SOIL_PRM.from_handle(soil_handle)
                self._objs[tuple(soil_handle)] = soil
            return soil
        
        @soil.setter
        def soil(self, soil):
            soil = soil._handle
            _supy_driver.f90wrap_lc_water_prm__set__soil(self._handle, soil)
        
        @property
        def statelimit(self):
            """
            Element statelimit ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 381
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__statelimit(self._handle)
        
        @statelimit.setter
        def statelimit(self, statelimit):
            _supy_driver.f90wrap_lc_water_prm__set__statelimit(self._handle, statelimit)
        
        @property
        def irrfracwater(self):
            """
            Element irrfracwater ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 382
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__irrfracwater(self._handle)
        
        @irrfracwater.setter
        def irrfracwater(self, irrfracwater):
            _supy_driver.f90wrap_lc_water_prm__set__irrfracwater(self._handle, irrfracwater)
        
        @property
        def wetthresh(self):
            """
            Element wetthresh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 383
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__wetthresh(self._handle)
        
        @wetthresh.setter
        def wetthresh(self, wetthresh):
            _supy_driver.f90wrap_lc_water_prm__set__wetthresh(self._handle, wetthresh)
        
        @property
        def flowchange(self):
            """
            Element flowchange ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 384
            
            """
            return _supy_driver.f90wrap_lc_water_prm__get__flowchange(self._handle)
        
        @flowchange.setter
        def flowchange(self, flowchange):
            _supy_driver.f90wrap_lc_water_prm__set__flowchange(self._handle, flowchange)
        
        def __str__(self):
            ret = ['<lc_water_prm>{\n']
            ret.append('    sfr : ')
            ret.append(repr(self.sfr))
            ret.append(',\n    emis : ')
            ret.append(repr(self.emis))
            ret.append(',\n    ohm : ')
            ret.append(repr(self.ohm))
            ret.append(',\n    soil : ')
            ret.append(repr(self.soil))
            ret.append(',\n    statelimit : ')
            ret.append(repr(self.statelimit))
            ret.append(',\n    irrfracwater : ')
            ret.append(repr(self.irrfracwater))
            ret.append(',\n    wetthresh : ')
            ret.append(repr(self.wetthresh))
            ret.append(',\n    flowchange : ')
            ret.append(repr(self.flowchange))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.BUILDING_ARCHETYPE_PRM")
    class BUILDING_ARCHETYPE_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=building_archetype_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 386-435
        
        """
        def __init__(self, handle=None):
            """
            self = Building_Archetype_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 386-435
            
            
            Returns
            -------
            this : Building_Archetype_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for building_archetype_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__building_archetype_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Building_Archetype_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 386-435
            
            Parameters
            ----------
            this : Building_Archetype_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for building_archetype_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__building_archetype_prm_finalise(this=self._handle)
        
        @property
        def buildingcount(self):
            """
            Element buildingcount ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 392
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__buildingcount(self._handle)
        
        @buildingcount.setter
        def buildingcount(self, buildingcount):
            _supy_driver.f90wrap_building_archetype_prm__set__buildingcount(self._handle, \
                buildingcount)
        
        @property
        def occupants(self):
            """
            Element occupants ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 393
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__occupants(self._handle)
        
        @occupants.setter
        def occupants(self, occupants):
            _supy_driver.f90wrap_building_archetype_prm__set__occupants(self._handle, \
                occupants)
        
        @property
        def hhs0(self):
            """
            Element hhs0 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 394
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__hhs0(self._handle)
        
        @hhs0.setter
        def hhs0(self, hhs0):
            _supy_driver.f90wrap_building_archetype_prm__set__hhs0(self._handle, hhs0)
        
        @property
        def age_0_4(self):
            """
            Element age_0_4 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 395
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__age_0_4(self._handle)
        
        @age_0_4.setter
        def age_0_4(self, age_0_4):
            _supy_driver.f90wrap_building_archetype_prm__set__age_0_4(self._handle, age_0_4)
        
        @property
        def age_5_11(self):
            """
            Element age_5_11 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 396
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__age_5_11(self._handle)
        
        @age_5_11.setter
        def age_5_11(self, age_5_11):
            _supy_driver.f90wrap_building_archetype_prm__set__age_5_11(self._handle, \
                age_5_11)
        
        @property
        def age_12_18(self):
            """
            Element age_12_18 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 397
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__age_12_18(self._handle)
        
        @age_12_18.setter
        def age_12_18(self, age_12_18):
            _supy_driver.f90wrap_building_archetype_prm__set__age_12_18(self._handle, \
                age_12_18)
        
        @property
        def age_19_64(self):
            """
            Element age_19_64 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 398
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__age_19_64(self._handle)
        
        @age_19_64.setter
        def age_19_64(self, age_19_64):
            _supy_driver.f90wrap_building_archetype_prm__set__age_19_64(self._handle, \
                age_19_64)
        
        @property
        def age_65plus(self):
            """
            Element age_65plus ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 399
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__age_65plus(self._handle)
        
        @age_65plus.setter
        def age_65plus(self, age_65plus):
            _supy_driver.f90wrap_building_archetype_prm__set__age_65plus(self._handle, \
                age_65plus)
        
        @property
        def stebbs_height(self):
            """
            Element stebbs_height ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 400
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__stebbs_height(self._handle)
        
        @stebbs_height.setter
        def stebbs_height(self, stebbs_height):
            _supy_driver.f90wrap_building_archetype_prm__set__stebbs_height(self._handle, \
                stebbs_height)
        
        @property
        def footprintarea(self):
            """
            Element footprintarea ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 401
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__footprintarea(self._handle)
        
        @footprintarea.setter
        def footprintarea(self, footprintarea):
            _supy_driver.f90wrap_building_archetype_prm__set__footprintarea(self._handle, \
                footprintarea)
        
        @property
        def wallexternalarea(self):
            """
            Element wallexternalarea ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 402
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__wallexternalarea(self._handle)
        
        @wallexternalarea.setter
        def wallexternalarea(self, wallexternalarea):
            _supy_driver.f90wrap_building_archetype_prm__set__wallexternalarea(self._handle, \
                wallexternalarea)
        
        @property
        def ratiointernalvolume(self):
            """
            Element ratiointernalvolume ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 403
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__ratiointernalvolume(self._handle)
        
        @ratiointernalvolume.setter
        def ratiointernalvolume(self, ratiointernalvolume):
            _supy_driver.f90wrap_building_archetype_prm__set__ratiointernalvolume(self._handle, \
                ratiointernalvolume)
        
        @property
        def wwr(self):
            """
            Element wwr ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 404
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__wwr(self._handle)
        
        @wwr.setter
        def wwr(self, wwr):
            _supy_driver.f90wrap_building_archetype_prm__set__wwr(self._handle, wwr)
        
        @property
        def wallthickness(self):
            """
            Element wallthickness ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 405
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__wallthickness(self._handle)
        
        @wallthickness.setter
        def wallthickness(self, wallthickness):
            _supy_driver.f90wrap_building_archetype_prm__set__wallthickness(self._handle, \
                wallthickness)
        
        @property
        def walleffectiveconductivity(self):
            """
            Element walleffectiveconductivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 406
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__walleffectiveconductivity(self._handle)
        
        @walleffectiveconductivity.setter
        def walleffectiveconductivity(self, walleffectiveconductivity):
            _supy_driver.f90wrap_building_archetype_prm__set__walleffectiveconductivity(self._handle, \
                walleffectiveconductivity)
        
        @property
        def walldensity(self):
            """
            Element walldensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 407
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__walldensity(self._handle)
        
        @walldensity.setter
        def walldensity(self, walldensity):
            _supy_driver.f90wrap_building_archetype_prm__set__walldensity(self._handle, \
                walldensity)
        
        @property
        def wallcp(self):
            """
            Element wallcp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 408
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__wallcp(self._handle)
        
        @wallcp.setter
        def wallcp(self, wallcp):
            _supy_driver.f90wrap_building_archetype_prm__set__wallcp(self._handle, wallcp)
        
        @property
        def wallx1(self):
            """
            Element wallx1 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 409
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__wallx1(self._handle)
        
        @wallx1.setter
        def wallx1(self, wallx1):
            _supy_driver.f90wrap_building_archetype_prm__set__wallx1(self._handle, wallx1)
        
        @property
        def wallexternalemissivity(self):
            """
            Element wallexternalemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 410
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__wallexternalemissivity(self._handle)
        
        @wallexternalemissivity.setter
        def wallexternalemissivity(self, wallexternalemissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__wallexternalemissivity(self._handle, \
                wallexternalemissivity)
        
        @property
        def wallinternalemissivity(self):
            """
            Element wallinternalemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 411
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__wallinternalemissivity(self._handle)
        
        @wallinternalemissivity.setter
        def wallinternalemissivity(self, wallinternalemissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__wallinternalemissivity(self._handle, \
                wallinternalemissivity)
        
        @property
        def walltransmissivity(self):
            """
            Element walltransmissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 412
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__walltransmissivity(self._handle)
        
        @walltransmissivity.setter
        def walltransmissivity(self, walltransmissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__walltransmissivity(self._handle, \
                walltransmissivity)
        
        @property
        def wallabsorbtivity(self):
            """
            Element wallabsorbtivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 413
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__wallabsorbtivity(self._handle)
        
        @wallabsorbtivity.setter
        def wallabsorbtivity(self, wallabsorbtivity):
            _supy_driver.f90wrap_building_archetype_prm__set__wallabsorbtivity(self._handle, \
                wallabsorbtivity)
        
        @property
        def wallreflectivity(self):
            """
            Element wallreflectivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 414
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__wallreflectivity(self._handle)
        
        @wallreflectivity.setter
        def wallreflectivity(self, wallreflectivity):
            _supy_driver.f90wrap_building_archetype_prm__set__wallreflectivity(self._handle, \
                wallreflectivity)
        
        @property
        def floorthickness(self):
            """
            Element floorthickness ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 415
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__floorthickness(self._handle)
        
        @floorthickness.setter
        def floorthickness(self, floorthickness):
            _supy_driver.f90wrap_building_archetype_prm__set__floorthickness(self._handle, \
                floorthickness)
        
        @property
        def groundflooreffectiveconductivity(self):
            """
            Element groundflooreffectiveconductivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 416
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__groundflooreffectiveco006f(self._handle)
        
        @groundflooreffectiveconductivity.setter
        def groundflooreffectiveconductivity(self, groundflooreffectiveconductivity):
            _supy_driver.f90wrap_building_archetype_prm__set__groundflooreffectivecoc3ca(self._handle, \
                groundflooreffectiveconductivity)
        
        @property
        def groundfloordensity(self):
            """
            Element groundfloordensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 417
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__groundfloordensity(self._handle)
        
        @groundfloordensity.setter
        def groundfloordensity(self, groundfloordensity):
            _supy_driver.f90wrap_building_archetype_prm__set__groundfloordensity(self._handle, \
                groundfloordensity)
        
        @property
        def groundfloorcp(self):
            """
            Element groundfloorcp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 418
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__groundfloorcp(self._handle)
        
        @groundfloorcp.setter
        def groundfloorcp(self, groundfloorcp):
            _supy_driver.f90wrap_building_archetype_prm__set__groundfloorcp(self._handle, \
                groundfloorcp)
        
        @property
        def windowthickness(self):
            """
            Element windowthickness ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 419
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowthickness(self._handle)
        
        @windowthickness.setter
        def windowthickness(self, windowthickness):
            _supy_driver.f90wrap_building_archetype_prm__set__windowthickness(self._handle, \
                windowthickness)
        
        @property
        def windoweffectiveconductivity(self):
            """
            Element windoweffectiveconductivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 420
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windoweffectiveconductd27c(self._handle)
        
        @windoweffectiveconductivity.setter
        def windoweffectiveconductivity(self, windoweffectiveconductivity):
            _supy_driver.f90wrap_building_archetype_prm__set__windoweffectiveconduct7f3d(self._handle, \
                windoweffectiveconductivity)
        
        @property
        def windowdensity(self):
            """
            Element windowdensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 421
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowdensity(self._handle)
        
        @windowdensity.setter
        def windowdensity(self, windowdensity):
            _supy_driver.f90wrap_building_archetype_prm__set__windowdensity(self._handle, \
                windowdensity)
        
        @property
        def windowcp(self):
            """
            Element windowcp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 422
            
            """
            return _supy_driver.f90wrap_building_archetype_prm__get__windowcp(self._handle)
        
        @windowcp.setter
        def windowcp(self, windowcp):
            _supy_driver.f90wrap_building_archetype_prm__set__windowcp(self._handle, \
                windowcp)
        
        @property
        def windowexternalemissivity(self):
            """
            Element windowexternalemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 423
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowexternalemissivity(self._handle)
        
        @windowexternalemissivity.setter
        def windowexternalemissivity(self, windowexternalemissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__windowexternalemissivity(self._handle, \
                windowexternalemissivity)
        
        @property
        def windowinternalemissivity(self):
            """
            Element windowinternalemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 424
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowinternalemissivity(self._handle)
        
        @windowinternalemissivity.setter
        def windowinternalemissivity(self, windowinternalemissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__windowinternalemissivity(self._handle, \
                windowinternalemissivity)
        
        @property
        def windowtransmissivity(self):
            """
            Element windowtransmissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 425
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowtransmissivity(self._handle)
        
        @windowtransmissivity.setter
        def windowtransmissivity(self, windowtransmissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__windowtransmissivity(self._handle, \
                windowtransmissivity)
        
        @property
        def windowabsorbtivity(self):
            """
            Element windowabsorbtivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 426
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowabsorbtivity(self._handle)
        
        @windowabsorbtivity.setter
        def windowabsorbtivity(self, windowabsorbtivity):
            _supy_driver.f90wrap_building_archetype_prm__set__windowabsorbtivity(self._handle, \
                windowabsorbtivity)
        
        @property
        def windowreflectivity(self):
            """
            Element windowreflectivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 427
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__windowreflectivity(self._handle)
        
        @windowreflectivity.setter
        def windowreflectivity(self, windowreflectivity):
            _supy_driver.f90wrap_building_archetype_prm__set__windowreflectivity(self._handle, \
                windowreflectivity)
        
        @property
        def internalmassdensity(self):
            """
            Element internalmassdensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 428
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__internalmassdensity(self._handle)
        
        @internalmassdensity.setter
        def internalmassdensity(self, internalmassdensity):
            _supy_driver.f90wrap_building_archetype_prm__set__internalmassdensity(self._handle, \
                internalmassdensity)
        
        @property
        def internalmasscp(self):
            """
            Element internalmasscp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 429
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__internalmasscp(self._handle)
        
        @internalmasscp.setter
        def internalmasscp(self, internalmasscp):
            _supy_driver.f90wrap_building_archetype_prm__set__internalmasscp(self._handle, \
                internalmasscp)
        
        @property
        def internalmassemissivity(self):
            """
            Element internalmassemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 430
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__internalmassemissivity(self._handle)
        
        @internalmassemissivity.setter
        def internalmassemissivity(self, internalmassemissivity):
            _supy_driver.f90wrap_building_archetype_prm__set__internalmassemissivity(self._handle, \
                internalmassemissivity)
        
        @property
        def maxheatingpower(self):
            """
            Element maxheatingpower ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 431
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__maxheatingpower(self._handle)
        
        @maxheatingpower.setter
        def maxheatingpower(self, maxheatingpower):
            _supy_driver.f90wrap_building_archetype_prm__set__maxheatingpower(self._handle, \
                maxheatingpower)
        
        @property
        def watertankwatervolume(self):
            """
            Element watertankwatervolume ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 432
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__watertankwatervolume(self._handle)
        
        @watertankwatervolume.setter
        def watertankwatervolume(self, watertankwatervolume):
            _supy_driver.f90wrap_building_archetype_prm__set__watertankwatervolume(self._handle, \
                watertankwatervolume)
        
        @property
        def maximumhotwaterheatingpower(self):
            """
            Element maximumhotwaterheatingpower ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 433
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__maximumhotwaterheating3354(self._handle)
        
        @maximumhotwaterheatingpower.setter
        def maximumhotwaterheatingpower(self, maximumhotwaterheatingpower):
            _supy_driver.f90wrap_building_archetype_prm__set__maximumhotwaterheatingde12(self._handle, \
                maximumhotwaterheatingpower)
        
        @property
        def heatingsetpointtemperature(self):
            """
            Element heatingsetpointtemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 434
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__heatingsetpointtemperature(self._handle)
        
        @heatingsetpointtemperature.setter
        def heatingsetpointtemperature(self, heatingsetpointtemperature):
            _supy_driver.f90wrap_building_archetype_prm__set__heatingsetpointtemperature(self._handle, \
                heatingsetpointtemperature)
        
        @property
        def coolingsetpointtemperature(self):
            """
            Element coolingsetpointtemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 435
            
            """
            return \
                _supy_driver.f90wrap_building_archetype_prm__get__coolingsetpointtemperature(self._handle)
        
        @coolingsetpointtemperature.setter
        def coolingsetpointtemperature(self, coolingsetpointtemperature):
            _supy_driver.f90wrap_building_archetype_prm__set__coolingsetpointtemperature(self._handle, \
                coolingsetpointtemperature)
        
        def __str__(self):
            ret = ['<building_archetype_prm>{\n']
            ret.append('    buildingcount : ')
            ret.append(repr(self.buildingcount))
            ret.append(',\n    occupants : ')
            ret.append(repr(self.occupants))
            ret.append(',\n    hhs0 : ')
            ret.append(repr(self.hhs0))
            ret.append(',\n    age_0_4 : ')
            ret.append(repr(self.age_0_4))
            ret.append(',\n    age_5_11 : ')
            ret.append(repr(self.age_5_11))
            ret.append(',\n    age_12_18 : ')
            ret.append(repr(self.age_12_18))
            ret.append(',\n    age_19_64 : ')
            ret.append(repr(self.age_19_64))
            ret.append(',\n    age_65plus : ')
            ret.append(repr(self.age_65plus))
            ret.append(',\n    stebbs_height : ')
            ret.append(repr(self.stebbs_height))
            ret.append(',\n    footprintarea : ')
            ret.append(repr(self.footprintarea))
            ret.append(',\n    wallexternalarea : ')
            ret.append(repr(self.wallexternalarea))
            ret.append(',\n    ratiointernalvolume : ')
            ret.append(repr(self.ratiointernalvolume))
            ret.append(',\n    wwr : ')
            ret.append(repr(self.wwr))
            ret.append(',\n    wallthickness : ')
            ret.append(repr(self.wallthickness))
            ret.append(',\n    walleffectiveconductivity : ')
            ret.append(repr(self.walleffectiveconductivity))
            ret.append(',\n    walldensity : ')
            ret.append(repr(self.walldensity))
            ret.append(',\n    wallcp : ')
            ret.append(repr(self.wallcp))
            ret.append(',\n    wallx1 : ')
            ret.append(repr(self.wallx1))
            ret.append(',\n    wallexternalemissivity : ')
            ret.append(repr(self.wallexternalemissivity))
            ret.append(',\n    wallinternalemissivity : ')
            ret.append(repr(self.wallinternalemissivity))
            ret.append(',\n    walltransmissivity : ')
            ret.append(repr(self.walltransmissivity))
            ret.append(',\n    wallabsorbtivity : ')
            ret.append(repr(self.wallabsorbtivity))
            ret.append(',\n    wallreflectivity : ')
            ret.append(repr(self.wallreflectivity))
            ret.append(',\n    floorthickness : ')
            ret.append(repr(self.floorthickness))
            ret.append(',\n    groundflooreffectiveconductivity : ')
            ret.append(repr(self.groundflooreffectiveconductivity))
            ret.append(',\n    groundfloordensity : ')
            ret.append(repr(self.groundfloordensity))
            ret.append(',\n    groundfloorcp : ')
            ret.append(repr(self.groundfloorcp))
            ret.append(',\n    windowthickness : ')
            ret.append(repr(self.windowthickness))
            ret.append(',\n    windoweffectiveconductivity : ')
            ret.append(repr(self.windoweffectiveconductivity))
            ret.append(',\n    windowdensity : ')
            ret.append(repr(self.windowdensity))
            ret.append(',\n    windowcp : ')
            ret.append(repr(self.windowcp))
            ret.append(',\n    windowexternalemissivity : ')
            ret.append(repr(self.windowexternalemissivity))
            ret.append(',\n    windowinternalemissivity : ')
            ret.append(repr(self.windowinternalemissivity))
            ret.append(',\n    windowtransmissivity : ')
            ret.append(repr(self.windowtransmissivity))
            ret.append(',\n    windowabsorbtivity : ')
            ret.append(repr(self.windowabsorbtivity))
            ret.append(',\n    windowreflectivity : ')
            ret.append(repr(self.windowreflectivity))
            ret.append(',\n    internalmassdensity : ')
            ret.append(repr(self.internalmassdensity))
            ret.append(',\n    internalmasscp : ')
            ret.append(repr(self.internalmasscp))
            ret.append(',\n    internalmassemissivity : ')
            ret.append(repr(self.internalmassemissivity))
            ret.append(',\n    maxheatingpower : ')
            ret.append(repr(self.maxheatingpower))
            ret.append(',\n    watertankwatervolume : ')
            ret.append(repr(self.watertankwatervolume))
            ret.append(',\n    maximumhotwaterheatingpower : ')
            ret.append(repr(self.maximumhotwaterheatingpower))
            ret.append(',\n    heatingsetpointtemperature : ')
            ret.append(repr(self.heatingsetpointtemperature))
            ret.append(',\n    coolingsetpointtemperature : ')
            ret.append(repr(self.coolingsetpointtemperature))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.STEBBS_PRM")
    class STEBBS_PRM(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=stebbs_prm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 437-487
        
        """
        def __init__(self, handle=None):
            """
            self = Stebbs_Prm()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 437-487
            
            
            Returns
            -------
            this : Stebbs_Prm
            	Object to be constructed
            
            
            Automatically generated constructor for stebbs_prm
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__stebbs_prm_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Stebbs_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 437-487
            
            Parameters
            ----------
            this : Stebbs_Prm
            	Object to be destructed
            
            
            Automatically generated destructor for stebbs_prm
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__stebbs_prm_finalise(this=self._handle)
        
        @property
        def wallinternalconvectioncoefficient(self):
            """
            Element wallinternalconvectioncoefficient ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 439
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__wallinternalconvectioncoefficient(self._handle)
        
        @wallinternalconvectioncoefficient.setter
        def wallinternalconvectioncoefficient(self, wallinternalconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__wallinternalconvectioncoefficient(self._handle, \
                wallinternalconvectioncoefficient)
        
        @property
        def internalmassconvectioncoefficient(self):
            """
            Element internalmassconvectioncoefficient ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 440
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__internalmassconvectioncoefficient(self._handle)
        
        @internalmassconvectioncoefficient.setter
        def internalmassconvectioncoefficient(self, internalmassconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__internalmassconvectioncoefficient(self._handle, \
                internalmassconvectioncoefficient)
        
        @property
        def floorinternalconvectioncoefficient(self):
            """
            Element floorinternalconvectioncoefficient ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 441
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__floorinternalconvectioncoefficient(self._handle)
        
        @floorinternalconvectioncoefficient.setter
        def floorinternalconvectioncoefficient(self, \
            floorinternalconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__floorinternalconvectioncoefficient(self._handle, \
                floorinternalconvectioncoefficient)
        
        @property
        def windowinternalconvectioncoefficient(self):
            """
            Element windowinternalconvectioncoefficient ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 442
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__windowinternalconvectioncoefficient(self._handle)
        
        @windowinternalconvectioncoefficient.setter
        def windowinternalconvectioncoefficient(self, \
            windowinternalconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__windowinternalconvectioncoefficient(self._handle, \
                windowinternalconvectioncoefficient)
        
        @property
        def wallexternalconvectioncoefficient(self):
            """
            Element wallexternalconvectioncoefficient ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 443
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__wallexternalconvectioncoefficient(self._handle)
        
        @wallexternalconvectioncoefficient.setter
        def wallexternalconvectioncoefficient(self, wallexternalconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__wallexternalconvectioncoefficient(self._handle, \
                wallexternalconvectioncoefficient)
        
        @property
        def windowexternalconvectioncoefficient(self):
            """
            Element windowexternalconvectioncoefficient ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 444
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__windowexternalconvectioncoefficient(self._handle)
        
        @windowexternalconvectioncoefficient.setter
        def windowexternalconvectioncoefficient(self, \
            windowexternalconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__windowexternalconvectioncoefficient(self._handle, \
                windowexternalconvectioncoefficient)
        
        @property
        def grounddepth(self):
            """
            Element grounddepth ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 445
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__grounddepth(self._handle)
        
        @grounddepth.setter
        def grounddepth(self, grounddepth):
            _supy_driver.f90wrap_stebbs_prm__set__grounddepth(self._handle, grounddepth)
        
        @property
        def externalgroundconductivity(self):
            """
            Element externalgroundconductivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 446
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__externalgroundconductivity(self._handle)
        
        @externalgroundconductivity.setter
        def externalgroundconductivity(self, externalgroundconductivity):
            _supy_driver.f90wrap_stebbs_prm__set__externalgroundconductivity(self._handle, \
                externalgroundconductivity)
        
        @property
        def indoorairdensity(self):
            """
            Element indoorairdensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 447
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__indoorairdensity(self._handle)
        
        @indoorairdensity.setter
        def indoorairdensity(self, indoorairdensity):
            _supy_driver.f90wrap_stebbs_prm__set__indoorairdensity(self._handle, \
                indoorairdensity)
        
        @property
        def indooraircp(self):
            """
            Element indooraircp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 448
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__indooraircp(self._handle)
        
        @indooraircp.setter
        def indooraircp(self, indooraircp):
            _supy_driver.f90wrap_stebbs_prm__set__indooraircp(self._handle, indooraircp)
        
        @property
        def wallbuildingviewfactor(self):
            """
            Element wallbuildingviewfactor ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 449
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__wallbuildingviewfactor(self._handle)
        
        @wallbuildingviewfactor.setter
        def wallbuildingviewfactor(self, wallbuildingviewfactor):
            _supy_driver.f90wrap_stebbs_prm__set__wallbuildingviewfactor(self._handle, \
                wallbuildingviewfactor)
        
        @property
        def wallgroundviewfactor(self):
            """
            Element wallgroundviewfactor ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 450
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__wallgroundviewfactor(self._handle)
        
        @wallgroundviewfactor.setter
        def wallgroundviewfactor(self, wallgroundviewfactor):
            _supy_driver.f90wrap_stebbs_prm__set__wallgroundviewfactor(self._handle, \
                wallgroundviewfactor)
        
        @property
        def wallskyviewfactor(self):
            """
            Element wallskyviewfactor ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 451
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__wallskyviewfactor(self._handle)
        
        @wallskyviewfactor.setter
        def wallskyviewfactor(self, wallskyviewfactor):
            _supy_driver.f90wrap_stebbs_prm__set__wallskyviewfactor(self._handle, \
                wallskyviewfactor)
        
        @property
        def metabolicrate(self):
            """
            Element metabolicrate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 452
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__metabolicrate(self._handle)
        
        @metabolicrate.setter
        def metabolicrate(self, metabolicrate):
            _supy_driver.f90wrap_stebbs_prm__set__metabolicrate(self._handle, metabolicrate)
        
        @property
        def latentsensibleratio(self):
            """
            Element latentsensibleratio ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 453
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__latentsensibleratio(self._handle)
        
        @latentsensibleratio.setter
        def latentsensibleratio(self, latentsensibleratio):
            _supy_driver.f90wrap_stebbs_prm__set__latentsensibleratio(self._handle, \
                latentsensibleratio)
        
        @property
        def appliancerating(self):
            """
            Element appliancerating ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 454
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__appliancerating(self._handle)
        
        @appliancerating.setter
        def appliancerating(self, appliancerating):
            _supy_driver.f90wrap_stebbs_prm__set__appliancerating(self._handle, \
                appliancerating)
        
        @property
        def totalnumberofappliances(self):
            """
            Element totalnumberofappliances ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 455
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__totalnumberofappliances(self._handle)
        
        @totalnumberofappliances.setter
        def totalnumberofappliances(self, totalnumberofappliances):
            _supy_driver.f90wrap_stebbs_prm__set__totalnumberofappliances(self._handle, \
                totalnumberofappliances)
        
        @property
        def applianceusagefactor(self):
            """
            Element applianceusagefactor ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 456
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__applianceusagefactor(self._handle)
        
        @applianceusagefactor.setter
        def applianceusagefactor(self, applianceusagefactor):
            _supy_driver.f90wrap_stebbs_prm__set__applianceusagefactor(self._handle, \
                applianceusagefactor)
        
        @property
        def heatingsystemefficiency(self):
            """
            Element heatingsystemefficiency ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 457
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__heatingsystemefficiency(self._handle)
        
        @heatingsystemefficiency.setter
        def heatingsystemefficiency(self, heatingsystemefficiency):
            _supy_driver.f90wrap_stebbs_prm__set__heatingsystemefficiency(self._handle, \
                heatingsystemefficiency)
        
        @property
        def maxcoolingpower(self):
            """
            Element maxcoolingpower ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 458
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__maxcoolingpower(self._handle)
        
        @maxcoolingpower.setter
        def maxcoolingpower(self, maxcoolingpower):
            _supy_driver.f90wrap_stebbs_prm__set__maxcoolingpower(self._handle, \
                maxcoolingpower)
        
        @property
        def coolingsystemcop(self):
            """
            Element coolingsystemcop ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 459
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__coolingsystemcop(self._handle)
        
        @coolingsystemcop.setter
        def coolingsystemcop(self, coolingsystemcop):
            _supy_driver.f90wrap_stebbs_prm__set__coolingsystemcop(self._handle, \
                coolingsystemcop)
        
        @property
        def ventilationrate(self):
            """
            Element ventilationrate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 460
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__ventilationrate(self._handle)
        
        @ventilationrate.setter
        def ventilationrate(self, ventilationrate):
            _supy_driver.f90wrap_stebbs_prm__set__ventilationrate(self._handle, \
                ventilationrate)
        
        @property
        def watertankwallthickness(self):
            """
            Element watertankwallthickness ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 461
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__watertankwallthickness(self._handle)
        
        @watertankwallthickness.setter
        def watertankwallthickness(self, watertankwallthickness):
            _supy_driver.f90wrap_stebbs_prm__set__watertankwallthickness(self._handle, \
                watertankwallthickness)
        
        @property
        def watertanksurfacearea(self):
            """
            Element watertanksurfacearea ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 462
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__watertanksurfacearea(self._handle)
        
        @watertanksurfacearea.setter
        def watertanksurfacearea(self, watertanksurfacearea):
            _supy_driver.f90wrap_stebbs_prm__set__watertanksurfacearea(self._handle, \
                watertanksurfacearea)
        
        @property
        def hotwaterheatingsetpointtemperature(self):
            """
            Element hotwaterheatingsetpointtemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 463
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwaterheatingsetpointtemperature(self._handle)
        
        @hotwaterheatingsetpointtemperature.setter
        def hotwaterheatingsetpointtemperature(self, \
            hotwaterheatingsetpointtemperature):
            _supy_driver.f90wrap_stebbs_prm__set__hotwaterheatingsetpointtemperature(self._handle, \
                hotwaterheatingsetpointtemperature)
        
        @property
        def hotwatertankwallemissivity(self):
            """
            Element hotwatertankwallemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 464
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankwallemissivity(self._handle)
        
        @hotwatertankwallemissivity.setter
        def hotwatertankwallemissivity(self, hotwatertankwallemissivity):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankwallemissivity(self._handle, \
                hotwatertankwallemissivity)
        
        @property
        def dhwvesselwallthickness(self):
            """
            Element dhwvesselwallthickness ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 465
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwvesselwallthickness(self._handle)
        
        @dhwvesselwallthickness.setter
        def dhwvesselwallthickness(self, dhwvesselwallthickness):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselwallthickness(self._handle, \
                dhwvesselwallthickness)
        
        @property
        def dhwwatervolume(self):
            """
            Element dhwwatervolume ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 466
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__dhwwatervolume(self._handle)
        
        @dhwwatervolume.setter
        def dhwwatervolume(self, dhwwatervolume):
            _supy_driver.f90wrap_stebbs_prm__set__dhwwatervolume(self._handle, \
                dhwwatervolume)
        
        @property
        def dhwsurfacearea(self):
            """
            Element dhwsurfacearea ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 467
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__dhwsurfacearea(self._handle)
        
        @dhwsurfacearea.setter
        def dhwsurfacearea(self, dhwsurfacearea):
            _supy_driver.f90wrap_stebbs_prm__set__dhwsurfacearea(self._handle, \
                dhwsurfacearea)
        
        @property
        def dhwvesselemissivity(self):
            """
            Element dhwvesselemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 468
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__dhwvesselemissivity(self._handle)
        
        @dhwvesselemissivity.setter
        def dhwvesselemissivity(self, dhwvesselemissivity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselemissivity(self._handle, \
                dhwvesselemissivity)
        
        @property
        def hotwaterflowrate(self):
            """
            Element hotwaterflowrate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 469
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__hotwaterflowrate(self._handle)
        
        @hotwaterflowrate.setter
        def hotwaterflowrate(self, hotwaterflowrate):
            _supy_driver.f90wrap_stebbs_prm__set__hotwaterflowrate(self._handle, \
                hotwaterflowrate)
        
        @property
        def dhwdrainflowrate(self):
            """
            Element dhwdrainflowrate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 470
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__dhwdrainflowrate(self._handle)
        
        @dhwdrainflowrate.setter
        def dhwdrainflowrate(self, dhwdrainflowrate):
            _supy_driver.f90wrap_stebbs_prm__set__dhwdrainflowrate(self._handle, \
                dhwdrainflowrate)
        
        @property
        def dhwspecificheatcapacity(self):
            """
            Element dhwspecificheatcapacity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 471
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwspecificheatcapacity(self._handle)
        
        @dhwspecificheatcapacity.setter
        def dhwspecificheatcapacity(self, dhwspecificheatcapacity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwspecificheatcapacity(self._handle, \
                dhwspecificheatcapacity)
        
        @property
        def hotwatertankspecificheatcapacity(self):
            """
            Element hotwatertankspecificheatcapacity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 472
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankspecificheatcapacity(self._handle)
        
        @hotwatertankspecificheatcapacity.setter
        def hotwatertankspecificheatcapacity(self, hotwatertankspecificheatcapacity):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankspecificheatcapacity(self._handle, \
                hotwatertankspecificheatcapacity)
        
        @property
        def dhwvesselspecificheatcapacity(self):
            """
            Element dhwvesselspecificheatcapacity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 473
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwvesselspecificheatcapacity(self._handle)
        
        @dhwvesselspecificheatcapacity.setter
        def dhwvesselspecificheatcapacity(self, dhwvesselspecificheatcapacity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselspecificheatcapacity(self._handle, \
                dhwvesselspecificheatcapacity)
        
        @property
        def dhwdensity(self):
            """
            Element dhwdensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 474
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__dhwdensity(self._handle)
        
        @dhwdensity.setter
        def dhwdensity(self, dhwdensity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwdensity(self._handle, dhwdensity)
        
        @property
        def hotwatertankwalldensity(self):
            """
            Element hotwatertankwalldensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 475
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankwalldensity(self._handle)
        
        @hotwatertankwalldensity.setter
        def hotwatertankwalldensity(self, hotwatertankwalldensity):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankwalldensity(self._handle, \
                hotwatertankwalldensity)
        
        @property
        def dhwvesseldensity(self):
            """
            Element dhwvesseldensity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 476
            
            """
            return _supy_driver.f90wrap_stebbs_prm__get__dhwvesseldensity(self._handle)
        
        @dhwvesseldensity.setter
        def dhwvesseldensity(self, dhwvesseldensity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesseldensity(self._handle, \
                dhwvesseldensity)
        
        @property
        def hotwatertankbuildingwallviewfactor(self):
            """
            Element hotwatertankbuildingwallviewfactor ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 477
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankbuildingwallviewfactor(self._handle)
        
        @hotwatertankbuildingwallviewfactor.setter
        def hotwatertankbuildingwallviewfactor(self, \
            hotwatertankbuildingwallviewfactor):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankbuildingwallviewfactor(self._handle, \
                hotwatertankbuildingwallviewfactor)
        
        @property
        def hotwatertankinternalmassviewfactor(self):
            """
            Element hotwatertankinternalmassviewfactor ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 478
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankinternalmassviewfactor(self._handle)
        
        @hotwatertankinternalmassviewfactor.setter
        def hotwatertankinternalmassviewfactor(self, \
            hotwatertankinternalmassviewfactor):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankinternalmassviewfactor(self._handle, \
                hotwatertankinternalmassviewfactor)
        
        @property
        def hotwatertankwallconductivity(self):
            """
            Element hotwatertankwallconductivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 479
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankwallconductivity(self._handle)
        
        @hotwatertankwallconductivity.setter
        def hotwatertankwallconductivity(self, hotwatertankwallconductivity):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankwallconductivity(self._handle, \
                hotwatertankwallconductivity)
        
        @property
        def hotwatertankinternalwallconvectioncoefficient(self):
            """
            Element hotwatertankinternalwallconvectioncoefficient ftype=real(kind(1d0) \
                pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 480
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankinternalwallconvectiona077(self._handle)
        
        @hotwatertankinternalwallconvectioncoefficient.setter
        def hotwatertankinternalwallconvectioncoefficient(self, \
            hotwatertankinternalwallconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankinternalwallconvectioncf37(self._handle, \
                hotwatertankinternalwallconvectioncoefficient)
        
        @property
        def hotwatertankexternalwallconvectioncoefficient(self):
            """
            Element hotwatertankexternalwallconvectioncoefficient ftype=real(kind(1d0) \
                pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 481
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwatertankexternalwallconvection6933(self._handle)
        
        @hotwatertankexternalwallconvectioncoefficient.setter
        def hotwatertankexternalwallconvectioncoefficient(self, \
            hotwatertankexternalwallconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__hotwatertankexternalwallconvection5c76(self._handle, \
                hotwatertankexternalwallconvectioncoefficient)
        
        @property
        def dhwvesselwallconductivity(self):
            """
            Element dhwvesselwallconductivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 482
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwvesselwallconductivity(self._handle)
        
        @dhwvesselwallconductivity.setter
        def dhwvesselwallconductivity(self, dhwvesselwallconductivity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselwallconductivity(self._handle, \
                dhwvesselwallconductivity)
        
        @property
        def dhwvesselinternalwallconvectioncoefficient(self):
            """
            Element dhwvesselinternalwallconvectioncoefficient ftype=real(kind(1d0) \
                pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 483
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwvesselinternalwallconvectioncoea143(self._handle)
        
        @dhwvesselinternalwallconvectioncoefficient.setter
        def dhwvesselinternalwallconvectioncoefficient(self, \
            dhwvesselinternalwallconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselinternalwallconvectioncoee929(self._handle, \
                dhwvesselinternalwallconvectioncoefficient)
        
        @property
        def dhwvesselexternalwallconvectioncoefficient(self):
            """
            Element dhwvesselexternalwallconvectioncoefficient ftype=real(kind(1d0) \
                pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 484
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwvesselexternalwallconvectioncoecd87(self._handle)
        
        @dhwvesselexternalwallconvectioncoefficient.setter
        def dhwvesselexternalwallconvectioncoefficient(self, \
            dhwvesselexternalwallconvectioncoefficient):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselexternalwallconvectioncoe561e(self._handle, \
                dhwvesselexternalwallconvectioncoefficient)
        
        @property
        def dhwvesselwallemissivity(self):
            """
            Element dhwvesselwallemissivity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 485
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__dhwvesselwallemissivity(self._handle)
        
        @dhwvesselwallemissivity.setter
        def dhwvesselwallemissivity(self, dhwvesselwallemissivity):
            _supy_driver.f90wrap_stebbs_prm__set__dhwvesselwallemissivity(self._handle, \
                dhwvesselwallemissivity)
        
        @property
        def hotwaterheatingefficiency(self):
            """
            Element hotwaterheatingefficiency ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 486
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__hotwaterheatingefficiency(self._handle)
        
        @hotwaterheatingefficiency.setter
        def hotwaterheatingefficiency(self, hotwaterheatingefficiency):
            _supy_driver.f90wrap_stebbs_prm__set__hotwaterheatingefficiency(self._handle, \
                hotwaterheatingefficiency)
        
        @property
        def minimumvolumeofdhwinuse(self):
            """
            Element minimumvolumeofdhwinuse ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 487
            
            """
            return \
                _supy_driver.f90wrap_stebbs_prm__get__minimumvolumeofdhwinuse(self._handle)
        
        @minimumvolumeofdhwinuse.setter
        def minimumvolumeofdhwinuse(self, minimumvolumeofdhwinuse):
            _supy_driver.f90wrap_stebbs_prm__set__minimumvolumeofdhwinuse(self._handle, \
                minimumvolumeofdhwinuse)
        
        def __str__(self):
            ret = ['<stebbs_prm>{\n']
            ret.append('    wallinternalconvectioncoefficient : ')
            ret.append(repr(self.wallinternalconvectioncoefficient))
            ret.append(',\n    internalmassconvectioncoefficient : ')
            ret.append(repr(self.internalmassconvectioncoefficient))
            ret.append(',\n    floorinternalconvectioncoefficient : ')
            ret.append(repr(self.floorinternalconvectioncoefficient))
            ret.append(',\n    windowinternalconvectioncoefficient : ')
            ret.append(repr(self.windowinternalconvectioncoefficient))
            ret.append(',\n    wallexternalconvectioncoefficient : ')
            ret.append(repr(self.wallexternalconvectioncoefficient))
            ret.append(',\n    windowexternalconvectioncoefficient : ')
            ret.append(repr(self.windowexternalconvectioncoefficient))
            ret.append(',\n    grounddepth : ')
            ret.append(repr(self.grounddepth))
            ret.append(',\n    externalgroundconductivity : ')
            ret.append(repr(self.externalgroundconductivity))
            ret.append(',\n    indoorairdensity : ')
            ret.append(repr(self.indoorairdensity))
            ret.append(',\n    indooraircp : ')
            ret.append(repr(self.indooraircp))
            ret.append(',\n    wallbuildingviewfactor : ')
            ret.append(repr(self.wallbuildingviewfactor))
            ret.append(',\n    wallgroundviewfactor : ')
            ret.append(repr(self.wallgroundviewfactor))
            ret.append(',\n    wallskyviewfactor : ')
            ret.append(repr(self.wallskyviewfactor))
            ret.append(',\n    metabolicrate : ')
            ret.append(repr(self.metabolicrate))
            ret.append(',\n    latentsensibleratio : ')
            ret.append(repr(self.latentsensibleratio))
            ret.append(',\n    appliancerating : ')
            ret.append(repr(self.appliancerating))
            ret.append(',\n    totalnumberofappliances : ')
            ret.append(repr(self.totalnumberofappliances))
            ret.append(',\n    applianceusagefactor : ')
            ret.append(repr(self.applianceusagefactor))
            ret.append(',\n    heatingsystemefficiency : ')
            ret.append(repr(self.heatingsystemefficiency))
            ret.append(',\n    maxcoolingpower : ')
            ret.append(repr(self.maxcoolingpower))
            ret.append(',\n    coolingsystemcop : ')
            ret.append(repr(self.coolingsystemcop))
            ret.append(',\n    ventilationrate : ')
            ret.append(repr(self.ventilationrate))
            ret.append(',\n    watertankwallthickness : ')
            ret.append(repr(self.watertankwallthickness))
            ret.append(',\n    watertanksurfacearea : ')
            ret.append(repr(self.watertanksurfacearea))
            ret.append(',\n    hotwaterheatingsetpointtemperature : ')
            ret.append(repr(self.hotwaterheatingsetpointtemperature))
            ret.append(',\n    hotwatertankwallemissivity : ')
            ret.append(repr(self.hotwatertankwallemissivity))
            ret.append(',\n    dhwvesselwallthickness : ')
            ret.append(repr(self.dhwvesselwallthickness))
            ret.append(',\n    dhwwatervolume : ')
            ret.append(repr(self.dhwwatervolume))
            ret.append(',\n    dhwsurfacearea : ')
            ret.append(repr(self.dhwsurfacearea))
            ret.append(',\n    dhwvesselemissivity : ')
            ret.append(repr(self.dhwvesselemissivity))
            ret.append(',\n    hotwaterflowrate : ')
            ret.append(repr(self.hotwaterflowrate))
            ret.append(',\n    dhwdrainflowrate : ')
            ret.append(repr(self.dhwdrainflowrate))
            ret.append(',\n    dhwspecificheatcapacity : ')
            ret.append(repr(self.dhwspecificheatcapacity))
            ret.append(',\n    hotwatertankspecificheatcapacity : ')
            ret.append(repr(self.hotwatertankspecificheatcapacity))
            ret.append(',\n    dhwvesselspecificheatcapacity : ')
            ret.append(repr(self.dhwvesselspecificheatcapacity))
            ret.append(',\n    dhwdensity : ')
            ret.append(repr(self.dhwdensity))
            ret.append(',\n    hotwatertankwalldensity : ')
            ret.append(repr(self.hotwatertankwalldensity))
            ret.append(',\n    dhwvesseldensity : ')
            ret.append(repr(self.dhwvesseldensity))
            ret.append(',\n    hotwatertankbuildingwallviewfactor : ')
            ret.append(repr(self.hotwatertankbuildingwallviewfactor))
            ret.append(',\n    hotwatertankinternalmassviewfactor : ')
            ret.append(repr(self.hotwatertankinternalmassviewfactor))
            ret.append(',\n    hotwatertankwallconductivity : ')
            ret.append(repr(self.hotwatertankwallconductivity))
            ret.append(',\n hotwatertankinternalwallconvectioncoefficient : ')
            ret.append(repr(self.hotwatertankinternalwallconvectioncoefficient))
            ret.append(',\n hotwatertankexternalwallconvectioncoefficient : ')
            ret.append(repr(self.hotwatertankexternalwallconvectioncoefficient))
            ret.append(',\n    dhwvesselwallconductivity : ')
            ret.append(repr(self.dhwvesselwallconductivity))
            ret.append(',\n    dhwvesselinternalwallconvectioncoefficient : ')
            ret.append(repr(self.dhwvesselinternalwallconvectioncoefficient))
            ret.append(',\n    dhwvesselexternalwallconvectioncoefficient : ')
            ret.append(repr(self.dhwvesselexternalwallconvectioncoefficient))
            ret.append(',\n    dhwvesselwallemissivity : ')
            ret.append(repr(self.dhwvesselwallemissivity))
            ret.append(',\n    hotwaterheatingefficiency : ')
            ret.append(repr(self.hotwaterheatingefficiency))
            ret.append(',\n    minimumvolumeofdhwinuse : ')
            ret.append(repr(self.minimumvolumeofdhwinuse))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_SITE")
    class SUEWS_SITE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_site)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 489-538
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Site()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 489-538
            
            
            Returns
            -------
            this : Suews_Site
            	Object to be constructed
            
            
            Automatically generated constructor for suews_site
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_site_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Site
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 489-538
            
            Parameters
            ----------
            this : Suews_Site
            	Object to be destructed
            
            
            Automatically generated destructor for suews_site
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_site_finalise(this=self._handle)
        
        def allocate(self, nlayer):
            """
            allocate__binding__suews_site(self, nlayer)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1292-1297
            
            Parameters
            ----------
            self : Suews_Site
            nlayer : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__allocate__binding__suews_site(self=self._handle, \
                nlayer=nlayer)
        
        def deallocate(self):
            """
            deallocate__binding__suews_site(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1299-1306
            
            Parameters
            ----------
            self : Suews_Site
            
            """
            _supy_driver.f90wrap_suews_def_dts__deallocate__binding__suews_site(self=self._handle)
        
        def cal_surf(self, config):
            """
            cal_surf__binding__suews_site(self, config)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1308-1398
            
            Parameters
            ----------
            self : Suews_Site
            config : Suews_Config
            
            """
            _supy_driver.f90wrap_suews_def_dts__cal_surf__binding__suews_site(self=self._handle, \
                config=config._handle)
        
        @property
        def lat(self):
            """
            Element lat ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 490
            
            """
            return _supy_driver.f90wrap_suews_site__get__lat(self._handle)
        
        @lat.setter
        def lat(self, lat):
            _supy_driver.f90wrap_suews_site__set__lat(self._handle, lat)
        
        @property
        def lon(self):
            """
            Element lon ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 491
            
            """
            return _supy_driver.f90wrap_suews_site__get__lon(self._handle)
        
        @lon.setter
        def lon(self, lon):
            _supy_driver.f90wrap_suews_site__set__lon(self._handle, lon)
        
        @property
        def alt(self):
            """
            Element alt ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 492
            
            """
            return _supy_driver.f90wrap_suews_site__get__alt(self._handle)
        
        @alt.setter
        def alt(self, alt):
            _supy_driver.f90wrap_suews_site__set__alt(self._handle, alt)
        
        @property
        def gridiv(self):
            """
            Element gridiv ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 493
            
            """
            return _supy_driver.f90wrap_suews_site__get__gridiv(self._handle)
        
        @gridiv.setter
        def gridiv(self, gridiv):
            _supy_driver.f90wrap_suews_site__set__gridiv(self._handle, gridiv)
        
        @property
        def timezone(self):
            """
            Element timezone ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 494
            
            """
            return _supy_driver.f90wrap_suews_site__get__timezone(self._handle)
        
        @timezone.setter
        def timezone(self, timezone):
            _supy_driver.f90wrap_suews_site__set__timezone(self._handle, timezone)
        
        @property
        def surfacearea(self):
            """
            Element surfacearea ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 495
            
            """
            return _supy_driver.f90wrap_suews_site__get__surfacearea(self._handle)
        
        @surfacearea.setter
        def surfacearea(self, surfacearea):
            _supy_driver.f90wrap_suews_site__set__surfacearea(self._handle, surfacearea)
        
        @property
        def z(self):
            """
            Element z ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 496
            
            """
            return _supy_driver.f90wrap_suews_site__get__z(self._handle)
        
        @z.setter
        def z(self, z):
            _supy_driver.f90wrap_suews_site__set__z(self._handle, z)
        
        @property
        def z0m_in(self):
            """
            Element z0m_in ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 497
            
            """
            return _supy_driver.f90wrap_suews_site__get__z0m_in(self._handle)
        
        @z0m_in.setter
        def z0m_in(self, z0m_in):
            _supy_driver.f90wrap_suews_site__set__z0m_in(self._handle, z0m_in)
        
        @property
        def zdm_in(self):
            """
            Element zdm_in ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 498
            
            """
            return _supy_driver.f90wrap_suews_site__get__zdm_in(self._handle)
        
        @zdm_in.setter
        def zdm_in(self, zdm_in):
            _supy_driver.f90wrap_suews_site__set__zdm_in(self._handle, zdm_in)
        
        @property
        def pipecapacity(self):
            """
            Element pipecapacity ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 499
            
            """
            return _supy_driver.f90wrap_suews_site__get__pipecapacity(self._handle)
        
        @pipecapacity.setter
        def pipecapacity(self, pipecapacity):
            _supy_driver.f90wrap_suews_site__set__pipecapacity(self._handle, pipecapacity)
        
        @property
        def runofftowater(self):
            """
            Element runofftowater ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 500
            
            """
            return _supy_driver.f90wrap_suews_site__get__runofftowater(self._handle)
        
        @runofftowater.setter
        def runofftowater(self, runofftowater):
            _supy_driver.f90wrap_suews_site__set__runofftowater(self._handle, runofftowater)
        
        @property
        def narp_trans_site(self):
            """
            Element narp_trans_site ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 501
            
            """
            return _supy_driver.f90wrap_suews_site__get__narp_trans_site(self._handle)
        
        @narp_trans_site.setter
        def narp_trans_site(self, narp_trans_site):
            _supy_driver.f90wrap_suews_site__set__narp_trans_site(self._handle, \
                narp_trans_site)
        
        @property
        def co2pointsource(self):
            """
            Element co2pointsource ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 502
            
            """
            return _supy_driver.f90wrap_suews_site__get__co2pointsource(self._handle)
        
        @co2pointsource.setter
        def co2pointsource(self, co2pointsource):
            _supy_driver.f90wrap_suews_site__set__co2pointsource(self._handle, \
                co2pointsource)
        
        @property
        def flowchange(self):
            """
            Element flowchange ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 503
            
            """
            return _supy_driver.f90wrap_suews_site__get__flowchange(self._handle)
        
        @flowchange.setter
        def flowchange(self, flowchange):
            _supy_driver.f90wrap_suews_site__set__flowchange(self._handle, flowchange)
        
        @property
        def n_buildings(self):
            """
            Element n_buildings ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 504
            
            """
            return _supy_driver.f90wrap_suews_site__get__n_buildings(self._handle)
        
        @n_buildings.setter
        def n_buildings(self, n_buildings):
            _supy_driver.f90wrap_suews_site__set__n_buildings(self._handle, n_buildings)
        
        @property
        def h_std(self):
            """
            Element h_std ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 505
            
            """
            return _supy_driver.f90wrap_suews_site__get__h_std(self._handle)
        
        @h_std.setter
        def h_std(self, h_std):
            _supy_driver.f90wrap_suews_site__set__h_std(self._handle, h_std)
        
        @property
        def lambda_c(self):
            """
            Element lambda_c ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 506
            
            """
            return _supy_driver.f90wrap_suews_site__get__lambda_c(self._handle)
        
        @lambda_c.setter
        def lambda_c(self, lambda_c):
            _supy_driver.f90wrap_suews_site__set__lambda_c(self._handle, lambda_c)
        
        @property
        def sfr_surf(self):
            """
            Element sfr_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 508
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_suews_site__array__sfr_surf(self._handle)
            if array_handle in self._arrays:
                sfr_surf = self._arrays[array_handle]
            else:
                sfr_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_suews_site__array__sfr_surf)
                self._arrays[array_handle] = sfr_surf
            return sfr_surf
        
        @sfr_surf.setter
        def sfr_surf(self, sfr_surf):
            self.sfr_surf[...] = sfr_surf
        
        @property
        def vegfraction(self):
            """
            Element vegfraction ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 509
            
            """
            return _supy_driver.f90wrap_suews_site__get__vegfraction(self._handle)
        
        @vegfraction.setter
        def vegfraction(self, vegfraction):
            _supy_driver.f90wrap_suews_site__set__vegfraction(self._handle, vegfraction)
        
        @property
        def impervfraction(self):
            """
            Element impervfraction ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 510
            
            """
            return _supy_driver.f90wrap_suews_site__get__impervfraction(self._handle)
        
        @impervfraction.setter
        def impervfraction(self, impervfraction):
            _supy_driver.f90wrap_suews_site__set__impervfraction(self._handle, \
                impervfraction)
        
        @property
        def pervfraction(self):
            """
            Element pervfraction ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 511
            
            """
            return _supy_driver.f90wrap_suews_site__get__pervfraction(self._handle)
        
        @pervfraction.setter
        def pervfraction(self, pervfraction):
            _supy_driver.f90wrap_suews_site__set__pervfraction(self._handle, pervfraction)
        
        @property
        def nonwaterfraction(self):
            """
            Element nonwaterfraction ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 512
            
            """
            return _supy_driver.f90wrap_suews_site__get__nonwaterfraction(self._handle)
        
        @nonwaterfraction.setter
        def nonwaterfraction(self, nonwaterfraction):
            _supy_driver.f90wrap_suews_site__set__nonwaterfraction(self._handle, \
                nonwaterfraction)
        
        @property
        def sfr_roof(self):
            """
            Element sfr_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 513
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_suews_site__array__sfr_roof(self._handle)
            if array_handle in self._arrays:
                sfr_roof = self._arrays[array_handle]
            else:
                sfr_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_suews_site__array__sfr_roof)
                self._arrays[array_handle] = sfr_roof
            return sfr_roof
        
        @sfr_roof.setter
        def sfr_roof(self, sfr_roof):
            self.sfr_roof[...] = sfr_roof
        
        @property
        def sfr_wall(self):
            """
            Element sfr_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 514
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_suews_site__array__sfr_wall(self._handle)
            if array_handle in self._arrays:
                sfr_wall = self._arrays[array_handle]
            else:
                sfr_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_suews_site__array__sfr_wall)
                self._arrays[array_handle] = sfr_wall
            return sfr_wall
        
        @sfr_wall.setter
        def sfr_wall(self, sfr_wall):
            self.sfr_wall[...] = sfr_wall
        
        @property
        def nlayer(self):
            """
            Element nlayer ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 515
            
            """
            return _supy_driver.f90wrap_suews_site__get__nlayer(self._handle)
        
        @nlayer.setter
        def nlayer(self, nlayer):
            _supy_driver.f90wrap_suews_site__set__nlayer(self._handle, nlayer)
        
        @property
        def spartacus(self):
            """
            Element spartacus ftype=type(spartacus_prm) pytype=Spartacus_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 516
            
            """
            spartacus_handle = _supy_driver.f90wrap_suews_site__get__spartacus(self._handle)
            if tuple(spartacus_handle) in self._objs:
                spartacus = self._objs[tuple(spartacus_handle)]
            else:
                spartacus = suews_def_dts.SPARTACUS_PRM.from_handle(spartacus_handle)
                self._objs[tuple(spartacus_handle)] = spartacus
            return spartacus
        
        @spartacus.setter
        def spartacus(self, spartacus):
            spartacus = spartacus._handle
            _supy_driver.f90wrap_suews_site__set__spartacus(self._handle, spartacus)
        
        @property
        def lumps(self):
            """
            Element lumps ftype=type(lumps_prm) pytype=Lumps_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 517
            
            """
            lumps_handle = _supy_driver.f90wrap_suews_site__get__lumps(self._handle)
            if tuple(lumps_handle) in self._objs:
                lumps = self._objs[tuple(lumps_handle)]
            else:
                lumps = suews_def_dts.LUMPS_PRM.from_handle(lumps_handle)
                self._objs[tuple(lumps_handle)] = lumps
            return lumps
        
        @lumps.setter
        def lumps(self, lumps):
            lumps = lumps._handle
            _supy_driver.f90wrap_suews_site__set__lumps(self._handle, lumps)
        
        @property
        def ehc(self):
            """
            Element ehc ftype=type(ehc_prm) pytype=Ehc_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 518
            
            """
            ehc_handle = _supy_driver.f90wrap_suews_site__get__ehc(self._handle)
            if tuple(ehc_handle) in self._objs:
                ehc = self._objs[tuple(ehc_handle)]
            else:
                ehc = suews_def_dts.EHC_PRM.from_handle(ehc_handle)
                self._objs[tuple(ehc_handle)] = ehc
            return ehc
        
        @ehc.setter
        def ehc(self, ehc):
            ehc = ehc._handle
            _supy_driver.f90wrap_suews_site__set__ehc(self._handle, ehc)
        
        @property
        def spartacus_layer(self):
            """
            Element spartacus_layer ftype=type(spartacus_layer_prm) \
                pytype=Spartacus_Layer_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 519
            
            """
            spartacus_layer_handle = \
                _supy_driver.f90wrap_suews_site__get__spartacus_layer(self._handle)
            if tuple(spartacus_layer_handle) in self._objs:
                spartacus_layer = self._objs[tuple(spartacus_layer_handle)]
            else:
                spartacus_layer = \
                    suews_def_dts.SPARTACUS_LAYER_PRM.from_handle(spartacus_layer_handle)
                self._objs[tuple(spartacus_layer_handle)] = spartacus_layer
            return spartacus_layer
        
        @spartacus_layer.setter
        def spartacus_layer(self, spartacus_layer):
            spartacus_layer = spartacus_layer._handle
            _supy_driver.f90wrap_suews_site__set__spartacus_layer(self._handle, \
                spartacus_layer)
        
        @property
        def surf_store(self):
            """
            Element surf_store ftype=type(surf_store_prm) pytype=Surf_Store_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 520
            
            """
            surf_store_handle = \
                _supy_driver.f90wrap_suews_site__get__surf_store(self._handle)
            if tuple(surf_store_handle) in self._objs:
                surf_store = self._objs[tuple(surf_store_handle)]
            else:
                surf_store = suews_def_dts.SURF_STORE_PRM.from_handle(surf_store_handle)
                self._objs[tuple(surf_store_handle)] = surf_store
            return surf_store
        
        @surf_store.setter
        def surf_store(self, surf_store):
            surf_store = surf_store._handle
            _supy_driver.f90wrap_suews_site__set__surf_store(self._handle, surf_store)
        
        @property
        def irrigation(self):
            """
            Element irrigation ftype=type(irrigation_prm) pytype=Irrigation_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 521
            
            """
            irrigation_handle = \
                _supy_driver.f90wrap_suews_site__get__irrigation(self._handle)
            if tuple(irrigation_handle) in self._objs:
                irrigation = self._objs[tuple(irrigation_handle)]
            else:
                irrigation = suews_def_dts.IRRIGATION_PRM.from_handle(irrigation_handle)
                self._objs[tuple(irrigation_handle)] = irrigation
            return irrigation
        
        @irrigation.setter
        def irrigation(self, irrigation):
            irrigation = irrigation._handle
            _supy_driver.f90wrap_suews_site__set__irrigation(self._handle, irrigation)
        
        @property
        def anthroemis(self):
            """
            Element anthroemis ftype=type(anthroemis_prm) pytype=Anthroemis_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 522
            
            """
            anthroemis_handle = \
                _supy_driver.f90wrap_suews_site__get__anthroemis(self._handle)
            if tuple(anthroemis_handle) in self._objs:
                anthroemis = self._objs[tuple(anthroemis_handle)]
            else:
                anthroemis = suews_def_dts.anthroEMIS_PRM.from_handle(anthroemis_handle)
                self._objs[tuple(anthroemis_handle)] = anthroemis
            return anthroemis
        
        @anthroemis.setter
        def anthroemis(self, anthroemis):
            anthroemis = anthroemis._handle
            _supy_driver.f90wrap_suews_site__set__anthroemis(self._handle, anthroemis)
        
        @property
        def snow(self):
            """
            Element snow ftype=type(snow_prm) pytype=Snow_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 524
            
            """
            snow_handle = _supy_driver.f90wrap_suews_site__get__snow(self._handle)
            if tuple(snow_handle) in self._objs:
                snow = self._objs[tuple(snow_handle)]
            else:
                snow = suews_def_dts.SNOW_PRM.from_handle(snow_handle)
                self._objs[tuple(snow_handle)] = snow
            return snow
        
        @snow.setter
        def snow(self, snow):
            snow = snow._handle
            _supy_driver.f90wrap_suews_site__set__snow(self._handle, snow)
        
        @property
        def conductance(self):
            """
            Element conductance ftype=type(conductance_prm) pytype=Conductance_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 525
            
            """
            conductance_handle = \
                _supy_driver.f90wrap_suews_site__get__conductance(self._handle)
            if tuple(conductance_handle) in self._objs:
                conductance = self._objs[tuple(conductance_handle)]
            else:
                conductance = suews_def_dts.CONDUCTANCE_PRM.from_handle(conductance_handle)
                self._objs[tuple(conductance_handle)] = conductance
            return conductance
        
        @conductance.setter
        def conductance(self, conductance):
            conductance = conductance._handle
            _supy_driver.f90wrap_suews_site__set__conductance(self._handle, conductance)
        
        @property
        def lc_paved(self):
            """
            Element lc_paved ftype=type(lc_paved_prm) pytype=Lc_Paved_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 526
            
            """
            lc_paved_handle = _supy_driver.f90wrap_suews_site__get__lc_paved(self._handle)
            if tuple(lc_paved_handle) in self._objs:
                lc_paved = self._objs[tuple(lc_paved_handle)]
            else:
                lc_paved = suews_def_dts.LC_PAVED_PRM.from_handle(lc_paved_handle)
                self._objs[tuple(lc_paved_handle)] = lc_paved
            return lc_paved
        
        @lc_paved.setter
        def lc_paved(self, lc_paved):
            lc_paved = lc_paved._handle
            _supy_driver.f90wrap_suews_site__set__lc_paved(self._handle, lc_paved)
        
        @property
        def lc_bldg(self):
            """
            Element lc_bldg ftype=type(lc_bldg_prm) pytype=Lc_Bldg_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 527
            
            """
            lc_bldg_handle = _supy_driver.f90wrap_suews_site__get__lc_bldg(self._handle)
            if tuple(lc_bldg_handle) in self._objs:
                lc_bldg = self._objs[tuple(lc_bldg_handle)]
            else:
                lc_bldg = suews_def_dts.LC_BLDG_PRM.from_handle(lc_bldg_handle)
                self._objs[tuple(lc_bldg_handle)] = lc_bldg
            return lc_bldg
        
        @lc_bldg.setter
        def lc_bldg(self, lc_bldg):
            lc_bldg = lc_bldg._handle
            _supy_driver.f90wrap_suews_site__set__lc_bldg(self._handle, lc_bldg)
        
        @property
        def lc_dectr(self):
            """
            Element lc_dectr ftype=type(lc_dectr_prm) pytype=Lc_Dectr_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 528
            
            """
            lc_dectr_handle = _supy_driver.f90wrap_suews_site__get__lc_dectr(self._handle)
            if tuple(lc_dectr_handle) in self._objs:
                lc_dectr = self._objs[tuple(lc_dectr_handle)]
            else:
                lc_dectr = suews_def_dts.LC_DECTR_PRM.from_handle(lc_dectr_handle)
                self._objs[tuple(lc_dectr_handle)] = lc_dectr
            return lc_dectr
        
        @lc_dectr.setter
        def lc_dectr(self, lc_dectr):
            lc_dectr = lc_dectr._handle
            _supy_driver.f90wrap_suews_site__set__lc_dectr(self._handle, lc_dectr)
        
        @property
        def lc_evetr(self):
            """
            Element lc_evetr ftype=type(lc_evetr_prm) pytype=Lc_Evetr_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 529
            
            """
            lc_evetr_handle = _supy_driver.f90wrap_suews_site__get__lc_evetr(self._handle)
            if tuple(lc_evetr_handle) in self._objs:
                lc_evetr = self._objs[tuple(lc_evetr_handle)]
            else:
                lc_evetr = suews_def_dts.LC_EVETR_PRM.from_handle(lc_evetr_handle)
                self._objs[tuple(lc_evetr_handle)] = lc_evetr
            return lc_evetr
        
        @lc_evetr.setter
        def lc_evetr(self, lc_evetr):
            lc_evetr = lc_evetr._handle
            _supy_driver.f90wrap_suews_site__set__lc_evetr(self._handle, lc_evetr)
        
        @property
        def lc_grass(self):
            """
            Element lc_grass ftype=type(lc_grass_prm) pytype=Lc_Grass_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 530
            
            """
            lc_grass_handle = _supy_driver.f90wrap_suews_site__get__lc_grass(self._handle)
            if tuple(lc_grass_handle) in self._objs:
                lc_grass = self._objs[tuple(lc_grass_handle)]
            else:
                lc_grass = suews_def_dts.LC_GRASS_PRM.from_handle(lc_grass_handle)
                self._objs[tuple(lc_grass_handle)] = lc_grass
            return lc_grass
        
        @lc_grass.setter
        def lc_grass(self, lc_grass):
            lc_grass = lc_grass._handle
            _supy_driver.f90wrap_suews_site__set__lc_grass(self._handle, lc_grass)
        
        @property
        def lc_bsoil(self):
            """
            Element lc_bsoil ftype=type(lc_bsoil_prm) pytype=Lc_Bsoil_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 531
            
            """
            lc_bsoil_handle = _supy_driver.f90wrap_suews_site__get__lc_bsoil(self._handle)
            if tuple(lc_bsoil_handle) in self._objs:
                lc_bsoil = self._objs[tuple(lc_bsoil_handle)]
            else:
                lc_bsoil = suews_def_dts.LC_BSOIL_PRM.from_handle(lc_bsoil_handle)
                self._objs[tuple(lc_bsoil_handle)] = lc_bsoil
            return lc_bsoil
        
        @lc_bsoil.setter
        def lc_bsoil(self, lc_bsoil):
            lc_bsoil = lc_bsoil._handle
            _supy_driver.f90wrap_suews_site__set__lc_bsoil(self._handle, lc_bsoil)
        
        @property
        def lc_water(self):
            """
            Element lc_water ftype=type(lc_water_prm) pytype=Lc_Water_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 532
            
            """
            lc_water_handle = _supy_driver.f90wrap_suews_site__get__lc_water(self._handle)
            if tuple(lc_water_handle) in self._objs:
                lc_water = self._objs[tuple(lc_water_handle)]
            else:
                lc_water = suews_def_dts.LC_WATER_PRM.from_handle(lc_water_handle)
                self._objs[tuple(lc_water_handle)] = lc_water
            return lc_water
        
        @lc_water.setter
        def lc_water(self, lc_water):
            lc_water = lc_water._handle
            _supy_driver.f90wrap_suews_site__set__lc_water(self._handle, lc_water)
        
        @property
        def building_archtype(self):
            """
            Element building_archtype ftype=type(building_archetype_prm) \
                pytype=Building_Archetype_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 533
            
            """
            building_archtype_handle = \
                _supy_driver.f90wrap_suews_site__get__building_archtype(self._handle)
            if tuple(building_archtype_handle) in self._objs:
                building_archtype = self._objs[tuple(building_archtype_handle)]
            else:
                building_archtype = \
                    suews_def_dts.BUILDING_ARCHETYPE_PRM.from_handle(building_archtype_handle)
                self._objs[tuple(building_archtype_handle)] = building_archtype
            return building_archtype
        
        @building_archtype.setter
        def building_archtype(self, building_archtype):
            building_archtype = building_archtype._handle
            _supy_driver.f90wrap_suews_site__set__building_archtype(self._handle, \
                building_archtype)
        
        @property
        def stebbs(self):
            """
            Element stebbs ftype=type(stebbs_prm) pytype=Stebbs_Prm
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 534
            
            """
            stebbs_handle = _supy_driver.f90wrap_suews_site__get__stebbs(self._handle)
            if tuple(stebbs_handle) in self._objs:
                stebbs = self._objs[tuple(stebbs_handle)]
            else:
                stebbs = suews_def_dts.STEBBS_PRM.from_handle(stebbs_handle)
                self._objs[tuple(stebbs_handle)] = stebbs
            return stebbs
        
        @stebbs.setter
        def stebbs(self, stebbs):
            stebbs = stebbs._handle
            _supy_driver.f90wrap_suews_site__set__stebbs(self._handle, stebbs)
        
        def __str__(self):
            ret = ['<suews_site>{\n']
            ret.append('    lat : ')
            ret.append(repr(self.lat))
            ret.append(',\n    lon : ')
            ret.append(repr(self.lon))
            ret.append(',\n    alt : ')
            ret.append(repr(self.alt))
            ret.append(',\n    gridiv : ')
            ret.append(repr(self.gridiv))
            ret.append(',\n    timezone : ')
            ret.append(repr(self.timezone))
            ret.append(',\n    surfacearea : ')
            ret.append(repr(self.surfacearea))
            ret.append(',\n    z : ')
            ret.append(repr(self.z))
            ret.append(',\n    z0m_in : ')
            ret.append(repr(self.z0m_in))
            ret.append(',\n    zdm_in : ')
            ret.append(repr(self.zdm_in))
            ret.append(',\n    pipecapacity : ')
            ret.append(repr(self.pipecapacity))
            ret.append(',\n    runofftowater : ')
            ret.append(repr(self.runofftowater))
            ret.append(',\n    narp_trans_site : ')
            ret.append(repr(self.narp_trans_site))
            ret.append(',\n    co2pointsource : ')
            ret.append(repr(self.co2pointsource))
            ret.append(',\n    flowchange : ')
            ret.append(repr(self.flowchange))
            ret.append(',\n    n_buildings : ')
            ret.append(repr(self.n_buildings))
            ret.append(',\n    h_std : ')
            ret.append(repr(self.h_std))
            ret.append(',\n    lambda_c : ')
            ret.append(repr(self.lambda_c))
            ret.append(',\n    sfr_surf : ')
            ret.append(repr(self.sfr_surf))
            ret.append(',\n    vegfraction : ')
            ret.append(repr(self.vegfraction))
            ret.append(',\n    impervfraction : ')
            ret.append(repr(self.impervfraction))
            ret.append(',\n    pervfraction : ')
            ret.append(repr(self.pervfraction))
            ret.append(',\n    nonwaterfraction : ')
            ret.append(repr(self.nonwaterfraction))
            ret.append(',\n    sfr_roof : ')
            ret.append(repr(self.sfr_roof))
            ret.append(',\n    sfr_wall : ')
            ret.append(repr(self.sfr_wall))
            ret.append(',\n    nlayer : ')
            ret.append(repr(self.nlayer))
            ret.append(',\n    spartacus : ')
            ret.append(repr(self.spartacus))
            ret.append(',\n    lumps : ')
            ret.append(repr(self.lumps))
            ret.append(',\n    ehc : ')
            ret.append(repr(self.ehc))
            ret.append(',\n    spartacus_layer : ')
            ret.append(repr(self.spartacus_layer))
            ret.append(',\n    surf_store : ')
            ret.append(repr(self.surf_store))
            ret.append(',\n    irrigation : ')
            ret.append(repr(self.irrigation))
            ret.append(',\n    anthroemis : ')
            ret.append(repr(self.anthroemis))
            ret.append(',\n    snow : ')
            ret.append(repr(self.snow))
            ret.append(',\n    conductance : ')
            ret.append(repr(self.conductance))
            ret.append(',\n    lc_paved : ')
            ret.append(repr(self.lc_paved))
            ret.append(',\n    lc_bldg : ')
            ret.append(repr(self.lc_bldg))
            ret.append(',\n    lc_dectr : ')
            ret.append(repr(self.lc_dectr))
            ret.append(',\n    lc_evetr : ')
            ret.append(repr(self.lc_evetr))
            ret.append(',\n    lc_grass : ')
            ret.append(repr(self.lc_grass))
            ret.append(',\n    lc_bsoil : ')
            ret.append(repr(self.lc_bsoil))
            ret.append(',\n    lc_water : ')
            ret.append(repr(self.lc_water))
            ret.append(',\n    building_archtype : ')
            ret.append(repr(self.building_archtype))
            ret.append(',\n    stebbs : ')
            ret.append(repr(self.stebbs))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.flag_STATE")
    class flag_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=flag_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 541-545
        
        """
        def __init__(self, handle=None):
            """
            self = Flag_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 541-545
            
            
            Returns
            -------
            this : Flag_State
            	Object to be constructed
            
            
            Automatically generated constructor for flag_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__flag_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Flag_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 541-545
            
            Parameters
            ----------
            this : Flag_State
            	Object to be destructed
            
            
            Automatically generated destructor for flag_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__flag_state_finalise(this=self._handle)
        
        @property
        def flag_converge(self):
            """
            Element flag_converge ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 542
            
            """
            return _supy_driver.f90wrap_flag_state__get__flag_converge(self._handle)
        
        @flag_converge.setter
        def flag_converge(self, flag_converge):
            _supy_driver.f90wrap_flag_state__set__flag_converge(self._handle, flag_converge)
        
        @property
        def i_iter(self):
            """
            Element i_iter ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 543
            
            """
            return _supy_driver.f90wrap_flag_state__get__i_iter(self._handle)
        
        @i_iter.setter
        def i_iter(self, i_iter):
            _supy_driver.f90wrap_flag_state__set__i_iter(self._handle, i_iter)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 545
            
            """
            return _supy_driver.f90wrap_flag_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_flag_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<flag_state>{\n']
            ret.append('    flag_converge : ')
            ret.append(repr(self.flag_converge))
            ret.append(',\n    i_iter : ')
            ret.append(repr(self.i_iter))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.anthroEmis_STATE")
    class anthroEmis_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=anthroemis_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 547-576
        
        """
        def __init__(self, handle=None):
            """
            self = Anthroemis_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 547-576
            
            
            Returns
            -------
            this : Anthroemis_State
            	Object to be constructed
            
            
            Automatically generated constructor for anthroemis_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__anthroemis_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Anthroemis_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 547-576
            
            Parameters
            ----------
            this : Anthroemis_State
            	Object to be destructed
            
            
            Automatically generated destructor for anthroemis_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__anthroemis_state_finalise(this=self._handle)
        
        @property
        def hdd_id(self):
            """
            Element hdd_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 549
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_anthroemis_state__array__hdd_id(self._handle)
            if array_handle in self._arrays:
                hdd_id = self._arrays[array_handle]
            else:
                hdd_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_anthroemis_state__array__hdd_id)
                self._arrays[array_handle] = hdd_id
            return hdd_id
        
        @hdd_id.setter
        def hdd_id(self, hdd_id):
            self.hdd_id[...] = hdd_id
        
        @property
        def fc(self):
            """
            Element fc ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 565
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc(self._handle)
        
        @fc.setter
        def fc(self, fc):
            _supy_driver.f90wrap_anthroemis_state__set__fc(self._handle, fc)
        
        @property
        def fc_anthro(self):
            """
            Element fc_anthro ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 566
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_anthro(self._handle)
        
        @fc_anthro.setter
        def fc_anthro(self, fc_anthro):
            _supy_driver.f90wrap_anthroemis_state__set__fc_anthro(self._handle, fc_anthro)
        
        @property
        def fc_biogen(self):
            """
            Element fc_biogen ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 567
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_biogen(self._handle)
        
        @fc_biogen.setter
        def fc_biogen(self, fc_biogen):
            _supy_driver.f90wrap_anthroemis_state__set__fc_biogen(self._handle, fc_biogen)
        
        @property
        def fc_build(self):
            """
            Element fc_build ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 568
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_build(self._handle)
        
        @fc_build.setter
        def fc_build(self, fc_build):
            _supy_driver.f90wrap_anthroemis_state__set__fc_build(self._handle, fc_build)
        
        @property
        def fc_metab(self):
            """
            Element fc_metab ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 569
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_metab(self._handle)
        
        @fc_metab.setter
        def fc_metab(self, fc_metab):
            _supy_driver.f90wrap_anthroemis_state__set__fc_metab(self._handle, fc_metab)
        
        @property
        def fc_photo(self):
            """
            Element fc_photo ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 570
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_photo(self._handle)
        
        @fc_photo.setter
        def fc_photo(self, fc_photo):
            _supy_driver.f90wrap_anthroemis_state__set__fc_photo(self._handle, fc_photo)
        
        @property
        def fc_point(self):
            """
            Element fc_point ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 571
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_point(self._handle)
        
        @fc_point.setter
        def fc_point(self, fc_point):
            _supy_driver.f90wrap_anthroemis_state__set__fc_point(self._handle, fc_point)
        
        @property
        def fc_respi(self):
            """
            Element fc_respi ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 572
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_respi(self._handle)
        
        @fc_respi.setter
        def fc_respi(self, fc_respi):
            _supy_driver.f90wrap_anthroemis_state__set__fc_respi(self._handle, fc_respi)
        
        @property
        def fc_traff(self):
            """
            Element fc_traff ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 573
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__fc_traff(self._handle)
        
        @fc_traff.setter
        def fc_traff(self, fc_traff):
            _supy_driver.f90wrap_anthroemis_state__set__fc_traff(self._handle, fc_traff)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 576
            
            """
            return _supy_driver.f90wrap_anthroemis_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_anthroemis_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<anthroemis_state>{\n']
            ret.append('    hdd_id : ')
            ret.append(repr(self.hdd_id))
            ret.append(',\n    fc : ')
            ret.append(repr(self.fc))
            ret.append(',\n    fc_anthro : ')
            ret.append(repr(self.fc_anthro))
            ret.append(',\n    fc_biogen : ')
            ret.append(repr(self.fc_biogen))
            ret.append(',\n    fc_build : ')
            ret.append(repr(self.fc_build))
            ret.append(',\n    fc_metab : ')
            ret.append(repr(self.fc_metab))
            ret.append(',\n    fc_photo : ')
            ret.append(repr(self.fc_photo))
            ret.append(',\n    fc_point : ')
            ret.append(repr(self.fc_point))
            ret.append(',\n    fc_respi : ')
            ret.append(repr(self.fc_respi))
            ret.append(',\n    fc_traff : ')
            ret.append(repr(self.fc_traff))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.OHM_STATE")
    class OHM_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=ohm_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 578-595
        
        """
        def __init__(self, handle=None):
            """
            self = Ohm_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 578-595
            
            
            Returns
            -------
            this : Ohm_State
            	Object to be constructed
            
            
            Automatically generated constructor for ohm_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__ohm_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Ohm_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 578-595
            
            Parameters
            ----------
            this : Ohm_State
            	Object to be destructed
            
            
            Automatically generated destructor for ohm_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__ohm_state_finalise(this=self._handle)
        
        @property
        def qn_av(self):
            """
            Element qn_av ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 579
            
            """
            return _supy_driver.f90wrap_ohm_state__get__qn_av(self._handle)
        
        @qn_av.setter
        def qn_av(self, qn_av):
            _supy_driver.f90wrap_ohm_state__set__qn_av(self._handle, qn_av)
        
        @property
        def dqndt(self):
            """
            Element dqndt ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 580
            
            """
            return _supy_driver.f90wrap_ohm_state__get__dqndt(self._handle)
        
        @dqndt.setter
        def dqndt(self, dqndt):
            _supy_driver.f90wrap_ohm_state__set__dqndt(self._handle, dqndt)
        
        @property
        def qn_s_av(self):
            """
            Element qn_s_av ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 581
            
            """
            return _supy_driver.f90wrap_ohm_state__get__qn_s_av(self._handle)
        
        @qn_s_av.setter
        def qn_s_av(self, qn_s_av):
            _supy_driver.f90wrap_ohm_state__set__qn_s_av(self._handle, qn_s_av)
        
        @property
        def dqnsdt(self):
            """
            Element dqnsdt ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 582
            
            """
            return _supy_driver.f90wrap_ohm_state__get__dqnsdt(self._handle)
        
        @dqnsdt.setter
        def dqnsdt(self, dqnsdt):
            _supy_driver.f90wrap_ohm_state__set__dqnsdt(self._handle, dqnsdt)
        
        @property
        def a1(self):
            """
            Element a1 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 583
            
            """
            return _supy_driver.f90wrap_ohm_state__get__a1(self._handle)
        
        @a1.setter
        def a1(self, a1):
            _supy_driver.f90wrap_ohm_state__set__a1(self._handle, a1)
        
        @property
        def a2(self):
            """
            Element a2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 584
            
            """
            return _supy_driver.f90wrap_ohm_state__get__a2(self._handle)
        
        @a2.setter
        def a2(self, a2):
            _supy_driver.f90wrap_ohm_state__set__a2(self._handle, a2)
        
        @property
        def a3(self):
            """
            Element a3 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 585
            
            """
            return _supy_driver.f90wrap_ohm_state__get__a3(self._handle)
        
        @a3.setter
        def a3(self, a3):
            _supy_driver.f90wrap_ohm_state__set__a3(self._handle, a3)
        
        @property
        def t2_prev(self):
            """
            Element t2_prev ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 587
            
            """
            return _supy_driver.f90wrap_ohm_state__get__t2_prev(self._handle)
        
        @t2_prev.setter
        def t2_prev(self, t2_prev):
            _supy_driver.f90wrap_ohm_state__set__t2_prev(self._handle, t2_prev)
        
        @property
        def ws_rav(self):
            """
            Element ws_rav ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 588
            
            """
            return _supy_driver.f90wrap_ohm_state__get__ws_rav(self._handle)
        
        @ws_rav.setter
        def ws_rav(self, ws_rav):
            _supy_driver.f90wrap_ohm_state__set__ws_rav(self._handle, ws_rav)
        
        @property
        def tair_prev(self):
            """
            Element tair_prev ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 589
            
            """
            return _supy_driver.f90wrap_ohm_state__get__tair_prev(self._handle)
        
        @tair_prev.setter
        def tair_prev(self, tair_prev):
            _supy_driver.f90wrap_ohm_state__set__tair_prev(self._handle, tair_prev)
        
        @property
        def qn_rav(self):
            """
            Element qn_rav ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 590
            
            """
            return _supy_driver.f90wrap_ohm_state__get__qn_rav(self._handle)
        
        @qn_rav.setter
        def qn_rav(self, qn_rav):
            _supy_driver.f90wrap_ohm_state__set__qn_rav(self._handle, qn_rav)
        
        @property
        def a1_bldg(self):
            """
            Element a1_bldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 591
            
            """
            return _supy_driver.f90wrap_ohm_state__get__a1_bldg(self._handle)
        
        @a1_bldg.setter
        def a1_bldg(self, a1_bldg):
            _supy_driver.f90wrap_ohm_state__set__a1_bldg(self._handle, a1_bldg)
        
        @property
        def a2_bldg(self):
            """
            Element a2_bldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 592
            
            """
            return _supy_driver.f90wrap_ohm_state__get__a2_bldg(self._handle)
        
        @a2_bldg.setter
        def a2_bldg(self, a2_bldg):
            _supy_driver.f90wrap_ohm_state__set__a2_bldg(self._handle, a2_bldg)
        
        @property
        def a3_bldg(self):
            """
            Element a3_bldg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 593
            
            """
            return _supy_driver.f90wrap_ohm_state__get__a3_bldg(self._handle)
        
        @a3_bldg.setter
        def a3_bldg(self, a3_bldg):
            _supy_driver.f90wrap_ohm_state__set__a3_bldg(self._handle, a3_bldg)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 595
            
            """
            return _supy_driver.f90wrap_ohm_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_ohm_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<ohm_state>{\n']
            ret.append('    qn_av : ')
            ret.append(repr(self.qn_av))
            ret.append(',\n    dqndt : ')
            ret.append(repr(self.dqndt))
            ret.append(',\n    qn_s_av : ')
            ret.append(repr(self.qn_s_av))
            ret.append(',\n    dqnsdt : ')
            ret.append(repr(self.dqnsdt))
            ret.append(',\n    a1 : ')
            ret.append(repr(self.a1))
            ret.append(',\n    a2 : ')
            ret.append(repr(self.a2))
            ret.append(',\n    a3 : ')
            ret.append(repr(self.a3))
            ret.append(',\n    t2_prev : ')
            ret.append(repr(self.t2_prev))
            ret.append(',\n    ws_rav : ')
            ret.append(repr(self.ws_rav))
            ret.append(',\n    tair_prev : ')
            ret.append(repr(self.tair_prev))
            ret.append(',\n    qn_rav : ')
            ret.append(repr(self.qn_rav))
            ret.append(',\n    a1_bldg : ')
            ret.append(repr(self.a1_bldg))
            ret.append(',\n    a2_bldg : ')
            ret.append(repr(self.a2_bldg))
            ret.append(',\n    a3_bldg : ')
            ret.append(repr(self.a3_bldg))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.solar_State")
    class solar_State(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=solar_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 597-602
        
        """
        def __init__(self, handle=None):
            """
            self = Solar_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 597-602
            
            
            Returns
            -------
            this : Solar_State
            	Object to be constructed
            
            
            Automatically generated constructor for solar_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__solar_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Solar_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 597-602
            
            Parameters
            ----------
            this : Solar_State
            	Object to be destructed
            
            
            Automatically generated destructor for solar_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__solar_state_finalise(this=self._handle)
        
        @property
        def azimuth_deg(self):
            """
            Element azimuth_deg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 598
            
            """
            return _supy_driver.f90wrap_solar_state__get__azimuth_deg(self._handle)
        
        @azimuth_deg.setter
        def azimuth_deg(self, azimuth_deg):
            _supy_driver.f90wrap_solar_state__set__azimuth_deg(self._handle, azimuth_deg)
        
        @property
        def zenith_deg(self):
            """
            Element zenith_deg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 599
            
            """
            return _supy_driver.f90wrap_solar_state__get__zenith_deg(self._handle)
        
        @zenith_deg.setter
        def zenith_deg(self, zenith_deg):
            _supy_driver.f90wrap_solar_state__set__zenith_deg(self._handle, zenith_deg)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 602
            
            """
            return _supy_driver.f90wrap_solar_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_solar_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<solar_state>{\n']
            ret.append('    azimuth_deg : ')
            ret.append(repr(self.azimuth_deg))
            ret.append(',\n    zenith_deg : ')
            ret.append(repr(self.zenith_deg))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.atm_state")
    class atm_state(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=atm_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 604-639
        
        """
        def __init__(self, handle=None):
            """
            self = Atm_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 604-639
            
            
            Returns
            -------
            this : Atm_State
            	Object to be constructed
            
            
            Automatically generated constructor for atm_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__atm_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Atm_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 604-639
            
            Parameters
            ----------
            this : Atm_State
            	Object to be destructed
            
            
            Automatically generated destructor for atm_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__atm_state_finalise(this=self._handle)
        
        @property
        def fcld(self):
            """
            Element fcld ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 605
            
            """
            return _supy_driver.f90wrap_atm_state__get__fcld(self._handle)
        
        @fcld.setter
        def fcld(self, fcld):
            _supy_driver.f90wrap_atm_state__set__fcld(self._handle, fcld)
        
        @property
        def avcp(self):
            """
            Element avcp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 606
            
            """
            return _supy_driver.f90wrap_atm_state__get__avcp(self._handle)
        
        @avcp.setter
        def avcp(self, avcp):
            _supy_driver.f90wrap_atm_state__set__avcp(self._handle, avcp)
        
        @property
        def dens_dry(self):
            """
            Element dens_dry ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 607
            
            """
            return _supy_driver.f90wrap_atm_state__get__dens_dry(self._handle)
        
        @dens_dry.setter
        def dens_dry(self, dens_dry):
            _supy_driver.f90wrap_atm_state__set__dens_dry(self._handle, dens_dry)
        
        @property
        def avdens(self):
            """
            Element avdens ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 608
            
            """
            return _supy_driver.f90wrap_atm_state__get__avdens(self._handle)
        
        @avdens.setter
        def avdens(self, avdens):
            _supy_driver.f90wrap_atm_state__set__avdens(self._handle, avdens)
        
        @property
        def dq(self):
            """
            Element dq ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 609
            
            """
            return _supy_driver.f90wrap_atm_state__get__dq(self._handle)
        
        @dq.setter
        def dq(self, dq):
            _supy_driver.f90wrap_atm_state__set__dq(self._handle, dq)
        
        @property
        def ea_hpa(self):
            """
            Element ea_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 610
            
            """
            return _supy_driver.f90wrap_atm_state__get__ea_hpa(self._handle)
        
        @ea_hpa.setter
        def ea_hpa(self, ea_hpa):
            _supy_driver.f90wrap_atm_state__set__ea_hpa(self._handle, ea_hpa)
        
        @property
        def es_hpa(self):
            """
            Element es_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 611
            
            """
            return _supy_driver.f90wrap_atm_state__get__es_hpa(self._handle)
        
        @es_hpa.setter
        def es_hpa(self, es_hpa):
            _supy_driver.f90wrap_atm_state__set__es_hpa(self._handle, es_hpa)
        
        @property
        def lv_j_kg(self):
            """
            Element lv_j_kg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 612
            
            """
            return _supy_driver.f90wrap_atm_state__get__lv_j_kg(self._handle)
        
        @lv_j_kg.setter
        def lv_j_kg(self, lv_j_kg):
            _supy_driver.f90wrap_atm_state__set__lv_j_kg(self._handle, lv_j_kg)
        
        @property
        def lvs_j_kg(self):
            """
            Element lvs_j_kg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 613
            
            """
            return _supy_driver.f90wrap_atm_state__get__lvs_j_kg(self._handle)
        
        @lvs_j_kg.setter
        def lvs_j_kg(self, lvs_j_kg):
            _supy_driver.f90wrap_atm_state__set__lvs_j_kg(self._handle, lvs_j_kg)
        
        @property
        def tlv(self):
            """
            Element tlv ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 614
            
            """
            return _supy_driver.f90wrap_atm_state__get__tlv(self._handle)
        
        @tlv.setter
        def tlv(self, tlv):
            _supy_driver.f90wrap_atm_state__set__tlv(self._handle, tlv)
        
        @property
        def psyc_hpa(self):
            """
            Element psyc_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 615
            
            """
            return _supy_driver.f90wrap_atm_state__get__psyc_hpa(self._handle)
        
        @psyc_hpa.setter
        def psyc_hpa(self, psyc_hpa):
            _supy_driver.f90wrap_atm_state__set__psyc_hpa(self._handle, psyc_hpa)
        
        @property
        def psycice_hpa(self):
            """
            Element psycice_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 616
            
            """
            return _supy_driver.f90wrap_atm_state__get__psycice_hpa(self._handle)
        
        @psycice_hpa.setter
        def psycice_hpa(self, psycice_hpa):
            _supy_driver.f90wrap_atm_state__set__psycice_hpa(self._handle, psycice_hpa)
        
        @property
        def s_pa(self):
            """
            Element s_pa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 617
            
            """
            return _supy_driver.f90wrap_atm_state__get__s_pa(self._handle)
        
        @s_pa.setter
        def s_pa(self, s_pa):
            _supy_driver.f90wrap_atm_state__set__s_pa(self._handle, s_pa)
        
        @property
        def s_hpa(self):
            """
            Element s_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 618
            
            """
            return _supy_driver.f90wrap_atm_state__get__s_hpa(self._handle)
        
        @s_hpa.setter
        def s_hpa(self, s_hpa):
            _supy_driver.f90wrap_atm_state__set__s_hpa(self._handle, s_hpa)
        
        @property
        def sice_hpa(self):
            """
            Element sice_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 619
            
            """
            return _supy_driver.f90wrap_atm_state__get__sice_hpa(self._handle)
        
        @sice_hpa.setter
        def sice_hpa(self, sice_hpa):
            _supy_driver.f90wrap_atm_state__set__sice_hpa(self._handle, sice_hpa)
        
        @property
        def vpd_hpa(self):
            """
            Element vpd_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 620
            
            """
            return _supy_driver.f90wrap_atm_state__get__vpd_hpa(self._handle)
        
        @vpd_hpa.setter
        def vpd_hpa(self, vpd_hpa):
            _supy_driver.f90wrap_atm_state__set__vpd_hpa(self._handle, vpd_hpa)
        
        @property
        def vpd_pa(self):
            """
            Element vpd_pa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 621
            
            """
            return _supy_driver.f90wrap_atm_state__get__vpd_pa(self._handle)
        
        @vpd_pa.setter
        def vpd_pa(self, vpd_pa):
            _supy_driver.f90wrap_atm_state__set__vpd_pa(self._handle, vpd_pa)
        
        @property
        def u10_ms(self):
            """
            Element u10_ms ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 622
            
            """
            return _supy_driver.f90wrap_atm_state__get__u10_ms(self._handle)
        
        @u10_ms.setter
        def u10_ms(self, u10_ms):
            _supy_driver.f90wrap_atm_state__set__u10_ms(self._handle, u10_ms)
        
        @property
        def u_hbh(self):
            """
            Element u_hbh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 623
            
            """
            return _supy_driver.f90wrap_atm_state__get__u_hbh(self._handle)
        
        @u_hbh.setter
        def u_hbh(self, u_hbh):
            _supy_driver.f90wrap_atm_state__set__u_hbh(self._handle, u_hbh)
        
        @property
        def t2_c(self):
            """
            Element t2_c ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 624
            
            """
            return _supy_driver.f90wrap_atm_state__get__t2_c(self._handle)
        
        @t2_c.setter
        def t2_c(self, t2_c):
            _supy_driver.f90wrap_atm_state__set__t2_c(self._handle, t2_c)
        
        @property
        def t_hbh_c(self):
            """
            Element t_hbh_c ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 625
            
            """
            return _supy_driver.f90wrap_atm_state__get__t_hbh_c(self._handle)
        
        @t_hbh_c.setter
        def t_hbh_c(self, t_hbh_c):
            _supy_driver.f90wrap_atm_state__set__t_hbh_c(self._handle, t_hbh_c)
        
        @property
        def q2_gkg(self):
            """
            Element q2_gkg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 626
            
            """
            return _supy_driver.f90wrap_atm_state__get__q2_gkg(self._handle)
        
        @q2_gkg.setter
        def q2_gkg(self, q2_gkg):
            _supy_driver.f90wrap_atm_state__set__q2_gkg(self._handle, q2_gkg)
        
        @property
        def rh2(self):
            """
            Element rh2 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 627
            
            """
            return _supy_driver.f90wrap_atm_state__get__rh2(self._handle)
        
        @rh2.setter
        def rh2(self, rh2):
            _supy_driver.f90wrap_atm_state__set__rh2(self._handle, rh2)
        
        @property
        def l_mod(self):
            """
            Element l_mod ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 628
            
            """
            return _supy_driver.f90wrap_atm_state__get__l_mod(self._handle)
        
        @l_mod.setter
        def l_mod(self, l_mod):
            _supy_driver.f90wrap_atm_state__set__l_mod(self._handle, l_mod)
        
        @property
        def zl(self):
            """
            Element zl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 629
            
            """
            return _supy_driver.f90wrap_atm_state__get__zl(self._handle)
        
        @zl.setter
        def zl(self, zl):
            _supy_driver.f90wrap_atm_state__set__zl(self._handle, zl)
        
        @property
        def ra_h(self):
            """
            Element ra_h ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 630
            
            """
            return _supy_driver.f90wrap_atm_state__get__ra_h(self._handle)
        
        @ra_h.setter
        def ra_h(self, ra_h):
            _supy_driver.f90wrap_atm_state__set__ra_h(self._handle, ra_h)
        
        @property
        def rs(self):
            """
            Element rs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 631
            
            """
            return _supy_driver.f90wrap_atm_state__get__rs(self._handle)
        
        @rs.setter
        def rs(self, rs):
            _supy_driver.f90wrap_atm_state__set__rs(self._handle, rs)
        
        @property
        def ustar(self):
            """
            Element ustar ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 632
            
            """
            return _supy_driver.f90wrap_atm_state__get__ustar(self._handle)
        
        @ustar.setter
        def ustar(self, ustar):
            _supy_driver.f90wrap_atm_state__set__ustar(self._handle, ustar)
        
        @property
        def tstar(self):
            """
            Element tstar ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 633
            
            """
            return _supy_driver.f90wrap_atm_state__get__tstar(self._handle)
        
        @tstar.setter
        def tstar(self, tstar):
            _supy_driver.f90wrap_atm_state__set__tstar(self._handle, tstar)
        
        @property
        def rb(self):
            """
            Element rb ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 634
            
            """
            return _supy_driver.f90wrap_atm_state__get__rb(self._handle)
        
        @rb.setter
        def rb(self, rb):
            _supy_driver.f90wrap_atm_state__set__rb(self._handle, rb)
        
        @property
        def tair_av(self):
            """
            Element tair_av ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 635
            
            """
            return _supy_driver.f90wrap_atm_state__get__tair_av(self._handle)
        
        @tair_av.setter
        def tair_av(self, tair_av):
            _supy_driver.f90wrap_atm_state__set__tair_av(self._handle, tair_av)
        
        @property
        def rss_surf(self):
            """
            Element rss_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 636
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_atm_state__array__rss_surf(self._handle)
            if array_handle in self._arrays:
                rss_surf = self._arrays[array_handle]
            else:
                rss_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_atm_state__array__rss_surf)
                self._arrays[array_handle] = rss_surf
            return rss_surf
        
        @rss_surf.setter
        def rss_surf(self, rss_surf):
            self.rss_surf[...] = rss_surf
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 639
            
            """
            return _supy_driver.f90wrap_atm_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_atm_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<atm_state>{\n']
            ret.append('    fcld : ')
            ret.append(repr(self.fcld))
            ret.append(',\n    avcp : ')
            ret.append(repr(self.avcp))
            ret.append(',\n    dens_dry : ')
            ret.append(repr(self.dens_dry))
            ret.append(',\n    avdens : ')
            ret.append(repr(self.avdens))
            ret.append(',\n    dq : ')
            ret.append(repr(self.dq))
            ret.append(',\n    ea_hpa : ')
            ret.append(repr(self.ea_hpa))
            ret.append(',\n    es_hpa : ')
            ret.append(repr(self.es_hpa))
            ret.append(',\n    lv_j_kg : ')
            ret.append(repr(self.lv_j_kg))
            ret.append(',\n    lvs_j_kg : ')
            ret.append(repr(self.lvs_j_kg))
            ret.append(',\n    tlv : ')
            ret.append(repr(self.tlv))
            ret.append(',\n    psyc_hpa : ')
            ret.append(repr(self.psyc_hpa))
            ret.append(',\n    psycice_hpa : ')
            ret.append(repr(self.psycice_hpa))
            ret.append(',\n    s_pa : ')
            ret.append(repr(self.s_pa))
            ret.append(',\n    s_hpa : ')
            ret.append(repr(self.s_hpa))
            ret.append(',\n    sice_hpa : ')
            ret.append(repr(self.sice_hpa))
            ret.append(',\n    vpd_hpa : ')
            ret.append(repr(self.vpd_hpa))
            ret.append(',\n    vpd_pa : ')
            ret.append(repr(self.vpd_pa))
            ret.append(',\n    u10_ms : ')
            ret.append(repr(self.u10_ms))
            ret.append(',\n    u_hbh : ')
            ret.append(repr(self.u_hbh))
            ret.append(',\n    t2_c : ')
            ret.append(repr(self.t2_c))
            ret.append(',\n    t_hbh_c : ')
            ret.append(repr(self.t_hbh_c))
            ret.append(',\n    q2_gkg : ')
            ret.append(repr(self.q2_gkg))
            ret.append(',\n    rh2 : ')
            ret.append(repr(self.rh2))
            ret.append(',\n    l_mod : ')
            ret.append(repr(self.l_mod))
            ret.append(',\n    zl : ')
            ret.append(repr(self.zl))
            ret.append(',\n    ra_h : ')
            ret.append(repr(self.ra_h))
            ret.append(',\n    rs : ')
            ret.append(repr(self.rs))
            ret.append(',\n    ustar : ')
            ret.append(repr(self.ustar))
            ret.append(',\n    tstar : ')
            ret.append(repr(self.tstar))
            ret.append(',\n    rb : ')
            ret.append(repr(self.rb))
            ret.append(',\n    tair_av : ')
            ret.append(repr(self.tair_av))
            ret.append(',\n    rss_surf : ')
            ret.append(repr(self.rss_surf))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.PHENOLOGY_STATE")
    class PHENOLOGY_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=phenology_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 641-666
        
        """
        def __init__(self, handle=None):
            """
            self = Phenology_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 641-666
            
            
            Returns
            -------
            this : Phenology_State
            	Object to be constructed
            
            
            Automatically generated constructor for phenology_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__phenology_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Phenology_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 641-666
            
            Parameters
            ----------
            this : Phenology_State
            	Object to be destructed
            
            
            Automatically generated destructor for phenology_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__phenology_state_finalise(this=self._handle)
        
        @property
        def alb(self):
            """
            Element alb ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 642
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__alb(self._handle)
            if array_handle in self._arrays:
                alb = self._arrays[array_handle]
            else:
                alb = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__alb)
                self._arrays[array_handle] = alb
            return alb
        
        @alb.setter
        def alb(self, alb):
            self.alb[...] = alb
        
        @property
        def lai_id(self):
            """
            Element lai_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 643
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__lai_id(self._handle)
            if array_handle in self._arrays:
                lai_id = self._arrays[array_handle]
            else:
                lai_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__lai_id)
                self._arrays[array_handle] = lai_id
            return lai_id
        
        @lai_id.setter
        def lai_id(self, lai_id):
            self.lai_id[...] = lai_id
        
        @property
        def gdd_id(self):
            """
            Element gdd_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 644
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__gdd_id(self._handle)
            if array_handle in self._arrays:
                gdd_id = self._arrays[array_handle]
            else:
                gdd_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__gdd_id)
                self._arrays[array_handle] = gdd_id
            return gdd_id
        
        @gdd_id.setter
        def gdd_id(self, gdd_id):
            self.gdd_id[...] = gdd_id
        
        @property
        def sdd_id(self):
            """
            Element sdd_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 645
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__sdd_id(self._handle)
            if array_handle in self._arrays:
                sdd_id = self._arrays[array_handle]
            else:
                sdd_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__sdd_id)
                self._arrays[array_handle] = sdd_id
            return sdd_id
        
        @sdd_id.setter
        def sdd_id(self, sdd_id):
            self.sdd_id[...] = sdd_id
        
        @property
        def vegphenlumps(self):
            """
            Element vegphenlumps ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 646
            
            """
            return _supy_driver.f90wrap_phenology_state__get__vegphenlumps(self._handle)
        
        @vegphenlumps.setter
        def vegphenlumps(self, vegphenlumps):
            _supy_driver.f90wrap_phenology_state__set__vegphenlumps(self._handle, \
                vegphenlumps)
        
        @property
        def porosity_id(self):
            """
            Element porosity_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 647
            
            """
            return _supy_driver.f90wrap_phenology_state__get__porosity_id(self._handle)
        
        @porosity_id.setter
        def porosity_id(self, porosity_id):
            _supy_driver.f90wrap_phenology_state__set__porosity_id(self._handle, \
                porosity_id)
        
        @property
        def decidcap_id(self):
            """
            Element decidcap_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 648
            
            """
            return _supy_driver.f90wrap_phenology_state__get__decidcap_id(self._handle)
        
        @decidcap_id.setter
        def decidcap_id(self, decidcap_id):
            _supy_driver.f90wrap_phenology_state__set__decidcap_id(self._handle, \
                decidcap_id)
        
        @property
        def albdectr_id(self):
            """
            Element albdectr_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 649
            
            """
            return _supy_driver.f90wrap_phenology_state__get__albdectr_id(self._handle)
        
        @albdectr_id.setter
        def albdectr_id(self, albdectr_id):
            _supy_driver.f90wrap_phenology_state__set__albdectr_id(self._handle, \
                albdectr_id)
        
        @property
        def albevetr_id(self):
            """
            Element albevetr_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 650
            
            """
            return _supy_driver.f90wrap_phenology_state__get__albevetr_id(self._handle)
        
        @albevetr_id.setter
        def albevetr_id(self, albevetr_id):
            _supy_driver.f90wrap_phenology_state__set__albevetr_id(self._handle, \
                albevetr_id)
        
        @property
        def albgrass_id(self):
            """
            Element albgrass_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 651
            
            """
            return _supy_driver.f90wrap_phenology_state__get__albgrass_id(self._handle)
        
        @albgrass_id.setter
        def albgrass_id(self, albgrass_id):
            _supy_driver.f90wrap_phenology_state__set__albgrass_id(self._handle, \
                albgrass_id)
        
        @property
        def tmin_id(self):
            """
            Element tmin_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 652
            
            """
            return _supy_driver.f90wrap_phenology_state__get__tmin_id(self._handle)
        
        @tmin_id.setter
        def tmin_id(self, tmin_id):
            _supy_driver.f90wrap_phenology_state__set__tmin_id(self._handle, tmin_id)
        
        @property
        def tmax_id(self):
            """
            Element tmax_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 653
            
            """
            return _supy_driver.f90wrap_phenology_state__get__tmax_id(self._handle)
        
        @tmax_id.setter
        def tmax_id(self, tmax_id):
            _supy_driver.f90wrap_phenology_state__set__tmax_id(self._handle, tmax_id)
        
        @property
        def lenday_id(self):
            """
            Element lenday_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 654
            
            """
            return _supy_driver.f90wrap_phenology_state__get__lenday_id(self._handle)
        
        @lenday_id.setter
        def lenday_id(self, lenday_id):
            _supy_driver.f90wrap_phenology_state__set__lenday_id(self._handle, lenday_id)
        
        @property
        def tempveg(self):
            """
            Element tempveg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 655
            
            """
            return _supy_driver.f90wrap_phenology_state__get__tempveg(self._handle)
        
        @tempveg.setter
        def tempveg(self, tempveg):
            _supy_driver.f90wrap_phenology_state__set__tempveg(self._handle, tempveg)
        
        @property
        def storedrainprm(self):
            """
            Element storedrainprm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 656
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_phenology_state__array__storedrainprm(self._handle)
            if array_handle in self._arrays:
                storedrainprm = self._arrays[array_handle]
            else:
                storedrainprm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_phenology_state__array__storedrainprm)
                self._arrays[array_handle] = storedrainprm
            return storedrainprm
        
        @storedrainprm.setter
        def storedrainprm(self, storedrainprm):
            self.storedrainprm[...] = storedrainprm
        
        @property
        def gfunc(self):
            """
            Element gfunc ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 657
            
            """
            return _supy_driver.f90wrap_phenology_state__get__gfunc(self._handle)
        
        @gfunc.setter
        def gfunc(self, gfunc):
            _supy_driver.f90wrap_phenology_state__set__gfunc(self._handle, gfunc)
        
        @property
        def gsc(self):
            """
            Element gsc ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 658
            
            """
            return _supy_driver.f90wrap_phenology_state__get__gsc(self._handle)
        
        @gsc.setter
        def gsc(self, gsc):
            _supy_driver.f90wrap_phenology_state__set__gsc(self._handle, gsc)
        
        @property
        def g_kdown(self):
            """
            Element g_kdown ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 659
            
            """
            return _supy_driver.f90wrap_phenology_state__get__g_kdown(self._handle)
        
        @g_kdown.setter
        def g_kdown(self, g_kdown):
            _supy_driver.f90wrap_phenology_state__set__g_kdown(self._handle, g_kdown)
        
        @property
        def g_dq(self):
            """
            Element g_dq ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 660
            
            """
            return _supy_driver.f90wrap_phenology_state__get__g_dq(self._handle)
        
        @g_dq.setter
        def g_dq(self, g_dq):
            _supy_driver.f90wrap_phenology_state__set__g_dq(self._handle, g_dq)
        
        @property
        def g_ta(self):
            """
            Element g_ta ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 661
            
            """
            return _supy_driver.f90wrap_phenology_state__get__g_ta(self._handle)
        
        @g_ta.setter
        def g_ta(self, g_ta):
            _supy_driver.f90wrap_phenology_state__set__g_ta(self._handle, g_ta)
        
        @property
        def g_smd(self):
            """
            Element g_smd ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 662
            
            """
            return _supy_driver.f90wrap_phenology_state__get__g_smd(self._handle)
        
        @g_smd.setter
        def g_smd(self, g_smd):
            _supy_driver.f90wrap_phenology_state__set__g_smd(self._handle, g_smd)
        
        @property
        def g_lai(self):
            """
            Element g_lai ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 663
            
            """
            return _supy_driver.f90wrap_phenology_state__get__g_lai(self._handle)
        
        @g_lai.setter
        def g_lai(self, g_lai):
            _supy_driver.f90wrap_phenology_state__set__g_lai(self._handle, g_lai)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 666
            
            """
            return _supy_driver.f90wrap_phenology_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_phenology_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<phenology_state>{\n']
            ret.append('    alb : ')
            ret.append(repr(self.alb))
            ret.append(',\n    lai_id : ')
            ret.append(repr(self.lai_id))
            ret.append(',\n    gdd_id : ')
            ret.append(repr(self.gdd_id))
            ret.append(',\n    sdd_id : ')
            ret.append(repr(self.sdd_id))
            ret.append(',\n    vegphenlumps : ')
            ret.append(repr(self.vegphenlumps))
            ret.append(',\n    porosity_id : ')
            ret.append(repr(self.porosity_id))
            ret.append(',\n    decidcap_id : ')
            ret.append(repr(self.decidcap_id))
            ret.append(',\n    albdectr_id : ')
            ret.append(repr(self.albdectr_id))
            ret.append(',\n    albevetr_id : ')
            ret.append(repr(self.albevetr_id))
            ret.append(',\n    albgrass_id : ')
            ret.append(repr(self.albgrass_id))
            ret.append(',\n    tmin_id : ')
            ret.append(repr(self.tmin_id))
            ret.append(',\n    tmax_id : ')
            ret.append(repr(self.tmax_id))
            ret.append(',\n    lenday_id : ')
            ret.append(repr(self.lenday_id))
            ret.append(',\n    tempveg : ')
            ret.append(repr(self.tempveg))
            ret.append(',\n    storedrainprm : ')
            ret.append(repr(self.storedrainprm))
            ret.append(',\n    gfunc : ')
            ret.append(repr(self.gfunc))
            ret.append(',\n    gsc : ')
            ret.append(repr(self.gsc))
            ret.append(',\n    g_kdown : ')
            ret.append(repr(self.g_kdown))
            ret.append(',\n    g_dq : ')
            ret.append(repr(self.g_dq))
            ret.append(',\n    g_ta : ')
            ret.append(repr(self.g_ta))
            ret.append(',\n    g_smd : ')
            ret.append(repr(self.g_smd))
            ret.append(',\n    g_lai : ')
            ret.append(repr(self.g_lai))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SNOW_STATE")
    class SNOW_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=snow_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 668-694
        
        """
        def __init__(self, handle=None):
            """
            self = Snow_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 668-694
            
            
            Returns
            -------
            this : Snow_State
            	Object to be constructed
            
            
            Automatically generated constructor for snow_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__snow_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Snow_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 668-694
            
            Parameters
            ----------
            this : Snow_State
            	Object to be destructed
            
            
            Automatically generated destructor for snow_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__snow_state_finalise(this=self._handle)
        
        @property
        def snowfallcum(self):
            """
            Element snowfallcum ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 669
            
            """
            return _supy_driver.f90wrap_snow_state__get__snowfallcum(self._handle)
        
        @snowfallcum.setter
        def snowfallcum(self, snowfallcum):
            _supy_driver.f90wrap_snow_state__set__snowfallcum(self._handle, snowfallcum)
        
        @property
        def snowalb(self):
            """
            Element snowalb ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 670
            
            """
            return _supy_driver.f90wrap_snow_state__get__snowalb(self._handle)
        
        @snowalb.setter
        def snowalb(self, snowalb):
            _supy_driver.f90wrap_snow_state__set__snowalb(self._handle, snowalb)
        
        @property
        def chsnow_per_interval(self):
            """
            Element chsnow_per_interval ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 671
            
            """
            return _supy_driver.f90wrap_snow_state__get__chsnow_per_interval(self._handle)
        
        @chsnow_per_interval.setter
        def chsnow_per_interval(self, chsnow_per_interval):
            _supy_driver.f90wrap_snow_state__set__chsnow_per_interval(self._handle, \
                chsnow_per_interval)
        
        @property
        def mwh(self):
            """
            Element mwh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 672
            
            """
            return _supy_driver.f90wrap_snow_state__get__mwh(self._handle)
        
        @mwh.setter
        def mwh(self, mwh):
            _supy_driver.f90wrap_snow_state__set__mwh(self._handle, mwh)
        
        @property
        def mwstore(self):
            """
            Element mwstore ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 673
            
            """
            return _supy_driver.f90wrap_snow_state__get__mwstore(self._handle)
        
        @mwstore.setter
        def mwstore(self, mwstore):
            _supy_driver.f90wrap_snow_state__set__mwstore(self._handle, mwstore)
        
        @property
        def qn_snow(self):
            """
            Element qn_snow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 674
            
            """
            return _supy_driver.f90wrap_snow_state__get__qn_snow(self._handle)
        
        @qn_snow.setter
        def qn_snow(self, qn_snow):
            _supy_driver.f90wrap_snow_state__set__qn_snow(self._handle, qn_snow)
        
        @property
        def qm(self):
            """
            Element qm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 675
            
            """
            return _supy_driver.f90wrap_snow_state__get__qm(self._handle)
        
        @qm.setter
        def qm(self, qm):
            _supy_driver.f90wrap_snow_state__set__qm(self._handle, qm)
        
        @property
        def qmfreez(self):
            """
            Element qmfreez ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 676
            
            """
            return _supy_driver.f90wrap_snow_state__get__qmfreez(self._handle)
        
        @qmfreez.setter
        def qmfreez(self, qmfreez):
            _supy_driver.f90wrap_snow_state__set__qmfreez(self._handle, qmfreez)
        
        @property
        def qmrain(self):
            """
            Element qmrain ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 677
            
            """
            return _supy_driver.f90wrap_snow_state__get__qmrain(self._handle)
        
        @qmrain.setter
        def qmrain(self, qmrain):
            _supy_driver.f90wrap_snow_state__set__qmrain(self._handle, qmrain)
        
        @property
        def swe(self):
            """
            Element swe ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 678
            
            """
            return _supy_driver.f90wrap_snow_state__get__swe(self._handle)
        
        @swe.setter
        def swe(self, swe):
            _supy_driver.f90wrap_snow_state__set__swe(self._handle, swe)
        
        @property
        def z0vsnow(self):
            """
            Element z0vsnow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 679
            
            """
            return _supy_driver.f90wrap_snow_state__get__z0vsnow(self._handle)
        
        @z0vsnow.setter
        def z0vsnow(self, z0vsnow):
            _supy_driver.f90wrap_snow_state__set__z0vsnow(self._handle, z0vsnow)
        
        @property
        def rasnow(self):
            """
            Element rasnow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 680
            
            """
            return _supy_driver.f90wrap_snow_state__get__rasnow(self._handle)
        
        @rasnow.setter
        def rasnow(self, rasnow):
            _supy_driver.f90wrap_snow_state__set__rasnow(self._handle, rasnow)
        
        @property
        def sice_hpa(self):
            """
            Element sice_hpa ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 681
            
            """
            return _supy_driver.f90wrap_snow_state__get__sice_hpa(self._handle)
        
        @sice_hpa.setter
        def sice_hpa(self, sice_hpa):
            _supy_driver.f90wrap_snow_state__set__sice_hpa(self._handle, sice_hpa)
        
        @property
        def snowremoval(self):
            """
            Element snowremoval ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 682
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowremoval(self._handle)
            if array_handle in self._arrays:
                snowremoval = self._arrays[array_handle]
            else:
                snowremoval = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowremoval)
                self._arrays[array_handle] = snowremoval
            return snowremoval
        
        @snowremoval.setter
        def snowremoval(self, snowremoval):
            self.snowremoval[...] = snowremoval
        
        @property
        def icefrac(self):
            """
            Element icefrac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 683
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__icefrac(self._handle)
            if array_handle in self._arrays:
                icefrac = self._arrays[array_handle]
            else:
                icefrac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__icefrac)
                self._arrays[array_handle] = icefrac
            return icefrac
        
        @icefrac.setter
        def icefrac(self, icefrac):
            self.icefrac[...] = icefrac
        
        @property
        def snowdens(self):
            """
            Element snowdens ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 684
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowdens(self._handle)
            if array_handle in self._arrays:
                snowdens = self._arrays[array_handle]
            else:
                snowdens = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowdens)
                self._arrays[array_handle] = snowdens
            return snowdens
        
        @snowdens.setter
        def snowdens(self, snowdens):
            self.snowdens[...] = snowdens
        
        @property
        def snowfrac(self):
            """
            Element snowfrac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 685
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowfrac(self._handle)
            if array_handle in self._arrays:
                snowfrac = self._arrays[array_handle]
            else:
                snowfrac = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowfrac)
                self._arrays[array_handle] = snowfrac
            return snowfrac
        
        @snowfrac.setter
        def snowfrac(self, snowfrac):
            self.snowfrac[...] = snowfrac
        
        @property
        def snowpack(self):
            """
            Element snowpack ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 686
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowpack(self._handle)
            if array_handle in self._arrays:
                snowpack = self._arrays[array_handle]
            else:
                snowpack = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowpack)
                self._arrays[array_handle] = snowpack
            return snowpack
        
        @snowpack.setter
        def snowpack(self, snowpack):
            self.snowpack[...] = snowpack
        
        @property
        def snowwater(self):
            """
            Element snowwater ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 687
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__snowwater(self._handle)
            if array_handle in self._arrays:
                snowwater = self._arrays[array_handle]
            else:
                snowwater = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__snowwater)
                self._arrays[array_handle] = snowwater
            return snowwater
        
        @snowwater.setter
        def snowwater(self, snowwater):
            self.snowwater[...] = snowwater
        
        @property
        def kup_ind_snow(self):
            """
            Element kup_ind_snow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 688
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__kup_ind_snow(self._handle)
            if array_handle in self._arrays:
                kup_ind_snow = self._arrays[array_handle]
            else:
                kup_ind_snow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__kup_ind_snow)
                self._arrays[array_handle] = kup_ind_snow
            return kup_ind_snow
        
        @kup_ind_snow.setter
        def kup_ind_snow(self, kup_ind_snow):
            self.kup_ind_snow[...] = kup_ind_snow
        
        @property
        def qn_ind_snow(self):
            """
            Element qn_ind_snow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 689
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__qn_ind_snow(self._handle)
            if array_handle in self._arrays:
                qn_ind_snow = self._arrays[array_handle]
            else:
                qn_ind_snow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__qn_ind_snow)
                self._arrays[array_handle] = qn_ind_snow
            return qn_ind_snow
        
        @qn_ind_snow.setter
        def qn_ind_snow(self, qn_ind_snow):
            self.qn_ind_snow[...] = qn_ind_snow
        
        @property
        def deltaqi(self):
            """
            Element deltaqi ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 690
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__deltaqi(self._handle)
            if array_handle in self._arrays:
                deltaqi = self._arrays[array_handle]
            else:
                deltaqi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__deltaqi)
                self._arrays[array_handle] = deltaqi
            return deltaqi
        
        @deltaqi.setter
        def deltaqi(self, deltaqi):
            self.deltaqi[...] = deltaqi
        
        @property
        def tsurf_ind_snow(self):
            """
            Element tsurf_ind_snow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 691
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_snow_state__array__tsurf_ind_snow(self._handle)
            if array_handle in self._arrays:
                tsurf_ind_snow = self._arrays[array_handle]
            else:
                tsurf_ind_snow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_snow_state__array__tsurf_ind_snow)
                self._arrays[array_handle] = tsurf_ind_snow
            return tsurf_ind_snow
        
        @tsurf_ind_snow.setter
        def tsurf_ind_snow(self, tsurf_ind_snow):
            self.tsurf_ind_snow[...] = tsurf_ind_snow
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 694
            
            """
            return _supy_driver.f90wrap_snow_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_snow_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<snow_state>{\n']
            ret.append('    snowfallcum : ')
            ret.append(repr(self.snowfallcum))
            ret.append(',\n    snowalb : ')
            ret.append(repr(self.snowalb))
            ret.append(',\n    chsnow_per_interval : ')
            ret.append(repr(self.chsnow_per_interval))
            ret.append(',\n    mwh : ')
            ret.append(repr(self.mwh))
            ret.append(',\n    mwstore : ')
            ret.append(repr(self.mwstore))
            ret.append(',\n    qn_snow : ')
            ret.append(repr(self.qn_snow))
            ret.append(',\n    qm : ')
            ret.append(repr(self.qm))
            ret.append(',\n    qmfreez : ')
            ret.append(repr(self.qmfreez))
            ret.append(',\n    qmrain : ')
            ret.append(repr(self.qmrain))
            ret.append(',\n    swe : ')
            ret.append(repr(self.swe))
            ret.append(',\n    z0vsnow : ')
            ret.append(repr(self.z0vsnow))
            ret.append(',\n    rasnow : ')
            ret.append(repr(self.rasnow))
            ret.append(',\n    sice_hpa : ')
            ret.append(repr(self.sice_hpa))
            ret.append(',\n    snowremoval : ')
            ret.append(repr(self.snowremoval))
            ret.append(',\n    icefrac : ')
            ret.append(repr(self.icefrac))
            ret.append(',\n    snowdens : ')
            ret.append(repr(self.snowdens))
            ret.append(',\n    snowfrac : ')
            ret.append(repr(self.snowfrac))
            ret.append(',\n    snowpack : ')
            ret.append(repr(self.snowpack))
            ret.append(',\n    snowwater : ')
            ret.append(repr(self.snowwater))
            ret.append(',\n    kup_ind_snow : ')
            ret.append(repr(self.kup_ind_snow))
            ret.append(',\n    qn_ind_snow : ')
            ret.append(repr(self.qn_ind_snow))
            ret.append(',\n    deltaqi : ')
            ret.append(repr(self.deltaqi))
            ret.append(',\n    tsurf_ind_snow : ')
            ret.append(repr(self.tsurf_ind_snow))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.HYDRO_STATE")
    class HYDRO_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=hydro_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 696-760
        
        """
        def __init__(self, handle=None):
            """
            self = Hydro_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 696-760
            
            
            Returns
            -------
            this : Hydro_State
            	Object to be constructed
            
            
            Automatically generated constructor for hydro_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__hydro_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Hydro_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 696-760
            
            Parameters
            ----------
            this : Hydro_State
            	Object to be destructed
            
            
            Automatically generated destructor for hydro_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__hydro_state_finalise(this=self._handle)
        
        def allocate(self, nlayer):
            """
            allocate__binding__hydro_state(self, nlayer)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1165-1178
            
            Parameters
            ----------
            self : Hydro_State
            nlayer : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__allocate__binding__hydro_state(self=self._handle, \
                nlayer=nlayer)
        
        def deallocate(self):
            """
            deallocate__binding__hydro_state(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1180-1191
            
            Parameters
            ----------
            self : Hydro_State
            
            """
            _supy_driver.f90wrap_suews_def_dts__deallocate__binding__hydro_state(self=self._handle)
        
        @property
        def soilstore_surf(self):
            """
            Element soilstore_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 698
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__soilstore_surf(self._handle)
            if array_handle in self._arrays:
                soilstore_surf = self._arrays[array_handle]
            else:
                soilstore_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__soilstore_surf)
                self._arrays[array_handle] = soilstore_surf
            return soilstore_surf
        
        @soilstore_surf.setter
        def soilstore_surf(self, soilstore_surf):
            self.soilstore_surf[...] = soilstore_surf
        
        @property
        def state_surf(self):
            """
            Element state_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 699
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__state_surf(self._handle)
            if array_handle in self._arrays:
                state_surf = self._arrays[array_handle]
            else:
                state_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__state_surf)
                self._arrays[array_handle] = state_surf
            return state_surf
        
        @state_surf.setter
        def state_surf(self, state_surf):
            self.state_surf[...] = state_surf
        
        @property
        def wuday_id(self):
            """
            Element wuday_id ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 702
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__wuday_id(self._handle)
            if array_handle in self._arrays:
                wuday_id = self._arrays[array_handle]
            else:
                wuday_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__wuday_id)
                self._arrays[array_handle] = wuday_id
            return wuday_id
        
        @wuday_id.setter
        def wuday_id(self, wuday_id):
            self.wuday_id[...] = wuday_id
        
        @property
        def soilstore_roof(self):
            """
            Element soilstore_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 714
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__soilstore_roof(self._handle)
            if array_handle in self._arrays:
                soilstore_roof = self._arrays[array_handle]
            else:
                soilstore_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__soilstore_roof)
                self._arrays[array_handle] = soilstore_roof
            return soilstore_roof
        
        @soilstore_roof.setter
        def soilstore_roof(self, soilstore_roof):
            self.soilstore_roof[...] = soilstore_roof
        
        @property
        def state_roof(self):
            """
            Element state_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 715
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__state_roof(self._handle)
            if array_handle in self._arrays:
                state_roof = self._arrays[array_handle]
            else:
                state_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__state_roof)
                self._arrays[array_handle] = state_roof
            return state_roof
        
        @state_roof.setter
        def state_roof(self, state_roof):
            self.state_roof[...] = state_roof
        
        @property
        def soilstore_wall(self):
            """
            Element soilstore_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 716
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__soilstore_wall(self._handle)
            if array_handle in self._arrays:
                soilstore_wall = self._arrays[array_handle]
            else:
                soilstore_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__soilstore_wall)
                self._arrays[array_handle] = soilstore_wall
            return soilstore_wall
        
        @soilstore_wall.setter
        def soilstore_wall(self, soilstore_wall):
            self.soilstore_wall[...] = soilstore_wall
        
        @property
        def state_wall(self):
            """
            Element state_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 717
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__state_wall(self._handle)
            if array_handle in self._arrays:
                state_wall = self._arrays[array_handle]
            else:
                state_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__state_wall)
                self._arrays[array_handle] = state_wall
            return state_wall
        
        @state_wall.setter
        def state_wall(self, state_wall):
            self.state_wall[...] = state_wall
        
        @property
        def ev_roof(self):
            """
            Element ev_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 718
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__ev_roof(self._handle)
            if array_handle in self._arrays:
                ev_roof = self._arrays[array_handle]
            else:
                ev_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__ev_roof)
                self._arrays[array_handle] = ev_roof
            return ev_roof
        
        @ev_roof.setter
        def ev_roof(self, ev_roof):
            self.ev_roof[...] = ev_roof
        
        @property
        def ev_wall(self):
            """
            Element ev_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 719
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__ev_wall(self._handle)
            if array_handle in self._arrays:
                ev_wall = self._arrays[array_handle]
            else:
                ev_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__ev_wall)
                self._arrays[array_handle] = ev_wall
            return ev_wall
        
        @ev_wall.setter
        def ev_wall(self, ev_wall):
            self.ev_wall[...] = ev_wall
        
        @property
        def ev0_surf(self):
            """
            Element ev0_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 720
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__ev0_surf(self._handle)
            if array_handle in self._arrays:
                ev0_surf = self._arrays[array_handle]
            else:
                ev0_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__ev0_surf)
                self._arrays[array_handle] = ev0_surf
            return ev0_surf
        
        @ev0_surf.setter
        def ev0_surf(self, ev0_surf):
            self.ev0_surf[...] = ev0_surf
        
        @property
        def ev_surf(self):
            """
            Element ev_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 721
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__ev_surf(self._handle)
            if array_handle in self._arrays:
                ev_surf = self._arrays[array_handle]
            else:
                ev_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__ev_surf)
                self._arrays[array_handle] = ev_surf
            return ev_surf
        
        @ev_surf.setter
        def ev_surf(self, ev_surf):
            self.ev_surf[...] = ev_surf
        
        @property
        def wu_surf(self):
            """
            Element wu_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 722
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__wu_surf(self._handle)
            if array_handle in self._arrays:
                wu_surf = self._arrays[array_handle]
            else:
                wu_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__wu_surf)
                self._arrays[array_handle] = wu_surf
            return wu_surf
        
        @wu_surf.setter
        def wu_surf(self, wu_surf):
            self.wu_surf[...] = wu_surf
        
        @property
        def runoffsoil(self):
            """
            Element runoffsoil ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 723
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__runoffsoil(self._handle)
            if array_handle in self._arrays:
                runoffsoil = self._arrays[array_handle]
            else:
                runoffsoil = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__runoffsoil)
                self._arrays[array_handle] = runoffsoil
            return runoffsoil
        
        @runoffsoil.setter
        def runoffsoil(self, runoffsoil):
            self.runoffsoil[...] = runoffsoil
        
        @property
        def smd_surf(self):
            """
            Element smd_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 724
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__smd_surf(self._handle)
            if array_handle in self._arrays:
                smd_surf = self._arrays[array_handle]
            else:
                smd_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__smd_surf)
                self._arrays[array_handle] = smd_surf
            return smd_surf
        
        @smd_surf.setter
        def smd_surf(self, smd_surf):
            self.smd_surf[...] = smd_surf
        
        @property
        def drain_surf(self):
            """
            Element drain_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 725
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__drain_surf(self._handle)
            if array_handle in self._arrays:
                drain_surf = self._arrays[array_handle]
            else:
                drain_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__drain_surf)
                self._arrays[array_handle] = drain_surf
            return drain_surf
        
        @drain_surf.setter
        def drain_surf(self, drain_surf):
            self.drain_surf[...] = drain_surf
        
        @property
        def drain_per_tstep(self):
            """
            Element drain_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 726
            
            """
            return _supy_driver.f90wrap_hydro_state__get__drain_per_tstep(self._handle)
        
        @drain_per_tstep.setter
        def drain_per_tstep(self, drain_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__drain_per_tstep(self._handle, \
                drain_per_tstep)
        
        @property
        def ev_per_tstep(self):
            """
            Element ev_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 727
            
            """
            return _supy_driver.f90wrap_hydro_state__get__ev_per_tstep(self._handle)
        
        @ev_per_tstep.setter
        def ev_per_tstep(self, ev_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__ev_per_tstep(self._handle, ev_per_tstep)
        
        @property
        def wu_ext(self):
            """
            Element wu_ext ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 728
            
            """
            return _supy_driver.f90wrap_hydro_state__get__wu_ext(self._handle)
        
        @wu_ext.setter
        def wu_ext(self, wu_ext):
            _supy_driver.f90wrap_hydro_state__set__wu_ext(self._handle, wu_ext)
        
        @property
        def wu_int(self):
            """
            Element wu_int ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 729
            
            """
            return _supy_driver.f90wrap_hydro_state__get__wu_int(self._handle)
        
        @wu_int.setter
        def wu_int(self, wu_int):
            _supy_driver.f90wrap_hydro_state__set__wu_int(self._handle, wu_int)
        
        @property
        def runoffagveg(self):
            """
            Element runoffagveg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 730
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoffagveg(self._handle)
        
        @runoffagveg.setter
        def runoffagveg(self, runoffagveg):
            _supy_driver.f90wrap_hydro_state__set__runoffagveg(self._handle, runoffagveg)
        
        @property
        def runoffagimpervious(self):
            """
            Element runoffagimpervious ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 731
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoffagimpervious(self._handle)
        
        @runoffagimpervious.setter
        def runoffagimpervious(self, runoffagimpervious):
            _supy_driver.f90wrap_hydro_state__set__runoffagimpervious(self._handle, \
                runoffagimpervious)
        
        @property
        def runoff_per_tstep(self):
            """
            Element runoff_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 732
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoff_per_tstep(self._handle)
        
        @runoff_per_tstep.setter
        def runoff_per_tstep(self, runoff_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__runoff_per_tstep(self._handle, \
                runoff_per_tstep)
        
        @property
        def runoffpipes(self):
            """
            Element runoffpipes ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 733
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoffpipes(self._handle)
        
        @runoffpipes.setter
        def runoffpipes(self, runoffpipes):
            _supy_driver.f90wrap_hydro_state__set__runoffpipes(self._handle, runoffpipes)
        
        @property
        def runoffsoil_per_tstep(self):
            """
            Element runoffsoil_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 734
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoffsoil_per_tstep(self._handle)
        
        @runoffsoil_per_tstep.setter
        def runoffsoil_per_tstep(self, runoffsoil_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__runoffsoil_per_tstep(self._handle, \
                runoffsoil_per_tstep)
        
        @property
        def runoffwaterbody(self):
            """
            Element runoffwaterbody ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 735
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoffwaterbody(self._handle)
        
        @runoffwaterbody.setter
        def runoffwaterbody(self, runoffwaterbody):
            _supy_driver.f90wrap_hydro_state__set__runoffwaterbody(self._handle, \
                runoffwaterbody)
        
        @property
        def smd(self):
            """
            Element smd ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 736
            
            """
            return _supy_driver.f90wrap_hydro_state__get__smd(self._handle)
        
        @smd.setter
        def smd(self, smd):
            _supy_driver.f90wrap_hydro_state__set__smd(self._handle, smd)
        
        @property
        def soilstate(self):
            """
            Element soilstate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 737
            
            """
            return _supy_driver.f90wrap_hydro_state__get__soilstate(self._handle)
        
        @soilstate.setter
        def soilstate(self, soilstate):
            _supy_driver.f90wrap_hydro_state__set__soilstate(self._handle, soilstate)
        
        @property
        def state_per_tstep(self):
            """
            Element state_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 738
            
            """
            return _supy_driver.f90wrap_hydro_state__get__state_per_tstep(self._handle)
        
        @state_per_tstep.setter
        def state_per_tstep(self, state_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__state_per_tstep(self._handle, \
                state_per_tstep)
        
        @property
        def surf_chang_per_tstep(self):
            """
            Element surf_chang_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 739
            
            """
            return _supy_driver.f90wrap_hydro_state__get__surf_chang_per_tstep(self._handle)
        
        @surf_chang_per_tstep.setter
        def surf_chang_per_tstep(self, surf_chang_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__surf_chang_per_tstep(self._handle, \
                surf_chang_per_tstep)
        
        @property
        def tot_chang_per_tstep(self):
            """
            Element tot_chang_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 740
            
            """
            return _supy_driver.f90wrap_hydro_state__get__tot_chang_per_tstep(self._handle)
        
        @tot_chang_per_tstep.setter
        def tot_chang_per_tstep(self, tot_chang_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__tot_chang_per_tstep(self._handle, \
                tot_chang_per_tstep)
        
        @property
        def runoff_per_interval(self):
            """
            Element runoff_per_interval ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 741
            
            """
            return _supy_driver.f90wrap_hydro_state__get__runoff_per_interval(self._handle)
        
        @runoff_per_interval.setter
        def runoff_per_interval(self, runoff_per_interval):
            _supy_driver.f90wrap_hydro_state__set__runoff_per_interval(self._handle, \
                runoff_per_interval)
        
        @property
        def nwstate_per_tstep(self):
            """
            Element nwstate_per_tstep ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 742
            
            """
            return _supy_driver.f90wrap_hydro_state__get__nwstate_per_tstep(self._handle)
        
        @nwstate_per_tstep.setter
        def nwstate_per_tstep(self, nwstate_per_tstep):
            _supy_driver.f90wrap_hydro_state__set__nwstate_per_tstep(self._handle, \
                nwstate_per_tstep)
        
        @property
        def soilmoistcap(self):
            """
            Element soilmoistcap ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 743
            
            """
            return _supy_driver.f90wrap_hydro_state__get__soilmoistcap(self._handle)
        
        @soilmoistcap.setter
        def soilmoistcap(self, soilmoistcap):
            _supy_driver.f90wrap_hydro_state__set__soilmoistcap(self._handle, soilmoistcap)
        
        @property
        def vsmd(self):
            """
            Element vsmd ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 744
            
            """
            return _supy_driver.f90wrap_hydro_state__get__vsmd(self._handle)
        
        @vsmd.setter
        def vsmd(self, vsmd):
            _supy_driver.f90wrap_hydro_state__set__vsmd(self._handle, vsmd)
        
        @property
        def additionalwater(self):
            """
            Element additionalwater ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 748
            
            """
            return _supy_driver.f90wrap_hydro_state__get__additionalwater(self._handle)
        
        @additionalwater.setter
        def additionalwater(self, additionalwater):
            _supy_driver.f90wrap_hydro_state__set__additionalwater(self._handle, \
                additionalwater)
        
        @property
        def addimpervious(self):
            """
            Element addimpervious ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 749
            
            """
            return _supy_driver.f90wrap_hydro_state__get__addimpervious(self._handle)
        
        @addimpervious.setter
        def addimpervious(self, addimpervious):
            _supy_driver.f90wrap_hydro_state__set__addimpervious(self._handle, \
                addimpervious)
        
        @property
        def addpipes(self):
            """
            Element addpipes ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 750
            
            """
            return _supy_driver.f90wrap_hydro_state__get__addpipes(self._handle)
        
        @addpipes.setter
        def addpipes(self, addpipes):
            _supy_driver.f90wrap_hydro_state__set__addpipes(self._handle, addpipes)
        
        @property
        def addveg(self):
            """
            Element addveg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 751
            
            """
            return _supy_driver.f90wrap_hydro_state__get__addveg(self._handle)
        
        @addveg.setter
        def addveg(self, addveg):
            _supy_driver.f90wrap_hydro_state__set__addveg(self._handle, addveg)
        
        @property
        def addwaterbody(self):
            """
            Element addwaterbody ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 752
            
            """
            return _supy_driver.f90wrap_hydro_state__get__addwaterbody(self._handle)
        
        @addwaterbody.setter
        def addwaterbody(self, addwaterbody):
            _supy_driver.f90wrap_hydro_state__set__addwaterbody(self._handle, addwaterbody)
        
        @property
        def addwater(self):
            """
            Element addwater ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 753
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__addwater(self._handle)
            if array_handle in self._arrays:
                addwater = self._arrays[array_handle]
            else:
                addwater = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__addwater)
                self._arrays[array_handle] = addwater
            return addwater
        
        @addwater.setter
        def addwater(self, addwater):
            self.addwater[...] = addwater
        
        @property
        def frac_water2runoff(self):
            """
            Element frac_water2runoff ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 754
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_hydro_state__array__frac_water2runoff(self._handle)
            if array_handle in self._arrays:
                frac_water2runoff = self._arrays[array_handle]
            else:
                frac_water2runoff = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_hydro_state__array__frac_water2runoff)
                self._arrays[array_handle] = frac_water2runoff
            return frac_water2runoff
        
        @frac_water2runoff.setter
        def frac_water2runoff(self, frac_water2runoff):
            self.frac_water2runoff[...] = frac_water2runoff
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 757
            
            """
            return _supy_driver.f90wrap_hydro_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_hydro_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<hydro_state>{\n']
            ret.append('    soilstore_surf : ')
            ret.append(repr(self.soilstore_surf))
            ret.append(',\n    state_surf : ')
            ret.append(repr(self.state_surf))
            ret.append(',\n    wuday_id : ')
            ret.append(repr(self.wuday_id))
            ret.append(',\n    soilstore_roof : ')
            ret.append(repr(self.soilstore_roof))
            ret.append(',\n    state_roof : ')
            ret.append(repr(self.state_roof))
            ret.append(',\n    soilstore_wall : ')
            ret.append(repr(self.soilstore_wall))
            ret.append(',\n    state_wall : ')
            ret.append(repr(self.state_wall))
            ret.append(',\n    ev_roof : ')
            ret.append(repr(self.ev_roof))
            ret.append(',\n    ev_wall : ')
            ret.append(repr(self.ev_wall))
            ret.append(',\n    ev0_surf : ')
            ret.append(repr(self.ev0_surf))
            ret.append(',\n    ev_surf : ')
            ret.append(repr(self.ev_surf))
            ret.append(',\n    wu_surf : ')
            ret.append(repr(self.wu_surf))
            ret.append(',\n    runoffsoil : ')
            ret.append(repr(self.runoffsoil))
            ret.append(',\n    smd_surf : ')
            ret.append(repr(self.smd_surf))
            ret.append(',\n    drain_surf : ')
            ret.append(repr(self.drain_surf))
            ret.append(',\n    drain_per_tstep : ')
            ret.append(repr(self.drain_per_tstep))
            ret.append(',\n    ev_per_tstep : ')
            ret.append(repr(self.ev_per_tstep))
            ret.append(',\n    wu_ext : ')
            ret.append(repr(self.wu_ext))
            ret.append(',\n    wu_int : ')
            ret.append(repr(self.wu_int))
            ret.append(',\n    runoffagveg : ')
            ret.append(repr(self.runoffagveg))
            ret.append(',\n    runoffagimpervious : ')
            ret.append(repr(self.runoffagimpervious))
            ret.append(',\n    runoff_per_tstep : ')
            ret.append(repr(self.runoff_per_tstep))
            ret.append(',\n    runoffpipes : ')
            ret.append(repr(self.runoffpipes))
            ret.append(',\n    runoffsoil_per_tstep : ')
            ret.append(repr(self.runoffsoil_per_tstep))
            ret.append(',\n    runoffwaterbody : ')
            ret.append(repr(self.runoffwaterbody))
            ret.append(',\n    smd : ')
            ret.append(repr(self.smd))
            ret.append(',\n    soilstate : ')
            ret.append(repr(self.soilstate))
            ret.append(',\n    state_per_tstep : ')
            ret.append(repr(self.state_per_tstep))
            ret.append(',\n    surf_chang_per_tstep : ')
            ret.append(repr(self.surf_chang_per_tstep))
            ret.append(',\n    tot_chang_per_tstep : ')
            ret.append(repr(self.tot_chang_per_tstep))
            ret.append(',\n    runoff_per_interval : ')
            ret.append(repr(self.runoff_per_interval))
            ret.append(',\n    nwstate_per_tstep : ')
            ret.append(repr(self.nwstate_per_tstep))
            ret.append(',\n    soilmoistcap : ')
            ret.append(repr(self.soilmoistcap))
            ret.append(',\n    vsmd : ')
            ret.append(repr(self.vsmd))
            ret.append(',\n    additionalwater : ')
            ret.append(repr(self.additionalwater))
            ret.append(',\n    addimpervious : ')
            ret.append(repr(self.addimpervious))
            ret.append(',\n    addpipes : ')
            ret.append(repr(self.addpipes))
            ret.append(',\n    addveg : ')
            ret.append(repr(self.addveg))
            ret.append(',\n    addwaterbody : ')
            ret.append(repr(self.addwaterbody))
            ret.append(',\n    addwater : ')
            ret.append(repr(self.addwater))
            ret.append(',\n    frac_water2runoff : ')
            ret.append(repr(self.frac_water2runoff))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.HEAT_STATE")
    class HEAT_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=heat_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 762-813
        
        """
        def __init__(self, handle=None):
            """
            self = Heat_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 762-813
            
            
            Returns
            -------
            this : Heat_State
            	Object to be constructed
            
            
            Automatically generated constructor for heat_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__heat_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Heat_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 762-813
            
            Parameters
            ----------
            this : Heat_State
            	Object to be destructed
            
            
            Automatically generated destructor for heat_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__heat_state_finalise(this=self._handle)
        
        def allocate(self, num_surf, num_layer, num_depth):
            """
            allocate__binding__heat_state(self, num_surf, num_layer, num_depth)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1193-1219
            
            Parameters
            ----------
            self : Heat_State
            num_surf : int
            num_layer : int
            num_depth : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__allocate__binding__heat_state(self=self._handle, \
                num_surf=num_surf, num_layer=num_layer, num_depth=num_depth)
        
        def deallocate(self):
            """
            deallocate__binding__heat_state(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1221-1244
            
            Parameters
            ----------
            self : Heat_State
            
            """
            _supy_driver.f90wrap_suews_def_dts__deallocate__binding__heat_state(self=self._handle)
        
        @property
        def temp_roof(self):
            """
            Element temp_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 763
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__temp_roof(self._handle)
            if array_handle in self._arrays:
                temp_roof = self._arrays[array_handle]
            else:
                temp_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__temp_roof)
                self._arrays[array_handle] = temp_roof
            return temp_roof
        
        @temp_roof.setter
        def temp_roof(self, temp_roof):
            self.temp_roof[...] = temp_roof
        
        @property
        def temp_wall(self):
            """
            Element temp_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 764
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__temp_wall(self._handle)
            if array_handle in self._arrays:
                temp_wall = self._arrays[array_handle]
            else:
                temp_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__temp_wall)
                self._arrays[array_handle] = temp_wall
            return temp_wall
        
        @temp_wall.setter
        def temp_wall(self, temp_wall):
            self.temp_wall[...] = temp_wall
        
        @property
        def temp_surf(self):
            """
            Element temp_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 765
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__temp_surf(self._handle)
            if array_handle in self._arrays:
                temp_surf = self._arrays[array_handle]
            else:
                temp_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__temp_surf)
                self._arrays[array_handle] = temp_surf
            return temp_surf
        
        @temp_surf.setter
        def temp_surf(self, temp_surf):
            self.temp_surf[...] = temp_surf
        
        @property
        def tsfc_roof(self):
            """
            Element tsfc_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 766
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_roof(self._handle)
            if array_handle in self._arrays:
                tsfc_roof = self._arrays[array_handle]
            else:
                tsfc_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_roof)
                self._arrays[array_handle] = tsfc_roof
            return tsfc_roof
        
        @tsfc_roof.setter
        def tsfc_roof(self, tsfc_roof):
            self.tsfc_roof[...] = tsfc_roof
        
        @property
        def tsfc_wall(self):
            """
            Element tsfc_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 767
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_wall(self._handle)
            if array_handle in self._arrays:
                tsfc_wall = self._arrays[array_handle]
            else:
                tsfc_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_wall)
                self._arrays[array_handle] = tsfc_wall
            return tsfc_wall
        
        @tsfc_wall.setter
        def tsfc_wall(self, tsfc_wall):
            self.tsfc_wall[...] = tsfc_wall
        
        @property
        def tsfc_surf(self):
            """
            Element tsfc_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 768
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_surf(self._handle)
            if array_handle in self._arrays:
                tsfc_surf = self._arrays[array_handle]
            else:
                tsfc_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_surf)
                self._arrays[array_handle] = tsfc_surf
            return tsfc_surf
        
        @tsfc_surf.setter
        def tsfc_surf(self, tsfc_surf):
            self.tsfc_surf[...] = tsfc_surf
        
        @property
        def tsfc_roof_stepstart(self):
            """
            Element tsfc_roof_stepstart ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 770
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_roof_stepstart(self._handle)
            if array_handle in self._arrays:
                tsfc_roof_stepstart = self._arrays[array_handle]
            else:
                tsfc_roof_stepstart = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_roof_stepstart)
                self._arrays[array_handle] = tsfc_roof_stepstart
            return tsfc_roof_stepstart
        
        @tsfc_roof_stepstart.setter
        def tsfc_roof_stepstart(self, tsfc_roof_stepstart):
            self.tsfc_roof_stepstart[...] = tsfc_roof_stepstart
        
        @property
        def tsfc_wall_stepstart(self):
            """
            Element tsfc_wall_stepstart ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 771
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_wall_stepstart(self._handle)
            if array_handle in self._arrays:
                tsfc_wall_stepstart = self._arrays[array_handle]
            else:
                tsfc_wall_stepstart = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_wall_stepstart)
                self._arrays[array_handle] = tsfc_wall_stepstart
            return tsfc_wall_stepstart
        
        @tsfc_wall_stepstart.setter
        def tsfc_wall_stepstart(self, tsfc_wall_stepstart):
            self.tsfc_wall_stepstart[...] = tsfc_wall_stepstart
        
        @property
        def tsfc_surf_stepstart(self):
            """
            Element tsfc_surf_stepstart ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 772
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsfc_surf_stepstart(self._handle)
            if array_handle in self._arrays:
                tsfc_surf_stepstart = self._arrays[array_handle]
            else:
                tsfc_surf_stepstart = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsfc_surf_stepstart)
                self._arrays[array_handle] = tsfc_surf_stepstart
            return tsfc_surf_stepstart
        
        @tsfc_surf_stepstart.setter
        def tsfc_surf_stepstart(self, tsfc_surf_stepstart):
            self.tsfc_surf_stepstart[...] = tsfc_surf_stepstart
        
        @property
        def qs_roof(self):
            """
            Element qs_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 773
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qs_roof(self._handle)
            if array_handle in self._arrays:
                qs_roof = self._arrays[array_handle]
            else:
                qs_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qs_roof)
                self._arrays[array_handle] = qs_roof
            return qs_roof
        
        @qs_roof.setter
        def qs_roof(self, qs_roof):
            self.qs_roof[...] = qs_roof
        
        @property
        def qn_roof(self):
            """
            Element qn_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 774
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qn_roof(self._handle)
            if array_handle in self._arrays:
                qn_roof = self._arrays[array_handle]
            else:
                qn_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qn_roof)
                self._arrays[array_handle] = qn_roof
            return qn_roof
        
        @qn_roof.setter
        def qn_roof(self, qn_roof):
            self.qn_roof[...] = qn_roof
        
        @property
        def qe_roof(self):
            """
            Element qe_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 775
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qe_roof(self._handle)
            if array_handle in self._arrays:
                qe_roof = self._arrays[array_handle]
            else:
                qe_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qe_roof)
                self._arrays[array_handle] = qe_roof
            return qe_roof
        
        @qe_roof.setter
        def qe_roof(self, qe_roof):
            self.qe_roof[...] = qe_roof
        
        @property
        def qh_roof(self):
            """
            Element qh_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 776
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qh_roof(self._handle)
            if array_handle in self._arrays:
                qh_roof = self._arrays[array_handle]
            else:
                qh_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qh_roof)
                self._arrays[array_handle] = qh_roof
            return qh_roof
        
        @qh_roof.setter
        def qh_roof(self, qh_roof):
            self.qh_roof[...] = qh_roof
        
        @property
        def qh_resist_roof(self):
            """
            Element qh_resist_roof ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 777
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qh_resist_roof(self._handle)
            if array_handle in self._arrays:
                qh_resist_roof = self._arrays[array_handle]
            else:
                qh_resist_roof = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qh_resist_roof)
                self._arrays[array_handle] = qh_resist_roof
            return qh_resist_roof
        
        @qh_resist_roof.setter
        def qh_resist_roof(self, qh_resist_roof):
            self.qh_resist_roof[...] = qh_resist_roof
        
        @property
        def qs_wall(self):
            """
            Element qs_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 778
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qs_wall(self._handle)
            if array_handle in self._arrays:
                qs_wall = self._arrays[array_handle]
            else:
                qs_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qs_wall)
                self._arrays[array_handle] = qs_wall
            return qs_wall
        
        @qs_wall.setter
        def qs_wall(self, qs_wall):
            self.qs_wall[...] = qs_wall
        
        @property
        def qn_wall(self):
            """
            Element qn_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 779
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qn_wall(self._handle)
            if array_handle in self._arrays:
                qn_wall = self._arrays[array_handle]
            else:
                qn_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qn_wall)
                self._arrays[array_handle] = qn_wall
            return qn_wall
        
        @qn_wall.setter
        def qn_wall(self, qn_wall):
            self.qn_wall[...] = qn_wall
        
        @property
        def qe_wall(self):
            """
            Element qe_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 780
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qe_wall(self._handle)
            if array_handle in self._arrays:
                qe_wall = self._arrays[array_handle]
            else:
                qe_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qe_wall)
                self._arrays[array_handle] = qe_wall
            return qe_wall
        
        @qe_wall.setter
        def qe_wall(self, qe_wall):
            self.qe_wall[...] = qe_wall
        
        @property
        def qh_wall(self):
            """
            Element qh_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 781
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qh_wall(self._handle)
            if array_handle in self._arrays:
                qh_wall = self._arrays[array_handle]
            else:
                qh_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qh_wall)
                self._arrays[array_handle] = qh_wall
            return qh_wall
        
        @qh_wall.setter
        def qh_wall(self, qh_wall):
            self.qh_wall[...] = qh_wall
        
        @property
        def qh_resist_wall(self):
            """
            Element qh_resist_wall ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 782
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qh_resist_wall(self._handle)
            if array_handle in self._arrays:
                qh_resist_wall = self._arrays[array_handle]
            else:
                qh_resist_wall = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qh_resist_wall)
                self._arrays[array_handle] = qh_resist_wall
            return qh_resist_wall
        
        @qh_resist_wall.setter
        def qh_resist_wall(self, qh_resist_wall):
            self.qh_resist_wall[...] = qh_resist_wall
        
        @property
        def qs_surf(self):
            """
            Element qs_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 783
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qs_surf(self._handle)
            if array_handle in self._arrays:
                qs_surf = self._arrays[array_handle]
            else:
                qs_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qs_surf)
                self._arrays[array_handle] = qs_surf
            return qs_surf
        
        @qs_surf.setter
        def qs_surf(self, qs_surf):
            self.qs_surf[...] = qs_surf
        
        @property
        def qn_surf(self):
            """
            Element qn_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 784
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qn_surf(self._handle)
            if array_handle in self._arrays:
                qn_surf = self._arrays[array_handle]
            else:
                qn_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qn_surf)
                self._arrays[array_handle] = qn_surf
            return qn_surf
        
        @qn_surf.setter
        def qn_surf(self, qn_surf):
            self.qn_surf[...] = qn_surf
        
        @property
        def qe0_surf(self):
            """
            Element qe0_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 785
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qe0_surf(self._handle)
            if array_handle in self._arrays:
                qe0_surf = self._arrays[array_handle]
            else:
                qe0_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qe0_surf)
                self._arrays[array_handle] = qe0_surf
            return qe0_surf
        
        @qe0_surf.setter
        def qe0_surf(self, qe0_surf):
            self.qe0_surf[...] = qe0_surf
        
        @property
        def qe_surf(self):
            """
            Element qe_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 786
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qe_surf(self._handle)
            if array_handle in self._arrays:
                qe_surf = self._arrays[array_handle]
            else:
                qe_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qe_surf)
                self._arrays[array_handle] = qe_surf
            return qe_surf
        
        @qe_surf.setter
        def qe_surf(self, qe_surf):
            self.qe_surf[...] = qe_surf
        
        @property
        def qh_surf(self):
            """
            Element qh_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 787
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qh_surf(self._handle)
            if array_handle in self._arrays:
                qh_surf = self._arrays[array_handle]
            else:
                qh_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qh_surf)
                self._arrays[array_handle] = qh_surf
            return qh_surf
        
        @qh_surf.setter
        def qh_surf(self, qh_surf):
            self.qh_surf[...] = qh_surf
        
        @property
        def qh_resist_surf(self):
            """
            Element qh_resist_surf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 788
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__qh_resist_surf(self._handle)
            if array_handle in self._arrays:
                qh_resist_surf = self._arrays[array_handle]
            else:
                qh_resist_surf = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__qh_resist_surf)
                self._arrays[array_handle] = qh_resist_surf
            return qh_resist_surf
        
        @qh_resist_surf.setter
        def qh_resist_surf(self, qh_resist_surf):
            self.qh_resist_surf[...] = qh_resist_surf
        
        @property
        def tsurf_ind(self):
            """
            Element tsurf_ind ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 789
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_heat_state__array__tsurf_ind(self._handle)
            if array_handle in self._arrays:
                tsurf_ind = self._arrays[array_handle]
            else:
                tsurf_ind = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_heat_state__array__tsurf_ind)
                self._arrays[array_handle] = tsurf_ind
            return tsurf_ind
        
        @tsurf_ind.setter
        def tsurf_ind(self, tsurf_ind):
            self.tsurf_ind[...] = tsurf_ind
        
        @property
        def qh_lumps(self):
            """
            Element qh_lumps ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 790
            
            """
            return _supy_driver.f90wrap_heat_state__get__qh_lumps(self._handle)
        
        @qh_lumps.setter
        def qh_lumps(self, qh_lumps):
            _supy_driver.f90wrap_heat_state__set__qh_lumps(self._handle, qh_lumps)
        
        @property
        def qe_lumps(self):
            """
            Element qe_lumps ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 791
            
            """
            return _supy_driver.f90wrap_heat_state__get__qe_lumps(self._handle)
        
        @qe_lumps.setter
        def qe_lumps(self, qe_lumps):
            _supy_driver.f90wrap_heat_state__set__qe_lumps(self._handle, qe_lumps)
        
        @property
        def kclear(self):
            """
            Element kclear ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 792
            
            """
            return _supy_driver.f90wrap_heat_state__get__kclear(self._handle)
        
        @kclear.setter
        def kclear(self, kclear):
            _supy_driver.f90wrap_heat_state__set__kclear(self._handle, kclear)
        
        @property
        def kup(self):
            """
            Element kup ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 793
            
            """
            return _supy_driver.f90wrap_heat_state__get__kup(self._handle)
        
        @kup.setter
        def kup(self, kup):
            _supy_driver.f90wrap_heat_state__set__kup(self._handle, kup)
        
        @property
        def ldown(self):
            """
            Element ldown ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 794
            
            """
            return _supy_driver.f90wrap_heat_state__get__ldown(self._handle)
        
        @ldown.setter
        def ldown(self, ldown):
            _supy_driver.f90wrap_heat_state__set__ldown(self._handle, ldown)
        
        @property
        def lup(self):
            """
            Element lup ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 795
            
            """
            return _supy_driver.f90wrap_heat_state__get__lup(self._handle)
        
        @lup.setter
        def lup(self, lup):
            _supy_driver.f90wrap_heat_state__set__lup(self._handle, lup)
        
        @property
        def qe(self):
            """
            Element qe ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 796
            
            """
            return _supy_driver.f90wrap_heat_state__get__qe(self._handle)
        
        @qe.setter
        def qe(self, qe):
            _supy_driver.f90wrap_heat_state__set__qe(self._handle, qe)
        
        @property
        def qf(self):
            """
            Element qf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 797
            
            """
            return _supy_driver.f90wrap_heat_state__get__qf(self._handle)
        
        @qf.setter
        def qf(self, qf):
            _supy_driver.f90wrap_heat_state__set__qf(self._handle, qf)
        
        @property
        def qf_sahp(self):
            """
            Element qf_sahp ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 798
            
            """
            return _supy_driver.f90wrap_heat_state__get__qf_sahp(self._handle)
        
        @qf_sahp.setter
        def qf_sahp(self, qf_sahp):
            _supy_driver.f90wrap_heat_state__set__qf_sahp(self._handle, qf_sahp)
        
        @property
        def qh(self):
            """
            Element qh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 799
            
            """
            return _supy_driver.f90wrap_heat_state__get__qh(self._handle)
        
        @qh.setter
        def qh(self, qh):
            _supy_driver.f90wrap_heat_state__set__qh(self._handle, qh)
        
        @property
        def qh_residual(self):
            """
            Element qh_residual ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 800
            
            """
            return _supy_driver.f90wrap_heat_state__get__qh_residual(self._handle)
        
        @qh_residual.setter
        def qh_residual(self, qh_residual):
            _supy_driver.f90wrap_heat_state__set__qh_residual(self._handle, qh_residual)
        
        @property
        def qh_resist(self):
            """
            Element qh_resist ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 801
            
            """
            return _supy_driver.f90wrap_heat_state__get__qh_resist(self._handle)
        
        @qh_resist.setter
        def qh_resist(self, qh_resist):
            _supy_driver.f90wrap_heat_state__set__qh_resist(self._handle, qh_resist)
        
        @property
        def qn(self):
            """
            Element qn ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 802
            
            """
            return _supy_driver.f90wrap_heat_state__get__qn(self._handle)
        
        @qn.setter
        def qn(self, qn):
            _supy_driver.f90wrap_heat_state__set__qn(self._handle, qn)
        
        @property
        def qn_snowfree(self):
            """
            Element qn_snowfree ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 803
            
            """
            return _supy_driver.f90wrap_heat_state__get__qn_snowfree(self._handle)
        
        @qn_snowfree.setter
        def qn_snowfree(self, qn_snowfree):
            _supy_driver.f90wrap_heat_state__set__qn_snowfree(self._handle, qn_snowfree)
        
        @property
        def qs(self):
            """
            Element qs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 804
            
            """
            return _supy_driver.f90wrap_heat_state__get__qs(self._handle)
        
        @qs.setter
        def qs(self, qs):
            _supy_driver.f90wrap_heat_state__set__qs(self._handle, qs)
        
        @property
        def tsfc_c(self):
            """
            Element tsfc_c ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 805
            
            """
            return _supy_driver.f90wrap_heat_state__get__tsfc_c(self._handle)
        
        @tsfc_c.setter
        def tsfc_c(self, tsfc_c):
            _supy_driver.f90wrap_heat_state__set__tsfc_c(self._handle, tsfc_c)
        
        @property
        def tsurf(self):
            """
            Element tsurf ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 806
            
            """
            return _supy_driver.f90wrap_heat_state__get__tsurf(self._handle)
        
        @tsurf.setter
        def tsurf(self, tsurf):
            _supy_driver.f90wrap_heat_state__set__tsurf(self._handle, tsurf)
        
        @property
        def qh_init(self):
            """
            Element qh_init ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 807
            
            """
            return _supy_driver.f90wrap_heat_state__get__qh_init(self._handle)
        
        @qh_init.setter
        def qh_init(self, qh_init):
            _supy_driver.f90wrap_heat_state__set__qh_init(self._handle, qh_init)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 810
            
            """
            return _supy_driver.f90wrap_heat_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_heat_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<heat_state>{\n']
            ret.append('    temp_roof : ')
            ret.append(repr(self.temp_roof))
            ret.append(',\n    temp_wall : ')
            ret.append(repr(self.temp_wall))
            ret.append(',\n    temp_surf : ')
            ret.append(repr(self.temp_surf))
            ret.append(',\n    tsfc_roof : ')
            ret.append(repr(self.tsfc_roof))
            ret.append(',\n    tsfc_wall : ')
            ret.append(repr(self.tsfc_wall))
            ret.append(',\n    tsfc_surf : ')
            ret.append(repr(self.tsfc_surf))
            ret.append(',\n    tsfc_roof_stepstart : ')
            ret.append(repr(self.tsfc_roof_stepstart))
            ret.append(',\n    tsfc_wall_stepstart : ')
            ret.append(repr(self.tsfc_wall_stepstart))
            ret.append(',\n    tsfc_surf_stepstart : ')
            ret.append(repr(self.tsfc_surf_stepstart))
            ret.append(',\n    qs_roof : ')
            ret.append(repr(self.qs_roof))
            ret.append(',\n    qn_roof : ')
            ret.append(repr(self.qn_roof))
            ret.append(',\n    qe_roof : ')
            ret.append(repr(self.qe_roof))
            ret.append(',\n    qh_roof : ')
            ret.append(repr(self.qh_roof))
            ret.append(',\n    qh_resist_roof : ')
            ret.append(repr(self.qh_resist_roof))
            ret.append(',\n    qs_wall : ')
            ret.append(repr(self.qs_wall))
            ret.append(',\n    qn_wall : ')
            ret.append(repr(self.qn_wall))
            ret.append(',\n    qe_wall : ')
            ret.append(repr(self.qe_wall))
            ret.append(',\n    qh_wall : ')
            ret.append(repr(self.qh_wall))
            ret.append(',\n    qh_resist_wall : ')
            ret.append(repr(self.qh_resist_wall))
            ret.append(',\n    qs_surf : ')
            ret.append(repr(self.qs_surf))
            ret.append(',\n    qn_surf : ')
            ret.append(repr(self.qn_surf))
            ret.append(',\n    qe0_surf : ')
            ret.append(repr(self.qe0_surf))
            ret.append(',\n    qe_surf : ')
            ret.append(repr(self.qe_surf))
            ret.append(',\n    qh_surf : ')
            ret.append(repr(self.qh_surf))
            ret.append(',\n    qh_resist_surf : ')
            ret.append(repr(self.qh_resist_surf))
            ret.append(',\n    tsurf_ind : ')
            ret.append(repr(self.tsurf_ind))
            ret.append(',\n    qh_lumps : ')
            ret.append(repr(self.qh_lumps))
            ret.append(',\n    qe_lumps : ')
            ret.append(repr(self.qe_lumps))
            ret.append(',\n    kclear : ')
            ret.append(repr(self.kclear))
            ret.append(',\n    kup : ')
            ret.append(repr(self.kup))
            ret.append(',\n    ldown : ')
            ret.append(repr(self.ldown))
            ret.append(',\n    lup : ')
            ret.append(repr(self.lup))
            ret.append(',\n    qe : ')
            ret.append(repr(self.qe))
            ret.append(',\n    qf : ')
            ret.append(repr(self.qf))
            ret.append(',\n    qf_sahp : ')
            ret.append(repr(self.qf_sahp))
            ret.append(',\n    qh : ')
            ret.append(repr(self.qh))
            ret.append(',\n    qh_residual : ')
            ret.append(repr(self.qh_residual))
            ret.append(',\n    qh_resist : ')
            ret.append(repr(self.qh_resist))
            ret.append(',\n    qn : ')
            ret.append(repr(self.qn))
            ret.append(',\n    qn_snowfree : ')
            ret.append(repr(self.qn_snowfree))
            ret.append(',\n    qs : ')
            ret.append(repr(self.qs))
            ret.append(',\n    tsfc_c : ')
            ret.append(repr(self.tsfc_c))
            ret.append(',\n    tsurf : ')
            ret.append(repr(self.tsurf))
            ret.append(',\n    qh_init : ')
            ret.append(repr(self.qh_init))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.ROUGHNESS_STATE")
    class ROUGHNESS_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=roughness_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 815-830
        
        """
        def __init__(self, handle=None):
            """
            self = Roughness_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 815-830
            
            
            Returns
            -------
            this : Roughness_State
            	Object to be constructed
            
            
            Automatically generated constructor for roughness_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__roughness_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Roughness_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 815-830
            
            Parameters
            ----------
            this : Roughness_State
            	Object to be destructed
            
            
            Automatically generated destructor for roughness_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__roughness_state_finalise(this=self._handle)
        
        @property
        def faibldg_use(self):
            """
            Element faibldg_use ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 818
            
            """
            return _supy_driver.f90wrap_roughness_state__get__faibldg_use(self._handle)
        
        @faibldg_use.setter
        def faibldg_use(self, faibldg_use):
            _supy_driver.f90wrap_roughness_state__set__faibldg_use(self._handle, \
                faibldg_use)
        
        @property
        def faievetree_use(self):
            """
            Element faievetree_use ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 819
            
            """
            return _supy_driver.f90wrap_roughness_state__get__faievetree_use(self._handle)
        
        @faievetree_use.setter
        def faievetree_use(self, faievetree_use):
            _supy_driver.f90wrap_roughness_state__set__faievetree_use(self._handle, \
                faievetree_use)
        
        @property
        def faidectree_use(self):
            """
            Element faidectree_use ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 820
            
            """
            return _supy_driver.f90wrap_roughness_state__get__faidectree_use(self._handle)
        
        @faidectree_use.setter
        def faidectree_use(self, faidectree_use):
            _supy_driver.f90wrap_roughness_state__set__faidectree_use(self._handle, \
                faidectree_use)
        
        @property
        def fai(self):
            """
            Element fai ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 821
            
            """
            return _supy_driver.f90wrap_roughness_state__get__fai(self._handle)
        
        @fai.setter
        def fai(self, fai):
            _supy_driver.f90wrap_roughness_state__set__fai(self._handle, fai)
        
        @property
        def pai(self):
            """
            Element pai ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 822
            
            """
            return _supy_driver.f90wrap_roughness_state__get__pai(self._handle)
        
        @pai.setter
        def pai(self, pai):
            _supy_driver.f90wrap_roughness_state__set__pai(self._handle, pai)
        
        @property
        def zh(self):
            """
            Element zh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 823
            
            """
            return _supy_driver.f90wrap_roughness_state__get__zh(self._handle)
        
        @zh.setter
        def zh(self, zh):
            _supy_driver.f90wrap_roughness_state__set__zh(self._handle, zh)
        
        @property
        def z0m(self):
            """
            Element z0m ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 824
            
            """
            return _supy_driver.f90wrap_roughness_state__get__z0m(self._handle)
        
        @z0m.setter
        def z0m(self, z0m):
            _supy_driver.f90wrap_roughness_state__set__z0m(self._handle, z0m)
        
        @property
        def z0v(self):
            """
            Element z0v ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 825
            
            """
            return _supy_driver.f90wrap_roughness_state__get__z0v(self._handle)
        
        @z0v.setter
        def z0v(self, z0v):
            _supy_driver.f90wrap_roughness_state__set__z0v(self._handle, z0v)
        
        @property
        def zdm(self):
            """
            Element zdm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 826
            
            """
            return _supy_driver.f90wrap_roughness_state__get__zdm(self._handle)
        
        @zdm.setter
        def zdm(self, zdm):
            _supy_driver.f90wrap_roughness_state__set__zdm(self._handle, zdm)
        
        @property
        def zzd(self):
            """
            Element zzd ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 827
            
            """
            return _supy_driver.f90wrap_roughness_state__get__zzd(self._handle)
        
        @zzd.setter
        def zzd(self, zzd):
            _supy_driver.f90wrap_roughness_state__set__zzd(self._handle, zzd)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 830
            
            """
            return _supy_driver.f90wrap_roughness_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_roughness_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<roughness_state>{\n']
            ret.append('    faibldg_use : ')
            ret.append(repr(self.faibldg_use))
            ret.append(',\n    faievetree_use : ')
            ret.append(repr(self.faievetree_use))
            ret.append(',\n    faidectree_use : ')
            ret.append(repr(self.faidectree_use))
            ret.append(',\n    fai : ')
            ret.append(repr(self.fai))
            ret.append(',\n    pai : ')
            ret.append(repr(self.pai))
            ret.append(',\n    zh : ')
            ret.append(repr(self.zh))
            ret.append(',\n    z0m : ')
            ret.append(repr(self.z0m))
            ret.append(',\n    z0v : ')
            ret.append(repr(self.z0v))
            ret.append(',\n    zdm : ')
            ret.append(repr(self.zdm))
            ret.append(',\n    zzd : ')
            ret.append(repr(self.zzd))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.STEBBS_STATE")
    class STEBBS_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=stebbs_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 832-864
        
        """
        def __init__(self, handle=None):
            """
            self = Stebbs_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 832-864
            
            
            Returns
            -------
            this : Stebbs_State
            	Object to be constructed
            
            
            Automatically generated constructor for stebbs_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__stebbs_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Stebbs_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 832-864
            
            Parameters
            ----------
            this : Stebbs_State
            	Object to be destructed
            
            
            Automatically generated destructor for stebbs_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__stebbs_state_finalise(this=self._handle)
        
        @property
        def kdown2d(self):
            """
            Element kdown2d ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 834
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__kdown2d(self._handle)
        
        @kdown2d.setter
        def kdown2d(self, kdown2d):
            _supy_driver.f90wrap_stebbs_state__set__kdown2d(self._handle, kdown2d)
        
        @property
        def kup2d(self):
            """
            Element kup2d ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 835
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__kup2d(self._handle)
        
        @kup2d.setter
        def kup2d(self, kup2d):
            _supy_driver.f90wrap_stebbs_state__set__kup2d(self._handle, kup2d)
        
        @property
        def kwest(self):
            """
            Element kwest ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 836
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__kwest(self._handle)
        
        @kwest.setter
        def kwest(self, kwest):
            _supy_driver.f90wrap_stebbs_state__set__kwest(self._handle, kwest)
        
        @property
        def ksouth(self):
            """
            Element ksouth ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 837
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__ksouth(self._handle)
        
        @ksouth.setter
        def ksouth(self, ksouth):
            _supy_driver.f90wrap_stebbs_state__set__ksouth(self._handle, ksouth)
        
        @property
        def knorth(self):
            """
            Element knorth ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 838
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__knorth(self._handle)
        
        @knorth.setter
        def knorth(self, knorth):
            _supy_driver.f90wrap_stebbs_state__set__knorth(self._handle, knorth)
        
        @property
        def keast(self):
            """
            Element keast ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 839
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__keast(self._handle)
        
        @keast.setter
        def keast(self, keast):
            _supy_driver.f90wrap_stebbs_state__set__keast(self._handle, keast)
        
        @property
        def ldown2d(self):
            """
            Element ldown2d ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 840
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__ldown2d(self._handle)
        
        @ldown2d.setter
        def ldown2d(self, ldown2d):
            _supy_driver.f90wrap_stebbs_state__set__ldown2d(self._handle, ldown2d)
        
        @property
        def lup2d(self):
            """
            Element lup2d ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 841
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__lup2d(self._handle)
        
        @lup2d.setter
        def lup2d(self, lup2d):
            _supy_driver.f90wrap_stebbs_state__set__lup2d(self._handle, lup2d)
        
        @property
        def lwest(self):
            """
            Element lwest ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 842
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__lwest(self._handle)
        
        @lwest.setter
        def lwest(self, lwest):
            _supy_driver.f90wrap_stebbs_state__set__lwest(self._handle, lwest)
        
        @property
        def lsouth(self):
            """
            Element lsouth ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 843
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__lsouth(self._handle)
        
        @lsouth.setter
        def lsouth(self, lsouth):
            _supy_driver.f90wrap_stebbs_state__set__lsouth(self._handle, lsouth)
        
        @property
        def lnorth(self):
            """
            Element lnorth ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 844
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__lnorth(self._handle)
        
        @lnorth.setter
        def lnorth(self, lnorth):
            _supy_driver.f90wrap_stebbs_state__set__lnorth(self._handle, lnorth)
        
        @property
        def least(self):
            """
            Element least ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 845
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__least(self._handle)
        
        @least.setter
        def least(self, least):
            _supy_driver.f90wrap_stebbs_state__set__least(self._handle, least)
        
        @property
        def indoorairstarttemperature(self):
            """
            Element indoorairstarttemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 847
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__indoorairstarttemperature(self._handle)
        
        @indoorairstarttemperature.setter
        def indoorairstarttemperature(self, indoorairstarttemperature):
            _supy_driver.f90wrap_stebbs_state__set__indoorairstarttemperature(self._handle, \
                indoorairstarttemperature)
        
        @property
        def indoormassstarttemperature(self):
            """
            Element indoormassstarttemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 848
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__indoormassstarttemperature(self._handle)
        
        @indoormassstarttemperature.setter
        def indoormassstarttemperature(self, indoormassstarttemperature):
            _supy_driver.f90wrap_stebbs_state__set__indoormassstarttemperature(self._handle, \
                indoormassstarttemperature)
        
        @property
        def wallindoorsurfacetemperature(self):
            """
            Element wallindoorsurfacetemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 849
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__wallindoorsurfacetemperature(self._handle)
        
        @wallindoorsurfacetemperature.setter
        def wallindoorsurfacetemperature(self, wallindoorsurfacetemperature):
            _supy_driver.f90wrap_stebbs_state__set__wallindoorsurfacetemperature(self._handle, \
                wallindoorsurfacetemperature)
        
        @property
        def walloutdoorsurfacetemperature(self):
            """
            Element walloutdoorsurfacetemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 850
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__walloutdoorsurfacetemperature(self._handle)
        
        @walloutdoorsurfacetemperature.setter
        def walloutdoorsurfacetemperature(self, walloutdoorsurfacetemperature):
            _supy_driver.f90wrap_stebbs_state__set__walloutdoorsurfacetemperature(self._handle, \
                walloutdoorsurfacetemperature)
        
        @property
        def windowindoorsurfacetemperature(self):
            """
            Element windowindoorsurfacetemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 851
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__windowindoorsurfacetemperature(self._handle)
        
        @windowindoorsurfacetemperature.setter
        def windowindoorsurfacetemperature(self, windowindoorsurfacetemperature):
            _supy_driver.f90wrap_stebbs_state__set__windowindoorsurfacetemperature(self._handle, \
                windowindoorsurfacetemperature)
        
        @property
        def windowoutdoorsurfacetemperature(self):
            """
            Element windowoutdoorsurfacetemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 852
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__windowoutdoorsurfacetemperature(self._handle)
        
        @windowoutdoorsurfacetemperature.setter
        def windowoutdoorsurfacetemperature(self, windowoutdoorsurfacetemperature):
            _supy_driver.f90wrap_stebbs_state__set__windowoutdoorsurfacetemperature(self._handle, \
                windowoutdoorsurfacetemperature)
        
        @property
        def groundfloorindoorsurfacetemperature(self):
            """
            Element groundfloorindoorsurfacetemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 853
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__groundfloorindoorsurfacetemperature(self._handle)
        
        @groundfloorindoorsurfacetemperature.setter
        def groundfloorindoorsurfacetemperature(self, \
            groundfloorindoorsurfacetemperature):
            _supy_driver.f90wrap_stebbs_state__set__groundfloorindoorsurfacetemperature(self._handle, \
                groundfloorindoorsurfacetemperature)
        
        @property
        def groundflooroutdoorsurfacetemperature(self):
            """
            Element groundflooroutdoorsurfacetemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 854
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__groundflooroutdoorsurfacetemperature(self._handle)
        
        @groundflooroutdoorsurfacetemperature.setter
        def groundflooroutdoorsurfacetemperature(self, \
            groundflooroutdoorsurfacetemperature):
            _supy_driver.f90wrap_stebbs_state__set__groundflooroutdoorsurfacetemperature(self._handle, \
                groundflooroutdoorsurfacetemperature)
        
        @property
        def watertanktemperature(self):
            """
            Element watertanktemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 855
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__watertanktemperature(self._handle)
        
        @watertanktemperature.setter
        def watertanktemperature(self, watertanktemperature):
            _supy_driver.f90wrap_stebbs_state__set__watertanktemperature(self._handle, \
                watertanktemperature)
        
        @property
        def internalwallwatertanktemperature(self):
            """
            Element internalwallwatertanktemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 856
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__internalwallwatertanktemperature(self._handle)
        
        @internalwallwatertanktemperature.setter
        def internalwallwatertanktemperature(self, internalwallwatertanktemperature):
            _supy_driver.f90wrap_stebbs_state__set__internalwallwatertanktemperature(self._handle, \
                internalwallwatertanktemperature)
        
        @property
        def externalwallwatertanktemperature(self):
            """
            Element externalwallwatertanktemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 857
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__externalwallwatertanktemperature(self._handle)
        
        @externalwallwatertanktemperature.setter
        def externalwallwatertanktemperature(self, externalwallwatertanktemperature):
            _supy_driver.f90wrap_stebbs_state__set__externalwallwatertanktemperature(self._handle, \
                externalwallwatertanktemperature)
        
        @property
        def mainswatertemperature(self):
            """
            Element mainswatertemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 858
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__mainswatertemperature(self._handle)
        
        @mainswatertemperature.setter
        def mainswatertemperature(self, mainswatertemperature):
            _supy_driver.f90wrap_stebbs_state__set__mainswatertemperature(self._handle, \
                mainswatertemperature)
        
        @property
        def domestichotwatertemperatureinuseinbuilding(self):
            """
            Element domestichotwatertemperatureinuseinbuilding ftype=real(kind(1d0) \
                pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 859
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__domestichotwatertemperatureinused14f(self._handle)
        
        @domestichotwatertemperatureinuseinbuilding.setter
        def domestichotwatertemperatureinuseinbuilding(self, \
            domestichotwatertemperatureinuseinbuilding):
            _supy_driver.f90wrap_stebbs_state__set__domestichotwatertemperatureinuse0ba7(self._handle, \
                domestichotwatertemperatureinuseinbuilding)
        
        @property
        def internalwalldhwvesseltemperature(self):
            """
            Element internalwalldhwvesseltemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 860
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__internalwalldhwvesseltemperature(self._handle)
        
        @internalwalldhwvesseltemperature.setter
        def internalwalldhwvesseltemperature(self, internalwalldhwvesseltemperature):
            _supy_driver.f90wrap_stebbs_state__set__internalwalldhwvesseltemperature(self._handle, \
                internalwalldhwvesseltemperature)
        
        @property
        def externalwalldhwvesseltemperature(self):
            """
            Element externalwalldhwvesseltemperature ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 861
            
            """
            return \
                _supy_driver.f90wrap_stebbs_state__get__externalwalldhwvesseltemperature(self._handle)
        
        @externalwalldhwvesseltemperature.setter
        def externalwalldhwvesseltemperature(self, externalwalldhwvesseltemperature):
            _supy_driver.f90wrap_stebbs_state__set__externalwalldhwvesseltemperature(self._handle, \
                externalwalldhwvesseltemperature)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 864
            
            """
            return _supy_driver.f90wrap_stebbs_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_stebbs_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<stebbs_state>{\n']
            ret.append('    kdown2d : ')
            ret.append(repr(self.kdown2d))
            ret.append(',\n    kup2d : ')
            ret.append(repr(self.kup2d))
            ret.append(',\n    kwest : ')
            ret.append(repr(self.kwest))
            ret.append(',\n    ksouth : ')
            ret.append(repr(self.ksouth))
            ret.append(',\n    knorth : ')
            ret.append(repr(self.knorth))
            ret.append(',\n    keast : ')
            ret.append(repr(self.keast))
            ret.append(',\n    ldown2d : ')
            ret.append(repr(self.ldown2d))
            ret.append(',\n    lup2d : ')
            ret.append(repr(self.lup2d))
            ret.append(',\n    lwest : ')
            ret.append(repr(self.lwest))
            ret.append(',\n    lsouth : ')
            ret.append(repr(self.lsouth))
            ret.append(',\n    lnorth : ')
            ret.append(repr(self.lnorth))
            ret.append(',\n    least : ')
            ret.append(repr(self.least))
            ret.append(',\n    indoorairstarttemperature : ')
            ret.append(repr(self.indoorairstarttemperature))
            ret.append(',\n    indoormassstarttemperature : ')
            ret.append(repr(self.indoormassstarttemperature))
            ret.append(',\n    wallindoorsurfacetemperature : ')
            ret.append(repr(self.wallindoorsurfacetemperature))
            ret.append(',\n    walloutdoorsurfacetemperature : ')
            ret.append(repr(self.walloutdoorsurfacetemperature))
            ret.append(',\n    windowindoorsurfacetemperature : ')
            ret.append(repr(self.windowindoorsurfacetemperature))
            ret.append(',\n    windowoutdoorsurfacetemperature : ')
            ret.append(repr(self.windowoutdoorsurfacetemperature))
            ret.append(',\n    groundfloorindoorsurfacetemperature : ')
            ret.append(repr(self.groundfloorindoorsurfacetemperature))
            ret.append(',\n    groundflooroutdoorsurfacetemperature : ')
            ret.append(repr(self.groundflooroutdoorsurfacetemperature))
            ret.append(',\n    watertanktemperature : ')
            ret.append(repr(self.watertanktemperature))
            ret.append(',\n    internalwallwatertanktemperature : ')
            ret.append(repr(self.internalwallwatertanktemperature))
            ret.append(',\n    externalwallwatertanktemperature : ')
            ret.append(repr(self.externalwallwatertanktemperature))
            ret.append(',\n    mainswatertemperature : ')
            ret.append(repr(self.mainswatertemperature))
            ret.append(',\n    domestichotwatertemperatureinuseinbuilding : ')
            ret.append(repr(self.domestichotwatertemperatureinuseinbuilding))
            ret.append(',\n    internalwalldhwvesseltemperature : ')
            ret.append(repr(self.internalwalldhwvesseltemperature))
            ret.append(',\n    externalwalldhwvesseltemperature : ')
            ret.append(repr(self.externalwalldhwvesseltemperature))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.NHOOD_STATE")
    class NHOOD_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=nhood_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 866-873
        
        """
        def __init__(self, handle=None):
            """
            self = Nhood_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 866-873
            
            
            Returns
            -------
            this : Nhood_State
            	Object to be constructed
            
            
            Automatically generated constructor for nhood_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__nhood_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Nhood_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 866-873
            
            Parameters
            ----------
            this : Nhood_State
            	Object to be destructed
            
            
            Automatically generated destructor for nhood_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__nhood_state_finalise(this=self._handle)
        
        @property
        def u_hbh_1dravg(self):
            """
            Element u_hbh_1dravg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 867
            
            """
            return _supy_driver.f90wrap_nhood_state__get__u_hbh_1dravg(self._handle)
        
        @u_hbh_1dravg.setter
        def u_hbh_1dravg(self, u_hbh_1dravg):
            _supy_driver.f90wrap_nhood_state__set__u_hbh_1dravg(self._handle, u_hbh_1dravg)
        
        @property
        def qn_1dravg(self):
            """
            Element qn_1dravg ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 868
            
            """
            return _supy_driver.f90wrap_nhood_state__get__qn_1dravg(self._handle)
        
        @qn_1dravg.setter
        def qn_1dravg(self, qn_1dravg):
            _supy_driver.f90wrap_nhood_state__set__qn_1dravg(self._handle, qn_1dravg)
        
        @property
        def tair_mn_prev(self):
            """
            Element tair_mn_prev ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 869
            
            """
            return _supy_driver.f90wrap_nhood_state__get__tair_mn_prev(self._handle)
        
        @tair_mn_prev.setter
        def tair_mn_prev(self, tair_mn_prev):
            _supy_driver.f90wrap_nhood_state__set__tair_mn_prev(self._handle, tair_mn_prev)
        
        @property
        def iter_count(self):
            """
            Element iter_count ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 870
            
            """
            return _supy_driver.f90wrap_nhood_state__get__iter_count(self._handle)
        
        @iter_count.setter
        def iter_count(self, iter_count):
            _supy_driver.f90wrap_nhood_state__set__iter_count(self._handle, iter_count)
        
        @property
        def iter_safe(self):
            """
            Element iter_safe ftype=logical pytype=bool
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 873
            
            """
            return _supy_driver.f90wrap_nhood_state__get__iter_safe(self._handle)
        
        @iter_safe.setter
        def iter_safe(self, iter_safe):
            _supy_driver.f90wrap_nhood_state__set__iter_safe(self._handle, iter_safe)
        
        def __str__(self):
            ret = ['<nhood_state>{\n']
            ret.append('    u_hbh_1dravg : ')
            ret.append(repr(self.u_hbh_1dravg))
            ret.append(',\n    qn_1dravg : ')
            ret.append(repr(self.qn_1dravg))
            ret.append(',\n    tair_mn_prev : ')
            ret.append(repr(self.tair_mn_prev))
            ret.append(',\n    iter_count : ')
            ret.append(repr(self.iter_count))
            ret.append(',\n    iter_safe : ')
            ret.append(repr(self.iter_safe))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_STATE")
    class SUEWS_STATE(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 875-892
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_State()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 875-892
            
            
            Returns
            -------
            this : Suews_State
            	Object to be constructed
            
            
            Automatically generated constructor for suews_state
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_state_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 875-892
            
            Parameters
            ----------
            this : Suews_State
            	Object to be destructed
            
            
            Automatically generated destructor for suews_state
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_state_finalise(this=self._handle)
        
        def allocate(self, nlayer, ndepth):
            """
            allocate__binding__suews_state(self, nlayer, ndepth)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1105-1112
            
            Parameters
            ----------
            self : Suews_State
            nlayer : int
            ndepth : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__allocate__binding__suews_state(self=self._handle, \
                nlayer=nlayer, ndepth=ndepth)
        
        def deallocate(self):
            """
            deallocate__binding__suews_state(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1114-1118
            
            Parameters
            ----------
            self : Suews_State
            
            """
            _supy_driver.f90wrap_suews_def_dts__deallocate__binding__suews_state(self=self._handle)
        
        def reset_atm_state(self):
            """
            reset_atm_state__binding__suews_state(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1120-1133
            
            Parameters
            ----------
            self : Suews_State
            
            """
            _supy_driver.f90wrap_suews_def_dts__reset_atm_state__binding__suews_state(self=self._handle)
        
        def check_and_reset_states(self, ref_state):
            """
            check_and_reset_states__binding__suews_state(self, ref_state)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1400-1439
            
            Parameters
            ----------
            self : Suews_State
            ref_state : Suews_State
            
            """
            _supy_driver.f90wrap_suews_def_dts__check_and_reset_states__binding__sue4993(self=self._handle, \
                ref_state=ref_state._handle)
        
        @property
        def flagstate(self):
            """
            Element flagstate ftype=type(flag_state) pytype=Flag_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 876
            
            """
            flagstate_handle = \
                _supy_driver.f90wrap_suews_state__get__flagstate(self._handle)
            if tuple(flagstate_handle) in self._objs:
                flagstate = self._objs[tuple(flagstate_handle)]
            else:
                flagstate = suews_def_dts.flag_STATE.from_handle(flagstate_handle)
                self._objs[tuple(flagstate_handle)] = flagstate
            return flagstate
        
        @flagstate.setter
        def flagstate(self, flagstate):
            flagstate = flagstate._handle
            _supy_driver.f90wrap_suews_state__set__flagstate(self._handle, flagstate)
        
        @property
        def anthroemisstate(self):
            """
            Element anthroemisstate ftype=type(anthroemis_state) pytype=Anthroemis_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 877
            
            """
            anthroemisstate_handle = \
                _supy_driver.f90wrap_suews_state__get__anthroemisstate(self._handle)
            if tuple(anthroemisstate_handle) in self._objs:
                anthroemisstate = self._objs[tuple(anthroemisstate_handle)]
            else:
                anthroemisstate = \
                    suews_def_dts.anthroEmis_STATE.from_handle(anthroemisstate_handle)
                self._objs[tuple(anthroemisstate_handle)] = anthroemisstate
            return anthroemisstate
        
        @anthroemisstate.setter
        def anthroemisstate(self, anthroemisstate):
            anthroemisstate = anthroemisstate._handle
            _supy_driver.f90wrap_suews_state__set__anthroemisstate(self._handle, \
                anthroemisstate)
        
        @property
        def ohmstate(self):
            """
            Element ohmstate ftype=type(ohm_state) pytype=Ohm_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 878
            
            """
            ohmstate_handle = _supy_driver.f90wrap_suews_state__get__ohmstate(self._handle)
            if tuple(ohmstate_handle) in self._objs:
                ohmstate = self._objs[tuple(ohmstate_handle)]
            else:
                ohmstate = suews_def_dts.OHM_STATE.from_handle(ohmstate_handle)
                self._objs[tuple(ohmstate_handle)] = ohmstate
            return ohmstate
        
        @ohmstate.setter
        def ohmstate(self, ohmstate):
            ohmstate = ohmstate._handle
            _supy_driver.f90wrap_suews_state__set__ohmstate(self._handle, ohmstate)
        
        @property
        def solarstate(self):
            """
            Element solarstate ftype=type(solar_state) pytype=Solar_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 879
            
            """
            solarstate_handle = \
                _supy_driver.f90wrap_suews_state__get__solarstate(self._handle)
            if tuple(solarstate_handle) in self._objs:
                solarstate = self._objs[tuple(solarstate_handle)]
            else:
                solarstate = suews_def_dts.solar_State.from_handle(solarstate_handle)
                self._objs[tuple(solarstate_handle)] = solarstate
            return solarstate
        
        @solarstate.setter
        def solarstate(self, solarstate):
            solarstate = solarstate._handle
            _supy_driver.f90wrap_suews_state__set__solarstate(self._handle, solarstate)
        
        @property
        def atmstate(self):
            """
            Element atmstate ftype=type(atm_state) pytype=Atm_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 880
            
            """
            atmstate_handle = _supy_driver.f90wrap_suews_state__get__atmstate(self._handle)
            if tuple(atmstate_handle) in self._objs:
                atmstate = self._objs[tuple(atmstate_handle)]
            else:
                atmstate = suews_def_dts.atm_state.from_handle(atmstate_handle)
                self._objs[tuple(atmstate_handle)] = atmstate
            return atmstate
        
        @atmstate.setter
        def atmstate(self, atmstate):
            atmstate = atmstate._handle
            _supy_driver.f90wrap_suews_state__set__atmstate(self._handle, atmstate)
        
        @property
        def phenstate(self):
            """
            Element phenstate ftype=type(phenology_state) pytype=Phenology_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 881
            
            """
            phenstate_handle = \
                _supy_driver.f90wrap_suews_state__get__phenstate(self._handle)
            if tuple(phenstate_handle) in self._objs:
                phenstate = self._objs[tuple(phenstate_handle)]
            else:
                phenstate = suews_def_dts.PHENOLOGY_STATE.from_handle(phenstate_handle)
                self._objs[tuple(phenstate_handle)] = phenstate
            return phenstate
        
        @phenstate.setter
        def phenstate(self, phenstate):
            phenstate = phenstate._handle
            _supy_driver.f90wrap_suews_state__set__phenstate(self._handle, phenstate)
        
        @property
        def snowstate(self):
            """
            Element snowstate ftype=type(snow_state) pytype=Snow_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 882
            
            """
            snowstate_handle = \
                _supy_driver.f90wrap_suews_state__get__snowstate(self._handle)
            if tuple(snowstate_handle) in self._objs:
                snowstate = self._objs[tuple(snowstate_handle)]
            else:
                snowstate = suews_def_dts.SNOW_STATE.from_handle(snowstate_handle)
                self._objs[tuple(snowstate_handle)] = snowstate
            return snowstate
        
        @snowstate.setter
        def snowstate(self, snowstate):
            snowstate = snowstate._handle
            _supy_driver.f90wrap_suews_state__set__snowstate(self._handle, snowstate)
        
        @property
        def hydrostate(self):
            """
            Element hydrostate ftype=type(hydro_state) pytype=Hydro_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 883
            
            """
            hydrostate_handle = \
                _supy_driver.f90wrap_suews_state__get__hydrostate(self._handle)
            if tuple(hydrostate_handle) in self._objs:
                hydrostate = self._objs[tuple(hydrostate_handle)]
            else:
                hydrostate = suews_def_dts.HYDRO_STATE.from_handle(hydrostate_handle)
                self._objs[tuple(hydrostate_handle)] = hydrostate
            return hydrostate
        
        @hydrostate.setter
        def hydrostate(self, hydrostate):
            hydrostate = hydrostate._handle
            _supy_driver.f90wrap_suews_state__set__hydrostate(self._handle, hydrostate)
        
        @property
        def heatstate(self):
            """
            Element heatstate ftype=type(heat_state) pytype=Heat_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 884
            
            """
            heatstate_handle = \
                _supy_driver.f90wrap_suews_state__get__heatstate(self._handle)
            if tuple(heatstate_handle) in self._objs:
                heatstate = self._objs[tuple(heatstate_handle)]
            else:
                heatstate = suews_def_dts.HEAT_STATE.from_handle(heatstate_handle)
                self._objs[tuple(heatstate_handle)] = heatstate
            return heatstate
        
        @heatstate.setter
        def heatstate(self, heatstate):
            heatstate = heatstate._handle
            _supy_driver.f90wrap_suews_state__set__heatstate(self._handle, heatstate)
        
        @property
        def roughnessstate(self):
            """
            Element roughnessstate ftype=type(roughness_state) pytype=Roughness_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 885
            
            """
            roughnessstate_handle = \
                _supy_driver.f90wrap_suews_state__get__roughnessstate(self._handle)
            if tuple(roughnessstate_handle) in self._objs:
                roughnessstate = self._objs[tuple(roughnessstate_handle)]
            else:
                roughnessstate = \
                    suews_def_dts.ROUGHNESS_STATE.from_handle(roughnessstate_handle)
                self._objs[tuple(roughnessstate_handle)] = roughnessstate
            return roughnessstate
        
        @roughnessstate.setter
        def roughnessstate(self, roughnessstate):
            roughnessstate = roughnessstate._handle
            _supy_driver.f90wrap_suews_state__set__roughnessstate(self._handle, \
                roughnessstate)
        
        @property
        def stebbsstate(self):
            """
            Element stebbsstate ftype=type(stebbs_state) pytype=Stebbs_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 886
            
            """
            stebbsstate_handle = \
                _supy_driver.f90wrap_suews_state__get__stebbsstate(self._handle)
            if tuple(stebbsstate_handle) in self._objs:
                stebbsstate = self._objs[tuple(stebbsstate_handle)]
            else:
                stebbsstate = suews_def_dts.STEBBS_STATE.from_handle(stebbsstate_handle)
                self._objs[tuple(stebbsstate_handle)] = stebbsstate
            return stebbsstate
        
        @stebbsstate.setter
        def stebbsstate(self, stebbsstate):
            stebbsstate = stebbsstate._handle
            _supy_driver.f90wrap_suews_state__set__stebbsstate(self._handle, stebbsstate)
        
        @property
        def nhoodstate(self):
            """
            Element nhoodstate ftype=type(nhood_state) pytype=Nhood_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 887
            
            """
            nhoodstate_handle = \
                _supy_driver.f90wrap_suews_state__get__nhoodstate(self._handle)
            if tuple(nhoodstate_handle) in self._objs:
                nhoodstate = self._objs[tuple(nhoodstate_handle)]
            else:
                nhoodstate = suews_def_dts.NHOOD_STATE.from_handle(nhoodstate_handle)
                self._objs[tuple(nhoodstate_handle)] = nhoodstate
            return nhoodstate
        
        @nhoodstate.setter
        def nhoodstate(self, nhoodstate):
            nhoodstate = nhoodstate._handle
            _supy_driver.f90wrap_suews_state__set__nhoodstate(self._handle, nhoodstate)
        
        def __str__(self):
            ret = ['<suews_state>{\n']
            ret.append('    flagstate : ')
            ret.append(repr(self.flagstate))
            ret.append(',\n    anthroemisstate : ')
            ret.append(repr(self.anthroemisstate))
            ret.append(',\n    ohmstate : ')
            ret.append(repr(self.ohmstate))
            ret.append(',\n    solarstate : ')
            ret.append(repr(self.solarstate))
            ret.append(',\n    atmstate : ')
            ret.append(repr(self.atmstate))
            ret.append(',\n    phenstate : ')
            ret.append(repr(self.phenstate))
            ret.append(',\n    snowstate : ')
            ret.append(repr(self.snowstate))
            ret.append(',\n    hydrostate : ')
            ret.append(repr(self.hydrostate))
            ret.append(',\n    heatstate : ')
            ret.append(repr(self.heatstate))
            ret.append(',\n    roughnessstate : ')
            ret.append(repr(self.roughnessstate))
            ret.append(',\n    stebbsstate : ')
            ret.append(repr(self.stebbsstate))
            ret.append(',\n    nhoodstate : ')
            ret.append(repr(self.nhoodstate))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_FORCING")
    class SUEWS_FORCING(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_forcing)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 895-912
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Forcing()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 895-912
            
            
            Returns
            -------
            this : Suews_Forcing
            	Object to be constructed
            
            
            Automatically generated constructor for suews_forcing
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_forcing_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Forcing
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 895-912
            
            Parameters
            ----------
            this : Suews_Forcing
            	Object to be destructed
            
            
            Automatically generated destructor for suews_forcing
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_forcing_finalise(this=self._handle)
        
        @property
        def kdown(self):
            """
            Element kdown ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 896
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__kdown(self._handle)
        
        @kdown.setter
        def kdown(self, kdown):
            _supy_driver.f90wrap_suews_forcing__set__kdown(self._handle, kdown)
        
        @property
        def ldown(self):
            """
            Element ldown ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 897
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__ldown(self._handle)
        
        @ldown.setter
        def ldown(self, ldown):
            _supy_driver.f90wrap_suews_forcing__set__ldown(self._handle, ldown)
        
        @property
        def rh(self):
            """
            Element rh ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 898
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__rh(self._handle)
        
        @rh.setter
        def rh(self, rh):
            _supy_driver.f90wrap_suews_forcing__set__rh(self._handle, rh)
        
        @property
        def pres(self):
            """
            Element pres ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 899
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__pres(self._handle)
        
        @pres.setter
        def pres(self, pres):
            _supy_driver.f90wrap_suews_forcing__set__pres(self._handle, pres)
        
        @property
        def tair_av_5d(self):
            """
            Element tair_av_5d ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 900
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__tair_av_5d(self._handle)
        
        @tair_av_5d.setter
        def tair_av_5d(self, tair_av_5d):
            _supy_driver.f90wrap_suews_forcing__set__tair_av_5d(self._handle, tair_av_5d)
        
        @property
        def u(self):
            """
            Element u ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 901
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__u(self._handle)
        
        @u.setter
        def u(self, u):
            _supy_driver.f90wrap_suews_forcing__set__u(self._handle, u)
        
        @property
        def rain(self):
            """
            Element rain ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 902
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__rain(self._handle)
        
        @rain.setter
        def rain(self, rain):
            _supy_driver.f90wrap_suews_forcing__set__rain(self._handle, rain)
        
        @property
        def wu_m3(self):
            """
            Element wu_m3 ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 903
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__wu_m3(self._handle)
        
        @wu_m3.setter
        def wu_m3(self, wu_m3):
            _supy_driver.f90wrap_suews_forcing__set__wu_m3(self._handle, wu_m3)
        
        @property
        def fcld(self):
            """
            Element fcld ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 904
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__fcld(self._handle)
        
        @fcld.setter
        def fcld(self, fcld):
            _supy_driver.f90wrap_suews_forcing__set__fcld(self._handle, fcld)
        
        @property
        def lai_obs(self):
            """
            Element lai_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 905
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__lai_obs(self._handle)
        
        @lai_obs.setter
        def lai_obs(self, lai_obs):
            _supy_driver.f90wrap_suews_forcing__set__lai_obs(self._handle, lai_obs)
        
        @property
        def snowfrac(self):
            """
            Element snowfrac ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 906
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__snowfrac(self._handle)
        
        @snowfrac.setter
        def snowfrac(self, snowfrac):
            _supy_driver.f90wrap_suews_forcing__set__snowfrac(self._handle, snowfrac)
        
        @property
        def xsmd(self):
            """
            Element xsmd ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 907
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__xsmd(self._handle)
        
        @xsmd.setter
        def xsmd(self, xsmd):
            _supy_driver.f90wrap_suews_forcing__set__xsmd(self._handle, xsmd)
        
        @property
        def qf_obs(self):
            """
            Element qf_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 908
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__qf_obs(self._handle)
        
        @qf_obs.setter
        def qf_obs(self, qf_obs):
            _supy_driver.f90wrap_suews_forcing__set__qf_obs(self._handle, qf_obs)
        
        @property
        def qn1_obs(self):
            """
            Element qn1_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 909
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__qn1_obs(self._handle)
        
        @qn1_obs.setter
        def qn1_obs(self, qn1_obs):
            _supy_driver.f90wrap_suews_forcing__set__qn1_obs(self._handle, qn1_obs)
        
        @property
        def qs_obs(self):
            """
            Element qs_obs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 910
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__qs_obs(self._handle)
        
        @qs_obs.setter
        def qs_obs(self, qs_obs):
            _supy_driver.f90wrap_suews_forcing__set__qs_obs(self._handle, qs_obs)
        
        @property
        def temp_c(self):
            """
            Element temp_c ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 911
            
            """
            return _supy_driver.f90wrap_suews_forcing__get__temp_c(self._handle)
        
        @temp_c.setter
        def temp_c(self, temp_c):
            _supy_driver.f90wrap_suews_forcing__set__temp_c(self._handle, temp_c)
        
        @property
        def ts5mindata_ir(self):
            """
            Element ts5mindata_ir ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 912
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_suews_forcing__array__ts5mindata_ir(self._handle)
            if array_handle in self._arrays:
                ts5mindata_ir = self._arrays[array_handle]
            else:
                ts5mindata_ir = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_suews_forcing__array__ts5mindata_ir)
                self._arrays[array_handle] = ts5mindata_ir
            return ts5mindata_ir
        
        @ts5mindata_ir.setter
        def ts5mindata_ir(self, ts5mindata_ir):
            self.ts5mindata_ir[...] = ts5mindata_ir
        
        def __str__(self):
            ret = ['<suews_forcing>{\n']
            ret.append('    kdown : ')
            ret.append(repr(self.kdown))
            ret.append(',\n    ldown : ')
            ret.append(repr(self.ldown))
            ret.append(',\n    rh : ')
            ret.append(repr(self.rh))
            ret.append(',\n    pres : ')
            ret.append(repr(self.pres))
            ret.append(',\n    tair_av_5d : ')
            ret.append(repr(self.tair_av_5d))
            ret.append(',\n    u : ')
            ret.append(repr(self.u))
            ret.append(',\n    rain : ')
            ret.append(repr(self.rain))
            ret.append(',\n    wu_m3 : ')
            ret.append(repr(self.wu_m3))
            ret.append(',\n    fcld : ')
            ret.append(repr(self.fcld))
            ret.append(',\n    lai_obs : ')
            ret.append(repr(self.lai_obs))
            ret.append(',\n    snowfrac : ')
            ret.append(repr(self.snowfrac))
            ret.append(',\n    xsmd : ')
            ret.append(repr(self.xsmd))
            ret.append(',\n    qf_obs : ')
            ret.append(repr(self.qf_obs))
            ret.append(',\n    qn1_obs : ')
            ret.append(repr(self.qn1_obs))
            ret.append(',\n    qs_obs : ')
            ret.append(repr(self.qs_obs))
            ret.append(',\n    temp_c : ')
            ret.append(repr(self.temp_c))
            ret.append(',\n    ts5mindata_ir : ')
            ret.append(repr(self.ts5mindata_ir))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_TIMER")
    class SUEWS_TIMER(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_timer)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 914-933
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Timer()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 914-933
            
            
            Returns
            -------
            this : Suews_Timer
            	Object to be constructed
            
            
            Automatically generated constructor for suews_timer
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_timer_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Timer
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 914-933
            
            Parameters
            ----------
            this : Suews_Timer
            	Object to be destructed
            
            
            Automatically generated destructor for suews_timer
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_timer_finalise(this=self._handle)
        
        @property
        def id(self):
            """
            Element id ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 917
            
            """
            return _supy_driver.f90wrap_suews_timer__get__id(self._handle)
        
        @id.setter
        def id(self, id):
            _supy_driver.f90wrap_suews_timer__set__id(self._handle, id)
        
        @property
        def imin(self):
            """
            Element imin ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 918
            
            """
            return _supy_driver.f90wrap_suews_timer__get__imin(self._handle)
        
        @imin.setter
        def imin(self, imin):
            _supy_driver.f90wrap_suews_timer__set__imin(self._handle, imin)
        
        @property
        def isec(self):
            """
            Element isec ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 919
            
            """
            return _supy_driver.f90wrap_suews_timer__get__isec(self._handle)
        
        @isec.setter
        def isec(self, isec):
            _supy_driver.f90wrap_suews_timer__set__isec(self._handle, isec)
        
        @property
        def it(self):
            """
            Element it ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 920
            
            """
            return _supy_driver.f90wrap_suews_timer__get__it(self._handle)
        
        @it.setter
        def it(self, it):
            _supy_driver.f90wrap_suews_timer__set__it(self._handle, it)
        
        @property
        def iy(self):
            """
            Element iy ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 921
            
            """
            return _supy_driver.f90wrap_suews_timer__get__iy(self._handle)
        
        @iy.setter
        def iy(self, iy):
            _supy_driver.f90wrap_suews_timer__set__iy(self._handle, iy)
        
        @property
        def tstep(self):
            """
            Element tstep ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 922
            
            """
            return _supy_driver.f90wrap_suews_timer__get__tstep(self._handle)
        
        @tstep.setter
        def tstep(self, tstep):
            _supy_driver.f90wrap_suews_timer__set__tstep(self._handle, tstep)
        
        @property
        def tstep_prev(self):
            """
            Element tstep_prev ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 923
            
            """
            return _supy_driver.f90wrap_suews_timer__get__tstep_prev(self._handle)
        
        @tstep_prev.setter
        def tstep_prev(self, tstep_prev):
            _supy_driver.f90wrap_suews_timer__set__tstep_prev(self._handle, tstep_prev)
        
        @property
        def dt_since_start(self):
            """
            Element dt_since_start ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 924
            
            """
            return _supy_driver.f90wrap_suews_timer__get__dt_since_start(self._handle)
        
        @dt_since_start.setter
        def dt_since_start(self, dt_since_start):
            _supy_driver.f90wrap_suews_timer__set__dt_since_start(self._handle, \
                dt_since_start)
        
        @property
        def dt_since_start_prev(self):
            """
            Element dt_since_start_prev ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 925
            
            """
            return _supy_driver.f90wrap_suews_timer__get__dt_since_start_prev(self._handle)
        
        @dt_since_start_prev.setter
        def dt_since_start_prev(self, dt_since_start_prev):
            _supy_driver.f90wrap_suews_timer__set__dt_since_start_prev(self._handle, \
                dt_since_start_prev)
        
        @property
        def nsh(self):
            """
            Element nsh ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 927
            
            """
            return _supy_driver.f90wrap_suews_timer__get__nsh(self._handle)
        
        @nsh.setter
        def nsh(self, nsh):
            _supy_driver.f90wrap_suews_timer__set__nsh(self._handle, nsh)
        
        @property
        def nsh_real(self):
            """
            Element nsh_real ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 928
            
            """
            return _supy_driver.f90wrap_suews_timer__get__nsh_real(self._handle)
        
        @nsh_real.setter
        def nsh_real(self, nsh_real):
            _supy_driver.f90wrap_suews_timer__set__nsh_real(self._handle, nsh_real)
        
        @property
        def tstep_real(self):
            """
            Element tstep_real ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 929
            
            """
            return _supy_driver.f90wrap_suews_timer__get__tstep_real(self._handle)
        
        @tstep_real.setter
        def tstep_real(self, tstep_real):
            _supy_driver.f90wrap_suews_timer__set__tstep_real(self._handle, tstep_real)
        
        @property
        def dectime(self):
            """
            Element dectime ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 930
            
            """
            return _supy_driver.f90wrap_suews_timer__get__dectime(self._handle)
        
        @dectime.setter
        def dectime(self, dectime):
            _supy_driver.f90wrap_suews_timer__set__dectime(self._handle, dectime)
        
        @property
        def dayofweek_id(self):
            """
            Element dayofweek_id ftype=integer pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 931
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_suews_timer__array__dayofweek_id(self._handle)
            if array_handle in self._arrays:
                dayofweek_id = self._arrays[array_handle]
            else:
                dayofweek_id = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_suews_timer__array__dayofweek_id)
                self._arrays[array_handle] = dayofweek_id
            return dayofweek_id
        
        @dayofweek_id.setter
        def dayofweek_id(self, dayofweek_id):
            self.dayofweek_id[...] = dayofweek_id
        
        @property
        def dls(self):
            """
            Element dls ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 932
            
            """
            return _supy_driver.f90wrap_suews_timer__get__dls(self._handle)
        
        @dls.setter
        def dls(self, dls):
            _supy_driver.f90wrap_suews_timer__set__dls(self._handle, dls)
        
        @property
        def new_day(self):
            """
            Element new_day ftype=integer  pytype=int
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 933
            
            """
            return _supy_driver.f90wrap_suews_timer__get__new_day(self._handle)
        
        @new_day.setter
        def new_day(self, new_day):
            _supy_driver.f90wrap_suews_timer__set__new_day(self._handle, new_day)
        
        def __str__(self):
            ret = ['<suews_timer>{\n']
            ret.append('    id : ')
            ret.append(repr(self.id))
            ret.append(',\n    imin : ')
            ret.append(repr(self.imin))
            ret.append(',\n    isec : ')
            ret.append(repr(self.isec))
            ret.append(',\n    it : ')
            ret.append(repr(self.it))
            ret.append(',\n    iy : ')
            ret.append(repr(self.iy))
            ret.append(',\n    tstep : ')
            ret.append(repr(self.tstep))
            ret.append(',\n    tstep_prev : ')
            ret.append(repr(self.tstep_prev))
            ret.append(',\n    dt_since_start : ')
            ret.append(repr(self.dt_since_start))
            ret.append(',\n    dt_since_start_prev : ')
            ret.append(repr(self.dt_since_start_prev))
            ret.append(',\n    nsh : ')
            ret.append(repr(self.nsh))
            ret.append(',\n    nsh_real : ')
            ret.append(repr(self.nsh_real))
            ret.append(',\n    tstep_real : ')
            ret.append(repr(self.tstep_real))
            ret.append(',\n    dectime : ')
            ret.append(repr(self.dectime))
            ret.append(',\n    dayofweek_id : ')
            ret.append(repr(self.dayofweek_id))
            ret.append(',\n    dls : ')
            ret.append(repr(self.dls))
            ret.append(',\n    new_day : ')
            ret.append(repr(self.new_day))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.output_block")
    class output_block(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=output_block)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 935-951
        
        """
        def __init__(self, handle=None):
            """
            self = Output_Block()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 935-951
            
            
            Returns
            -------
            this : Output_Block
            	Object to be constructed
            
            
            Automatically generated constructor for output_block
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__output_block_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Output_Block
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 935-951
            
            Parameters
            ----------
            this : Output_Block
            	Object to be destructed
            
            
            Automatically generated destructor for output_block
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__output_block_finalise(this=self._handle)
        
        def init(self, len_bn):
            """
            init__binding__output_block(self, len_bn)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1062-1088
            
            Parameters
            ----------
            self : Output_Block
            len_bn : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__init__binding__output_block(self=self._handle, \
                len_bn=len_bn)
        
        def cleanup(self):
            """
            cleanup__binding__output_block(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1090-1103
            
            Parameters
            ----------
            self : Output_Block
            
            """
            _supy_driver.f90wrap_suews_def_dts__cleanup__binding__output_block(self=self._handle)
        
        @property
        def dataoutblocksuews(self):
            """
            Element dataoutblocksuews ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 936
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblocksuews(self._handle)
            if array_handle in self._arrays:
                dataoutblocksuews = self._arrays[array_handle]
            else:
                dataoutblocksuews = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblocksuews)
                self._arrays[array_handle] = dataoutblocksuews
            return dataoutblocksuews
        
        @dataoutblocksuews.setter
        def dataoutblocksuews(self, dataoutblocksuews):
            self.dataoutblocksuews[...] = dataoutblocksuews
        
        @property
        def dataoutblocksnow(self):
            """
            Element dataoutblocksnow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 937
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblocksnow(self._handle)
            if array_handle in self._arrays:
                dataoutblocksnow = self._arrays[array_handle]
            else:
                dataoutblocksnow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblocksnow)
                self._arrays[array_handle] = dataoutblocksnow
            return dataoutblocksnow
        
        @dataoutblocksnow.setter
        def dataoutblocksnow(self, dataoutblocksnow):
            self.dataoutblocksnow[...] = dataoutblocksnow
        
        @property
        def dataoutblockestm(self):
            """
            Element dataoutblockestm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 938
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockestm(self._handle)
            if array_handle in self._arrays:
                dataoutblockestm = self._arrays[array_handle]
            else:
                dataoutblockestm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockestm)
                self._arrays[array_handle] = dataoutblockestm
            return dataoutblockestm
        
        @dataoutblockestm.setter
        def dataoutblockestm(self, dataoutblockestm):
            self.dataoutblockestm[...] = dataoutblockestm
        
        @property
        def dataoutblockehc(self):
            """
            Element dataoutblockehc ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 939
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockehc(self._handle)
            if array_handle in self._arrays:
                dataoutblockehc = self._arrays[array_handle]
            else:
                dataoutblockehc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockehc)
                self._arrays[array_handle] = dataoutblockehc
            return dataoutblockehc
        
        @dataoutblockehc.setter
        def dataoutblockehc(self, dataoutblockehc):
            self.dataoutblockehc[...] = dataoutblockehc
        
        @property
        def dataoutblockrsl(self):
            """
            Element dataoutblockrsl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 940
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockrsl(self._handle)
            if array_handle in self._arrays:
                dataoutblockrsl = self._arrays[array_handle]
            else:
                dataoutblockrsl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockrsl)
                self._arrays[array_handle] = dataoutblockrsl
            return dataoutblockrsl
        
        @dataoutblockrsl.setter
        def dataoutblockrsl(self, dataoutblockrsl):
            self.dataoutblockrsl[...] = dataoutblockrsl
        
        @property
        def dataoutblockbeers(self):
            """
            Element dataoutblockbeers ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 941
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockbeers(self._handle)
            if array_handle in self._arrays:
                dataoutblockbeers = self._arrays[array_handle]
            else:
                dataoutblockbeers = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockbeers)
                self._arrays[array_handle] = dataoutblockbeers
            return dataoutblockbeers
        
        @dataoutblockbeers.setter
        def dataoutblockbeers(self, dataoutblockbeers):
            self.dataoutblockbeers[...] = dataoutblockbeers
        
        @property
        def dataoutblockdebug(self):
            """
            Element dataoutblockdebug ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 942
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockdebug(self._handle)
            if array_handle in self._arrays:
                dataoutblockdebug = self._arrays[array_handle]
            else:
                dataoutblockdebug = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockdebug)
                self._arrays[array_handle] = dataoutblockdebug
            return dataoutblockdebug
        
        @dataoutblockdebug.setter
        def dataoutblockdebug(self, dataoutblockdebug):
            self.dataoutblockdebug[...] = dataoutblockdebug
        
        @property
        def dataoutblockspartacus(self):
            """
            Element dataoutblockspartacus ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 943
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockspartacus(self._handle)
            if array_handle in self._arrays:
                dataoutblockspartacus = self._arrays[array_handle]
            else:
                dataoutblockspartacus = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockspartacus)
                self._arrays[array_handle] = dataoutblockspartacus
            return dataoutblockspartacus
        
        @dataoutblockspartacus.setter
        def dataoutblockspartacus(self, dataoutblockspartacus):
            self.dataoutblockspartacus[...] = dataoutblockspartacus
        
        @property
        def dataoutblockdailystate(self):
            """
            Element dataoutblockdailystate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 944
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockdailystate(self._handle)
            if array_handle in self._arrays:
                dataoutblockdailystate = self._arrays[array_handle]
            else:
                dataoutblockdailystate = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockdailystate)
                self._arrays[array_handle] = dataoutblockdailystate
            return dataoutblockdailystate
        
        @dataoutblockdailystate.setter
        def dataoutblockdailystate(self, dataoutblockdailystate):
            self.dataoutblockdailystate[...] = dataoutblockdailystate
        
        @property
        def dataoutblockstebbs(self):
            """
            Element dataoutblockstebbs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 945
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblockstebbs(self._handle)
            if array_handle in self._arrays:
                dataoutblockstebbs = self._arrays[array_handle]
            else:
                dataoutblockstebbs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblockstebbs)
                self._arrays[array_handle] = dataoutblockstebbs
            return dataoutblockstebbs
        
        @dataoutblockstebbs.setter
        def dataoutblockstebbs(self, dataoutblockstebbs):
            self.dataoutblockstebbs[...] = dataoutblockstebbs
        
        @property
        def dataoutblocknhood(self):
            """
            Element dataoutblocknhood ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 946
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_block__array__dataoutblocknhood(self._handle)
            if array_handle in self._arrays:
                dataoutblocknhood = self._arrays[array_handle]
            else:
                dataoutblocknhood = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_block__array__dataoutblocknhood)
                self._arrays[array_handle] = dataoutblocknhood
            return dataoutblocknhood
        
        @dataoutblocknhood.setter
        def dataoutblocknhood(self, dataoutblocknhood):
            self.dataoutblocknhood[...] = dataoutblocknhood
        
        def __str__(self):
            ret = ['<output_block>{\n']
            ret.append('    dataoutblocksuews : ')
            ret.append(repr(self.dataoutblocksuews))
            ret.append(',\n    dataoutblocksnow : ')
            ret.append(repr(self.dataoutblocksnow))
            ret.append(',\n    dataoutblockestm : ')
            ret.append(repr(self.dataoutblockestm))
            ret.append(',\n    dataoutblockehc : ')
            ret.append(repr(self.dataoutblockehc))
            ret.append(',\n    dataoutblockrsl : ')
            ret.append(repr(self.dataoutblockrsl))
            ret.append(',\n    dataoutblockbeers : ')
            ret.append(repr(self.dataoutblockbeers))
            ret.append(',\n    dataoutblockdebug : ')
            ret.append(repr(self.dataoutblockdebug))
            ret.append(',\n    dataoutblockspartacus : ')
            ret.append(repr(self.dataoutblockspartacus))
            ret.append(',\n    dataoutblockdailystate : ')
            ret.append(repr(self.dataoutblockdailystate))
            ret.append(',\n    dataoutblockstebbs : ')
            ret.append(repr(self.dataoutblockstebbs))
            ret.append(',\n    dataoutblocknhood : ')
            ret.append(repr(self.dataoutblocknhood))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.output_line")
    class output_line(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=output_line)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 953-971
        
        """
        def __init__(self, handle=None):
            """
            self = Output_Line()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 953-971
            
            
            Returns
            -------
            this : Output_Line
            	Object to be constructed
            
            
            Automatically generated constructor for output_line
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__output_line_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Output_Line
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 953-971
            
            Parameters
            ----------
            this : Output_Line
            	Object to be destructed
            
            
            Automatically generated destructor for output_line
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__output_line_finalise(this=self._handle)
        
        def init(self):
            """
            init__binding__output_line(self)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1042-1060
            
            Parameters
            ----------
            self : Output_Line
            
            """
            _supy_driver.f90wrap_suews_def_dts__init__binding__output_line(self=self._handle)
        
        @property
        def datetimeline(self):
            """
            Element datetimeline ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 954
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__datetimeline(self._handle)
            if array_handle in self._arrays:
                datetimeline = self._arrays[array_handle]
            else:
                datetimeline = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__datetimeline)
                self._arrays[array_handle] = datetimeline
            return datetimeline
        
        @datetimeline.setter
        def datetimeline(self, datetimeline):
            self.datetimeline[...] = datetimeline
        
        @property
        def dataoutlinesuews(self):
            """
            Element dataoutlinesuews ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 955
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinesuews(self._handle)
            if array_handle in self._arrays:
                dataoutlinesuews = self._arrays[array_handle]
            else:
                dataoutlinesuews = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinesuews)
                self._arrays[array_handle] = dataoutlinesuews
            return dataoutlinesuews
        
        @dataoutlinesuews.setter
        def dataoutlinesuews(self, dataoutlinesuews):
            self.dataoutlinesuews[...] = dataoutlinesuews
        
        @property
        def dataoutlinesnow(self):
            """
            Element dataoutlinesnow ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 956
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinesnow(self._handle)
            if array_handle in self._arrays:
                dataoutlinesnow = self._arrays[array_handle]
            else:
                dataoutlinesnow = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinesnow)
                self._arrays[array_handle] = dataoutlinesnow
            return dataoutlinesnow
        
        @dataoutlinesnow.setter
        def dataoutlinesnow(self, dataoutlinesnow):
            self.dataoutlinesnow[...] = dataoutlinesnow
        
        @property
        def dataoutlineestm(self):
            """
            Element dataoutlineestm ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 957
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlineestm(self._handle)
            if array_handle in self._arrays:
                dataoutlineestm = self._arrays[array_handle]
            else:
                dataoutlineestm = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlineestm)
                self._arrays[array_handle] = dataoutlineestm
            return dataoutlineestm
        
        @dataoutlineestm.setter
        def dataoutlineestm(self, dataoutlineestm):
            self.dataoutlineestm[...] = dataoutlineestm
        
        @property
        def dataoutlineehc(self):
            """
            Element dataoutlineehc ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 958
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlineehc(self._handle)
            if array_handle in self._arrays:
                dataoutlineehc = self._arrays[array_handle]
            else:
                dataoutlineehc = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlineehc)
                self._arrays[array_handle] = dataoutlineehc
            return dataoutlineehc
        
        @dataoutlineehc.setter
        def dataoutlineehc(self, dataoutlineehc):
            self.dataoutlineehc[...] = dataoutlineehc
        
        @property
        def dataoutlinersl(self):
            """
            Element dataoutlinersl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 959
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinersl(self._handle)
            if array_handle in self._arrays:
                dataoutlinersl = self._arrays[array_handle]
            else:
                dataoutlinersl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinersl)
                self._arrays[array_handle] = dataoutlinersl
            return dataoutlinersl
        
        @dataoutlinersl.setter
        def dataoutlinersl(self, dataoutlinersl):
            self.dataoutlinersl[...] = dataoutlinersl
        
        @property
        def dataoutlinebeers(self):
            """
            Element dataoutlinebeers ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 960
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinebeers(self._handle)
            if array_handle in self._arrays:
                dataoutlinebeers = self._arrays[array_handle]
            else:
                dataoutlinebeers = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinebeers)
                self._arrays[array_handle] = dataoutlinebeers
            return dataoutlinebeers
        
        @dataoutlinebeers.setter
        def dataoutlinebeers(self, dataoutlinebeers):
            self.dataoutlinebeers[...] = dataoutlinebeers
        
        @property
        def dataoutlinedebug(self):
            """
            Element dataoutlinedebug ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 961
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinedebug(self._handle)
            if array_handle in self._arrays:
                dataoutlinedebug = self._arrays[array_handle]
            else:
                dataoutlinedebug = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinedebug)
                self._arrays[array_handle] = dataoutlinedebug
            return dataoutlinedebug
        
        @dataoutlinedebug.setter
        def dataoutlinedebug(self, dataoutlinedebug):
            self.dataoutlinedebug[...] = dataoutlinedebug
        
        @property
        def dataoutlinespartacus(self):
            """
            Element dataoutlinespartacus ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 962
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinespartacus(self._handle)
            if array_handle in self._arrays:
                dataoutlinespartacus = self._arrays[array_handle]
            else:
                dataoutlinespartacus = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinespartacus)
                self._arrays[array_handle] = dataoutlinespartacus
            return dataoutlinespartacus
        
        @dataoutlinespartacus.setter
        def dataoutlinespartacus(self, dataoutlinespartacus):
            self.dataoutlinespartacus[...] = dataoutlinespartacus
        
        @property
        def dataoutlinedailystate(self):
            """
            Element dataoutlinedailystate ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 963
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinedailystate(self._handle)
            if array_handle in self._arrays:
                dataoutlinedailystate = self._arrays[array_handle]
            else:
                dataoutlinedailystate = \
                    f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinedailystate)
                self._arrays[array_handle] = dataoutlinedailystate
            return dataoutlinedailystate
        
        @dataoutlinedailystate.setter
        def dataoutlinedailystate(self, dataoutlinedailystate):
            self.dataoutlinedailystate[...] = dataoutlinedailystate
        
        @property
        def dataoutlinestebbs(self):
            """
            Element dataoutlinestebbs ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 964
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinestebbs(self._handle)
            if array_handle in self._arrays:
                dataoutlinestebbs = self._arrays[array_handle]
            else:
                dataoutlinestebbs = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinestebbs)
                self._arrays[array_handle] = dataoutlinestebbs
            return dataoutlinestebbs
        
        @dataoutlinestebbs.setter
        def dataoutlinestebbs(self, dataoutlinestebbs):
            self.dataoutlinestebbs[...] = dataoutlinestebbs
        
        @property
        def dataoutlinenhood(self):
            """
            Element dataoutlinenhood ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 965
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinenhood(self._handle)
            if array_handle in self._arrays:
                dataoutlinenhood = self._arrays[array_handle]
            else:
                dataoutlinenhood = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinenhood)
                self._arrays[array_handle] = dataoutlinenhood
            return dataoutlinenhood
        
        @dataoutlinenhood.setter
        def dataoutlinenhood(self, dataoutlinenhood):
            self.dataoutlinenhood[...] = dataoutlinenhood
        
        @property
        def dataoutlineursl(self):
            """
            Element dataoutlineursl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 966
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlineursl(self._handle)
            if array_handle in self._arrays:
                dataoutlineursl = self._arrays[array_handle]
            else:
                dataoutlineursl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlineursl)
                self._arrays[array_handle] = dataoutlineursl
            return dataoutlineursl
        
        @dataoutlineursl.setter
        def dataoutlineursl(self, dataoutlineursl):
            self.dataoutlineursl[...] = dataoutlineursl
        
        @property
        def dataoutlinetrsl(self):
            """
            Element dataoutlinetrsl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 967
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlinetrsl(self._handle)
            if array_handle in self._arrays:
                dataoutlinetrsl = self._arrays[array_handle]
            else:
                dataoutlinetrsl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlinetrsl)
                self._arrays[array_handle] = dataoutlinetrsl
            return dataoutlinetrsl
        
        @dataoutlinetrsl.setter
        def dataoutlinetrsl(self, dataoutlinetrsl):
            self.dataoutlinetrsl[...] = dataoutlinetrsl
        
        @property
        def dataoutlineqrsl(self):
            """
            Element dataoutlineqrsl ftype=real(kind(1d0) pytype=float
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 968
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _supy_driver.f90wrap_output_line__array__dataoutlineqrsl(self._handle)
            if array_handle in self._arrays:
                dataoutlineqrsl = self._arrays[array_handle]
            else:
                dataoutlineqrsl = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _supy_driver.f90wrap_output_line__array__dataoutlineqrsl)
                self._arrays[array_handle] = dataoutlineqrsl
            return dataoutlineqrsl
        
        @dataoutlineqrsl.setter
        def dataoutlineqrsl(self, dataoutlineqrsl):
            self.dataoutlineqrsl[...] = dataoutlineqrsl
        
        def __str__(self):
            ret = ['<output_line>{\n']
            ret.append('    datetimeline : ')
            ret.append(repr(self.datetimeline))
            ret.append(',\n    dataoutlinesuews : ')
            ret.append(repr(self.dataoutlinesuews))
            ret.append(',\n    dataoutlinesnow : ')
            ret.append(repr(self.dataoutlinesnow))
            ret.append(',\n    dataoutlineestm : ')
            ret.append(repr(self.dataoutlineestm))
            ret.append(',\n    dataoutlineehc : ')
            ret.append(repr(self.dataoutlineehc))
            ret.append(',\n    dataoutlinersl : ')
            ret.append(repr(self.dataoutlinersl))
            ret.append(',\n    dataoutlinebeers : ')
            ret.append(repr(self.dataoutlinebeers))
            ret.append(',\n    dataoutlinedebug : ')
            ret.append(repr(self.dataoutlinedebug))
            ret.append(',\n    dataoutlinespartacus : ')
            ret.append(repr(self.dataoutlinespartacus))
            ret.append(',\n    dataoutlinedailystate : ')
            ret.append(repr(self.dataoutlinedailystate))
            ret.append(',\n    dataoutlinestebbs : ')
            ret.append(repr(self.dataoutlinestebbs))
            ret.append(',\n    dataoutlinenhood : ')
            ret.append(repr(self.dataoutlinenhood))
            ret.append(',\n    dataoutlineursl : ')
            ret.append(repr(self.dataoutlineursl))
            ret.append(',\n    dataoutlinetrsl : ')
            ret.append(repr(self.dataoutlinetrsl))
            ret.append(',\n    dataoutlineqrsl : ')
            ret.append(repr(self.dataoutlineqrsl))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_DEBUG")
    class SUEWS_DEBUG(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_debug)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 973-996
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_Debug()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 973-996
            
            
            Returns
            -------
            this : Suews_Debug
            	Object to be constructed
            
            
            Automatically generated constructor for suews_debug
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_debug_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_Debug
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 973-996
            
            Parameters
            ----------
            this : Suews_Debug
            	Object to be destructed
            
            
            Automatically generated destructor for suews_debug
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_debug_finalise(this=self._handle)
        
        def init(self, nlayer, ndepth):
            """
            init__binding__suews_debug(self, nlayer, ndepth)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1023-1040
            
            Parameters
            ----------
            self : Suews_Debug
            nlayer : int
            ndepth : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__init__binding__suews_debug(self=self._handle, \
                nlayer=nlayer, ndepth=ndepth)
        
        @property
        def state_01_dailystate(self):
            """
            Element state_01_dailystate ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 979
            
            """
            state_01_dailystate_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_01_dailystate(self._handle)
            if tuple(state_01_dailystate_handle) in self._objs:
                state_01_dailystate = self._objs[tuple(state_01_dailystate_handle)]
            else:
                state_01_dailystate = \
                    suews_def_dts.SUEWS_STATE.from_handle(state_01_dailystate_handle)
                self._objs[tuple(state_01_dailystate_handle)] = state_01_dailystate
            return state_01_dailystate
        
        @state_01_dailystate.setter
        def state_01_dailystate(self, state_01_dailystate):
            state_01_dailystate = state_01_dailystate._handle
            _supy_driver.f90wrap_suews_debug__set__state_01_dailystate(self._handle, \
                state_01_dailystate)
        
        @property
        def state_02_soilmoist(self):
            """
            Element state_02_soilmoist ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 980
            
            """
            state_02_soilmoist_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_02_soilmoist(self._handle)
            if tuple(state_02_soilmoist_handle) in self._objs:
                state_02_soilmoist = self._objs[tuple(state_02_soilmoist_handle)]
            else:
                state_02_soilmoist = \
                    suews_def_dts.SUEWS_STATE.from_handle(state_02_soilmoist_handle)
                self._objs[tuple(state_02_soilmoist_handle)] = state_02_soilmoist
            return state_02_soilmoist
        
        @state_02_soilmoist.setter
        def state_02_soilmoist(self, state_02_soilmoist):
            state_02_soilmoist = state_02_soilmoist._handle
            _supy_driver.f90wrap_suews_debug__set__state_02_soilmoist(self._handle, \
                state_02_soilmoist)
        
        @property
        def state_03_wateruse(self):
            """
            Element state_03_wateruse ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 981
            
            """
            state_03_wateruse_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_03_wateruse(self._handle)
            if tuple(state_03_wateruse_handle) in self._objs:
                state_03_wateruse = self._objs[tuple(state_03_wateruse_handle)]
            else:
                state_03_wateruse = \
                    suews_def_dts.SUEWS_STATE.from_handle(state_03_wateruse_handle)
                self._objs[tuple(state_03_wateruse_handle)] = state_03_wateruse
            return state_03_wateruse
        
        @state_03_wateruse.setter
        def state_03_wateruse(self, state_03_wateruse):
            state_03_wateruse = state_03_wateruse._handle
            _supy_driver.f90wrap_suews_debug__set__state_03_wateruse(self._handle, \
                state_03_wateruse)
        
        @property
        def state_04_anthroemis(self):
            """
            Element state_04_anthroemis ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 982
            
            """
            state_04_anthroemis_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_04_anthroemis(self._handle)
            if tuple(state_04_anthroemis_handle) in self._objs:
                state_04_anthroemis = self._objs[tuple(state_04_anthroemis_handle)]
            else:
                state_04_anthroemis = \
                    suews_def_dts.SUEWS_STATE.from_handle(state_04_anthroemis_handle)
                self._objs[tuple(state_04_anthroemis_handle)] = state_04_anthroemis
            return state_04_anthroemis
        
        @state_04_anthroemis.setter
        def state_04_anthroemis(self, state_04_anthroemis):
            state_04_anthroemis = state_04_anthroemis._handle
            _supy_driver.f90wrap_suews_debug__set__state_04_anthroemis(self._handle, \
                state_04_anthroemis)
        
        @property
        def state_05_qn(self):
            """
            Element state_05_qn ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 983
            
            """
            state_05_qn_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_05_qn(self._handle)
            if tuple(state_05_qn_handle) in self._objs:
                state_05_qn = self._objs[tuple(state_05_qn_handle)]
            else:
                state_05_qn = suews_def_dts.SUEWS_STATE.from_handle(state_05_qn_handle)
                self._objs[tuple(state_05_qn_handle)] = state_05_qn
            return state_05_qn
        
        @state_05_qn.setter
        def state_05_qn(self, state_05_qn):
            state_05_qn = state_05_qn._handle
            _supy_driver.f90wrap_suews_debug__set__state_05_qn(self._handle, state_05_qn)
        
        @property
        def state_06_qs(self):
            """
            Element state_06_qs ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 984
            
            """
            state_06_qs_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_06_qs(self._handle)
            if tuple(state_06_qs_handle) in self._objs:
                state_06_qs = self._objs[tuple(state_06_qs_handle)]
            else:
                state_06_qs = suews_def_dts.SUEWS_STATE.from_handle(state_06_qs_handle)
                self._objs[tuple(state_06_qs_handle)] = state_06_qs
            return state_06_qs
        
        @state_06_qs.setter
        def state_06_qs(self, state_06_qs):
            state_06_qs = state_06_qs._handle
            _supy_driver.f90wrap_suews_debug__set__state_06_qs(self._handle, state_06_qs)
        
        @property
        def state_07_qhqe_lumps(self):
            """
            Element state_07_qhqe_lumps ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 985
            
            """
            state_07_qhqe_lumps_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_07_qhqe_lumps(self._handle)
            if tuple(state_07_qhqe_lumps_handle) in self._objs:
                state_07_qhqe_lumps = self._objs[tuple(state_07_qhqe_lumps_handle)]
            else:
                state_07_qhqe_lumps = \
                    suews_def_dts.SUEWS_STATE.from_handle(state_07_qhqe_lumps_handle)
                self._objs[tuple(state_07_qhqe_lumps_handle)] = state_07_qhqe_lumps
            return state_07_qhqe_lumps
        
        @state_07_qhqe_lumps.setter
        def state_07_qhqe_lumps(self, state_07_qhqe_lumps):
            state_07_qhqe_lumps = state_07_qhqe_lumps._handle
            _supy_driver.f90wrap_suews_debug__set__state_07_qhqe_lumps(self._handle, \
                state_07_qhqe_lumps)
        
        @property
        def state_08_water(self):
            """
            Element state_08_water ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 986
            
            """
            state_08_water_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_08_water(self._handle)
            if tuple(state_08_water_handle) in self._objs:
                state_08_water = self._objs[tuple(state_08_water_handle)]
            else:
                state_08_water = suews_def_dts.SUEWS_STATE.from_handle(state_08_water_handle)
                self._objs[tuple(state_08_water_handle)] = state_08_water
            return state_08_water
        
        @state_08_water.setter
        def state_08_water(self, state_08_water):
            state_08_water = state_08_water._handle
            _supy_driver.f90wrap_suews_debug__set__state_08_water(self._handle, \
                state_08_water)
        
        @property
        def state_09_resist(self):
            """
            Element state_09_resist ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 987
            
            """
            state_09_resist_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_09_resist(self._handle)
            if tuple(state_09_resist_handle) in self._objs:
                state_09_resist = self._objs[tuple(state_09_resist_handle)]
            else:
                state_09_resist = suews_def_dts.SUEWS_STATE.from_handle(state_09_resist_handle)
                self._objs[tuple(state_09_resist_handle)] = state_09_resist
            return state_09_resist
        
        @state_09_resist.setter
        def state_09_resist(self, state_09_resist):
            state_09_resist = state_09_resist._handle
            _supy_driver.f90wrap_suews_debug__set__state_09_resist(self._handle, \
                state_09_resist)
        
        @property
        def state_10_qe(self):
            """
            Element state_10_qe ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 988
            
            """
            state_10_qe_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_10_qe(self._handle)
            if tuple(state_10_qe_handle) in self._objs:
                state_10_qe = self._objs[tuple(state_10_qe_handle)]
            else:
                state_10_qe = suews_def_dts.SUEWS_STATE.from_handle(state_10_qe_handle)
                self._objs[tuple(state_10_qe_handle)] = state_10_qe
            return state_10_qe
        
        @state_10_qe.setter
        def state_10_qe(self, state_10_qe):
            state_10_qe = state_10_qe._handle
            _supy_driver.f90wrap_suews_debug__set__state_10_qe(self._handle, state_10_qe)
        
        @property
        def state_11_qh(self):
            """
            Element state_11_qh ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 989
            
            """
            state_11_qh_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_11_qh(self._handle)
            if tuple(state_11_qh_handle) in self._objs:
                state_11_qh = self._objs[tuple(state_11_qh_handle)]
            else:
                state_11_qh = suews_def_dts.SUEWS_STATE.from_handle(state_11_qh_handle)
                self._objs[tuple(state_11_qh_handle)] = state_11_qh
            return state_11_qh
        
        @state_11_qh.setter
        def state_11_qh(self, state_11_qh):
            state_11_qh = state_11_qh._handle
            _supy_driver.f90wrap_suews_debug__set__state_11_qh(self._handle, state_11_qh)
        
        @property
        def state_12_tsurf(self):
            """
            Element state_12_tsurf ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 990
            
            """
            state_12_tsurf_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_12_tsurf(self._handle)
            if tuple(state_12_tsurf_handle) in self._objs:
                state_12_tsurf = self._objs[tuple(state_12_tsurf_handle)]
            else:
                state_12_tsurf = suews_def_dts.SUEWS_STATE.from_handle(state_12_tsurf_handle)
                self._objs[tuple(state_12_tsurf_handle)] = state_12_tsurf
            return state_12_tsurf
        
        @state_12_tsurf.setter
        def state_12_tsurf(self, state_12_tsurf):
            state_12_tsurf = state_12_tsurf._handle
            _supy_driver.f90wrap_suews_debug__set__state_12_tsurf(self._handle, \
                state_12_tsurf)
        
        @property
        def state_13_rsl(self):
            """
            Element state_13_rsl ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 991
            
            """
            state_13_rsl_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_13_rsl(self._handle)
            if tuple(state_13_rsl_handle) in self._objs:
                state_13_rsl = self._objs[tuple(state_13_rsl_handle)]
            else:
                state_13_rsl = suews_def_dts.SUEWS_STATE.from_handle(state_13_rsl_handle)
                self._objs[tuple(state_13_rsl_handle)] = state_13_rsl
            return state_13_rsl
        
        @state_13_rsl.setter
        def state_13_rsl(self, state_13_rsl):
            state_13_rsl = state_13_rsl._handle
            _supy_driver.f90wrap_suews_debug__set__state_13_rsl(self._handle, state_13_rsl)
        
        @property
        def state_14_biogenco2(self):
            """
            Element state_14_biogenco2 ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 992
            
            """
            state_14_biogenco2_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_14_biogenco2(self._handle)
            if tuple(state_14_biogenco2_handle) in self._objs:
                state_14_biogenco2 = self._objs[tuple(state_14_biogenco2_handle)]
            else:
                state_14_biogenco2 = \
                    suews_def_dts.SUEWS_STATE.from_handle(state_14_biogenco2_handle)
                self._objs[tuple(state_14_biogenco2_handle)] = state_14_biogenco2
            return state_14_biogenco2
        
        @state_14_biogenco2.setter
        def state_14_biogenco2(self, state_14_biogenco2):
            state_14_biogenco2 = state_14_biogenco2._handle
            _supy_driver.f90wrap_suews_debug__set__state_14_biogenco2(self._handle, \
                state_14_biogenco2)
        
        @property
        def state_15_beers(self):
            """
            Element state_15_beers ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 993
            
            """
            state_15_beers_handle = \
                _supy_driver.f90wrap_suews_debug__get__state_15_beers(self._handle)
            if tuple(state_15_beers_handle) in self._objs:
                state_15_beers = self._objs[tuple(state_15_beers_handle)]
            else:
                state_15_beers = suews_def_dts.SUEWS_STATE.from_handle(state_15_beers_handle)
                self._objs[tuple(state_15_beers_handle)] = state_15_beers
            return state_15_beers
        
        @state_15_beers.setter
        def state_15_beers(self, state_15_beers):
            state_15_beers = state_15_beers._handle
            _supy_driver.f90wrap_suews_debug__set__state_15_beers(self._handle, \
                state_15_beers)
        
        def __str__(self):
            ret = ['<suews_debug>{\n']
            ret.append('    state_01_dailystate : ')
            ret.append(repr(self.state_01_dailystate))
            ret.append(',\n    state_02_soilmoist : ')
            ret.append(repr(self.state_02_soilmoist))
            ret.append(',\n    state_03_wateruse : ')
            ret.append(repr(self.state_03_wateruse))
            ret.append(',\n    state_04_anthroemis : ')
            ret.append(repr(self.state_04_anthroemis))
            ret.append(',\n    state_05_qn : ')
            ret.append(repr(self.state_05_qn))
            ret.append(',\n    state_06_qs : ')
            ret.append(repr(self.state_06_qs))
            ret.append(',\n    state_07_qhqe_lumps : ')
            ret.append(repr(self.state_07_qhqe_lumps))
            ret.append(',\n    state_08_water : ')
            ret.append(repr(self.state_08_water))
            ret.append(',\n    state_09_resist : ')
            ret.append(repr(self.state_09_resist))
            ret.append(',\n    state_10_qe : ')
            ret.append(repr(self.state_10_qe))
            ret.append(',\n    state_11_qh : ')
            ret.append(repr(self.state_11_qh))
            ret.append(',\n    state_12_tsurf : ')
            ret.append(repr(self.state_12_tsurf))
            ret.append(',\n    state_13_rsl : ')
            ret.append(repr(self.state_13_rsl))
            ret.append(',\n    state_14_biogenco2 : ')
            ret.append(repr(self.state_14_biogenco2))
            ret.append(',\n    state_15_beers : ')
            ret.append(repr(self.state_15_beers))
            ret.append('}')
            return ''.join(ret)
        
        _dt_array_initialisers = []
        
    
    @f90wrap.runtime.register_class("supy_driver.SUEWS_STATE_BLOCK")
    class SUEWS_STATE_BLOCK(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=suews_state_block)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 998-1001
        
        """
        def __init__(self, handle=None):
            """
            self = Suews_State_Block()
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 998-1001
            
            
            Returns
            -------
            this : Suews_State_Block
            	Object to be constructed
            
            
            Automatically generated constructor for suews_state_block
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _supy_driver.f90wrap_suews_def_dts__suews_state_block_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Suews_State_Block
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 998-1001
            
            Parameters
            ----------
            this : Suews_State_Block
            	Object to be destructed
            
            
            Automatically generated destructor for suews_state_block
            """
            if self._alloc:
                _supy_driver.f90wrap_suews_def_dts__suews_state_block_finalise(this=self._handle)
        
        def init(self, nlayer, ndepth, len_sim):
            """
            init__binding__suews_state_block(self, nlayer, ndepth, len_sim)
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                lines 1004-1014
            
            Parameters
            ----------
            self : Suews_State_Block
            nlayer : int
            ndepth : int
            len_sim : int
            
            """
            _supy_driver.f90wrap_suews_def_dts__init__binding__suews_state_block(self=self._handle, \
                nlayer=nlayer, ndepth=ndepth, len_sim=len_sim)
        
        def init_array_block(self):
            self.block = f90wrap.runtime.FortranDerivedTypeArray(self,
                                            _supy_driver.f90wrap_suews_state_block__array_getitem__block,
                                            _supy_driver.f90wrap_suews_state_block__array_setitem__block,
                                            _supy_driver.f90wrap_suews_state_block__array_len__block,
                                            """
            Element block ftype=type(suews_state) pytype=Suews_State
            
            
            Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
                line 999
            
            """, Suews_Def_Dts.SUEWS_STATE)
            return self.block
        
        _dt_array_initialisers = [init_array_block]
        
    
    @staticmethod
    def init_suews_state_block(self, nlayer, ndepth, len_sim):
        """
        init_suews_state_block(self, nlayer, ndepth, len_sim)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1004-1014
        
        Parameters
        ----------
        self : Suews_State_Block
        nlayer : int
        ndepth : int
        len_sim : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__init_suews_state_block(self=self._handle, \
            nlayer=nlayer, ndepth=ndepth, len_sim=len_sim)
    
    @staticmethod
    def init_suews_debug(self, nlayer, ndepth):
        """
        init_suews_debug(self, nlayer, ndepth)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1023-1040
        
        Parameters
        ----------
        self : Suews_Debug
        nlayer : int
        ndepth : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__init_suews_debug(self=self._handle, \
            nlayer=nlayer, ndepth=ndepth)
    
    @staticmethod
    def output_line_init(self):
        """
        output_line_init(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1042-1060
        
        Parameters
        ----------
        self : Output_Line
        
        """
        _supy_driver.f90wrap_suews_def_dts__output_line_init(self=self._handle)
    
    @staticmethod
    def output_block_init(self, len_bn):
        """
        output_block_init(self, len_bn)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1062-1088
        
        Parameters
        ----------
        self : Output_Block
        len_bn : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__output_block_init(self=self._handle, \
            len_bn=len_bn)
    
    @staticmethod
    def output_block_finalize(self):
        """
        output_block_finalize(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1090-1103
        
        Parameters
        ----------
        self : Output_Block
        
        """
        _supy_driver.f90wrap_suews_def_dts__output_block_finalize(self=self._handle)
    
    @staticmethod
    def allocsuewsstate_c(self, nlayer, ndepth):
        """
        allocsuewsstate_c(self, nlayer, ndepth)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1105-1112
        
        Parameters
        ----------
        self : Suews_State
        nlayer : int
        ndepth : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__allocsuewsstate_c(self=self._handle, \
            nlayer=nlayer, ndepth=ndepth)
    
    @staticmethod
    def deallocsuewsstate_c(self):
        """
        deallocsuewsstate_c(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1114-1118
        
        Parameters
        ----------
        self : Suews_State
        
        """
        _supy_driver.f90wrap_suews_def_dts__deallocsuewsstate_c(self=self._handle)
    
    @staticmethod
    def reset_atm_state(self):
        """
        reset_atm_state(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1120-1133
        
        Parameters
        ----------
        self : Suews_State
        
        """
        _supy_driver.f90wrap_suews_def_dts__reset_atm_state(self=self._handle)
    
    @staticmethod
    def allocate_spartacus_layer_prm_c(self, nlayer):
        """
        allocate_spartacus_layer_prm_c(self, nlayer)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1135-1149
        
        Parameters
        ----------
        self : Spartacus_Layer_Prm
        nlayer : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__allocate_spartacus_layer_prm_c(self=self._handle, \
            nlayer=nlayer)
    
    @staticmethod
    def deallocate_spartacus_layer_prm_c(self):
        """
        deallocate_spartacus_layer_prm_c(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1151-1163
        
        Parameters
        ----------
        self : Spartacus_Layer_Prm
        
        """
        _supy_driver.f90wrap_suews_def_dts__deallocate_spartacus_layer_prm_c(self=self._handle)
    
    @staticmethod
    def allochydrostate_c(self, nlayer):
        """
        allochydrostate_c(self, nlayer)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1165-1178
        
        Parameters
        ----------
        self : Hydro_State
        nlayer : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__allochydrostate_c(self=self._handle, \
            nlayer=nlayer)
    
    @staticmethod
    def deallochydrostate_c(self):
        """
        deallochydrostate_c(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1180-1191
        
        Parameters
        ----------
        self : Hydro_State
        
        """
        _supy_driver.f90wrap_suews_def_dts__deallochydrostate_c(self=self._handle)
    
    @staticmethod
    def allocheatstate_c(self, num_surf, num_layer, num_depth):
        """
        allocheatstate_c(self, num_surf, num_layer, num_depth)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1193-1219
        
        Parameters
        ----------
        self : Heat_State
        num_surf : int
        num_layer : int
        num_depth : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__allocheatstate_c(self=self._handle, \
            num_surf=num_surf, num_layer=num_layer, num_depth=num_depth)
    
    @staticmethod
    def deallocheatstate_c(self):
        """
        deallocheatstate_c(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1221-1244
        
        Parameters
        ----------
        self : Heat_State
        
        """
        _supy_driver.f90wrap_suews_def_dts__deallocheatstate_c(self=self._handle)
    
    @staticmethod
    def allocate_ehc_prm_c(self, nlayer, ndepth):
        """
        allocate_ehc_prm_c(self, nlayer, ndepth)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1246-1268
        
        Parameters
        ----------
        self : Ehc_Prm
        nlayer : int
        ndepth : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__allocate_ehc_prm_c(self=self._handle, \
            nlayer=nlayer, ndepth=ndepth)
    
    @staticmethod
    def deallocate_ehc_prm_c(self):
        """
        deallocate_ehc_prm_c(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1270-1290
        
        Parameters
        ----------
        self : Ehc_Prm
        
        """
        _supy_driver.f90wrap_suews_def_dts__deallocate_ehc_prm_c(self=self._handle)
    
    @staticmethod
    def allocate_site_prm_c(self, nlayer):
        """
        allocate_site_prm_c(self, nlayer)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1292-1297
        
        Parameters
        ----------
        self : Suews_Site
        nlayer : int
        
        """
        _supy_driver.f90wrap_suews_def_dts__allocate_site_prm_c(self=self._handle, \
            nlayer=nlayer)
    
    @staticmethod
    def deallocate_site_prm_c(self):
        """
        deallocate_site_prm_c(self)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1299-1306
        
        Parameters
        ----------
        self : Suews_Site
        
        """
        _supy_driver.f90wrap_suews_def_dts__deallocate_site_prm_c(self=self._handle)
    
    @staticmethod
    def suews_cal_surf_dts(self, config):
        """
        suews_cal_surf_dts(self, config)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1308-1398
        
        Parameters
        ----------
        self : Suews_Site
        config : Suews_Config
        
        """
        _supy_driver.f90wrap_suews_def_dts__suews_cal_surf_dts(self=self._handle, \
            config=config._handle)
    
    @staticmethod
    def check_and_reset_unsafe_states(self, ref_state):
        """
        check_and_reset_unsafe_states(self, ref_state)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_type.fpp \
            lines 1400-1439
        
        Parameters
        ----------
        self : Suews_State
        ref_state : Suews_State
        
        """
        _supy_driver.f90wrap_suews_def_dts__check_and_reset_unsafe_states(self=self._handle, \
            ref_state=ref_state._handle)
    
    _dt_array_initialisers = []
    

suews_def_dts = Suews_Def_Dts()

class Suews_Driver(f90wrap.runtime.FortranModule):
    """
    Module suews_driver
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
        lines 17-4781
    
    """
    @staticmethod
    def suews_cal_main(self, forcing, config, siteinfo, modstate, debugstate=None):
        """
        outputline = suews_cal_main(self, forcing, config, siteinfo, modstate[, \
            debugstate])
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 85-528
        
        Parameters
        ----------
        timer : Suews_Timer
        forcing : Suews_Forcing
        config : Suews_Config
        siteinfo : Suews_Site
        modstate : Suews_State
        debugstate : Suews_Debug
        
        Returns
        -------
        outputline : Output_Line
        
        ==============surface roughness calculation=======================
        """
        outputline = \
            _supy_driver.f90wrap_suews_driver__suews_cal_main(timer=self._handle, \
            forcing=forcing._handle, config=config._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, debugstate=None if debugstate is None else \
            debugstate._handle)
        outputline = \
            f90wrap.runtime.lookup_class("supy_driver.output_line").from_handle(outputline, \
            alloc=True)
        return outputline
    
    @staticmethod
    def update_debug_info(self, config, forcing, siteinfo, modstate_init, modstate, \
        dataoutlinedebug):
        """
        update_debug_info(self, config, forcing, siteinfo, modstate_init, modstate, \
            dataoutlinedebug)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 535-610
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate_init : Suews_State
        modstate : Suews_State
        dataoutlinedebug : float array
        
        """
        _supy_driver.f90wrap_suews_driver__update_debug_info(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate_init=modstate_init._handle, modstate=modstate._handle, \
            dataoutlinedebug=dataoutlinedebug)
    
    @staticmethod
    def suews_update_tsurf(self, config, forcing, siteinfo, modstate):
        """
        suews_update_tsurf(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 615-696
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        ============ calculate surface temperature ===============
        """
        _supy_driver.f90wrap_suews_driver__suews_update_tsurf(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def suews_cal_anthropogenicemission(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_anthropogenicemission(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 701-838
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_anthropogenicemission(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def suews_cal_qn(self, config, forcing, siteinfo, modstate, \
        dataoutlinespartacus):
        """
        suews_cal_qn(self, config, forcing, siteinfo, modstate, dataoutlinespartacus)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 1032-1254
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        dataoutlinespartacus : float array
        
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_qn(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, dataoutlinespartacus=dataoutlinespartacus)
    
    @staticmethod
    def suews_cal_qs(self, config, forcing, siteinfo, modstate, dataoutlineestm):
        """
        suews_cal_qs(self, config, forcing, siteinfo, modstate, dataoutlineestm)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 1261-1636
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        dataoutlineestm : float array
        
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_qs(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, dataoutlineestm=dataoutlineestm)
    
    @staticmethod
    def suews_cal_water(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_water(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 1642-1783
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        ============= Grid-to-grid runoff =============
         Calculate additional water coming from other grids
         i.e. the variables addImpervious, addVeg, addWaterBody, addPipes
        call RunoffFromGrid(GridFromFrac)
        Need to code between-grid water transfer
         Sum water coming from other grids(these are expressed as depths over the whole \
             surface)
         Initialise runoff in pipes
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_water(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def suews_cal_snow(self, config, forcing, siteinfo, modstate, dataoutlinesnow):
        """
        suews_cal_snow(self, config, forcing, siteinfo, modstate, dataoutlinesnow)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 1790-2116
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        dataoutlinesnow : float array
        
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_snow(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, dataoutlinesnow=dataoutlinesnow)
    
    @staticmethod
    def suews_cal_qe(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_qe(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 2122-2447
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        ========== Calculate soil moisture of a whole grid ============
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_qe(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def suews_cal_qh(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_qh(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 2453-2587
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_qh(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def suews_cal_resistance(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_resistance(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 2593-2750
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_suews_driver__suews_cal_resistance(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def suews_update_outputline(self, config, forcing, siteinfo, modstate, \
        datetimeline, dataoutlinesuews):
        """
        suews_update_outputline(self, config, forcing, siteinfo, modstate, datetimeline, \
            dataoutlinesuews)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 2757-2924
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        datetimeline : float array
        dataoutlinesuews : float array
        
        =====================================================================
        ====================== Prepare data for output ======================
         values outside of reasonable range are set as NAN-like numbers. TS 10 Jun 2018
        """
        _supy_driver.f90wrap_suews_driver__suews_update_outputline(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, datetimeline=datetimeline, \
            dataoutlinesuews=dataoutlinesuews)
    
    @staticmethod
    def ehc_update_outputline(self, modstate, datetimeline, dataoutlineehc):
        """
        ehc_update_outputline(self, modstate, datetimeline, dataoutlineehc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 2931-2995
        
        Parameters
        ----------
        timer : Suews_Timer
        modstate : Suews_State
        datetimeline : float array
        dataoutlineehc : float array
        
        ====================update output line end==============================
        """
        _supy_driver.f90wrap_suews_driver__ehc_update_outputline(timer=self._handle, \
            modstate=modstate._handle, datetimeline=datetimeline, \
            dataoutlineehc=dataoutlineehc)
    
    @staticmethod
    def fill_sim_res(res_valid, n_fill):
        """
        res_filled = fill_sim_res(res_valid, n_fill)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 2998-3004
        
        Parameters
        ----------
        res_valid : float array
        n_fill : int
        
        Returns
        -------
        res_filled : float array
        
        """
        res_filled = \
            _supy_driver.f90wrap_suews_driver__fill_sim_res(res_valid=res_valid, \
            n_fill=n_fill)
        return res_filled
    
    @staticmethod
    def suews_update_output(snowuse, storageheatmethod, readlinesmetdata, \
        numberofgrids, ir, gridiv, dataoutlinesuews, dataoutlinesnow, \
        dataoutlineestm, dataoutlinersl, dataoutlinebeers, dataoutlinedebug, \
        dataoutlinespartacus, dataoutlineehc, dataoutlinestebbs, dataoutlinenhood, \
        dataoutsuews, dataoutsnow, dataoutestm, dataoutrsl, dataoutbeers, \
        dataoutdebug, dataoutspartacus, dataoutehc, dataoutstebbs, dataoutnhood):
        """
        suews_update_output(snowuse, storageheatmethod, readlinesmetdata, numberofgrids, \
            ir, gridiv, dataoutlinesuews, dataoutlinesnow, dataoutlineestm, \
            dataoutlinersl, dataoutlinebeers, dataoutlinedebug, dataoutlinespartacus, \
            dataoutlineehc, dataoutlinestebbs, dataoutlinenhood, dataoutsuews, \
            dataoutsnow, dataoutestm, dataoutrsl, dataoutbeers, dataoutdebug, \
            dataoutspartacus, dataoutehc, dataoutstebbs, dataoutnhood)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3019-3070
        
        Parameters
        ----------
        snowuse : int
        storageheatmethod : int
        readlinesmetdata : int
        numberofgrids : int
        ir : int
        gridiv : int
        dataoutlinesuews : float array
        dataoutlinesnow : float array
        dataoutlineestm : float array
        dataoutlinersl : float array
        dataoutlinebeers : float array
        dataoutlinedebug : float array
        dataoutlinespartacus : float array
        dataoutlineehc : float array
        dataoutlinestebbs : float array
        dataoutlinenhood : float array
        dataoutsuews : float array
        dataoutsnow : float array
        dataoutestm : float array
        dataoutrsl : float array
        dataoutbeers : float array
        dataoutdebug : float array
        dataoutspartacus : float array
        dataoutehc : float array
        dataoutstebbs : float array
        dataoutnhood : float array
        
        ====================== update output arrays ==============================
        Define the overall output matrix to be printed out step by step
        """
        _supy_driver.f90wrap_suews_driver__suews_update_output(snowuse=snowuse, \
            storageheatmethod=storageheatmethod, readlinesmetdata=readlinesmetdata, \
            numberofgrids=numberofgrids, ir=ir, gridiv=gridiv, \
            dataoutlinesuews=dataoutlinesuews, dataoutlinesnow=dataoutlinesnow, \
            dataoutlineestm=dataoutlineestm, dataoutlinersl=dataoutlinersl, \
            dataoutlinebeers=dataoutlinebeers, dataoutlinedebug=dataoutlinedebug, \
            dataoutlinespartacus=dataoutlinespartacus, dataoutlineehc=dataoutlineehc, \
            dataoutlinestebbs=dataoutlinestebbs, dataoutlinenhood=dataoutlinenhood, \
            dataoutsuews=dataoutsuews, dataoutsnow=dataoutsnow, dataoutestm=dataoutestm, \
            dataoutrsl=dataoutrsl, dataoutbeers=dataoutbeers, dataoutdebug=dataoutdebug, \
            dataoutspartacus=dataoutspartacus, dataoutehc=dataoutehc, \
            dataoutstebbs=dataoutstebbs, dataoutnhood=dataoutnhood)
    
    @staticmethod
    def suews_cal_surf(storageheatmethod, netradiationmethod, nlayer, sfr_paved, \
        sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
        building_frac, building_scale, height, sfr_roof, sfr_wall):
        """
        vegfraction, impervfraction, pervfraction, nonwaterfraction = \
            suews_cal_surf(storageheatmethod, netradiationmethod, nlayer, sfr_paved, \
            sfr_bldg, sfr_evetr, sfr_dectr, sfr_grass, sfr_bsoil, sfr_water, \
            building_frac, building_scale, height, sfr_roof, sfr_wall)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3079-3133
        
        Parameters
        ----------
        storageheatmethod : int
        netradiationmethod : int
        nlayer : int
        sfr_paved : float
        sfr_bldg : float
        sfr_evetr : float
        sfr_dectr : float
        sfr_grass : float
        sfr_bsoil : float
        sfr_water : float
        building_frac : float array
        building_scale : float array
        height : float array
        sfr_roof : float array
        sfr_wall : float array
        
        Returns
        -------
        vegfraction : float
        impervfraction : float
        pervfraction : float
        nonwaterfraction : float
        
        """
        vegfraction, impervfraction, pervfraction, nonwaterfraction = \
            _supy_driver.f90wrap_suews_driver__suews_cal_surf(storageheatmethod=storageheatmethod, \
            netradiationmethod=netradiationmethod, nlayer=nlayer, sfr_paved=sfr_paved, \
            sfr_bldg=sfr_bldg, sfr_evetr=sfr_evetr, sfr_dectr=sfr_dectr, \
            sfr_grass=sfr_grass, sfr_bsoil=sfr_bsoil, sfr_water=sfr_water, \
            building_frac=building_frac, building_scale=building_scale, height=height, \
            sfr_roof=sfr_roof, sfr_wall=sfr_wall)
        return vegfraction, impervfraction, pervfraction, nonwaterfraction
    
    @staticmethod
    def set_nan(x):
        """
        xx = set_nan(x)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3136-3149
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        xx : float
        
        """
        xx = _supy_driver.f90wrap_suews_driver__set_nan(x=x)
        return xx
    
    @staticmethod
    def square(x):
        """
        xx = square(x)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3153-3160
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        xx : float
        
        """
        xx = _supy_driver.f90wrap_suews_driver__square(x=x)
        return xx
    
    @staticmethod
    def square_real(x):
        """
        xx = square_real(x)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3162-3169
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        xx : float
        
        """
        xx = _supy_driver.f90wrap_suews_driver__square_real(x=x)
        return xx
    
    @staticmethod
    def output_name_n(i):
        """
        name, group, aggreg, outlevel = output_name_n(i)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3171-3191
        
        Parameters
        ----------
        i : int
        
        Returns
        -------
        name : str
        group : str
        aggreg : str
        outlevel : int
        
        """
        name, group, aggreg, outlevel = \
            _supy_driver.f90wrap_suews_driver__output_name_n(i=i)
        return name, group, aggreg, outlevel
    
    @staticmethod
    def output_size():
        """
        nvar = output_size()
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3193-3302
        
        
        Returns
        -------
        nvar : int
        
        """
        nvar = _supy_driver.f90wrap_suews_driver__output_size()
        return nvar
    
    @staticmethod
    def suews_cal_multitsteps(n_buildings, h_std, flag_test, metforcingblock, \
        len_sim, ah_min, ahprof_24hr, ah_slope_cooling, ah_slope_heating, alb, \
        albmax_dectr, albmax_evetr, albmax_grass, albmin_dectr, albmin_evetr, \
        albmin_grass, alpha_bioco2, alpha_enh_bioco2, alt, baset, basete, \
        beta_bioco2, beta_enh_bioco2, bldgh, capmax_dec, capmin_dec, chanohm, \
        co2pointsource, cpanohm, crwmax, crwmin, daywat, daywatper, dectreeh, \
        diagmethod, diagnose, drainrt, dt_since_start, dqndt, qn_av, dqnsdt, \
        qn_s_av, ef_umolco2perj, emis, emissionsmethod, enef_v_jkm, enddls, \
        evetreeh, faibldg, faidectree, faievetree, faimethod, faut, fcef_v_kgkm, \
        flowchange, frfossilfuel_heat, frfossilfuel_nonheat, g_max, g_k, g_q_base, \
        g_q_shape, g_t, g_sm, gdd_id, gddfull, gridiv, gsmodel, h_maintain, hdd_id, \
        humactivity_24hr, icefrac, ie_a, ie_end, ie_m, ie_start, internalwateruse_h, \
        irrfracpaved, irrfracbldgs, irrfracevetr, irrfracdectr, irrfracgrass, \
        irrfracbsoil, irrfracwater, kkanohm, kmax, lai_id, laimax, laimin, laipower, \
        laitype, lat, lng, localclimatemethod, maxconductance, maxfcmetab, \
        maxqfmetab, snowwater, minfcmetab, minqfmetab, min_res_bioco2, \
        narp_emis_snow, narp_trans_site, netradiationmethod, ohm_coef, ohmincqf, \
        ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, popdensnighttime, \
        popprof_24hr, pormax_dec, pormin_dec, preciplimit, preciplimitalb, qf0_beu, \
        qf_a, qf_b, qf_c, nlayer, n_vegetation_region_urban, n_stream_sw_urban, \
        n_stream_lw_urban, sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, \
        air_ext_lw, air_ssa_lw, veg_ssa_lw, veg_fsd_const, \
        veg_contact_fraction_const, ground_albedo_dir_mult_fact, \
        use_sw_direct_albedo, lambda_c, stebbsmethod, buildingname, buildingtype, \
        buildingcount, occupants, stebbs_height, footprintarea, wallexternalarea, \
        ratiointernalvolume, wwr, wallthickness, walleffectiveconductivity, \
        walldensity, wallcp, wallx1, wallexternalemissivity, wallinternalemissivity, \
        walltransmissivity, wallabsorbtivity, wallreflectivity, floorthickness, \
        groundflooreffectiveconductivity, groundfloordensity, groundfloorcp, \
        windowthickness, windoweffectiveconductivity, windowdensity, windowcp, \
        windowexternalemissivity, windowinternalemissivity, windowtransmissivity, \
        windowabsorbtivity, windowreflectivity, internalmassdensity, internalmasscp, \
        internalmassemissivity, maxheatingpower, watertankwatervolume, \
        maximumhotwaterheatingpower, heatingsetpointtemperature, \
        coolingsetpointtemperature, wallinternalconvectioncoefficient, \
        internalmassconvectioncoefficient, floorinternalconvectioncoefficient, \
        windowinternalconvectioncoefficient, wallexternalconvectioncoefficient, \
        windowexternalconvectioncoefficient, grounddepth, \
        externalgroundconductivity, indoorairdensity, indooraircp, \
        wallbuildingviewfactor, wallgroundviewfactor, wallskyviewfactor, \
        metabolicrate, latentsensibleratio, appliancerating, \
        totalnumberofappliances, applianceusagefactor, heatingsystemefficiency, \
        maxcoolingpower, coolingsystemcop, ventilationrate, \
        indoorairstarttemperature, indoormassstarttemperature, \
        wallindoorsurfacetemperature, walloutdoorsurfacetemperature, \
        windowindoorsurfacetemperature, windowoutdoorsurfacetemperature, \
        groundfloorindoorsurfacetemperature, groundflooroutdoorsurfacetemperature, \
        watertanktemperature, internalwallwatertanktemperature, \
        externalwallwatertanktemperature, watertankwallthickness, \
        mainswatertemperature, watertanksurfacearea, \
        hotwaterheatingsetpointtemperature, hotwatertankwallemissivity, \
        domestichotwatertemperatureinuseinbuilding, \
        internalwalldhwvesseltemperature, externalwalldhwvesseltemperature, \
        dhwvesselwallthickness, dhwwatervolume, dhwsurfacearea, dhwvesselemissivity, \
        hotwaterflowrate, dhwdrainflowrate, dhwspecificheatcapacity, \
        hotwatertankspecificheatcapacity, dhwvesselspecificheatcapacity, dhwdensity, \
        hotwatertankwalldensity, dhwvesseldensity, \
        hotwatertankbuildingwallviewfactor, hotwatertankinternalmassviewfactor, \
        hotwatertankwallconductivity, hotwatertankinternalwallconvectioncoefficient, \
        hotwatertankexternalwallconvectioncoefficient, dhwvesselwallconductivity, \
        dhwvesselinternalwallconvectioncoefficient, \
        dhwvesselexternalwallconvectioncoefficient, dhwvesselwallemissivity, \
        hotwaterheatingefficiency, minimumvolumeofdhwinuse, height, building_frac, \
        veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
        emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, radmeltfact, \
        raincover, rainmaxres, resp_a, resp_b, roughlenheatmethod, \
        roughlenmommethod, runofftowater, s1, s2, sathydraulicconduct, sddfull, \
        sdd_id, smdmethod, snowalb, snowalbmax, snowalbmin, snowpacklimit, snowdens, \
        snowdensmax, snowdensmin, snowfallcum, snowfrac, snowlimbldg, snowlimpaved, \
        snowpack, snowprof_24hr, snowuse, soildepth, stabilitymethod, startdls, \
        soilstore_surf, soilstorecap_surf, state_surf, statelimit_surf, \
        wetthresh_surf, soilstore_roof, soilstorecap_roof, state_roof, \
        statelimit_roof, wetthresh_roof, soilstore_wall, soilstorecap_wall, \
        state_wall, statelimit_wall, wetthresh_wall, storageheatmethod, \
        storedrainprm, surfacearea, tair_av, tau_a, tau_f, tau_r, baset_cooling, \
        baset_heating, tempmeltfact, th, theta_bioco2, timezone, tl, trafficrate, \
        trafficunits, sfr_surf, tsfc_roof, tsfc_wall, tsfc_surf, temp_roof, \
        temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, k_wall, k_roof, k_surf, \
        cp_wall, cp_roof, cp_surf, dz_wall, dz_roof, dz_surf, tmin_id, tmax_id, \
        lenday_id, traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, \
        waterdist, waterusemethod, wuday_id, decidcap_id, albdectr_id, albevetr_id, \
        albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, z, z0m_in, zdm_in, \
        state_debug=None, block_mod_state=None):
        """
        output_block_suews = suews_cal_multitsteps(n_buildings, h_std, flag_test, \
            metforcingblock, len_sim, ah_min, ahprof_24hr, ah_slope_cooling, \
            ah_slope_heating, alb, albmax_dectr, albmax_evetr, albmax_grass, \
            albmin_dectr, albmin_evetr, albmin_grass, alpha_bioco2, alpha_enh_bioco2, \
            alt, baset, basete, beta_bioco2, beta_enh_bioco2, bldgh, capmax_dec, \
            capmin_dec, chanohm, co2pointsource, cpanohm, crwmax, crwmin, daywat, \
            daywatper, dectreeh, diagmethod, diagnose, drainrt, dt_since_start, dqndt, \
            qn_av, dqnsdt, qn_s_av, ef_umolco2perj, emis, emissionsmethod, enef_v_jkm, \
            enddls, evetreeh, faibldg, faidectree, faievetree, faimethod, faut, \
            fcef_v_kgkm, flowchange, frfossilfuel_heat, frfossilfuel_nonheat, g_max, \
            g_k, g_q_base, g_q_shape, g_t, g_sm, gdd_id, gddfull, gridiv, gsmodel, \
            h_maintain, hdd_id, humactivity_24hr, icefrac, ie_a, ie_end, ie_m, ie_start, \
            internalwateruse_h, irrfracpaved, irrfracbldgs, irrfracevetr, irrfracdectr, \
            irrfracgrass, irrfracbsoil, irrfracwater, kkanohm, kmax, lai_id, laimax, \
            laimin, laipower, laitype, lat, lng, localclimatemethod, maxconductance, \
            maxfcmetab, maxqfmetab, snowwater, minfcmetab, minqfmetab, min_res_bioco2, \
            narp_emis_snow, narp_trans_site, netradiationmethod, ohm_coef, ohmincqf, \
            ohm_threshsw, ohm_threshwd, pipecapacity, popdensdaytime, popdensnighttime, \
            popprof_24hr, pormax_dec, pormin_dec, preciplimit, preciplimitalb, qf0_beu, \
            qf_a, qf_b, qf_c, nlayer, n_vegetation_region_urban, n_stream_sw_urban, \
            n_stream_lw_urban, sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, \
            air_ext_lw, air_ssa_lw, veg_ssa_lw, veg_fsd_const, \
            veg_contact_fraction_const, ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo, lambda_c, stebbsmethod, buildingname, buildingtype, \
            buildingcount, occupants, stebbs_height, footprintarea, wallexternalarea, \
            ratiointernalvolume, wwr, wallthickness, walleffectiveconductivity, \
            walldensity, wallcp, wallx1, wallexternalemissivity, wallinternalemissivity, \
            walltransmissivity, wallabsorbtivity, wallreflectivity, floorthickness, \
            groundflooreffectiveconductivity, groundfloordensity, groundfloorcp, \
            windowthickness, windoweffectiveconductivity, windowdensity, windowcp, \
            windowexternalemissivity, windowinternalemissivity, windowtransmissivity, \
            windowabsorbtivity, windowreflectivity, internalmassdensity, internalmasscp, \
            internalmassemissivity, maxheatingpower, watertankwatervolume, \
            maximumhotwaterheatingpower, heatingsetpointtemperature, \
            coolingsetpointtemperature, wallinternalconvectioncoefficient, \
            internalmassconvectioncoefficient, floorinternalconvectioncoefficient, \
            windowinternalconvectioncoefficient, wallexternalconvectioncoefficient, \
            windowexternalconvectioncoefficient, grounddepth, \
            externalgroundconductivity, indoorairdensity, indooraircp, \
            wallbuildingviewfactor, wallgroundviewfactor, wallskyviewfactor, \
            metabolicrate, latentsensibleratio, appliancerating, \
            totalnumberofappliances, applianceusagefactor, heatingsystemefficiency, \
            maxcoolingpower, coolingsystemcop, ventilationrate, \
            indoorairstarttemperature, indoormassstarttemperature, \
            wallindoorsurfacetemperature, walloutdoorsurfacetemperature, \
            windowindoorsurfacetemperature, windowoutdoorsurfacetemperature, \
            groundfloorindoorsurfacetemperature, groundflooroutdoorsurfacetemperature, \
            watertanktemperature, internalwallwatertanktemperature, \
            externalwallwatertanktemperature, watertankwallthickness, \
            mainswatertemperature, watertanksurfacearea, \
            hotwaterheatingsetpointtemperature, hotwatertankwallemissivity, \
            domestichotwatertemperatureinuseinbuilding, \
            internalwalldhwvesseltemperature, externalwalldhwvesseltemperature, \
            dhwvesselwallthickness, dhwwatervolume, dhwsurfacearea, dhwvesselemissivity, \
            hotwaterflowrate, dhwdrainflowrate, dhwspecificheatcapacity, \
            hotwatertankspecificheatcapacity, dhwvesselspecificheatcapacity, dhwdensity, \
            hotwatertankwalldensity, dhwvesseldensity, \
            hotwatertankbuildingwallviewfactor, hotwatertankinternalmassviewfactor, \
            hotwatertankwallconductivity, hotwatertankinternalwallconvectioncoefficient, \
            hotwatertankexternalwallconvectioncoefficient, dhwvesselwallconductivity, \
            dhwvesselinternalwallconvectioncoefficient, \
            dhwvesselexternalwallconvectioncoefficient, dhwvesselwallemissivity, \
            hotwaterheatingefficiency, minimumvolumeofdhwinuse, height, building_frac, \
            veg_frac, building_scale, veg_scale, alb_roof, emis_roof, alb_wall, \
            emis_wall, roof_albedo_dir_mult_fact, wall_specular_frac, radmeltfact, \
            raincover, rainmaxres, resp_a, resp_b, roughlenheatmethod, \
            roughlenmommethod, runofftowater, s1, s2, sathydraulicconduct, sddfull, \
            sdd_id, smdmethod, snowalb, snowalbmax, snowalbmin, snowpacklimit, snowdens, \
            snowdensmax, snowdensmin, snowfallcum, snowfrac, snowlimbldg, snowlimpaved, \
            snowpack, snowprof_24hr, snowuse, soildepth, stabilitymethod, startdls, \
            soilstore_surf, soilstorecap_surf, state_surf, statelimit_surf, \
            wetthresh_surf, soilstore_roof, soilstorecap_roof, state_roof, \
            statelimit_roof, wetthresh_roof, soilstore_wall, soilstorecap_wall, \
            state_wall, statelimit_wall, wetthresh_wall, storageheatmethod, \
            storedrainprm, surfacearea, tair_av, tau_a, tau_f, tau_r, baset_cooling, \
            baset_heating, tempmeltfact, th, theta_bioco2, timezone, tl, trafficrate, \
            trafficunits, sfr_surf, tsfc_roof, tsfc_wall, tsfc_surf, temp_roof, \
            temp_wall, temp_surf, tin_roof, tin_wall, tin_surf, k_wall, k_roof, k_surf, \
            cp_wall, cp_roof, cp_surf, dz_wall, dz_roof, dz_surf, tmin_id, tmax_id, \
            lenday_id, traffprof_24hr, ts5mindata_ir, tstep, tstep_prev, veg_type, \
            waterdist, waterusemethod, wuday_id, decidcap_id, albdectr_id, albevetr_id, \
            albgrass_id, porosity_id, wuprofa_24hr, wuprofm_24hr, z, z0m_in, zdm_in[, \
            state_debug, block_mod_state])
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 3304-4692
        
        Parameters
        ----------
        n_buildings : float
        h_std : float
        flag_test : bool
        metforcingblock : float array
        len_sim : int
        ah_min : float array
        ahprof_24hr : float array
        ah_slope_cooling : float array
        ah_slope_heating : float array
        alb : float array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        alpha_bioco2 : float array
        alpha_enh_bioco2 : float array
        alt : float
        baset : float array
        basete : float array
        beta_bioco2 : float array
        beta_enh_bioco2 : float array
        bldgh : float
        capmax_dec : float
        capmin_dec : float
        chanohm : float array
        co2pointsource : float
        cpanohm : float array
        crwmax : float
        crwmin : float
        daywat : float array
        daywatper : float array
        dectreeh : float
        diagmethod : int
        diagnose : int
        drainrt : float
        dt_since_start : int
        dqndt : float
        qn_av : float
        dqnsdt : float
        qn_s_av : float
        ef_umolco2perj : float
        emis : float array
        emissionsmethod : int
        enef_v_jkm : float
        enddls : int
        evetreeh : float
        faibldg : float
        faidectree : float
        faievetree : float
        faimethod : int
        faut : float
        fcef_v_kgkm : float array
        flowchange : float
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        gdd_id : float array
        gddfull : float array
        gridiv : int
        gsmodel : int
        h_maintain : float
        hdd_id : float array
        humactivity_24hr : float array
        icefrac : float array
        ie_a : float array
        ie_end : int
        ie_m : float array
        ie_start : int
        internalwateruse_h : float
        irrfracpaved : float
        irrfracbldgs : float
        irrfracevetr : float
        irrfracdectr : float
        irrfracgrass : float
        irrfracbsoil : float
        irrfracwater : float
        kkanohm : float array
        kmax : float
        lai_id : float array
        laimax : float array
        laimin : float array
        laipower : float array
        laitype : int array
        lat : float
        lng : float
        localclimatemethod : int
        maxconductance : float array
        maxfcmetab : float
        maxqfmetab : float
        snowwater : float array
        minfcmetab : float
        minqfmetab : float
        min_res_bioco2 : float array
        narp_emis_snow : float
        narp_trans_site : float
        netradiationmethod : int
        ohm_coef : float array
        ohmincqf : int
        ohm_threshsw : float array
        ohm_threshwd : float array
        pipecapacity : float
        popdensdaytime : float array
        popdensnighttime : float
        popprof_24hr : float array
        pormax_dec : float
        pormin_dec : float
        preciplimit : float
        preciplimitalb : float
        qf0_beu : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        nlayer : int
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        lambda_c : float
        stebbsmethod : int
        buildingname : str
        buildingtype : str
        buildingcount : float
        occupants : float
        stebbs_height : float
        footprintarea : float
        wallexternalarea : float
        ratiointernalvolume : float
        wwr : float
        wallthickness : float
        walleffectiveconductivity : float
        walldensity : float
        wallcp : float
        wallx1 : float
        wallexternalemissivity : float
        wallinternalemissivity : float
        walltransmissivity : float
        wallabsorbtivity : float
        wallreflectivity : float
        floorthickness : float
        groundflooreffectiveconductivity : float
        groundfloordensity : float
        groundfloorcp : float
        windowthickness : float
        windoweffectiveconductivity : float
        windowdensity : float
        windowcp : float
        windowexternalemissivity : float
        windowinternalemissivity : float
        windowtransmissivity : float
        windowabsorbtivity : float
        windowreflectivity : float
        internalmassdensity : float
        internalmasscp : float
        internalmassemissivity : float
        maxheatingpower : float
        watertankwatervolume : float
        maximumhotwaterheatingpower : float
        heatingsetpointtemperature : float
        coolingsetpointtemperature : float
        wallinternalconvectioncoefficient : float
        internalmassconvectioncoefficient : float
        floorinternalconvectioncoefficient : float
        windowinternalconvectioncoefficient : float
        wallexternalconvectioncoefficient : float
        windowexternalconvectioncoefficient : float
        grounddepth : float
        externalgroundconductivity : float
        indoorairdensity : float
        indooraircp : float
        wallbuildingviewfactor : float
        wallgroundviewfactor : float
        wallskyviewfactor : float
        metabolicrate : float
        latentsensibleratio : float
        appliancerating : float
        totalnumberofappliances : float
        applianceusagefactor : float
        heatingsystemefficiency : float
        maxcoolingpower : float
        coolingsystemcop : float
        ventilationrate : float
        indoorairstarttemperature : float
        indoormassstarttemperature : float
        wallindoorsurfacetemperature : float
        walloutdoorsurfacetemperature : float
        windowindoorsurfacetemperature : float
        windowoutdoorsurfacetemperature : float
        groundfloorindoorsurfacetemperature : float
        groundflooroutdoorsurfacetemperature : float
        watertanktemperature : float
        internalwallwatertanktemperature : float
        externalwallwatertanktemperature : float
        watertankwallthickness : float
        mainswatertemperature : float
        watertanksurfacearea : float
        hotwaterheatingsetpointtemperature : float
        hotwatertankwallemissivity : float
        domestichotwatertemperatureinuseinbuilding : float
        internalwalldhwvesseltemperature : float
        externalwalldhwvesseltemperature : float
        dhwvesselwallthickness : float
        dhwwatervolume : float
        dhwsurfacearea : float
        dhwvesselemissivity : float
        hotwaterflowrate : float
        dhwdrainflowrate : float
        dhwspecificheatcapacity : float
        hotwatertankspecificheatcapacity : float
        dhwvesselspecificheatcapacity : float
        dhwdensity : float
        hotwatertankwalldensity : float
        dhwvesseldensity : float
        hotwatertankbuildingwallviewfactor : float
        hotwatertankinternalmassviewfactor : float
        hotwatertankwallconductivity : float
        hotwatertankinternalwallconvectioncoefficient : float
        hotwatertankexternalwallconvectioncoefficient : float
        dhwvesselwallconductivity : float
        dhwvesselinternalwallconvectioncoefficient : float
        dhwvesselexternalwallconvectioncoefficient : float
        dhwvesselwallemissivity : float
        hotwaterheatingefficiency : float
        minimumvolumeofdhwinuse : float
        height : float array
        building_frac : float array
        veg_frac : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        radmeltfact : float
        raincover : float
        rainmaxres : float
        resp_a : float array
        resp_b : float array
        roughlenheatmethod : int
        roughlenmommethod : int
        runofftowater : float
        s1 : float
        s2 : float
        sathydraulicconduct : float array
        sddfull : float array
        sdd_id : float array
        smdmethod : int
        snowalb : float
        snowalbmax : float
        snowalbmin : float
        snowpacklimit : float array
        snowdens : float array
        snowdensmax : float
        snowdensmin : float
        snowfallcum : float
        snowfrac : float array
        snowlimbldg : float
        snowlimpaved : float
        snowpack : float array
        snowprof_24hr : float array
        snowuse : int
        soildepth : float array
        stabilitymethod : int
        startdls : int
        soilstore_surf : float array
        soilstorecap_surf : float array
        state_surf : float array
        statelimit_surf : float array
        wetthresh_surf : float array
        soilstore_roof : float array
        soilstorecap_roof : float array
        state_roof : float array
        statelimit_roof : float array
        wetthresh_roof : float array
        soilstore_wall : float array
        soilstorecap_wall : float array
        state_wall : float array
        statelimit_wall : float array
        wetthresh_wall : float array
        storageheatmethod : int
        storedrainprm : float array
        surfacearea : float
        tair_av : float
        tau_a : float
        tau_f : float
        tau_r : float
        baset_cooling : float array
        baset_heating : float array
        tempmeltfact : float
        th : float
        theta_bioco2 : float array
        timezone : float
        tl : float
        trafficrate : float array
        trafficunits : float
        sfr_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        tsfc_surf : float array
        temp_roof : float array
        temp_wall : float array
        temp_surf : float array
        tin_roof : float array
        tin_wall : float array
        tin_surf : float array
        k_wall : float array
        k_roof : float array
        k_surf : float array
        cp_wall : float array
        cp_roof : float array
        cp_surf : float array
        dz_wall : float array
        dz_roof : float array
        dz_surf : float array
        tmin_id : float
        tmax_id : float
        lenday_id : float
        traffprof_24hr : float array
        ts5mindata_ir : float array
        tstep : int
        tstep_prev : int
        veg_type : int
        waterdist : float array
        waterusemethod : int
        wuday_id : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        wuprofa_24hr : float array
        wuprofm_24hr : float array
        z : float
        z0m_in : float
        zdm_in : float
        state_debug : Suews_Debug
        block_mod_state : Suews_State_Block
        
        Returns
        -------
        output_block_suews : Output_Block
        
        ============ update DailyStateBlock ===============
        """
        output_block_suews = \
            _supy_driver.f90wrap_suews_driver__suews_cal_multitsteps(n_buildings=n_buildings, \
            h_std=h_std, flag_test=flag_test, metforcingblock=metforcingblock, \
            len_sim=len_sim, ah_min=ah_min, ahprof_24hr=ahprof_24hr, \
            ah_slope_cooling=ah_slope_cooling, ah_slope_heating=ah_slope_heating, \
            alb=alb, albmax_dectr=albmax_dectr, albmax_evetr=albmax_evetr, \
            albmax_grass=albmax_grass, albmin_dectr=albmin_dectr, \
            albmin_evetr=albmin_evetr, albmin_grass=albmin_grass, \
            alpha_bioco2=alpha_bioco2, alpha_enh_bioco2=alpha_enh_bioco2, alt=alt, \
            baset=baset, basete=basete, beta_bioco2=beta_bioco2, \
            beta_enh_bioco2=beta_enh_bioco2, bldgh=bldgh, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, chanohm=chanohm, co2pointsource=co2pointsource, \
            cpanohm=cpanohm, crwmax=crwmax, crwmin=crwmin, daywat=daywat, \
            daywatper=daywatper, dectreeh=dectreeh, diagmethod=diagmethod, \
            diagnose=diagnose, drainrt=drainrt, dt_since_start=dt_since_start, \
            dqndt=dqndt, qn_av=qn_av, dqnsdt=dqnsdt, qn_s_av=qn_s_av, \
            ef_umolco2perj=ef_umolco2perj, emis=emis, emissionsmethod=emissionsmethod, \
            enef_v_jkm=enef_v_jkm, enddls=enddls, evetreeh=evetreeh, faibldg=faibldg, \
            faidectree=faidectree, faievetree=faievetree, faimethod=faimethod, \
            faut=faut, fcef_v_kgkm=fcef_v_kgkm, flowchange=flowchange, \
            frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, g_max=g_max, g_k=g_k, \
            g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, gdd_id=gdd_id, \
            gddfull=gddfull, gridiv=gridiv, gsmodel=gsmodel, h_maintain=h_maintain, \
            hdd_id=hdd_id, humactivity_24hr=humactivity_24hr, icefrac=icefrac, \
            ie_a=ie_a, ie_end=ie_end, ie_m=ie_m, ie_start=ie_start, \
            internalwateruse_h=internalwateruse_h, irrfracpaved=irrfracpaved, \
            irrfracbldgs=irrfracbldgs, irrfracevetr=irrfracevetr, \
            irrfracdectr=irrfracdectr, irrfracgrass=irrfracgrass, \
            irrfracbsoil=irrfracbsoil, irrfracwater=irrfracwater, kkanohm=kkanohm, \
            kmax=kmax, lai_id=lai_id, laimax=laimax, laimin=laimin, laipower=laipower, \
            laitype=laitype, lat=lat, lng=lng, localclimatemethod=localclimatemethod, \
            maxconductance=maxconductance, maxfcmetab=maxfcmetab, maxqfmetab=maxqfmetab, \
            snowwater=snowwater, minfcmetab=minfcmetab, minqfmetab=minqfmetab, \
            min_res_bioco2=min_res_bioco2, narp_emis_snow=narp_emis_snow, \
            narp_trans_site=narp_trans_site, netradiationmethod=netradiationmethod, \
            ohm_coef=ohm_coef, ohmincqf=ohmincqf, ohm_threshsw=ohm_threshsw, \
            ohm_threshwd=ohm_threshwd, pipecapacity=pipecapacity, \
            popdensdaytime=popdensdaytime, popdensnighttime=popdensnighttime, \
            popprof_24hr=popprof_24hr, pormax_dec=pormax_dec, pormin_dec=pormin_dec, \
            preciplimit=preciplimit, preciplimitalb=preciplimitalb, qf0_beu=qf0_beu, \
            qf_a=qf_a, qf_b=qf_b, qf_c=qf_c, nlayer=nlayer, \
            n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, lambda_c=lambda_c, \
            stebbsmethod=stebbsmethod, buildingname=buildingname, \
            buildingtype=buildingtype, buildingcount=buildingcount, occupants=occupants, \
            stebbs_height=stebbs_height, footprintarea=footprintarea, \
            wallexternalarea=wallexternalarea, ratiointernalvolume=ratiointernalvolume, \
            wwr=wwr, wallthickness=wallthickness, \
            walleffectiveconductivity=walleffectiveconductivity, \
            walldensity=walldensity, wallcp=wallcp, wallx1=wallx1, \
            wallexternalemissivity=wallexternalemissivity, \
            wallinternalemissivity=wallinternalemissivity, \
            walltransmissivity=walltransmissivity, wallabsorbtivity=wallabsorbtivity, \
            wallreflectivity=wallreflectivity, floorthickness=floorthickness, \
            groundflooreffectiveconductivity=groundflooreffectiveconductivity, \
            groundfloordensity=groundfloordensity, groundfloorcp=groundfloorcp, \
            windowthickness=windowthickness, \
            windoweffectiveconductivity=windoweffectiveconductivity, \
            windowdensity=windowdensity, windowcp=windowcp, \
            windowexternalemissivity=windowexternalemissivity, \
            windowinternalemissivity=windowinternalemissivity, \
            windowtransmissivity=windowtransmissivity, \
            windowabsorbtivity=windowabsorbtivity, \
            windowreflectivity=windowreflectivity, \
            internalmassdensity=internalmassdensity, internalmasscp=internalmasscp, \
            internalmassemissivity=internalmassemissivity, \
            maxheatingpower=maxheatingpower, watertankwatervolume=watertankwatervolume, \
            maximumhotwaterheatingpower=maximumhotwaterheatingpower, \
            heatingsetpointtemperature=heatingsetpointtemperature, \
            coolingsetpointtemperature=coolingsetpointtemperature, \
            wallinternalconvectioncoefficient=wallinternalconvectioncoefficient, \
            internalmassconvectioncoefficient=internalmassconvectioncoefficient, \
            floorinternalconvectioncoefficient=floorinternalconvectioncoefficient, \
            windowinternalconvectioncoefficient=windowinternalconvectioncoefficient, \
            wallexternalconvectioncoefficient=wallexternalconvectioncoefficient, \
            windowexternalconvectioncoefficient=windowexternalconvectioncoefficient, \
            grounddepth=grounddepth, \
            externalgroundconductivity=externalgroundconductivity, \
            indoorairdensity=indoorairdensity, indooraircp=indooraircp, \
            wallbuildingviewfactor=wallbuildingviewfactor, \
            wallgroundviewfactor=wallgroundviewfactor, \
            wallskyviewfactor=wallskyviewfactor, metabolicrate=metabolicrate, \
            latentsensibleratio=latentsensibleratio, appliancerating=appliancerating, \
            totalnumberofappliances=totalnumberofappliances, \
            applianceusagefactor=applianceusagefactor, \
            heatingsystemefficiency=heatingsystemefficiency, \
            maxcoolingpower=maxcoolingpower, coolingsystemcop=coolingsystemcop, \
            ventilationrate=ventilationrate, \
            indoorairstarttemperature=indoorairstarttemperature, \
            indoormassstarttemperature=indoormassstarttemperature, \
            wallindoorsurfacetemperature=wallindoorsurfacetemperature, \
            walloutdoorsurfacetemperature=walloutdoorsurfacetemperature, \
            windowindoorsurfacetemperature=windowindoorsurfacetemperature, \
            windowoutdoorsurfacetemperature=windowoutdoorsurfacetemperature, \
            groundfloorindoorsurfacetemperature=groundfloorindoorsurfacetemperature, \
            groundflooroutdoorsurfacetemperature=groundflooroutdoorsurfacetemperature, \
            watertanktemperature=watertanktemperature, \
            internalwallwatertanktemperature=internalwallwatertanktemperature, \
            externalwallwatertanktemperature=externalwallwatertanktemperature, \
            watertankwallthickness=watertankwallthickness, \
            mainswatertemperature=mainswatertemperature, \
            watertanksurfacearea=watertanksurfacearea, \
            hotwaterheatingsetpointtemperature=hotwaterheatingsetpointtemperature, \
            hotwatertankwallemissivity=hotwatertankwallemissivity, \
            domestichotwatertemperatureinuseinbuilding=domestichotwatertemperatureinuseinbuilding, \
            internalwalldhwvesseltemperature=internalwalldhwvesseltemperature, \
            externalwalldhwvesseltemperature=externalwalldhwvesseltemperature, \
            dhwvesselwallthickness=dhwvesselwallthickness, \
            dhwwatervolume=dhwwatervolume, dhwsurfacearea=dhwsurfacearea, \
            dhwvesselemissivity=dhwvesselemissivity, hotwaterflowrate=hotwaterflowrate, \
            dhwdrainflowrate=dhwdrainflowrate, \
            dhwspecificheatcapacity=dhwspecificheatcapacity, \
            hotwatertankspecificheatcapacity=hotwatertankspecificheatcapacity, \
            dhwvesselspecificheatcapacity=dhwvesselspecificheatcapacity, \
            dhwdensity=dhwdensity, hotwatertankwalldensity=hotwatertankwalldensity, \
            dhwvesseldensity=dhwvesseldensity, \
            hotwatertankbuildingwallviewfactor=hotwatertankbuildingwallviewfactor, \
            hotwatertankinternalmassviewfactor=hotwatertankinternalmassviewfactor, \
            hotwatertankwallconductivity=hotwatertankwallconductivity, \
            hotwatertankinternalwallconvectioncoefficient=hotwatertankinternalwallconvectioncoefficient, \
            hotwatertankexternalwallconvectioncoefficient=hotwatertankexternalwallconvectioncoefficient, \
            dhwvesselwallconductivity=dhwvesselwallconductivity, \
            dhwvesselinternalwallconvectioncoefficient=dhwvesselinternalwallconvectioncoefficient, \
            dhwvesselexternalwallconvectioncoefficient=dhwvesselexternalwallconvectioncoefficient, \
            dhwvesselwallemissivity=dhwvesselwallemissivity, \
            hotwaterheatingefficiency=hotwaterheatingefficiency, \
            minimumvolumeofdhwinuse=minimumvolumeofdhwinuse, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, \
            building_scale=building_scale, veg_scale=veg_scale, alb_roof=alb_roof, \
            emis_roof=emis_roof, alb_wall=alb_wall, emis_wall=emis_wall, \
            roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, radmeltfact=radmeltfact, \
            raincover=raincover, rainmaxres=rainmaxres, resp_a=resp_a, resp_b=resp_b, \
            roughlenheatmethod=roughlenheatmethod, roughlenmommethod=roughlenmommethod, \
            runofftowater=runofftowater, s1=s1, s2=s2, \
            sathydraulicconduct=sathydraulicconduct, sddfull=sddfull, sdd_id=sdd_id, \
            smdmethod=smdmethod, snowalb=snowalb, snowalbmax=snowalbmax, \
            snowalbmin=snowalbmin, snowpacklimit=snowpacklimit, snowdens=snowdens, \
            snowdensmax=snowdensmax, snowdensmin=snowdensmin, snowfallcum=snowfallcum, \
            snowfrac=snowfrac, snowlimbldg=snowlimbldg, snowlimpaved=snowlimpaved, \
            snowpack=snowpack, snowprof_24hr=snowprof_24hr, snowuse=snowuse, \
            soildepth=soildepth, stabilitymethod=stabilitymethod, startdls=startdls, \
            soilstore_surf=soilstore_surf, soilstorecap_surf=soilstorecap_surf, \
            state_surf=state_surf, statelimit_surf=statelimit_surf, \
            wetthresh_surf=wetthresh_surf, soilstore_roof=soilstore_roof, \
            soilstorecap_roof=soilstorecap_roof, state_roof=state_roof, \
            statelimit_roof=statelimit_roof, wetthresh_roof=wetthresh_roof, \
            soilstore_wall=soilstore_wall, soilstorecap_wall=soilstorecap_wall, \
            state_wall=state_wall, statelimit_wall=statelimit_wall, \
            wetthresh_wall=wetthresh_wall, storageheatmethod=storageheatmethod, \
            storedrainprm=storedrainprm, surfacearea=surfacearea, tair_av=tair_av, \
            tau_a=tau_a, tau_f=tau_f, tau_r=tau_r, baset_cooling=baset_cooling, \
            baset_heating=baset_heating, tempmeltfact=tempmeltfact, th=th, \
            theta_bioco2=theta_bioco2, timezone=timezone, tl=tl, \
            trafficrate=trafficrate, trafficunits=trafficunits, sfr_surf=sfr_surf, \
            tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, tsfc_surf=tsfc_surf, \
            temp_roof=temp_roof, temp_wall=temp_wall, temp_surf=temp_surf, \
            tin_roof=tin_roof, tin_wall=tin_wall, tin_surf=tin_surf, k_wall=k_wall, \
            k_roof=k_roof, k_surf=k_surf, cp_wall=cp_wall, cp_roof=cp_roof, \
            cp_surf=cp_surf, dz_wall=dz_wall, dz_roof=dz_roof, dz_surf=dz_surf, \
            tmin_id=tmin_id, tmax_id=tmax_id, lenday_id=lenday_id, \
            traffprof_24hr=traffprof_24hr, ts5mindata_ir=ts5mindata_ir, tstep=tstep, \
            tstep_prev=tstep_prev, veg_type=veg_type, waterdist=waterdist, \
            waterusemethod=waterusemethod, wuday_id=wuday_id, decidcap_id=decidcap_id, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            porosity_id=porosity_id, wuprofa_24hr=wuprofa_24hr, \
            wuprofm_24hr=wuprofm_24hr, z=z, z0m_in=z0m_in, zdm_in=zdm_in, \
            state_debug=None if state_debug is None else state_debug._handle, \
            block_mod_state=None if block_mod_state is None else \
            block_mod_state._handle)
        output_block_suews = \
            f90wrap.runtime.lookup_class("supy_driver.output_block").from_handle(output_block_suews, \
            alloc=True)
        return output_block_suews
    
    @staticmethod
    def suews_cal_sunposition(year, idectime, utc, locationlatitude, \
        locationlongitude, locationaltitude):
        """
        sunazimuth, sunzenith = suews_cal_sunposition(year, idectime, utc, \
            locationlatitude, locationlongitude, locationaltitude)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 4697-4704
        
        Parameters
        ----------
        year : float
        idectime : float
        utc : float
        locationlatitude : float
        locationlongitude : float
        locationaltitude : float
        
        Returns
        -------
        sunazimuth : float
        sunzenith : float
        
        """
        sunazimuth, sunzenith = \
            _supy_driver.f90wrap_suews_driver__suews_cal_sunposition(year=year, \
            idectime=idectime, utc=utc, locationlatitude=locationlatitude, \
            locationlongitude=locationlongitude, locationaltitude=locationaltitude)
        return sunazimuth, sunzenith
    
    @staticmethod
    def cal_tair_av(tair_av_prev, dt_since_start, tstep, temp_c):
        """
        tair_av_next = cal_tair_av(tair_av_prev, dt_since_start, tstep, temp_c)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 4706-4727
        
        Parameters
        ----------
        tair_av_prev : float
        dt_since_start : int
        tstep : int
        temp_c : float
        
        Returns
        -------
        tair_av_next : float
        
        """
        tair_av_next = \
            _supy_driver.f90wrap_suews_driver__cal_tair_av(tair_av_prev=tair_av_prev, \
            dt_since_start=dt_since_start, tstep=tstep, temp_c=temp_c)
        return tair_av_next
    
    @staticmethod
    def cal_tsfc(qh, dens_air, vcp_air, ra, temp_c):
        """
        tsfc_c = cal_tsfc(qh, dens_air, vcp_air, ra, temp_c)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 4729-4739
        
        Parameters
        ----------
        qh : float
        dens_air : float
        vcp_air : float
        ra : float
        temp_c : float
        
        Returns
        -------
        tsfc_c : float
        
        """
        tsfc_c = _supy_driver.f90wrap_suews_driver__cal_tsfc(qh=qh, dens_air=dens_air, \
            vcp_air=vcp_air, ra=ra, temp_c=temp_c)
        return tsfc_c
    
    @staticmethod
    def restore_state(self, mod_state_stepstart):
        """
        restore_state(self, mod_state_stepstart)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            lines 4741-4781
        
        Parameters
        ----------
        mod_state : Suews_State
        mod_state_stepstart : Suews_State
        
        """
        _supy_driver.f90wrap_suews_driver__restore_state(mod_state=self._handle, \
            mod_state_stepstart=mod_state_stepstart._handle)
    
    @property
    def snow_warning_shown(self):
        """
        Element snow_warning_shown ftype=logical pytype=bool
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_ctrl_driver.fpp \
            line 78
        
        """
        return _supy_driver.f90wrap_suews_driver__get__snow_warning_shown()
    
    @snow_warning_shown.setter
    def snow_warning_shown(self, snow_warning_shown):
        _supy_driver.f90wrap_suews_driver__set__snow_warning_shown(snow_warning_shown)
    
    def __str__(self):
        ret = ['<suews_driver>{\n']
        ret.append('    snow_warning_shown : ')
        ret.append(repr(self.snow_warning_shown))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

suews_driver = Suews_Driver()

class Anemsn_Module(f90wrap.runtime.FortranModule):
    """
    Module anemsn_module
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_anthro.fpp \
        lines 5-289
    
    """
    @staticmethod
    def anthropogenicemissions(co2pointsource, emissionsmethod, it, imin, dls, \
        dayofweek_id, ef_umolco2perj, fcef_v_kgkm, enef_v_jkm, trafficunits, \
        frfossilfuel_heat, frfossilfuel_nonheat, minfcmetab, maxfcmetab, minqfmetab, \
        maxqfmetab, popdensdaytime, popdensnighttime, tair, hdd_id, qf_a, qf_b, \
        qf_c, ah_min, ah_slope_heating, ah_slope_cooling, baset_heating, \
        baset_cooling, trafficrate, qf0_beu, ahprof_24hr, humactivity_24hr, \
        traffprof_24hr, popprof_24hr, surfacearea):
        """
        qf_sahp, fc_anthro, fc_metab, fc_traff, fc_build, fc_point = \
            anthropogenicemissions(co2pointsource, emissionsmethod, it, imin, dls, \
            dayofweek_id, ef_umolco2perj, fcef_v_kgkm, enef_v_jkm, trafficunits, \
            frfossilfuel_heat, frfossilfuel_nonheat, minfcmetab, maxfcmetab, minqfmetab, \
            maxqfmetab, popdensdaytime, popdensnighttime, tair, hdd_id, qf_a, qf_b, \
            qf_c, ah_min, ah_slope_heating, ah_slope_cooling, baset_heating, \
            baset_cooling, trafficrate, qf0_beu, ahprof_24hr, humactivity_24hr, \
            traffprof_24hr, popprof_24hr, surfacearea)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_anthro.fpp \
            lines 44-288
        
        Parameters
        ----------
        co2pointsource : float
        emissionsmethod : int
        it : int
        imin : int
        dls : int
        dayofweek_id : int array
        ef_umolco2perj : float
        fcef_v_kgkm : float array
        enef_v_jkm : float
        trafficunits : float
        frfossilfuel_heat : float
        frfossilfuel_nonheat : float
        minfcmetab : float
        maxfcmetab : float
        minqfmetab : float
        maxqfmetab : float
        popdensdaytime : float array
        popdensnighttime : float
        tair : float
        hdd_id : float array
        qf_a : float array
        qf_b : float array
        qf_c : float array
        ah_min : float array
        ah_slope_heating : float array
        ah_slope_cooling : float array
        baset_heating : float array
        baset_cooling : float array
        trafficrate : float array
        qf0_beu : float array
        ahprof_24hr : float array
        humactivity_24hr : float array
        traffprof_24hr : float array
        popprof_24hr : float array
        surfacearea : float
        
        Returns
        -------
        qf_sahp : float
        fc_anthro : float
        fc_metab : float
        fc_traff : float
        fc_build : float
        fc_point : float
        
        -----------------------------------------------------------------------
         Account for Daylight saving
        """
        qf_sahp, fc_anthro, fc_metab, fc_traff, fc_build, fc_point = \
            _supy_driver.f90wrap_anemsn_module__anthropogenicemissions(co2pointsource=co2pointsource, \
            emissionsmethod=emissionsmethod, it=it, imin=imin, dls=dls, \
            dayofweek_id=dayofweek_id, ef_umolco2perj=ef_umolco2perj, \
            fcef_v_kgkm=fcef_v_kgkm, enef_v_jkm=enef_v_jkm, trafficunits=trafficunits, \
            frfossilfuel_heat=frfossilfuel_heat, \
            frfossilfuel_nonheat=frfossilfuel_nonheat, minfcmetab=minfcmetab, \
            maxfcmetab=maxfcmetab, minqfmetab=minqfmetab, maxqfmetab=maxqfmetab, \
            popdensdaytime=popdensdaytime, popdensnighttime=popdensnighttime, tair=tair, \
            hdd_id=hdd_id, qf_a=qf_a, qf_b=qf_b, qf_c=qf_c, ah_min=ah_min, \
            ah_slope_heating=ah_slope_heating, ah_slope_cooling=ah_slope_cooling, \
            baset_heating=baset_heating, baset_cooling=baset_cooling, \
            trafficrate=trafficrate, qf0_beu=qf0_beu, ahprof_24hr=ahprof_24hr, \
            humactivity_24hr=humactivity_24hr, traffprof_24hr=traffprof_24hr, \
            popprof_24hr=popprof_24hr, surfacearea=surfacearea)
        return qf_sahp, fc_anthro, fc_metab, fc_traff, fc_build, fc_point
    
    _dt_array_initialisers = []
    

anemsn_module = Anemsn_Module()

class Atmmoiststab_Module(f90wrap.runtime.FortranModule):
    """
    Module atmmoiststab_module
    
    
    Defined at \
        src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
        lines 5-1006
    
    """
    @staticmethod
    def suews_update_atmstate(self, forcing, modstate):
        """
        suews_update_atmstate(self, forcing, modstate)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 18-49
        
        Parameters
        ----------
        timer : Suews_Timer
        forcing : Suews_Forcing
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_atmmoiststab_module__suews_update_atmstate(timer=self._handle, \
            forcing=forcing._handle, modstate=modstate._handle)
    
    @staticmethod
    def update_tair_av(tair_av_prev, dt_since_start, tstep, temp_c):
        """
        tair_av_next = update_tair_av(tair_av_prev, dt_since_start, tstep, temp_c)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 51-72
        
        Parameters
        ----------
        tair_av_prev : float
        dt_since_start : int
        tstep : int
        temp_c : float
        
        Returns
        -------
        tair_av_next : float
        
        """
        tair_av_next = \
            _supy_driver.f90wrap_atmmoiststab_module__update_tair_av(tair_av_prev=tair_av_prev, \
            dt_since_start=dt_since_start, tstep=tstep, temp_c=temp_c)
        return tair_av_next
    
    @staticmethod
    def cal_atmmoist(temp_c, press_hpa, avrh, dectime):
        """
        lv_j_kg, lvs_j_kg, es_hpa, ea_hpa, vpd_hpa, vpd_pa, dq, dens_dry, avcp, air_dens \
            = cal_atmmoist(temp_c, press_hpa, avrh, dectime)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 80-141
        
        Parameters
        ----------
        temp_c : float
        press_hpa : float
        avrh : float
        dectime : float
        
        Returns
        -------
        lv_j_kg : float
        lvs_j_kg : float
        es_hpa : float
        ea_hpa : float
        vpd_hpa : float
        vpd_pa : float
        dq : float
        dens_dry : float
        avcp : float
        air_dens : float
        
        """
        lv_j_kg, lvs_j_kg, es_hpa, ea_hpa, vpd_hpa, vpd_pa, dq, dens_dry, avcp, air_dens \
            = _supy_driver.f90wrap_atmmoiststab_module__cal_atmmoist(temp_c=temp_c, \
            press_hpa=press_hpa, avrh=avrh, dectime=dectime)
        return lv_j_kg, lvs_j_kg, es_hpa, ea_hpa, vpd_hpa, vpd_pa, dq, dens_dry, avcp, \
            air_dens
    
    @staticmethod
    def cal_stab(stabilitymethod, zzd, z0m, zdm, avu1, temp_c, qh_init, avdens, \
        avcp):
        """
        l_mod, tstar, ustar, zl = cal_stab(stabilitymethod, zzd, z0m, zdm, avu1, temp_c, \
            qh_init, avdens, avcp)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 168-313
        
        Parameters
        ----------
        stabilitymethod : int
        zzd : float
        z0m : float
        zdm : float
        avu1 : float
        temp_c : float
        qh_init : float
        avdens : float
        avcp : float
        
        Returns
        -------
        l_mod : float
        tstar : float
        ustar : float
        zl : float
        
        """
        l_mod, tstar, ustar, zl = \
            _supy_driver.f90wrap_atmmoiststab_module__cal_stab(stabilitymethod=stabilitymethod, \
            zzd=zzd, z0m=z0m, zdm=zdm, avu1=avu1, temp_c=temp_c, qh_init=qh_init, \
            avdens=avdens, avcp=avcp)
        return l_mod, tstar, ustar, zl
    
    @staticmethod
    def stab_psi_mom(stabilitymethod, zl):
        """
        psim = stab_psi_mom(stabilitymethod, zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 319-332
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = \
            _supy_driver.f90wrap_atmmoiststab_module__stab_psi_mom(stabilitymethod=stabilitymethod, \
            zl=zl)
        return psim
    
    @staticmethod
    def stab_psi_heat(stabilitymethod, zl):
        """
        psih = stab_psi_heat(stabilitymethod, zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 335-348
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = \
            _supy_driver.f90wrap_atmmoiststab_module__stab_psi_heat(stabilitymethod=stabilitymethod, \
            zl=zl)
        return psih
    
    @staticmethod
    def stab_phi_mom(stabilitymethod, zl):
        """
        phim = stab_phi_mom(stabilitymethod, zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 351-362
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = \
            _supy_driver.f90wrap_atmmoiststab_module__stab_phi_mom(stabilitymethod=stabilitymethod, \
            zl=zl)
        return phim
    
    @staticmethod
    def stab_phi_heat(stabilitymethod, zl):
        """
        phih = stab_phi_heat(stabilitymethod, zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 365-376
        
        Parameters
        ----------
        stabilitymethod : int
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = \
            _supy_driver.f90wrap_atmmoiststab_module__stab_phi_heat(stabilitymethod=stabilitymethod, \
            zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_j12(zl):
        """
        psim = psi_mom_j12(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 381-395
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_atmmoiststab_module__psi_mom_j12(zl=zl)
        return psim
    
    @staticmethod
    def phi_mom_j12(zl):
        """
        phim = phi_mom_j12(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 397-409
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_atmmoiststab_module__phi_mom_j12(zl=zl)
        return phim
    
    @staticmethod
    def psi_heat_j12(zl):
        """
        psih = psi_heat_j12(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 411-423
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_atmmoiststab_module__psi_heat_j12(zl=zl)
        return psih
    
    @staticmethod
    def phi_heat_j12(zl):
        """
        phih = phi_heat_j12(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 425-433
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_atmmoiststab_module__phi_heat_j12(zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_g00(zl):
        """
        psim = psi_mom_g00(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 441-458
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_atmmoiststab_module__psi_mom_g00(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_g00(zl):
        """
        psih = psi_heat_g00(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 460-477
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_atmmoiststab_module__psi_heat_g00(zl=zl)
        return psih
    
    @staticmethod
    def phi_mom_g00(zl):
        """
        phim = phi_mom_g00(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 485-506
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_atmmoiststab_module__phi_mom_g00(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_g00(zl):
        """
        phih = phi_heat_g00(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 508-526
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_atmmoiststab_module__phi_heat_g00(zl=zl)
        return phih
    
    @staticmethod
    def psi_conv(zl, ax):
        """
        psic = psi_conv(zl, ax)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 528-533
        
        Parameters
        ----------
        zl : float
        ax : float
        
        Returns
        -------
        psic : float
        
        """
        psic = _supy_driver.f90wrap_atmmoiststab_module__psi_conv(zl=zl, ax=ax)
        return psic
    
    @staticmethod
    def phi_conv(zl, ax):
        """
        phic = phi_conv(zl, ax)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 535-543
        
        Parameters
        ----------
        zl : float
        ax : float
        
        Returns
        -------
        phic : float
        
        """
        phic = _supy_driver.f90wrap_atmmoiststab_module__phi_conv(zl=zl, ax=ax)
        return phic
    
    @staticmethod
    def dpsi_dzl_g00(zl, psik, phik, psic, phic):
        """
        dpsi = dpsi_dzl_g00(zl, psik, phik, psic, phic)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 545-560
        
        Parameters
        ----------
        zl : float
        psik : float
        phik : float
        psic : float
        phic : float
        
        Returns
        -------
        dpsi : float
        
        """
        dpsi = _supy_driver.f90wrap_atmmoiststab_module__dpsi_dzl_g00(zl=zl, psik=psik, \
            phik=phik, psic=psic, phic=phic)
        return dpsi
    
    @staticmethod
    def psi_cb05(zl, k1, k2):
        """
        psi = psi_cb05(zl, k1, k2)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 567-570
        
        Parameters
        ----------
        zl : float
        k1 : float
        k2 : float
        
        Returns
        -------
        psi : float
        
        """
        psi = _supy_driver.f90wrap_atmmoiststab_module__psi_cb05(zl=zl, k1=k1, k2=k2)
        return psi
    
    @staticmethod
    def psi_mom_cb05(zl):
        """
        psim = psi_mom_cb05(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 572-581
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_atmmoiststab_module__psi_mom_cb05(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_cb05(zl):
        """
        psih = psi_heat_cb05(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 583-592
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_atmmoiststab_module__psi_heat_cb05(zl=zl)
        return psih
    
    @staticmethod
    def phi_cb05(zl, k1, k2):
        """
        phi = phi_cb05(zl, k1, k2)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 594-601
        
        Parameters
        ----------
        zl : float
        k1 : float
        k2 : float
        
        Returns
        -------
        phi : float
        
        """
        phi = _supy_driver.f90wrap_atmmoiststab_module__phi_cb05(zl=zl, k1=k1, k2=k2)
        return phi
    
    @staticmethod
    def phi_mom_cb05(zl):
        """
        phim = phi_mom_cb05(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 603-612
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_atmmoiststab_module__phi_mom_cb05(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_cb05(zl):
        """
        phih = phi_heat_cb05(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 614-624
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_atmmoiststab_module__phi_heat_cb05(zl=zl)
        return phih
    
    @staticmethod
    def phi_mom_k75(zl):
        """
        phim = phi_mom_k75(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 630-639
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_atmmoiststab_module__phi_mom_k75(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_k75(zl):
        """
        phih = phi_heat_k75(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 641-650
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_atmmoiststab_module__phi_heat_k75(zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_k75(zl):
        """
        psim = psi_mom_k75(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 652-661
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_atmmoiststab_module__psi_mom_k75(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_k75(zl):
        """
        psih = psi_heat_k75(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 663-672
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_atmmoiststab_module__psi_heat_k75(zl=zl)
        return psih
    
    @staticmethod
    def phi_mom_b71(zl):
        """
        phim = phi_mom_b71(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 678-688
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phim : float
        
        """
        phim = _supy_driver.f90wrap_atmmoiststab_module__phi_mom_b71(zl=zl)
        return phim
    
    @staticmethod
    def phi_heat_b71(zl):
        """
        phih = phi_heat_b71(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 690-700
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        phih : float
        
        """
        phih = _supy_driver.f90wrap_atmmoiststab_module__phi_heat_b71(zl=zl)
        return phih
    
    @staticmethod
    def psi_mom_b71(zl):
        """
        psim = psi_mom_b71(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 702-714
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psim : float
        
        """
        psim = _supy_driver.f90wrap_atmmoiststab_module__psi_mom_b71(zl=zl)
        return psim
    
    @staticmethod
    def psi_heat_b71(zl):
        """
        psih = psi_heat_b71(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 716-730
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psih : float
        
        """
        psih = _supy_driver.f90wrap_atmmoiststab_module__psi_heat_b71(zl=zl)
        return psih
    
    @staticmethod
    def psi_mom_w16(zl):
        """
        psym = psi_mom_w16(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 734-758
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psym : float
        
        """
        psym = _supy_driver.f90wrap_atmmoiststab_module__psi_mom_w16(zl=zl)
        return psym
    
    @staticmethod
    def psi_heat_w16(zl):
        """
        psyh = psi_heat_w16(zl)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            lines 762-783
        
        Parameters
        ----------
        zl : float
        
        Returns
        -------
        psyh : float
        
        """
        psyh = _supy_driver.f90wrap_atmmoiststab_module__psi_heat_w16(zl=zl)
        return psyh
    
    @property
    def neut_limit(self):
        """
        Element neut_limit ftype=real(kind(1d0) pytype=float
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 9
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__neut_limit()
    
    @property
    def k(self):
        """
        Element k ftype=real(kind(1d0) pytype=float
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 10
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__k()
    
    @property
    def grav(self):
        """
        Element grav ftype=real(kind(1d0) pytype=float
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 11
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__grav()
    
    @property
    def w16(self):
        """
        Element w16 ftype=integer pytype=int
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 13
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__w16()
    
    @property
    def k75(self):
        """
        Element k75 ftype=integer pytype=int
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 14
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__k75()
    
    @property
    def b71(self):
        """
        Element b71 ftype=integer pytype=int
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 15
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__b71()
    
    @property
    def j12(self):
        """
        Element j12 ftype=integer pytype=int
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_atmmoiststab.fpp \
            line 16
        
        """
        return _supy_driver.f90wrap_atmmoiststab_module__get__j12()
    
    def __str__(self):
        ret = ['<atmmoiststab_module>{\n']
        ret.append('    neut_limit : ')
        ret.append(repr(self.neut_limit))
        ret.append(',\n    k : ')
        ret.append(repr(self.k))
        ret.append(',\n    grav : ')
        ret.append(repr(self.grav))
        ret.append(',\n    w16 : ')
        ret.append(repr(self.w16))
        ret.append(',\n    k75 : ')
        ret.append(repr(self.k75))
        ret.append(',\n    b71 : ')
        ret.append(repr(self.b71))
        ret.append(',\n    j12 : ')
        ret.append(repr(self.j12))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

atmmoiststab_module = Atmmoiststab_Module()

class Dailystate_Module(f90wrap.runtime.FortranModule):
    """
    Module dailystate_module
    
    
    Defined at \
        src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
        lines 5-1190
    
    """
    @staticmethod
    def suews_cal_dailystate(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_dailystate(self, config, forcing, siteinfo, modstate)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 60-543
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        REAL(KIND(1D0)), DIMENSION(7) :: DayWatPer
        of houses following daily water
        ------------------------------------------------------------------------------
         Calculation of LAI from growing degree days
         This was revised and checked on 16 Feb 2014 by LJ
        ------------------------------------------------------------------------------
         save initial LAI_id
         LAI_id_in = LAI_id
        """
        _supy_driver.f90wrap_dailystate_module__suews_cal_dailystate(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def update_dailystate_day(basetmethod, dayofweek_id, avkdn, tair, precip, \
        baset_hc, baset_heating, baset_cooling, nsh_real, tmin_id, tmax_id, \
        lenday_id, hdd_id):
        """
        update_dailystate_day(basetmethod, dayofweek_id, avkdn, tair, precip, baset_hc, \
            baset_heating, baset_cooling, nsh_real, tmin_id, tmax_id, lenday_id, hdd_id)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 678-746
        
        Parameters
        ----------
        basetmethod : int
        dayofweek_id : int array
        avkdn : float
        tair : float
        precip : float
        baset_hc : float
        baset_heating : float array
        baset_cooling : float array
        nsh_real : float
        tmin_id : float
        tmax_id : float
        lenday_id : float
        hdd_id : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__update_dailystate_day(basetmethod=basetmethod, \
            dayofweek_id=dayofweek_id, avkdn=avkdn, tair=tair, precip=precip, \
            baset_hc=baset_hc, baset_heating=baset_heating, baset_cooling=baset_cooling, \
            nsh_real=nsh_real, tmin_id=tmin_id, tmax_id=tmax_id, lenday_id=lenday_id, \
            hdd_id=hdd_id)
    
    @staticmethod
    def update_veg(laimax, laimin, albmax_dectr, albmax_evetr, albmax_grass, \
        albmin_dectr, albmin_evetr, albmin_grass, capmax_dec, capmin_dec, \
        pormax_dec, pormin_dec, lai_id, lai_id_prev, decidcap_id, albdectr_id, \
        albevetr_id, albgrass_id, porosity_id, storedrainprm):
        """
        update_veg(laimax, laimin, albmax_dectr, albmax_evetr, albmax_grass, \
            albmin_dectr, albmin_evetr, albmin_grass, capmax_dec, capmin_dec, \
            pormax_dec, pormin_dec, lai_id, lai_id_prev, decidcap_id, albdectr_id, \
            albevetr_id, albgrass_id, porosity_id, storedrainprm)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 748-832
        
        Parameters
        ----------
        laimax : float array
        laimin : float array
        albmax_dectr : float
        albmax_evetr : float
        albmax_grass : float
        albmin_dectr : float
        albmin_evetr : float
        albmin_grass : float
        capmax_dec : float
        capmin_dec : float
        pormax_dec : float
        pormin_dec : float
        lai_id : float array
        lai_id_prev : float array
        decidcap_id : float
        albdectr_id : float
        albevetr_id : float
        albgrass_id : float
        porosity_id : float
        storedrainprm : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__update_veg(laimax=laimax, laimin=laimin, \
            albmax_dectr=albmax_dectr, albmax_evetr=albmax_evetr, \
            albmax_grass=albmax_grass, albmin_dectr=albmin_dectr, \
            albmin_evetr=albmin_evetr, albmin_grass=albmin_grass, capmax_dec=capmax_dec, \
            capmin_dec=capmin_dec, pormax_dec=pormax_dec, pormin_dec=pormin_dec, \
            lai_id=lai_id, lai_id_prev=lai_id_prev, decidcap_id=decidcap_id, \
            albdectr_id=albdectr_id, albevetr_id=albevetr_id, albgrass_id=albgrass_id, \
            porosity_id=porosity_id, storedrainprm=storedrainprm)
    
    @staticmethod
    def update_gddlai(id, laicalcyes, lat, lai_obs, tmin_id_prev, tmax_id_prev, \
        lenday_id_prev, baset_gdd, baset_sdd, gddfull, sddfull, laimin, laimax, \
        laipower, laitype, lai_id_prev, gdd_id, sdd_id, lai_id_next):
        """
        update_gddlai(id, laicalcyes, lat, lai_obs, tmin_id_prev, tmax_id_prev, \
            lenday_id_prev, baset_gdd, baset_sdd, gddfull, sddfull, laimin, laimax, \
            laipower, laitype, lai_id_prev, gdd_id, sdd_id, lai_id_next)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 834-970
        
        Parameters
        ----------
        id : int
        laicalcyes : int
        lat : float
        lai_obs : float
        tmin_id_prev : float
        tmax_id_prev : float
        lenday_id_prev : float
        baset_gdd : float array
        baset_sdd : float array
        gddfull : float array
        sddfull : float array
        laimin : float array
        laimax : float array
        laipower : float array
        laitype : int array
        lai_id_prev : float array
        gdd_id : float array
        sdd_id : float array
        lai_id_next : float array
        
        ------------------------------------------------------------------------------
         Calculation of LAI from growing degree days
         This was revised and checked on 16 Feb 2014 by LJ
        ------------------------------------------------------------------------------
        """
        _supy_driver.f90wrap_dailystate_module__update_gddlai(id=id, \
            laicalcyes=laicalcyes, lat=lat, lai_obs=lai_obs, tmin_id_prev=tmin_id_prev, \
            tmax_id_prev=tmax_id_prev, lenday_id_prev=lenday_id_prev, \
            baset_gdd=baset_gdd, baset_sdd=baset_sdd, gddfull=gddfull, sddfull=sddfull, \
            laimin=laimin, laimax=laimax, laipower=laipower, laitype=laitype, \
            lai_id_prev=lai_id_prev, gdd_id=gdd_id, sdd_id=sdd_id, \
            lai_id_next=lai_id_next)
    
    @staticmethod
    def update_wateruse(id, waterusemethod, dayofweek_id, lat, frirriauto, hdd_id, \
        state_surf, soilstore_surf, soilstorecap_surf, h_maintain, ie_a, ie_m, \
        ie_start, ie_end, daywatper, daywat, wuday_id):
        """
        update_wateruse(id, waterusemethod, dayofweek_id, lat, frirriauto, hdd_id, \
            state_surf, soilstore_surf, soilstorecap_surf, h_maintain, ie_a, ie_m, \
            ie_start, ie_end, daywatper, daywat, wuday_id)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 972-1052
        
        Parameters
        ----------
        id : int
        waterusemethod : int
        dayofweek_id : int array
        lat : float
        frirriauto : float
        hdd_id : float array
        state_surf : float array
        soilstore_surf : float array
        soilstorecap_surf : float array
        h_maintain : float
        ie_a : float array
        ie_m : float array
        ie_start : int
        ie_end : int
        daywatper : float array
        	of houses following daily water
        
        daywat : float array
        wuday_id : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__update_wateruse(id=id, \
            waterusemethod=waterusemethod, dayofweek_id=dayofweek_id, lat=lat, \
            frirriauto=frirriauto, hdd_id=hdd_id, state_surf=state_surf, \
            soilstore_surf=soilstore_surf, soilstorecap_surf=soilstorecap_surf, \
            h_maintain=h_maintain, ie_a=ie_a, ie_m=ie_m, ie_start=ie_start, \
            ie_end=ie_end, daywatper=daywatper, daywat=daywat, wuday_id=wuday_id)
    
    @staticmethod
    def update_hdd(dt_since_start, it, imin, tstep, hdd_id):
        """
        update_hdd(dt_since_start, it, imin, tstep, hdd_id)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 1054-1080
        
        Parameters
        ----------
        dt_since_start : int
        it : int
        imin : int
        tstep : int
        hdd_id : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__update_hdd(dt_since_start=dt_since_start, \
            it=it, imin=imin, tstep=tstep, hdd_id=hdd_id)
    
    @staticmethod
    def update_dailystate_start(it, imin, hdd_id):
        """
        update_dailystate_start(it, imin, hdd_id)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 1082-1101
        
        Parameters
        ----------
        it : int
        imin : int
        hdd_id : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__update_dailystate_start(it=it, \
            imin=imin, hdd_id=hdd_id)
    
    @staticmethod
    def suews_update_dailystate(id, datetimeline, gridiv, numberofgrids, \
        dailystateline, dataoutdailystate):
        """
        suews_update_dailystate(id, datetimeline, gridiv, numberofgrids, dailystateline, \
            dataoutdailystate)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 1103-1117
        
        Parameters
        ----------
        id : int
        datetimeline : float array
        gridiv : int
        numberofgrids : int
        dailystateline : float array
        dataoutdailystate : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__suews_update_dailystate(id=id, \
            datetimeline=datetimeline, gridiv=gridiv, numberofgrids=numberofgrids, \
            dailystateline=dailystateline, dataoutdailystate=dataoutdailystate)
    
    @staticmethod
    def update_dailystateline_dts(self, config, forcing, siteinfo, modstate, \
        dailystateline):
        """
        update_dailystateline_dts(self, config, forcing, siteinfo, modstate, \
            dailystateline)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_dailystate.fpp \
            lines 1123-1190
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        dailystateline : float array
        
        """
        _supy_driver.f90wrap_dailystate_module__update_dailystateline_dts(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, dailystateline=dailystateline)
    
    _dt_array_initialisers = []
    

dailystate_module = Dailystate_Module()

class Evap_Module(f90wrap.runtime.FortranModule):
    """
    Module evap_module
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_evap.fpp \
        lines 5-147
    
    """
    @staticmethod
    def cal_evap(evapmethod, state_is, wetthresh_is, capstore_is, vpd_hpa, avdens, \
        avcp, qn_e, s_hpa, psyc_hpa, rs, ra, rb, tlv):
        """
        rss, ev, qe = cal_evap(evapmethod, state_is, wetthresh_is, capstore_is, vpd_hpa, \
            avdens, avcp, qn_e, s_hpa, psyc_hpa, rs, ra, rb, tlv)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_evap.fpp \
            lines 11-107
        
        Parameters
        ----------
        evapmethod : int
        state_is : float
        wetthresh_is : float
        capstore_is : float
        vpd_hpa : float
        avdens : float
        avcp : float
        qn_e : float
        s_hpa : float
        psyc_hpa : float
        rs : float
        ra : float
        rb : float
        tlv : float
        
        Returns
        -------
        rss : float
        ev : float
        qe : float
        
        ------------------------------------------------------------------------------
        -Calculates evaporation for each surface from modified Penman-Monteith eqn
        -State determines whether each surface type is dry or wet(wet/transition)
        -Wet surfaces below storage capacity are in transition
         and QE depends on the state and storage capacity(i.e. varies with surface);
         for wet or dry surfaces QE does not vary between surface types
        -See Sect 2.4 of Jarvi et al. (2011) Ja11
        Last modified:
          HCW 06 Jul 2016
           Moved rss declaration to LUMPS_Module_Constants so it can be written out
          HCW 11 Jun 2015
           Added WetThresh to distinguish wet/partially wet surfaces from the storage \
               capacities used in SUEWS_drain
          HCW 30 Jan 2015
           Removed StorCap input because it is provided by module allocateArray
           Tidied and commented code
          LJ 10/2010
        ------------------------------------------------------------------------------
        """
        rss, ev, qe = _supy_driver.f90wrap_evap_module__cal_evap(evapmethod=evapmethod, \
            state_is=state_is, wetthresh_is=wetthresh_is, capstore_is=capstore_is, \
            vpd_hpa=vpd_hpa, avdens=avdens, avcp=avcp, qn_e=qn_e, s_hpa=s_hpa, \
            psyc_hpa=psyc_hpa, rs=rs, ra=ra, rb=rb, tlv=tlv)
        return rss, ev, qe
    
    @staticmethod
    def cal_evap_multi(evapmethod, sfr_multi, state_multi, wetthresh_multi, \
        capstore_multi, vpd_hpa, avdens, avcp, qn_e_multi, s_hpa, psyc_hpa, rs, ra, \
        rb, tlv, rss_multi, ev_multi, qe_multi):
        """
        cal_evap_multi(evapmethod, sfr_multi, state_multi, wetthresh_multi, \
            capstore_multi, vpd_hpa, avdens, avcp, qn_e_multi, s_hpa, psyc_hpa, rs, ra, \
            rb, tlv, rss_multi, ev_multi, qe_multi)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_evap.fpp \
            lines 109-147
        
        Parameters
        ----------
        evapmethod : int
        sfr_multi : float array
        state_multi : float array
        wetthresh_multi : float array
        capstore_multi : float array
        vpd_hpa : float
        avdens : float
        avcp : float
        qn_e_multi : float array
        s_hpa : float
        psyc_hpa : float
        rs : float
        ra : float
        rb : float
        tlv : float
        rss_multi : float array
        ev_multi : float array
        qe_multi : float array
        
        """
        _supy_driver.f90wrap_evap_module__cal_evap_multi(evapmethod=evapmethod, \
            sfr_multi=sfr_multi, state_multi=state_multi, \
            wetthresh_multi=wetthresh_multi, capstore_multi=capstore_multi, \
            vpd_hpa=vpd_hpa, avdens=avdens, avcp=avcp, qn_e_multi=qn_e_multi, \
            s_hpa=s_hpa, psyc_hpa=psyc_hpa, rs=rs, ra=ra, rb=rb, tlv=tlv, \
            rss_multi=rss_multi, ev_multi=ev_multi, qe_multi=qe_multi)
    
    _dt_array_initialisers = []
    

evap_module = Evap_Module()

class Narp_Module(f90wrap.runtime.FortranModule):
    """
    Module narp_module
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
        lines 5-1383
    
    """
    @staticmethod
    def radmethod(netradiationmethod, snowuse):
        """
        netradiationmethod_use, albedochoice, ldown_option = \
            radmethod(netradiationmethod, snowuse)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 48-110
        
        Parameters
        ----------
        netradiationmethod : int
        snowuse : int
        
        Returns
        -------
        netradiationmethod_use : int
        albedochoice : int
        ldown_option : int
        
        """
        netradiationmethod_use, albedochoice, ldown_option = \
            _supy_driver.f90wrap_narp_module__radmethod(netradiationmethod=netradiationmethod, \
            snowuse=snowuse)
        return netradiationmethod_use, albedochoice, ldown_option
    
    @staticmethod
    def narp(nsurf, sfr_surf, tsfc_surf, snowfrac, alb, emis, icefrac, \
        narp_trans_site, narp_emis_snow, dtime, zenith_deg, kdown, temp_c, rh, \
        press_hpa, qn1_obs, ldown_obs, snowalb, albedochoice, ldown_option, \
        netradiationmethod_use, diagqn, qn_surf, qn1_ind_snow, kup_ind_snow, \
        tsurf_ind_snow, tsurf_surf):
        """
        qstarall, qstar_sf, qstar_s, kclear, kupall, ldown, lupall, fcld, tsurfall, \
            albedo_snowfree = narp(nsurf, sfr_surf, tsfc_surf, snowfrac, alb, emis, \
            icefrac, narp_trans_site, narp_emis_snow, dtime, zenith_deg, kdown, temp_c, \
            rh, press_hpa, qn1_obs, ldown_obs, snowalb, albedochoice, ldown_option, \
            netradiationmethod_use, diagqn, qn_surf, qn1_ind_snow, kup_ind_snow, \
            tsurf_ind_snow, tsurf_surf)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 123-459
        
        Parameters
        ----------
        nsurf : int
        sfr_surf : float array
        tsfc_surf : float array
        snowfrac : float array
        alb : float array
        emis : float array
        icefrac : float array
        narp_trans_site : float
        narp_emis_snow : float
        dtime : float
        zenith_deg : float
        kdown : float
        temp_c : float
        rh : float
        press_hpa : float
        qn1_obs : float
        ldown_obs : float
        snowalb : float
        albedochoice : int
        ldown_option : int
        netradiationmethod_use : int
        diagqn : int
        qn_surf : float array
        qn1_ind_snow : float array
        kup_ind_snow : float array
        tsurf_ind_snow : float array
        tsurf_surf : float array
        
        Returns
        -------
        qstarall : float
        qstar_sf : float
        qstar_s : float
        kclear : float
        kupall : float
        ldown : float
        lupall : float
        fcld : float
        tsurfall : float
        albedo_snowfree : float
        
        -------------------------------------------------------------------------------
         USE allocateArray
         use gis_data
         use data_in
         Included 20140701, FL
         use moist
         Included 20140701, FL
         use time
         Included 20140701, FL
        """
        qstarall, qstar_sf, qstar_s, kclear, kupall, ldown, lupall, fcld, tsurfall, \
            albedo_snowfree = _supy_driver.f90wrap_narp_module__narp(nsurf=nsurf, \
            sfr_surf=sfr_surf, tsfc_surf=tsfc_surf, snowfrac=snowfrac, alb=alb, \
            emis=emis, icefrac=icefrac, narp_trans_site=narp_trans_site, \
            narp_emis_snow=narp_emis_snow, dtime=dtime, zenith_deg=zenith_deg, \
            kdown=kdown, temp_c=temp_c, rh=rh, press_hpa=press_hpa, qn1_obs=qn1_obs, \
            ldown_obs=ldown_obs, snowalb=snowalb, albedochoice=albedochoice, \
            ldown_option=ldown_option, netradiationmethod_use=netradiationmethod_use, \
            diagqn=diagqn, qn_surf=qn_surf, qn1_ind_snow=qn1_ind_snow, \
            kup_ind_snow=kup_ind_snow, tsurf_ind_snow=tsurf_ind_snow, \
            tsurf_surf=tsurf_surf)
        return qstarall, qstar_sf, qstar_s, kclear, kupall, ldown, lupall, fcld, \
            tsurfall, albedo_snowfree
    
    @staticmethod
    def narp_cal_sunposition(year, idectime, utc, locationlatitude, \
        locationlongitude, locationaltitude):
        """
        sunazimuth, sunzenith = narp_cal_sunposition(year, idectime, utc, \
            locationlatitude, locationlongitude, locationaltitude)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 464-549
        
        Parameters
        ----------
        year : float
        idectime : float
        utc : float
        locationlatitude : float
        locationlongitude : float
        locationaltitude : float
        
        Returns
        -------
        sunazimuth : float
        sunzenith : float
        
        """
        sunazimuth, sunzenith = \
            _supy_driver.f90wrap_narp_module__narp_cal_sunposition(year=year, \
            idectime=idectime, utc=utc, locationlatitude=locationlatitude, \
            locationlongitude=locationlongitude, locationaltitude=locationaltitude)
        return sunazimuth, sunzenith
    
    @staticmethod
    def narp_cal_sunposition_dts(self, config, forcing, siteinfo, modstate):
        """
        narp_cal_sunposition_dts(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 551-661
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_narp_module__narp_cal_sunposition_dts(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def julian_calculation(year, month, day, hour, min_bn, sec, utc, juliancentury, \
        julianday, julianephemeris_century, julianephemeris_day, \
        julianephemeris_millenium):
        """
        julian_calculation(year, month, day, hour, min_bn, sec, utc, juliancentury, \
            julianday, julianephemeris_century, julianephemeris_day, \
            julianephemeris_millenium)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 665-722
        
        Parameters
        ----------
        year : float
        month : int
        day : int
        hour : int
        min_bn : int
        sec : float
        utc : float
        juliancentury : float
        julianday : float
        julianephemeris_century : float
        julianephemeris_day : float
        julianephemeris_millenium : float
        
        """
        _supy_driver.f90wrap_narp_module__julian_calculation(year=year, month=month, \
            day=day, hour=hour, min_bn=min_bn, sec=sec, utc=utc, \
            juliancentury=juliancentury, julianday=julianday, \
            julianephemeris_century=julianephemeris_century, \
            julianephemeris_day=julianephemeris_day, \
            julianephemeris_millenium=julianephemeris_millenium)
    
    @staticmethod
    def earth_heliocentric_position_calculation(julianephemeris_millenium, \
        earth_heliocentric_positionlatitude, earth_heliocentric_positionlongitude, \
        earth_heliocentric_positionradius):
        """
        earth_heliocentric_position_calculation(julianephemeris_millenium, \
            earth_heliocentric_positionlatitude, earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionradius)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 724-890
        
        Parameters
        ----------
        julianephemeris_millenium : float
        earth_heliocentric_positionlatitude : float
        earth_heliocentric_positionlongitude : float
        earth_heliocentric_positionradius : float
        
        """
        _supy_driver.f90wrap_narp_module__earth_heliocentric_position_calculation(julianephemeris_millenium=julianephemeris_millenium, \
            earth_heliocentric_positionlatitude=earth_heliocentric_positionlatitude, \
            earth_heliocentric_positionlongitude=earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionradius=earth_heliocentric_positionradius)
    
    @staticmethod
    def sun_geocentric_position_calculation(earth_heliocentric_positionlongitude, \
        earth_heliocentric_positionlatitude, sun_geocentric_positionlatitude, \
        sun_geocentric_positionlongitude):
        """
        sun_geocentric_position_calculation(earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionlatitude, sun_geocentric_positionlatitude, \
            sun_geocentric_positionlongitude)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 892-904
        
        Parameters
        ----------
        earth_heliocentric_positionlongitude : float
        earth_heliocentric_positionlatitude : float
        sun_geocentric_positionlatitude : float
        sun_geocentric_positionlongitude : float
        
        """
        _supy_driver.f90wrap_narp_module__sun_geocentric_position_calculation(earth_heliocentric_positionlongitude=earth_heliocentric_positionlongitude, \
            earth_heliocentric_positionlatitude=earth_heliocentric_positionlatitude, \
            sun_geocentric_positionlatitude=sun_geocentric_positionlatitude, \
            sun_geocentric_positionlongitude=sun_geocentric_positionlongitude)
    
    @staticmethod
    def nutation_calculation(julianephemeris_century, nutationlongitude, \
        nutationobliquity):
        """
        nutation_calculation(julianephemeris_century, nutationlongitude, \
            nutationobliquity)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 906-1010
        
        Parameters
        ----------
        julianephemeris_century : float
        nutationlongitude : float
        nutationobliquity : float
        
        """
        _supy_driver.f90wrap_narp_module__nutation_calculation(julianephemeris_century=julianephemeris_century, \
            nutationlongitude=nutationlongitude, nutationobliquity=nutationobliquity)
    
    @staticmethod
    def corr_obliquity_calculation(julianephemeris_millenium, nutationobliquity):
        """
        corr_obliquity = corr_obliquity_calculation(julianephemeris_millenium, \
            nutationobliquity)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1012-1027
        
        Parameters
        ----------
        julianephemeris_millenium : float
        nutationobliquity : float
        
        Returns
        -------
        corr_obliquity : float
        
        """
        corr_obliquity = \
            _supy_driver.f90wrap_narp_module__corr_obliquity_calculation(julianephemeris_millenium=julianephemeris_millenium, \
            nutationobliquity=nutationobliquity)
        return corr_obliquity
    
    @staticmethod
    def abberation_correction_calculation(earth_heliocentric_positionradius):
        """
        aberration_correction = \
            abberation_correction_calculation(earth_heliocentric_positionradius)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1029-1036
        
        Parameters
        ----------
        earth_heliocentric_positionradius : float
        
        Returns
        -------
        aberration_correction : float
        
        """
        aberration_correction = \
            _supy_driver.f90wrap_narp_module__abberation_correction_calculation(earth_heliocentric_positionradius=earth_heliocentric_positionradius)
        return aberration_correction
    
    @staticmethod
    def apparent_sun_longitude_calculation(sun_geocentric_positionlongitude, \
        nutationlongitude, aberration_correction):
        """
        apparent_sun_longitude = \
            apparent_sun_longitude_calculation(sun_geocentric_positionlongitude, \
            nutationlongitude, aberration_correction)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1038-1046
        
        Parameters
        ----------
        sun_geocentric_positionlongitude : float
        nutationlongitude : float
        aberration_correction : float
        
        Returns
        -------
        apparent_sun_longitude : float
        
        """
        apparent_sun_longitude = \
            _supy_driver.f90wrap_narp_module__apparent_sun_longitude_calculation(sun_geocentric_positionlongitude=sun_geocentric_positionlongitude, \
            nutationlongitude=nutationlongitude, \
            aberration_correction=aberration_correction)
        return apparent_sun_longitude
    
    @staticmethod
    def apparent_stime_at_greenwich_calculation(julianday, juliancentury, \
        nutationlongitude, corr_obliquity):
        """
        apparent_stime_at_greenwich = apparent_stime_at_greenwich_calculation(julianday, \
            juliancentury, nutationlongitude, corr_obliquity)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1048-1067
        
        Parameters
        ----------
        julianday : float
        juliancentury : float
        nutationlongitude : float
        corr_obliquity : float
        
        Returns
        -------
        apparent_stime_at_greenwich : float
        
        """
        apparent_stime_at_greenwich = \
            _supy_driver.f90wrap_narp_module__apparent_stime_at_greenwich_calculation(julianday=julianday, \
            juliancentury=juliancentury, nutationlongitude=nutationlongitude, \
            corr_obliquity=corr_obliquity)
        return apparent_stime_at_greenwich
    
    @staticmethod
    def sun_rigth_ascension_calculation(apparent_sun_longitude, corr_obliquity, \
        sun_geocentric_positionlatitude):
        """
        sun_rigth_ascension = sun_rigth_ascension_calculation(apparent_sun_longitude, \
            corr_obliquity, sun_geocentric_positionlatitude)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1069-1085
        
        Parameters
        ----------
        apparent_sun_longitude : float
        corr_obliquity : float
        sun_geocentric_positionlatitude : float
        
        Returns
        -------
        sun_rigth_ascension : float
        
        """
        sun_rigth_ascension = \
            _supy_driver.f90wrap_narp_module__sun_rigth_ascension_calculation(apparent_sun_longitude=apparent_sun_longitude, \
            corr_obliquity=corr_obliquity, \
            sun_geocentric_positionlatitude=sun_geocentric_positionlatitude)
        return sun_rigth_ascension
    
    @staticmethod
    def sun_geocentric_declination_calculation(apparent_sun_longitude, \
        corr_obliquity, sun_geocentric_positionlatitude):
        """
        sun_geocentric_declination = \
            sun_geocentric_declination_calculation(apparent_sun_longitude, \
            corr_obliquity, sun_geocentric_positionlatitude)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1087-1098
        
        Parameters
        ----------
        apparent_sun_longitude : float
        corr_obliquity : float
        sun_geocentric_positionlatitude : float
        
        Returns
        -------
        sun_geocentric_declination : float
        
        """
        sun_geocentric_declination = \
            _supy_driver.f90wrap_narp_module__sun_geocentric_declination_calculation(apparent_sun_longitude=apparent_sun_longitude, \
            corr_obliquity=corr_obliquity, \
            sun_geocentric_positionlatitude=sun_geocentric_positionlatitude)
        return sun_geocentric_declination
    
    @staticmethod
    def observer_local_hour_calculation(apparent_stime_at_greenwich, \
        locationlongitude, sun_rigth_ascension):
        """
        observer_local_hour = \
            observer_local_hour_calculation(apparent_stime_at_greenwich, \
            locationlongitude, sun_rigth_ascension)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1100-1111
        
        Parameters
        ----------
        apparent_stime_at_greenwich : float
        locationlongitude : float
        sun_rigth_ascension : float
        
        Returns
        -------
        observer_local_hour : float
        
        """
        observer_local_hour = \
            _supy_driver.f90wrap_narp_module__observer_local_hour_calculation(apparent_stime_at_greenwich=apparent_stime_at_greenwich, \
            locationlongitude=locationlongitude, \
            sun_rigth_ascension=sun_rigth_ascension)
        return observer_local_hour
    
    @staticmethod
    def topocentric_sun_position_calculate(topocentric_sun_positionrigth_ascension, \
        topocentric_sun_positionrigth_ascension_parallax, \
        topocentric_sun_positiondeclination, locationaltitude, locationlatitude, \
        observer_local_hour, sun_rigth_ascension, sun_geocentric_declination, \
        earth_heliocentric_positionradius):
        """
        topocentric_sun_position_calculate(topocentric_sun_positionrigth_ascension, \
            topocentric_sun_positionrigth_ascension_parallax, \
            topocentric_sun_positiondeclination, locationaltitude, locationlatitude, \
            observer_local_hour, sun_rigth_ascension, sun_geocentric_declination, \
            earth_heliocentric_positionradius)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1113-1158
        
        Parameters
        ----------
        topocentric_sun_positionrigth_ascension : float
        topocentric_sun_positionrigth_ascension_parallax : float
        topocentric_sun_positiondeclination : float
        locationaltitude : float
        locationlatitude : float
        observer_local_hour : float
        sun_rigth_ascension : float
        sun_geocentric_declination : float
        earth_heliocentric_positionradius : float
        
        """
        _supy_driver.f90wrap_narp_module__topocentric_sun_position_calculate(topocentric_sun_positionrigth_ascension=topocentric_sun_positionrigth_ascension, \
            topocentric_sun_positionrigth_ascension_parallax=topocentric_sun_positionrigth_ascension_parallax, \
            topocentric_sun_positiondeclination=topocentric_sun_positiondeclination, \
            locationaltitude=locationaltitude, locationlatitude=locationlatitude, \
            observer_local_hour=observer_local_hour, \
            sun_rigth_ascension=sun_rigth_ascension, \
            sun_geocentric_declination=sun_geocentric_declination, \
            earth_heliocentric_positionradius=earth_heliocentric_positionradius)
    
    @staticmethod
    def topocentric_local_hour_calculate(observer_local_hour, \
        topocentric_sun_positionrigth_ascension_parallax):
        """
        topocentric_local_hour = topocentric_local_hour_calculate(observer_local_hour, \
            topocentric_sun_positionrigth_ascension_parallax)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1160-1167
        
        Parameters
        ----------
        observer_local_hour : float
        topocentric_sun_positionrigth_ascension_parallax : float
        
        Returns
        -------
        topocentric_local_hour : float
        
        """
        topocentric_local_hour = \
            _supy_driver.f90wrap_narp_module__topocentric_local_hour_calculate(observer_local_hour=observer_local_hour, \
            topocentric_sun_positionrigth_ascension_parallax=topocentric_sun_positionrigth_ascension_parallax)
        return topocentric_local_hour
    
    @staticmethod
    def sun_topocentric_zenith_angle_calculate(locationlatitude, \
        topocentric_sun_positiondeclination, topocentric_local_hour, sunazimuth, \
        sunzenith):
        """
        sun_topocentric_zenith_angle_calculate(locationlatitude, \
            topocentric_sun_positiondeclination, topocentric_local_hour, sunazimuth, \
            sunzenith)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1169-1208
        
        Parameters
        ----------
        locationlatitude : float
        topocentric_sun_positiondeclination : float
        topocentric_local_hour : float
        sunazimuth : float
        sunzenith : float
        
        """
        _supy_driver.f90wrap_narp_module__sun_topocentric_zenith_angle_calculate(locationlatitude=locationlatitude, \
            topocentric_sun_positiondeclination=topocentric_sun_positiondeclination, \
            topocentric_local_hour=topocentric_local_hour, sunazimuth=sunazimuth, \
            sunzenith=sunzenith)
    
    @staticmethod
    def set_to_range(var):
        """
        vari = set_to_range(var)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1210-1222
        
        Parameters
        ----------
        var : float
        
        Returns
        -------
        vari : float
        
        """
        vari = _supy_driver.f90wrap_narp_module__set_to_range(var=var)
        return vari
    
    @staticmethod
    def dewpoint_narp(temp_c, rh):
        """
        td = dewpoint_narp(temp_c, rh)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1225-1235
        
        Parameters
        ----------
        temp_c : float
        rh : float
        
        Returns
        -------
        td : float
        
        """
        td = _supy_driver.f90wrap_narp_module__dewpoint_narp(temp_c=temp_c, rh=rh)
        return td
    
    @staticmethod
    def prata_emis(temp_k, ea_hpa):
        """
        emis_a = prata_emis(temp_k, ea_hpa)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1238-1243
        
        Parameters
        ----------
        temp_k : float
        ea_hpa : float
        
        Returns
        -------
        emis_a : float
        
        """
        emis_a = _supy_driver.f90wrap_narp_module__prata_emis(temp_k=temp_k, \
            ea_hpa=ea_hpa)
        return emis_a
    
    @staticmethod
    def emis_cloud(emis_a, fcld):
        """
        em_adj = emis_cloud(emis_a, fcld)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1246-1251
        
        Parameters
        ----------
        emis_a : float
        fcld : float
        
        Returns
        -------
        em_adj : float
        
        """
        em_adj = _supy_driver.f90wrap_narp_module__emis_cloud(emis_a=emis_a, fcld=fcld)
        return em_adj
    
    @staticmethod
    def emis_cloud_sq(emis_a, fcld):
        """
        em_adj = emis_cloud_sq(emis_a, fcld)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1254-1257
        
        Parameters
        ----------
        emis_a : float
        fcld : float
        
        Returns
        -------
        em_adj : float
        
        """
        em_adj = _supy_driver.f90wrap_narp_module__emis_cloud_sq(emis_a=emis_a, \
            fcld=fcld)
        return em_adj
    
    @staticmethod
    def cloud_fraction(kdown, kclear):
        """
        fcld = cloud_fraction(kdown, kclear)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1260-1264
        
        Parameters
        ----------
        kdown : float
        kclear : float
        
        Returns
        -------
        fcld : float
        
        """
        fcld = _supy_driver.f90wrap_narp_module__cloud_fraction(kdown=kdown, \
            kclear=kclear)
        return fcld
    
    @staticmethod
    def wc_fraction(rh, temp):
        """
        fwc = wc_fraction(rh, temp)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1267-1282
        
        Parameters
        ----------
        rh : float
        temp : float
        
        Returns
        -------
        fwc : float
        
        """
        fwc = _supy_driver.f90wrap_narp_module__wc_fraction(rh=rh, temp=temp)
        return fwc
    
    @staticmethod
    def isurface(doy, zenith):
        """
        isurf = isurface(doy, zenith)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1305-1321
        
        Parameters
        ----------
        doy : int
        zenith : float
        
        Returns
        -------
        isurf : float
        
        """
        isurf = _supy_driver.f90wrap_narp_module__isurface(doy=doy, zenith=zenith)
        return isurf
    
    @staticmethod
    def solar_esdist(doy):
        """
        rse = solar_esdist(doy)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1324-1333
        
        Parameters
        ----------
        doy : int
        
        Returns
        -------
        rse : float
        
        """
        rse = _supy_driver.f90wrap_narp_module__solar_esdist(doy=doy)
        return rse
    
    @staticmethod
    def smithlambda(lat):
        """
        g = smithlambda(lat)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1336-1355
        
        Parameters
        ----------
        lat : int
        
        Returns
        -------
        g : float array
        
        """
        g = _supy_driver.f90wrap_narp_module__smithlambda(lat=lat)
        return g
    
    @staticmethod
    def transmissivity(press_hpa, temp_c_dew, g, zenith):
        """
        trans = transmissivity(press_hpa, temp_c_dew, g, zenith)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_narp.fpp \
            lines 1358-1382
        
        Parameters
        ----------
        press_hpa : float
        temp_c_dew : float
        g : float
        zenith : float
        
        Returns
        -------
        trans : float
        
        """
        trans = _supy_driver.f90wrap_narp_module__transmissivity(press_hpa=press_hpa, \
            temp_c_dew=temp_c_dew, g=g, zenith=zenith)
        return trans
    
    _dt_array_initialisers = []
    

narp_module = Narp_Module()

class Resist_Module(f90wrap.runtime.FortranModule):
    """
    Module resist_module
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
        lines 5-639
    
    """
    @staticmethod
    def aerodynamicresistance(zzd, z0m, avu1, l_mod, ustar, vegfraction, \
        aerodynamicresistancemethod, stabilitymethod, roughlenheatmethod):
        """
        ra_h, z0v = aerodynamicresistance(zzd, z0m, avu1, l_mod, ustar, vegfraction, \
            aerodynamicresistancemethod, stabilitymethod, roughlenheatmethod)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
            lines 18-101
        
        Parameters
        ----------
        zzd : float
        z0m : float
        avu1 : float
        l_mod : float
        ustar : float
        vegfraction : float
        aerodynamicresistancemethod : int
        stabilitymethod : int
        roughlenheatmethod : int
        
        Returns
        -------
        ra_h : float
        z0v : float
        
        """
        ra_h, z0v = _supy_driver.f90wrap_resist_module__aerodynamicresistance(zzd=zzd, \
            z0m=z0m, avu1=avu1, l_mod=l_mod, ustar=ustar, vegfraction=vegfraction, \
            aerodynamicresistancemethod=aerodynamicresistancemethod, \
            stabilitymethod=stabilitymethod, roughlenheatmethod=roughlenheatmethod)
        return ra_h, z0v
    
    @staticmethod
    def surfaceresistance(id, it, smdmethod, snowfrac, sfr_surf, avkdn, tair, dq, \
        xsmd, vsmd, maxconductance, laimax, lai_id, gsmodel, kmax, g_max, g_k, \
        g_q_base, g_q_shape, g_t, g_sm, th, tl, s1, s2):
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, gfunc, gsc, rs = surfaceresistance(id, it, \
            smdmethod, snowfrac, sfr_surf, avkdn, tair, dq, xsmd, vsmd, maxconductance, \
            laimax, lai_id, gsmodel, kmax, g_max, g_k, g_q_base, g_q_shape, g_t, g_sm, \
            th, tl, s1, s2)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
            lines 103-372
        
        Parameters
        ----------
        id : int
        it : int
        smdmethod : int
        snowfrac : float array
        sfr_surf : float array
        avkdn : float
        tair : float
        dq : float
        xsmd : float
        vsmd : float
        maxconductance : float array
        laimax : float array
        lai_id : float array
        gsmodel : int
        kmax : float
        g_max : float
        g_k : float
        g_q_base : float
        g_q_shape : float
        g_t : float
        g_sm : float
        th : float
        tl : float
        s1 : float
        s2 : float
        
        Returns
        -------
        g_kdown : float
        g_dq : float
        g_ta : float
        g_smd : float
        g_lai : float
        gfunc : float
        gsc : float
        rs : float
        
        """
        g_kdown, g_dq, g_ta, g_smd, g_lai, gfunc, gsc, rs = \
            _supy_driver.f90wrap_resist_module__surfaceresistance(id=id, it=it, \
            smdmethod=smdmethod, snowfrac=snowfrac, sfr_surf=sfr_surf, avkdn=avkdn, \
            tair=tair, dq=dq, xsmd=xsmd, vsmd=vsmd, maxconductance=maxconductance, \
            laimax=laimax, lai_id=lai_id, gsmodel=gsmodel, kmax=kmax, g_max=g_max, \
            g_k=g_k, g_q_base=g_q_base, g_q_shape=g_q_shape, g_t=g_t, g_sm=g_sm, th=th, \
            tl=tl, s1=s1, s2=s2)
        return g_kdown, g_dq, g_ta, g_smd, g_lai, gfunc, gsc, rs
    
    @staticmethod
    def boundarylayerresistance(zzd, z0m, avu1, ustar):
        """
        rb = boundarylayerresistance(zzd, z0m, avu1, ustar)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
            lines 374-388
        
        Parameters
        ----------
        zzd : float
        z0m : float
        avu1 : float
        ustar : float
        
        Returns
        -------
        rb : float
        
        """
        rb = _supy_driver.f90wrap_resist_module__boundarylayerresistance(zzd=zzd, \
            z0m=z0m, avu1=avu1, ustar=ustar)
        return rb
    
    @staticmethod
    def suews_cal_roughnessparameters(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_roughnessparameters(self, config, forcing, siteinfo, modstate)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
            lines 390-600
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        --------------------------------------------------------------------------------
        """
        _supy_driver.f90wrap_resist_module__suews_cal_roughnessparameters(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def cal_z0v(roughlenheatmethod, z0m, vegfraction, ustar):
        """
        z0v = cal_z0v(roughlenheatmethod, z0m, vegfraction, ustar)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
            lines 602-633
        
        Parameters
        ----------
        roughlenheatmethod : int
        z0m : float
        vegfraction : float
        ustar : float
        
        Returns
        -------
        z0v : float
        
        """
        z0v = \
            _supy_driver.f90wrap_resist_module__cal_z0v(roughlenheatmethod=roughlenheatmethod, \
            z0m=z0m, vegfraction=vegfraction, ustar=ustar)
        return z0v
    
    @staticmethod
    def sigmoid(x):
        """
        res = sigmoid(x)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_resist.fpp \
            lines 635-639
        
        Parameters
        ----------
        x : float
        
        Returns
        -------
        res : float
        
        """
        res = _supy_driver.f90wrap_resist_module__sigmoid(x=x)
        return res
    
    _dt_array_initialisers = []
    

resist_module = Resist_Module()

class Rsl_Module(f90wrap.runtime.FortranModule):
    """
    Module rsl_module
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
        lines 5-1863
    
    """
    @staticmethod
    def rslprofile(diagmethod, zh, z0m, zdm, z0v, l_mod, sfr_surf, fai, pai, \
        stabilitymethod, ra_h, avcp, lv_j_kg, avdens, avu1, temp_c, avrh, press_hpa, \
        zmeas, qh, qe, dataoutlinersl):
        """
        t2_c, q2_gkg, u10_ms, rh2 = rslprofile(diagmethod, zh, z0m, zdm, z0v, l_mod, \
            sfr_surf, fai, pai, stabilitymethod, ra_h, avcp, lv_j_kg, avdens, avu1, \
            temp_c, avrh, press_hpa, zmeas, qh, qe, dataoutlinersl)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 22-276
        
        Parameters
        ----------
        diagmethod : int
        zh : float
        z0m : float
        zdm : float
        z0v : float
        l_mod : float
        sfr_surf : float array
        fai : float
        pai : float
        stabilitymethod : int
        ra_h : float
        avcp : float
        lv_j_kg : float
        avdens : float
        avu1 : float
        temp_c : float
        avrh : float
        press_hpa : float
        zmeas : float
        qh : float
        qe : float
        dataoutlinersl : float array
        
        Returns
        -------
        t2_c : float
        q2_gkg : float
        u10_ms : float
        rh2 : float
        
        -----------------------------------------------------
         calculates windprofiles using MOST with a RSL-correction
         based on Harman & Finnigan 2007
         last modified by:
         NT 16 Mar 2019: initial version
         TS 16 Oct 2019: improved consistency in parameters/varaibles within SUEWS
         TODO how to improve the speed of this code
        -----------------------------------------------------
        """
        t2_c, q2_gkg, u10_ms, rh2 = \
            _supy_driver.f90wrap_rsl_module__rslprofile(diagmethod=diagmethod, zh=zh, \
            z0m=z0m, zdm=zdm, z0v=z0v, l_mod=l_mod, sfr_surf=sfr_surf, fai=fai, pai=pai, \
            stabilitymethod=stabilitymethod, ra_h=ra_h, avcp=avcp, lv_j_kg=lv_j_kg, \
            avdens=avdens, avu1=avu1, temp_c=temp_c, avrh=avrh, press_hpa=press_hpa, \
            zmeas=zmeas, qh=qh, qe=qe, dataoutlinersl=dataoutlinersl)
        return t2_c, q2_gkg, u10_ms, rh2
    
    @staticmethod
    def cal_profile_most(stabilitymethod, nz, zmeas, zdm, z0m, z0v, l_mod, avu1, \
        temp_c, tstar, qstar, qa_gkg, zarray, dataoutlineursl, dataoutlinetrsl, \
        dataoutlineqrsl):
        """
        cal_profile_most(stabilitymethod, nz, zmeas, zdm, z0m, z0v, l_mod, avu1, temp_c, \
            tstar, qstar, qa_gkg, zarray, dataoutlineursl, dataoutlinetrsl, \
            dataoutlineqrsl)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 278-321
        
        Parameters
        ----------
        stabilitymethod : int
        nz : int
        zmeas : float
        zdm : float
        z0m : float
        z0v : float
        l_mod : float
        avu1 : float
        temp_c : float
        tstar : float
        qstar : float
        qa_gkg : float
        zarray : float array
        dataoutlineursl : float array
        dataoutlinetrsl : float array
        dataoutlineqrsl : float array
        
        """
        _supy_driver.f90wrap_rsl_module__cal_profile_most(stabilitymethod=stabilitymethod, \
            nz=nz, zmeas=zmeas, zdm=zdm, z0m=z0m, z0v=z0v, l_mod=l_mod, avu1=avu1, \
            temp_c=temp_c, tstar=tstar, qstar=qstar, qa_gkg=qa_gkg, zarray=zarray, \
            dataoutlineursl=dataoutlineursl, dataoutlinetrsl=dataoutlinetrsl, \
            dataoutlineqrsl=dataoutlineqrsl)
    
    @staticmethod
    def cal_profile_rsl(stabilitymethod, nz, nz_can, zmeas, zh_rsl, l_mod_rsl, \
        zd_rsl, z0_rsl, beta, elm, scc, fx, temp_c, ustar_rsl, tstar_rsl, qstar_rsl, \
        qa_gkg, psihatm_z, psihath_z, zarray, dataoutlineursl, dataoutlinetrsl, \
        dataoutlineqrsl):
        """
        cal_profile_rsl(stabilitymethod, nz, nz_can, zmeas, zh_rsl, l_mod_rsl, zd_rsl, \
            z0_rsl, beta, elm, scc, fx, temp_c, ustar_rsl, tstar_rsl, qstar_rsl, qa_gkg, \
            psihatm_z, psihath_z, zarray, dataoutlineursl, dataoutlinetrsl, \
            dataoutlineqrsl)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 323-370
        
        Parameters
        ----------
        stabilitymethod : int
        nz : int
        nz_can : int
        zmeas : float
        zh_rsl : float
        l_mod_rsl : float
        zd_rsl : float
        z0_rsl : float
        beta : float
        elm : float
        scc : float
        fx : float
        temp_c : float
        ustar_rsl : float
        tstar_rsl : float
        qstar_rsl : float
        qa_gkg : float
        psihatm_z : float array
        psihath_z : float array
        zarray : float array
        dataoutlineursl : float array
        dataoutlinetrsl : float array
        dataoutlineqrsl : float array
        
        """
        _supy_driver.f90wrap_rsl_module__cal_profile_rsl(stabilitymethod=stabilitymethod, \
            nz=nz, nz_can=nz_can, zmeas=zmeas, zh_rsl=zh_rsl, l_mod_rsl=l_mod_rsl, \
            zd_rsl=zd_rsl, z0_rsl=z0_rsl, beta=beta, elm=elm, scc=scc, fx=fx, \
            temp_c=temp_c, ustar_rsl=ustar_rsl, tstar_rsl=tstar_rsl, \
            qstar_rsl=qstar_rsl, qa_gkg=qa_gkg, psihatm_z=psihatm_z, \
            psihath_z=psihath_z, zarray=zarray, dataoutlineursl=dataoutlineursl, \
            dataoutlinetrsl=dataoutlinetrsl, dataoutlineqrsl=dataoutlineqrsl)
    
    @staticmethod
    def setup_most_heights(nz, zdm, z0m, zmeas, zarray):
        """
        setup_most_heights(nz, zdm, z0m, zmeas, zarray)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 372-419
        
        Parameters
        ----------
        nz : int
        zdm : float
        z0m : float
        zmeas : float
        zarray : float array
        
        """
        _supy_driver.f90wrap_rsl_module__setup_most_heights(nz=nz, zdm=zdm, z0m=z0m, \
            zmeas=zmeas, zarray=zarray)
    
    @staticmethod
    def setup_rsl_heights(nz, nz_can, zh_rsl, zmeas, zarray):
        """
        setup_rsl_heights(nz, nz_can, zh_rsl, zmeas, zarray)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 421-453
        
        Parameters
        ----------
        nz : int
        nz_can : int
        zh_rsl : float
        zmeas : float
        zarray : float array
        
        """
        _supy_driver.f90wrap_rsl_module__setup_rsl_heights(nz=nz, nz_can=nz_can, \
            zh_rsl=zh_rsl, zmeas=zmeas, zarray=zarray)
    
    @staticmethod
    def rslprofile_dts(self, config, forcing, siteinfo, modstate, dataoutlineursl, \
        dataoutlinetrsl, dataoutlineqrsl, dataoutlinersl):
        """
        rslprofile_dts(self, config, forcing, siteinfo, modstate, dataoutlineursl, \
            dataoutlinetrsl, dataoutlineqrsl, dataoutlinersl)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 785-1151
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        dataoutlineursl : float array
        dataoutlinetrsl : float array
        dataoutlineqrsl : float array
        dataoutlinersl : float array
        
        -----------------------------------------------------
         calculates windprofiles using MOST with a RSL-correction
         based on Harman & Finnigan 2007
         last modified by:
         NT 16 Mar 2019: initial version
         TS 16 Oct 2019: improved consistency in parameters/varaibles within SUEWS
         TODO how to improve the speed of this code
        -----------------------------------------------------
        """
        _supy_driver.f90wrap_rsl_module__rslprofile_dts(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle, dataoutlineursl=dataoutlineursl, \
            dataoutlinetrsl=dataoutlinetrsl, dataoutlineqrsl=dataoutlineqrsl, \
            dataoutlinersl=dataoutlinersl)
    
    @staticmethod
    def interp_z(z_x, z, v):
        """
        v_x = interp_z(z_x, z, v)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1153-1198
        
        Parameters
        ----------
        z_x : float
        z : float array
        v : float array
        
        Returns
        -------
        v_x : float
        
        """
        v_x = _supy_driver.f90wrap_rsl_module__interp_z(z_x=z_x, z=z, v=v)
        return v_x
    
    @staticmethod
    def cal_elm_rsl(beta, lc):
        """
        elm = cal_elm_rsl(beta, lc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1200-1210
        
        Parameters
        ----------
        beta : float
        lc : float
        
        Returns
        -------
        elm : float
        
        """
        elm = _supy_driver.f90wrap_rsl_module__cal_elm_rsl(beta=beta, lc=lc)
        return elm
    
    @staticmethod
    def cal_psim_hat(stabilitymethod, psihatm_top, psihatm_mid, z_top, z_mid, z_btm, \
        cm, c2, zh_rsl, zd_rsl, l_mod, beta, elm, lc):
        """
        psihatm_btm = cal_psim_hat(stabilitymethod, psihatm_top, psihatm_mid, z_top, \
            z_mid, z_btm, cm, c2, zh_rsl, zd_rsl, l_mod, beta, elm, lc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1212-1277
        
        Parameters
        ----------
        stabilitymethod : int
        psihatm_top : float
        psihatm_mid : float
        z_top : float
        z_mid : float
        z_btm : float
        cm : float
        c2 : float
        zh_rsl : float
        zd_rsl : float
        l_mod : float
        beta : float
        elm : float
        lc : float
        
        Returns
        -------
        psihatm_btm : float
        
        """
        psihatm_btm = \
            _supy_driver.f90wrap_rsl_module__cal_psim_hat(stabilitymethod=stabilitymethod, \
            psihatm_top=psihatm_top, psihatm_mid=psihatm_mid, z_top=z_top, z_mid=z_mid, \
            z_btm=z_btm, cm=cm, c2=c2, zh_rsl=zh_rsl, zd_rsl=zd_rsl, l_mod=l_mod, \
            beta=beta, elm=elm, lc=lc)
        return psihatm_btm
    
    @staticmethod
    def cal_psih_hat(stabilitymethod, psihath_top, psihath_mid, z_top, z_mid, z_btm, \
        ch, c2h, zh_rsl, zd_rsl, l_mod, beta, elm, lc):
        """
        psihath_btm = cal_psih_hat(stabilitymethod, psihath_top, psihath_mid, z_top, \
            z_mid, z_btm, ch, c2h, zh_rsl, zd_rsl, l_mod, beta, elm, lc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1279-1340
        
        Parameters
        ----------
        stabilitymethod : int
        psihath_top : float
        psihath_mid : float
        z_top : float
        z_mid : float
        z_btm : float
        ch : float
        c2h : float
        zh_rsl : float
        zd_rsl : float
        l_mod : float
        beta : float
        elm : float
        lc : float
        
        Returns
        -------
        psihath_btm : float
        
        """
        psihath_btm = \
            _supy_driver.f90wrap_rsl_module__cal_psih_hat(stabilitymethod=stabilitymethod, \
            psihath_top=psihath_top, psihath_mid=psihath_mid, z_top=z_top, z_mid=z_mid, \
            z_btm=z_btm, ch=ch, c2h=c2h, zh_rsl=zh_rsl, zd_rsl=zd_rsl, l_mod=l_mod, \
            beta=beta, elm=elm, lc=lc)
        return psihath_btm
    
    @staticmethod
    def cal_phim_hat(stabilitymethod, z, zh_rsl, l_mod, beta, lc):
        """
        phim_hat = cal_phim_hat(stabilitymethod, z, zh_rsl, l_mod, beta, lc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1342-1358
        
        Parameters
        ----------
        stabilitymethod : int
        z : float
        zh_rsl : float
        l_mod : float
        beta : float
        lc : float
        
        Returns
        -------
        phim_hat : float
        
        """
        phim_hat = \
            _supy_driver.f90wrap_rsl_module__cal_phim_hat(stabilitymethod=stabilitymethod, \
            z=z, zh_rsl=zh_rsl, l_mod=l_mod, beta=beta, lc=lc)
        return phim_hat
    
    @staticmethod
    def cal_cm(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod):
        """
        c2, cm = cal_cm(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1360-1401
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zd_rsl : float
        lc : float
        beta : float
        l_mod : float
        
        Returns
        -------
        c2 : float
        cm : float
        
        """
        c2, cm = \
            _supy_driver.f90wrap_rsl_module__cal_cm(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zd_rsl=zd_rsl, lc=lc, beta=beta, l_mod=l_mod)
        return c2, cm
    
    @staticmethod
    def cal_ch(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod, scc, f):
        """
        c2h, ch = cal_ch(stabilitymethod, zh_rsl, zd_rsl, lc, beta, l_mod, scc, f)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1403-1443
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zd_rsl : float
        lc : float
        beta : float
        l_mod : float
        scc : float
        f : float
        
        Returns
        -------
        c2h : float
        ch : float
        
        """
        c2h, ch = \
            _supy_driver.f90wrap_rsl_module__cal_ch(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zd_rsl=zd_rsl, lc=lc, beta=beta, l_mod=l_mod, scc=scc, f=f)
        return c2h, ch
    
    @staticmethod
    def cal_zd_rsl(zh_rsl, beta, lc):
        """
        zd_rsl = cal_zd_rsl(zh_rsl, beta, lc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1569-1578
        
        Parameters
        ----------
        zh_rsl : float
        beta : float
        lc : float
        
        Returns
        -------
        zd_rsl : float
        
        """
        zd_rsl = _supy_driver.f90wrap_rsl_module__cal_zd_rsl(zh_rsl=zh_rsl, beta=beta, \
            lc=lc)
        return zd_rsl
    
    @staticmethod
    def cal_z0_rsl(stabilitymethod, zh_rsl, zd_rsl, beta, l_mod_rsl, psihatm_zh):
        """
        z0_rsl = cal_z0_rsl(stabilitymethod, zh_rsl, zd_rsl, beta, l_mod_rsl, \
            psihatm_zh)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1580-1617
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zd_rsl : float
        beta : float
        l_mod_rsl : float
        psihatm_zh : float
        
        Returns
        -------
        z0_rsl : float
        
        """
        z0_rsl = \
            _supy_driver.f90wrap_rsl_module__cal_z0_rsl(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zd_rsl=zd_rsl, beta=beta, l_mod_rsl=l_mod_rsl, \
            psihatm_zh=psihatm_zh)
        return z0_rsl
    
    @staticmethod
    def rsl_cal_prms(stabilitymethod, nz_above, z_array, zh, zstd, l_mod, sfr_surf, \
        fai, pai, surfacearea, nbuildings, psihatm_array, psihath_array):
        """
        zh_rsl, l_mod_rsl, lc, beta, zd_rsl, z0_rsl, elm, scc, fx = \
            rsl_cal_prms(stabilitymethod, nz_above, z_array, zh, zstd, l_mod, sfr_surf, \
            fai, pai, surfacearea, nbuildings, psihatm_array, psihath_array)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1619-1779
        
        Parameters
        ----------
        stabilitymethod : int
        nz_above : int
        z_array : float array
        zh : float
        zstd : float
        l_mod : float
        sfr_surf : float array
        fai : float
        pai : float
        surfacearea : float
        nbuildings : float
        psihatm_array : float array
        psihath_array : float array
        
        Returns
        -------
        zh_rsl : float
        l_mod_rsl : float
        lc : float
        beta : float
        zd_rsl : float
        z0_rsl : float
        elm : float
        scc : float
        fx : float
        
        """
        zh_rsl, l_mod_rsl, lc, beta, zd_rsl, z0_rsl, elm, scc, fx = \
            _supy_driver.f90wrap_rsl_module__rsl_cal_prms(stabilitymethod=stabilitymethod, \
            nz_above=nz_above, z_array=z_array, zh=zh, zstd=zstd, l_mod=l_mod, \
            sfr_surf=sfr_surf, fai=fai, pai=pai, surfacearea=surfacearea, \
            nbuildings=nbuildings, psihatm_array=psihatm_array, \
            psihath_array=psihath_array)
        return zh_rsl, l_mod_rsl, lc, beta, zd_rsl, z0_rsl, elm, scc, fx
    
    @staticmethod
    def cal_beta_rsl(stabilitymethod, zh_rsl, zstd, fai, pai, sfr_tr, lc_over_l):
        """
        beta = cal_beta_rsl(stabilitymethod, zh_rsl, zstd, fai, pai, sfr_tr, lc_over_l)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1781-1833
        
        Parameters
        ----------
        stabilitymethod : int
        zh_rsl : float
        zstd : float
        fai : float
        pai : float
        sfr_tr : float
        lc_over_l : float
        
        Returns
        -------
        beta : float
        
        """
        beta = \
            _supy_driver.f90wrap_rsl_module__cal_beta_rsl(stabilitymethod=stabilitymethod, \
            zh_rsl=zh_rsl, zstd=zstd, fai=fai, pai=pai, sfr_tr=sfr_tr, \
            lc_over_l=lc_over_l)
        return beta
    
    @staticmethod
    def cal_beta_lc(stabilitymethod, beta0, lc_over_l):
        """
        beta_x = cal_beta_lc(stabilitymethod, beta0, lc_over_l)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            lines 1835-1862
        
        Parameters
        ----------
        stabilitymethod : int
        beta0 : float
        lc_over_l : float
        
        Returns
        -------
        beta_x : float
        
        """
        beta_x = \
            _supy_driver.f90wrap_rsl_module__cal_beta_lc(stabilitymethod=stabilitymethod, \
            beta0=beta0, lc_over_l=lc_over_l)
        return beta_x
    
    @property
    def nz(self):
        """
        Element nz ftype=integer pytype=int
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_rslprof.fpp \
            line 12
        
        """
        return _supy_driver.f90wrap_rsl_module__get__nz()
    
    def __str__(self):
        ret = ['<rsl_module>{\n']
        ret.append('    nz : ')
        ret.append(repr(self.nz))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

rsl_module = Rsl_Module()

class Spartacus_Module(f90wrap.runtime.FortranModule):
    """
    Module spartacus_module
    
    
    Defined at \
        src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_spartacus.fpp lines \
        5-622
    
    """
    @staticmethod
    def spartacus_initialise():
        """
        spartacus_initialise()
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_spartacus.fpp lines \
            45-80
        
        
        """
        _supy_driver.f90wrap_spartacus_module__spartacus_initialise()
    
    @staticmethod
    def spartacus(diagqn, sfr_surf, zenith_deg, nlayer, tsfc_surf, tsfc_roof, \
        tsfc_wall, kdown, ldown, tair_c, alb_surf, emis_surf, lai_id, \
        n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
        sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
        air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
        ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
        veg_frac, sfr_roof, sfr_wall, building_scale, veg_scale, alb_roof, \
        emis_roof, alb_wall, emis_wall, roof_albedo_dir_mult_fact, \
        wall_specular_frac, qn_roof, qn_wall, qn_surf, dataoutlinespartacus):
        """
        qn, kup, lup = spartacus(diagqn, sfr_surf, zenith_deg, nlayer, tsfc_surf, \
            tsfc_roof, tsfc_wall, kdown, ldown, tair_c, alb_surf, emis_surf, lai_id, \
            n_vegetation_region_urban, n_stream_sw_urban, n_stream_lw_urban, \
            sw_dn_direct_frac, air_ext_sw, air_ssa_sw, veg_ssa_sw, air_ext_lw, \
            air_ssa_lw, veg_ssa_lw, veg_fsd_const, veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact, use_sw_direct_albedo, height, building_frac, \
            veg_frac, sfr_roof, sfr_wall, building_scale, veg_scale, alb_roof, \
            emis_roof, alb_wall, emis_wall, roof_albedo_dir_mult_fact, \
            wall_specular_frac, qn_roof, qn_wall, qn_surf, dataoutlinespartacus)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_spartacus.fpp lines \
            82-622
        
        Parameters
        ----------
        diagqn : int
        sfr_surf : float array
        zenith_deg : float
        nlayer : int
        tsfc_surf : float array
        tsfc_roof : float array
        tsfc_wall : float array
        kdown : float
        ldown : float
        tair_c : float
        alb_surf : float array
        emis_surf : float array
        lai_id : float array
        n_vegetation_region_urban : int
        n_stream_sw_urban : int
        n_stream_lw_urban : int
        sw_dn_direct_frac : float
        air_ext_sw : float
        air_ssa_sw : float
        veg_ssa_sw : float
        air_ext_lw : float
        air_ssa_lw : float
        veg_ssa_lw : float
        veg_fsd_const : float
        veg_contact_fraction_const : float
        ground_albedo_dir_mult_fact : float
        use_sw_direct_albedo : bool
        height : float array
        building_frac : float array
        veg_frac : float array
        sfr_roof : float array
        sfr_wall : float array
        building_scale : float array
        veg_scale : float array
        alb_roof : float array
        emis_roof : float array
        alb_wall : float array
        emis_wall : float array
        roof_albedo_dir_mult_fact : float array
        wall_specular_frac : float array
        qn_roof : float array
        qn_wall : float array
        qn_surf : float array
        dataoutlinespartacus : float array
        
        Returns
        -------
        qn : float
        kup : float
        lup : float
        
        """
        qn, kup, lup = _supy_driver.f90wrap_spartacus_module__spartacus(diagqn=diagqn, \
            sfr_surf=sfr_surf, zenith_deg=zenith_deg, nlayer=nlayer, \
            tsfc_surf=tsfc_surf, tsfc_roof=tsfc_roof, tsfc_wall=tsfc_wall, kdown=kdown, \
            ldown=ldown, tair_c=tair_c, alb_surf=alb_surf, emis_surf=emis_surf, \
            lai_id=lai_id, n_vegetation_region_urban=n_vegetation_region_urban, \
            n_stream_sw_urban=n_stream_sw_urban, n_stream_lw_urban=n_stream_lw_urban, \
            sw_dn_direct_frac=sw_dn_direct_frac, air_ext_sw=air_ext_sw, \
            air_ssa_sw=air_ssa_sw, veg_ssa_sw=veg_ssa_sw, air_ext_lw=air_ext_lw, \
            air_ssa_lw=air_ssa_lw, veg_ssa_lw=veg_ssa_lw, veg_fsd_const=veg_fsd_const, \
            veg_contact_fraction_const=veg_contact_fraction_const, \
            ground_albedo_dir_mult_fact=ground_albedo_dir_mult_fact, \
            use_sw_direct_albedo=use_sw_direct_albedo, height=height, \
            building_frac=building_frac, veg_frac=veg_frac, sfr_roof=sfr_roof, \
            sfr_wall=sfr_wall, building_scale=building_scale, veg_scale=veg_scale, \
            alb_roof=alb_roof, emis_roof=emis_roof, alb_wall=alb_wall, \
            emis_wall=emis_wall, roof_albedo_dir_mult_fact=roof_albedo_dir_mult_fact, \
            wall_specular_frac=wall_specular_frac, qn_roof=qn_roof, qn_wall=qn_wall, \
            qn_surf=qn_surf, dataoutlinespartacus=dataoutlinespartacus)
        return qn, kup, lup
    
    _dt_array_initialisers = []
    

spartacus_module = Spartacus_Module()

class Waterdist_Module(f90wrap.runtime.FortranModule):
    """
    Module waterdist_module
    
    
    Defined at \
        src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
        5-2125
    
    """
    @staticmethod
    def drainage(is_, state_is, storcap, draineq, draincoef1, draincoef2, nsh_real):
        """
        drain_is = drainage(is_, state_is, storcap, draineq, draincoef1, draincoef2, \
            nsh_real)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            31-79
        
        Parameters
        ----------
        is_ : int
        state_is : float
        storcap : float
        draineq : float
        draincoef1 : float
        draincoef2 : float
        nsh_real : float
        
        Returns
        -------
        drain_is : float
        
        ------------------------------------------------------------------------------
        """
        drain_is = _supy_driver.f90wrap_waterdist_module__drainage(is_=is_, \
            state_is=state_is, storcap=storcap, draineq=draineq, draincoef1=draincoef1, \
            draincoef2=draincoef2, nsh_real=nsh_real)
        return drain_is
    
    @staticmethod
    def cal_water_storage(is_, sfr_surf, pipecapacity, runofftowater, pin, wu_surf, \
        drain_surf, addwater, addimpervious, nsh_real, state_in, frac_water2runoff, \
        pervfraction, addveg, soilstorecap, addwaterbody, flowchange, statelimit, \
        runoffagimpervious, runoffagveg, runoffpipes, ev, soilstore, \
        surpluswaterbody, surplusevap, runoffwaterbody, runoff, state_out):
        """
        cal_water_storage(is_, sfr_surf, pipecapacity, runofftowater, pin, wu_surf, \
            drain_surf, addwater, addimpervious, nsh_real, state_in, frac_water2runoff, \
            pervfraction, addveg, soilstorecap, addwaterbody, flowchange, statelimit, \
            runoffagimpervious, runoffagveg, runoffpipes, ev, soilstore, \
            surpluswaterbody, surplusevap, runoffwaterbody, runoff, state_out)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            90-341
        
        Parameters
        ----------
        is_ : int
        sfr_surf : float array
        pipecapacity : float
        runofftowater : float
        pin : float
        wu_surf : float array
        drain_surf : float array
        addwater : float array
        addimpervious : float
        nsh_real : float
        state_in : float array
        frac_water2runoff : float array
        pervfraction : float
        addveg : float
        soilstorecap : float array
        addwaterbody : float
        flowchange : float
        statelimit : float array
        runoffagimpervious : float
        runoffagveg : float
        runoffpipes : float
        ev : float
        soilstore : float array
        surpluswaterbody : float
        surplusevap : float array
        runoffwaterbody : float
        runoff : float array
        state_out : float array
        
        ------------------------------------------------------------------------------
        Calculation of storage change
         TS 30 Nov 2019
           - Allow irrigation on all surfaces(previously only on vegetated surfaces)
         LJ 27 Jan 2016
           - Removed tabs and cleaned the code
         HCW 08 Dec 2015
           -Added if-loop check for no Paved surfaces
         LJ 6 May 2015
           - Calculations of the piperunoff exceedings moved to separate subroutine \
               updateFlood.
           - Now also called from snow subroutine
           - Evaporation is modified using EvapPart
           - when no water on impervious surfaces, evap occurs above pervious surfaces \
               instead
         Rewritten by HCW 12 Feb 2015
           - Old variable 'p' for water input to the surface renamed to 'p_mm'
           - All water now added to p_mm first, before threshold checks or other \
               calculations
           - Water from other grids now added to p_mm(instead of state_id for impervious \
               surfaces)
           - Removed division of runoff by nsh, as whole model now runs at the same \
               timestep
           - Adjusted transfer of ev between surfaces to conserve mass(not depth)
           - Volumes used for water transport between grids to account for SurfaceArea \
               changing between grids
           - Added threshold check for state_id(WaterSurf) - was going negative
         Last modified HCW 09 Feb 2015
           - Removed StorCap input because it is provided by module allocateArray
           - Tidied and commented code
         Modified by LJ in November 2012:
           - P>10 was not taken into account for impervious surfaces - Was fixed.
           - Above impervious surfaces possibility of the state_id to exceed max capacity \
               was limited
             although this should be possible - was fixed
         Modified by LJ 10/2010
         Rewritten mostly by LJ in 2010
         To do:
           - Finish area normalisation for RG2G & finish coding GridConnections
           - What is the 10 mm hr-1 threshold for?
          - Decide upon and correct storage capacities here & in evap subroutine
          - FlowChange units should be mm hr-1 - need to update everywhere
           - Add SurfaceFlood(is)?
           - What happens if sfr_surf(is) = 0 or 1?
           - Consider how irrigated trees actually works...
        ------------------------------------------------------------------------------
        """
        _supy_driver.f90wrap_waterdist_module__cal_water_storage(is_=is_, \
            sfr_surf=sfr_surf, pipecapacity=pipecapacity, runofftowater=runofftowater, \
            pin=pin, wu_surf=wu_surf, drain_surf=drain_surf, addwater=addwater, \
            addimpervious=addimpervious, nsh_real=nsh_real, state_in=state_in, \
            frac_water2runoff=frac_water2runoff, pervfraction=pervfraction, \
            addveg=addveg, soilstorecap=soilstorecap, addwaterbody=addwaterbody, \
            flowchange=flowchange, statelimit=statelimit, \
            runoffagimpervious=runoffagimpervious, runoffagveg=runoffagveg, \
            runoffpipes=runoffpipes, ev=ev, soilstore=soilstore, \
            surpluswaterbody=surpluswaterbody, surplusevap=surplusevap, \
            runoffwaterbody=runoffwaterbody, runoff=runoff, state_out=state_out)
    
    @staticmethod
    def cal_water_storage_surf(pin, nsh_real, snowfrac_in, pipecapacity, \
        runofftowater, addimpervious, addveg, addwaterbody, flowchange, \
        soilstorecap_surf, statelimit_surf, pervfraction, sfr_surf, drain_surf, \
        addwater_surf, frac_water2runoff_surf, wu_surf, ev_surf_in, state_surf_in, \
        soilstore_surf_in, ev_surf_out, state_surf_out, soilstore_surf_out, \
        runoff_surf):
        """
        runoffagimpervious_grid, runoffagveg_grid, runoffpipes_grid, \
            runoffwaterbody_grid = cal_water_storage_surf(pin, nsh_real, snowfrac_in, \
            pipecapacity, runofftowater, addimpervious, addveg, addwaterbody, \
            flowchange, soilstorecap_surf, statelimit_surf, pervfraction, sfr_surf, \
            drain_surf, addwater_surf, frac_water2runoff_surf, wu_surf, ev_surf_in, \
            state_surf_in, soilstore_surf_in, ev_surf_out, state_surf_out, \
            soilstore_surf_out, runoff_surf)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            356-451
        
        Parameters
        ----------
        pin : float
        nsh_real : float
        snowfrac_in : float array
        pipecapacity : float
        runofftowater : float
        addimpervious : float
        addveg : float
        addwaterbody : float
        flowchange : float
        soilstorecap_surf : float array
        statelimit_surf : float array
        pervfraction : float
        sfr_surf : float array
        drain_surf : float array
        addwater_surf : float array
        frac_water2runoff_surf : float array
        wu_surf : float array
        ev_surf_in : float array
        state_surf_in : float array
        soilstore_surf_in : float array
        ev_surf_out : float array
        state_surf_out : float array
        soilstore_surf_out : float array
        runoff_surf : float array
        
        Returns
        -------
        runoffagimpervious_grid : float
        runoffagveg_grid : float
        runoffpipes_grid : float
        runoffwaterbody_grid : float
        
        """
        runoffagimpervious_grid, runoffagveg_grid, runoffpipes_grid, \
            runoffwaterbody_grid = \
            _supy_driver.f90wrap_waterdist_module__cal_water_storage_surf(pin=pin, \
            nsh_real=nsh_real, snowfrac_in=snowfrac_in, pipecapacity=pipecapacity, \
            runofftowater=runofftowater, addimpervious=addimpervious, addveg=addveg, \
            addwaterbody=addwaterbody, flowchange=flowchange, \
            soilstorecap_surf=soilstorecap_surf, statelimit_surf=statelimit_surf, \
            pervfraction=pervfraction, sfr_surf=sfr_surf, drain_surf=drain_surf, \
            addwater_surf=addwater_surf, frac_water2runoff_surf=frac_water2runoff_surf, \
            wu_surf=wu_surf, ev_surf_in=ev_surf_in, state_surf_in=state_surf_in, \
            soilstore_surf_in=soilstore_surf_in, ev_surf_out=ev_surf_out, \
            state_surf_out=state_surf_out, soilstore_surf_out=soilstore_surf_out, \
            runoff_surf=runoff_surf)
        return runoffagimpervious_grid, runoffagveg_grid, runoffpipes_grid, \
            runoffwaterbody_grid
    
    @staticmethod
    def cal_water_storage_building(pin, nsh_real, nlayer, sfr_roof, statelimit_roof, \
        soilstorecap_roof, wetthresh_roof, ev_roof, state_roof_in, \
        soilstore_roof_in, sfr_wall, statelimit_wall, soilstorecap_wall, \
        wetthresh_wall, ev_wall, state_wall_in, soilstore_wall_in, state_roof_out, \
        soilstore_roof_out, runoff_roof, state_wall_out, soilstore_wall_out, \
        runoff_wall):
        """
        state_building, soilstore_building, runoff_building, soilstorecap_building = \
            cal_water_storage_building(pin, nsh_real, nlayer, sfr_roof, statelimit_roof, \
            soilstorecap_roof, wetthresh_roof, ev_roof, state_roof_in, \
            soilstore_roof_in, sfr_wall, statelimit_wall, soilstorecap_wall, \
            wetthresh_wall, ev_wall, state_wall_in, soilstore_wall_in, state_roof_out, \
            soilstore_roof_out, runoff_roof, state_wall_out, soilstore_wall_out, \
            runoff_wall)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            453-614
        
        Parameters
        ----------
        pin : float
        nsh_real : float
        nlayer : int
        sfr_roof : float array
        statelimit_roof : float array
        soilstorecap_roof : float array
        wetthresh_roof : float array
        ev_roof : float array
        state_roof_in : float array
        soilstore_roof_in : float array
        sfr_wall : float array
        statelimit_wall : float array
        soilstorecap_wall : float array
        wetthresh_wall : float array
        ev_wall : float array
        state_wall_in : float array
        soilstore_wall_in : float array
        state_roof_out : float array
        soilstore_roof_out : float array
        runoff_roof : float array
        state_wall_out : float array
        soilstore_wall_out : float array
        runoff_wall : float array
        
        Returns
        -------
        state_building : float
        soilstore_building : float
        runoff_building : float
        soilstorecap_building : float
        
        """
        state_building, soilstore_building, runoff_building, soilstorecap_building = \
            _supy_driver.f90wrap_waterdist_module__cal_water_storage_building(pin=pin, \
            nsh_real=nsh_real, nlayer=nlayer, sfr_roof=sfr_roof, \
            statelimit_roof=statelimit_roof, soilstorecap_roof=soilstorecap_roof, \
            wetthresh_roof=wetthresh_roof, ev_roof=ev_roof, state_roof_in=state_roof_in, \
            soilstore_roof_in=soilstore_roof_in, sfr_wall=sfr_wall, \
            statelimit_wall=statelimit_wall, soilstorecap_wall=soilstorecap_wall, \
            wetthresh_wall=wetthresh_wall, ev_wall=ev_wall, state_wall_in=state_wall_in, \
            soilstore_wall_in=soilstore_wall_in, state_roof_out=state_roof_out, \
            soilstore_roof_out=soilstore_roof_out, runoff_roof=runoff_roof, \
            state_wall_out=state_wall_out, soilstore_wall_out=soilstore_wall_out, \
            runoff_wall=runoff_wall)
        return state_building, soilstore_building, runoff_building, \
            soilstorecap_building
    
    @staticmethod
    def updateflood(is_, runoff, sfr_surf, pipecapacity, runofftowater, \
        runoffagimpervious, surpluswaterbody, runoffagveg, runoffpipes):
        """
        updateflood(is_, runoff, sfr_surf, pipecapacity, runofftowater, \
            runoffagimpervious, surpluswaterbody, runoffagveg, runoffpipes)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            620-653
        
        Parameters
        ----------
        is_ : int
        runoff : float array
        sfr_surf : float array
        pipecapacity : float
        runofftowater : float
        runoffagimpervious : float
        surpluswaterbody : float
        runoffagveg : float
        runoffpipes : float
        
        ------Paved and building surface
        """
        _supy_driver.f90wrap_waterdist_module__updateflood(is_=is_, runoff=runoff, \
            sfr_surf=sfr_surf, pipecapacity=pipecapacity, runofftowater=runofftowater, \
            runoffagimpervious=runoffagimpervious, surpluswaterbody=surpluswaterbody, \
            runoffagveg=runoffagveg, runoffpipes=runoffpipes)
    
    @staticmethod
    def redistributewater(snowuse, waterdist, sfr_surf, drain, addwaterrunoff, \
        addwater):
        """
        redistributewater(snowuse, waterdist, sfr_surf, drain, addwaterrunoff, addwater)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            659-698
        
        Parameters
        ----------
        snowuse : int
        waterdist : float array
        sfr_surf : float array
        drain : float array
        addwaterrunoff : float array
        addwater : float array
        
        -------------------------------------------------------------------
        """
        _supy_driver.f90wrap_waterdist_module__redistributewater(snowuse=snowuse, \
            waterdist=waterdist, sfr_surf=sfr_surf, drain=drain, \
            addwaterrunoff=addwaterrunoff, addwater=addwater)
    
    @staticmethod
    def suews_update_soilmoist(nonwaterfraction, soilstorecap, sfr_surf, \
        soilstore_id):
        """
        soilmoistcap, soilstate, vsmd, smd = suews_update_soilmoist(nonwaterfraction, \
            soilstorecap, sfr_surf, soilstore_id)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            706-742
        
        Parameters
        ----------
        nonwaterfraction : float
        soilstorecap : float array
        sfr_surf : float array
        soilstore_id : float array
        
        Returns
        -------
        soilmoistcap : float
        soilstate : float
        vsmd : float
        smd : float
        
        """
        soilmoistcap, soilstate, vsmd, smd = \
            _supy_driver.f90wrap_waterdist_module__suews_update_soilmoist(nonwaterfraction=nonwaterfraction, \
            soilstorecap=soilstorecap, sfr_surf=sfr_surf, soilstore_id=soilstore_id)
        return soilmoistcap, soilstate, vsmd, smd
    
    @staticmethod
    def suews_update_soilmoist_dts(self, config, forcing, siteinfo, modstate):
        """
        suews_update_soilmoist_dts(self, config, forcing, siteinfo, modstate)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            815-896
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_waterdist_module__suews_update_soilmoist_dts(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def cal_smd_veg(soilstorecap, soilstore_id, sfr_surf):
        """
        vsmd = cal_smd_veg(soilstorecap, soilstore_id, sfr_surf)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            900-915
        
        Parameters
        ----------
        soilstorecap : float array
        soilstore_id : float array
        sfr_surf : float array
        
        Returns
        -------
        vsmd : float
        
        """
        vsmd = \
            _supy_driver.f90wrap_waterdist_module__cal_smd_veg(soilstorecap=soilstorecap, \
            soilstore_id=soilstore_id, sfr_surf=sfr_surf)
        return vsmd
    
    @staticmethod
    def suews_cal_soilstate(smdmethod, xsmd, nonwaterfraction, soilmoistcap, \
        soilstorecap_surf, surf_chang_per_tstep, soilstore_surf, soilstore_surf_in, \
        sfr_surf, smd_surf):
        """
        smd, tot_chang_per_tstep, soilstate = suews_cal_soilstate(smdmethod, xsmd, \
            nonwaterfraction, soilmoistcap, soilstorecap_surf, surf_chang_per_tstep, \
            soilstore_surf, soilstore_surf_in, sfr_surf, smd_surf)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            922-973
        
        Parameters
        ----------
        smdmethod : int
        xsmd : float
        nonwaterfraction : float
        soilmoistcap : float
        soilstorecap_surf : float array
        surf_chang_per_tstep : float
        soilstore_surf : float array
        soilstore_surf_in : float array
        sfr_surf : float array
        smd_surf : float array
        
        Returns
        -------
        smd : float
        tot_chang_per_tstep : float
        soilstate : float
        
        """
        smd, tot_chang_per_tstep, soilstate = \
            _supy_driver.f90wrap_waterdist_module__suews_cal_soilstate(smdmethod=smdmethod, \
            xsmd=xsmd, nonwaterfraction=nonwaterfraction, soilmoistcap=soilmoistcap, \
            soilstorecap_surf=soilstorecap_surf, \
            surf_chang_per_tstep=surf_chang_per_tstep, soilstore_surf=soilstore_surf, \
            soilstore_surf_in=soilstore_surf_in, sfr_surf=sfr_surf, smd_surf=smd_surf)
        return smd, tot_chang_per_tstep, soilstate
    
    @staticmethod
    def suews_cal_horizontalsoilwater(sfr_surf, soilstorecap_surf, soildepth_surf, \
        sathydraulicconduct_surf, surfacearea, nonwaterfraction, tstep_real, \
        soilstore_surf, runoffsoil_surf):
        """
        runoffsoil_per_tstep = suews_cal_horizontalsoilwater(sfr_surf, \
            soilstorecap_surf, soildepth_surf, sathydraulicconduct_surf, surfacearea, \
            nonwaterfraction, tstep_real, soilstore_surf, runoffsoil_surf)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            1097-1279
        
        Parameters
        ----------
        sfr_surf : float array
        soilstorecap_surf : float array
        soildepth_surf : float array
        sathydraulicconduct_surf : float array
        surfacearea : float
        nonwaterfraction : float
        tstep_real : float
        soilstore_surf : float array
        runoffsoil_surf : float array
        
        Returns
        -------
        runoffsoil_per_tstep : float
        
        ------------------------------------------------------
         use SUES_data
         use gis_data
         use time
         use allocateArray
        """
        runoffsoil_per_tstep = \
            _supy_driver.f90wrap_waterdist_module__suews_cal_horizontalsoilwater(sfr_surf=sfr_surf, \
            soilstorecap_surf=soilstorecap_surf, soildepth_surf=soildepth_surf, \
            sathydraulicconduct_surf=sathydraulicconduct_surf, surfacearea=surfacearea, \
            nonwaterfraction=nonwaterfraction, tstep_real=tstep_real, \
            soilstore_surf=soilstore_surf, runoffsoil_surf=runoffsoil_surf)
        return runoffsoil_per_tstep
    
    @staticmethod
    def suews_cal_horizontalsoilwater_dts(self, config, forcing, siteinfo, \
        hydrostate):
        """
        suews_cal_horizontalsoilwater_dts(self, config, forcing, siteinfo, hydrostate)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            1281-1531
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        hydrostate : Hydro_State
        
        ------------------------------------------------------
         use SUES_data
         use gis_data
         use time
         use allocateArray
        """
        _supy_driver.f90wrap_waterdist_module__suews_cal_horizontalsoilwater_dts(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            hydrostate=hydrostate._handle)
    
    @staticmethod
    def suews_cal_wateruse(self, config, forcing, siteinfo, modstate):
        """
        suews_cal_wateruse(self, config, forcing, siteinfo, modstate)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            1894-2104
        
        Parameters
        ----------
        timer : Suews_Timer
        config : Suews_Config
        forcing : Suews_Forcing
        siteinfo : Suews_Site
        modstate : Suews_State
        
        """
        _supy_driver.f90wrap_waterdist_module__suews_cal_wateruse(timer=self._handle, \
            config=config._handle, forcing=forcing._handle, siteinfo=siteinfo._handle, \
            modstate=modstate._handle)
    
    @staticmethod
    def get_prof_spectime_sum(hour, min_bn, sec, prof_24h, dt):
        """
        prof_currtime = get_prof_spectime_sum(hour, min_bn, sec, prof_24h, dt)
        
        
        Defined at \
            src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_phys_waterdist.fpp lines \
            2108-2125
        
        Parameters
        ----------
        hour : int
        min_bn : int
        sec : int
        prof_24h : float array
        dt : int
        
        Returns
        -------
        prof_currtime : float
        
        """
        prof_currtime = \
            _supy_driver.f90wrap_waterdist_module__get_prof_spectime_sum(hour=hour, \
            min_bn=min_bn, sec=sec, prof_24h=prof_24h, dt=dt)
        return prof_currtime
    
    _dt_array_initialisers = []
    

waterdist_module = Waterdist_Module()

class Meteo(f90wrap.runtime.FortranModule):
    """
    Module meteo
    
    
    Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
        lines 6-446
    
    """
    @staticmethod
    def sat_vap_press(tk, p):
        """
        es = sat_vap_press(tk, p)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 25-38
        
        Parameters
        ----------
        tk : float
        p : float
        
        Returns
        -------
        es : float
        
        """
        es = _supy_driver.f90wrap_meteo__sat_vap_press(tk=tk, p=p)
        return es
    
    @staticmethod
    def sos_dryair(tk):
        """
        sos_dryair = sos_dryair(tk)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 40-43
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        sos_dryair : float
        
        """
        sos_dryair = _supy_driver.f90wrap_meteo__sos_dryair(tk=tk)
        return sos_dryair
    
    @staticmethod
    def potential_temp(tk, p):
        """
        potential_temp = potential_temp(tk, p)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 46-50
        
        Parameters
        ----------
        tk : float
        p : float
        
        Returns
        -------
        potential_temp : float
        
        """
        potential_temp = _supy_driver.f90wrap_meteo__potential_temp(tk=tk, p=p)
        return potential_temp
    
    @staticmethod
    def latentheat_v(tk):
        """
        latentheat_v = latentheat_v(tk)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 52-56
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        latentheat_v : float
        
        """
        latentheat_v = _supy_driver.f90wrap_meteo__latentheat_v(tk=tk)
        return latentheat_v
    
    @staticmethod
    def latentheat_m(tk):
        """
        latentheat_m = latentheat_m(tk)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 58-63
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        latentheat_m : float
        
        """
        latentheat_m = _supy_driver.f90wrap_meteo__latentheat_m(tk=tk)
        return latentheat_m
    
    @staticmethod
    def spec_heat_dryair(tk):
        """
        spec_heat_dryair = spec_heat_dryair(tk)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 65-69
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        spec_heat_dryair : float
        
        """
        spec_heat_dryair = _supy_driver.f90wrap_meteo__spec_heat_dryair(tk=tk)
        return spec_heat_dryair
    
    @staticmethod
    def spec_heat_vapor(tk, rh):
        """
        spec_heat_vapor = spec_heat_vapor(tk, rh)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 71-75
        
        Parameters
        ----------
        tk : float
        rh : float
        
        Returns
        -------
        spec_heat_vapor : float
        
        """
        spec_heat_vapor = _supy_driver.f90wrap_meteo__spec_heat_vapor(tk=tk, rh=rh)
        return spec_heat_vapor
    
    @staticmethod
    def heatcapacity_air(tk, rh, p):
        """
        heatcapacity_air = heatcapacity_air(tk, rh, p)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 77-85
        
        Parameters
        ----------
        tk : float
        rh : float
        p : float
        
        Returns
        -------
        heatcapacity_air : float
        
        """
        heatcapacity_air = _supy_driver.f90wrap_meteo__heatcapacity_air(tk=tk, rh=rh, \
            p=p)
        return heatcapacity_air
    
    @staticmethod
    def density_moist(tvk, p):
        """
        density_moist = density_moist(tvk, p)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 87-92
        
        Parameters
        ----------
        tvk : float
        p : float
        
        Returns
        -------
        density_moist : float
        
        """
        density_moist = _supy_driver.f90wrap_meteo__density_moist(tvk=tvk, p=p)
        return density_moist
    
    @staticmethod
    def density_vapor(tk, rh, p):
        """
        density_vapor = density_vapor(tk, rh, p)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 94-98
        
        Parameters
        ----------
        tk : float
        rh : float
        p : float
        
        Returns
        -------
        density_vapor : float
        
        """
        density_vapor = _supy_driver.f90wrap_meteo__density_vapor(tk=tk, rh=rh, p=p)
        return density_vapor
    
    @staticmethod
    def density_dryair(tk, p):
        """
        density_dryair = density_dryair(tk, p)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 100-102
        
        Parameters
        ----------
        tk : float
        p : float
        
        Returns
        -------
        density_dryair : float
        
        """
        density_dryair = _supy_driver.f90wrap_meteo__density_dryair(tk=tk, p=p)
        return density_dryair
    
    @staticmethod
    def density_gas(tk, pp, molmass):
        """
        density_gas = density_gas(tk, pp, molmass)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 104-107
        
        Parameters
        ----------
        tk : float
        pp : float
        molmass : float
        
        Returns
        -------
        density_gas : float
        
        """
        density_gas = _supy_driver.f90wrap_meteo__density_gas(tk=tk, pp=pp, \
            molmass=molmass)
        return density_gas
    
    @staticmethod
    def partial_pressure(tk, n):
        """
        partial_pressure = partial_pressure(tk, n)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 109-112
        
        Parameters
        ----------
        tk : float
        n : float
        
        Returns
        -------
        partial_pressure : float
        
        """
        partial_pressure = _supy_driver.f90wrap_meteo__partial_pressure(tk=tk, n=n)
        return partial_pressure
    
    @staticmethod
    def scale_height(tk):
        """
        scale_height = scale_height(tk)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 114-117
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        scale_height : float
        
        """
        scale_height = _supy_driver.f90wrap_meteo__scale_height(tk=tk)
        return scale_height
    
    @staticmethod
    def vaisala_brunt_f(tk):
        """
        vaisala_brunt_f = vaisala_brunt_f(tk)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 119-122
        
        Parameters
        ----------
        tk : float
        
        Returns
        -------
        vaisala_brunt_f : float
        
        """
        vaisala_brunt_f = _supy_driver.f90wrap_meteo__vaisala_brunt_f(tk=tk)
        return vaisala_brunt_f
    
    @staticmethod
    def sat_vap_press_x(temp_c, press_hpa, from_, dectime):
        """
        es_hpa = sat_vap_press_x(temp_c, press_hpa, from_, dectime)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 132-165
        
        Parameters
        ----------
        temp_c : float
        press_hpa : float
        from_ : int
        dectime : float
        
        Returns
        -------
        es_hpa : float
        
        """
        es_hpa = _supy_driver.f90wrap_meteo__sat_vap_press_x(temp_c=temp_c, \
            press_hpa=press_hpa, from_=from_, dectime=dectime)
        return es_hpa
    
    @staticmethod
    def sat_vap_pressice(temp_c, press_hpa, from_, dectime):
        """
        es_hpa = sat_vap_pressice(temp_c, press_hpa, from_, dectime)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 167-192
        
        Parameters
        ----------
        temp_c : float
        press_hpa : float
        from_ : int
        dectime : float
        
        Returns
        -------
        es_hpa : float
        
        """
        es_hpa = _supy_driver.f90wrap_meteo__sat_vap_pressice(temp_c=temp_c, \
            press_hpa=press_hpa, from_=from_, dectime=dectime)
        return es_hpa
    
    @staticmethod
    def spec_hum_def(vpd_hpa, press_hpa):
        """
        dq = spec_hum_def(vpd_hpa, press_hpa)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 197-202
        
        Parameters
        ----------
        vpd_hpa : float
        press_hpa : float
        
        Returns
        -------
        dq : float
        
        """
        dq = _supy_driver.f90wrap_meteo__spec_hum_def(vpd_hpa=vpd_hpa, \
            press_hpa=press_hpa)
        return dq
    
    @staticmethod
    def spec_heat_beer(temp_c, rh, rho_v, rho_d):
        """
        cp = spec_heat_beer(temp_c, rh, rho_v, rho_d)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 205-223
        
        Parameters
        ----------
        temp_c : float
        rh : float
        rho_v : float
        rho_d : float
        
        Returns
        -------
        cp : float
        
        -------------------------------------------------------------------------------
         USE defaultnotUsed
        """
        cp = _supy_driver.f90wrap_meteo__spec_heat_beer(temp_c=temp_c, rh=rh, \
            rho_v=rho_v, rho_d=rho_d)
        return cp
    
    @staticmethod
    def lat_vap(temp_c, ea_hpa, press_hpa, cp, dectime):
        """
        lv_j_kg = lat_vap(temp_c, ea_hpa, press_hpa, cp, dectime)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 229-280
        
        Parameters
        ----------
        temp_c : float
        ea_hpa : float
        press_hpa : float
        cp : float
        dectime : float
        
        Returns
        -------
        lv_j_kg : float
        
        """
        lv_j_kg = _supy_driver.f90wrap_meteo__lat_vap(temp_c=temp_c, ea_hpa=ea_hpa, \
            press_hpa=press_hpa, cp=cp, dectime=dectime)
        return lv_j_kg
    
    @staticmethod
    def lat_vapsublim(temp_c, ea_hpa, press_hpa, cp):
        """
        lvs_j_kg = lat_vapsublim(temp_c, ea_hpa, press_hpa, cp)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 282-321
        
        Parameters
        ----------
        temp_c : float
        ea_hpa : float
        press_hpa : float
        cp : float
        
        Returns
        -------
        lvs_j_kg : float
        
        """
        lvs_j_kg = _supy_driver.f90wrap_meteo__lat_vapsublim(temp_c=temp_c, \
            ea_hpa=ea_hpa, press_hpa=press_hpa, cp=cp)
        return lvs_j_kg
    
    @staticmethod
    def psyc_const(cp, press_hpa, lv_j_kg):
        """
        psyc_hpa = psyc_const(cp, press_hpa, lv_j_kg)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 327-343
        
        Parameters
        ----------
        cp : float
        press_hpa : float
        lv_j_kg : float
        
        Returns
        -------
        psyc_hpa : float
        
        """
        psyc_hpa = _supy_driver.f90wrap_meteo__psyc_const(cp=cp, press_hpa=press_hpa, \
            lv_j_kg=lv_j_kg)
        return psyc_hpa
    
    @staticmethod
    def dewpoint(ea_hpa):
        """
        temp_c_dew = dewpoint(ea_hpa)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 346-353
        
        Parameters
        ----------
        ea_hpa : float
        
        Returns
        -------
        temp_c_dew : float
        
        """
        temp_c_dew = _supy_driver.f90wrap_meteo__dewpoint(ea_hpa=ea_hpa)
        return temp_c_dew
    
    @staticmethod
    def slope_svp(temp_c):
        """
        s_hpa = slope_svp(temp_c)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 356-376
        
        Parameters
        ----------
        temp_c : float
        
        Returns
        -------
        s_hpa : float
        
        """
        s_hpa = _supy_driver.f90wrap_meteo__slope_svp(temp_c=temp_c)
        return s_hpa
    
    @staticmethod
    def slopeice_svp(temp_c):
        """
        s_hpa = slopeice_svp(temp_c)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 379-394
        
        Parameters
        ----------
        temp_c : float
        
        Returns
        -------
        s_hpa : float
        
        """
        s_hpa = _supy_driver.f90wrap_meteo__slopeice_svp(temp_c=temp_c)
        return s_hpa
    
    @staticmethod
    def qsatf(t, pmb):
        """
        qsat = qsatf(t, pmb)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 397-413
        
        Parameters
        ----------
        t : float
        pmb : float
        
        Returns
        -------
        qsat : float
        
        """
        qsat = _supy_driver.f90wrap_meteo__qsatf(t=t, pmb=pmb)
        return qsat
    
    @staticmethod
    def rh2qa(rh_dec, pres_hpa, ta_degc):
        """
        qa_gkg = rh2qa(rh_dec, pres_hpa, ta_degc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 415-427
        
        Parameters
        ----------
        rh_dec : float
        pres_hpa : float
        ta_degc : float
        
        Returns
        -------
        qa_gkg : float
        
        """
        qa_gkg = _supy_driver.f90wrap_meteo__rh2qa(rh_dec=rh_dec, pres_hpa=pres_hpa, \
            ta_degc=ta_degc)
        return qa_gkg
    
    @staticmethod
    def qa2rh(qa_gkg, pres_hpa, ta_degc):
        """
        rh = qa2rh(qa_gkg, pres_hpa, ta_degc)
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            lines 429-446
        
        Parameters
        ----------
        qa_gkg : float
        pres_hpa : float
        ta_degc : float
        
        Returns
        -------
        rh : float
        
        """
        rh = _supy_driver.f90wrap_meteo__qa2rh(qa_gkg=qa_gkg, pres_hpa=pres_hpa, \
            ta_degc=ta_degc)
        return rh
    
    @property
    def rad2deg(self):
        """
        Element rad2deg ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 10
        
        """
        return _supy_driver.f90wrap_meteo__get__rad2deg()
    
    @property
    def deg2rad(self):
        """
        Element deg2rad ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 11
        
        """
        return _supy_driver.f90wrap_meteo__get__deg2rad()
    
    @property
    def molmass_air(self):
        """
        Element molmass_air ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 12
        
        """
        return _supy_driver.f90wrap_meteo__get__molmass_air()
    
    @property
    def molmass_co2(self):
        """
        Element molmass_co2 ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 13
        
        """
        return _supy_driver.f90wrap_meteo__get__molmass_co2()
    
    @property
    def molmass_h2o(self):
        """
        Element molmass_h2o ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 14
        
        """
        return _supy_driver.f90wrap_meteo__get__molmass_h2o()
    
    @property
    def mu_h2o(self):
        """
        Element mu_h2o ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 15
        
        """
        return _supy_driver.f90wrap_meteo__get__mu_h2o()
    
    @property
    def mu_co2(self):
        """
        Element mu_co2 ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 16
        
        """
        return _supy_driver.f90wrap_meteo__get__mu_co2()
    
    @property
    def r_dry_mol(self):
        """
        Element r_dry_mol ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 17
        
        """
        return _supy_driver.f90wrap_meteo__get__r_dry_mol()
    
    @property
    def r_dry_mass(self):
        """
        Element r_dry_mass ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 18
        
        """
        return _supy_driver.f90wrap_meteo__get__r_dry_mass()
    
    @property
    def epsil(self):
        """
        Element epsil ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 20
        
        """
        return _supy_driver.f90wrap_meteo__get__epsil()
    
    @property
    def kb(self):
        """
        Element kb ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 21
        
        """
        return _supy_driver.f90wrap_meteo__get__kb()
    
    @property
    def avogadro(self):
        """
        Element avogadro ftype=real(kind(1d0) pytype=float
        
        
        Defined at src/supy_driver/f90wrap_suews_ctrl_type.f90.p/suews_util_meteo.fpp \
            line 22
        
        """
        return _supy_driver.f90wrap_meteo__get__avogadro()
    
    def __str__(self):
        ret = ['<meteo>{\n']
        ret.append('    rad2deg : ')
        ret.append(repr(self.rad2deg))
        ret.append(',\n    deg2rad : ')
        ret.append(repr(self.deg2rad))
        ret.append(',\n    molmass_air : ')
        ret.append(repr(self.molmass_air))
        ret.append(',\n    molmass_co2 : ')
        ret.append(repr(self.molmass_co2))
        ret.append(',\n    molmass_h2o : ')
        ret.append(repr(self.molmass_h2o))
        ret.append(',\n    mu_h2o : ')
        ret.append(repr(self.mu_h2o))
        ret.append(',\n    mu_co2 : ')
        ret.append(repr(self.mu_co2))
        ret.append(',\n    r_dry_mol : ')
        ret.append(repr(self.r_dry_mol))
        ret.append(',\n    r_dry_mass : ')
        ret.append(repr(self.r_dry_mass))
        ret.append(',\n    epsil : ')
        ret.append(repr(self.epsil))
        ret.append(',\n    kb : ')
        ret.append(repr(self.kb))
        ret.append(',\n    avogadro : ')
        ret.append(repr(self.avogadro))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

meteo = Meteo()

