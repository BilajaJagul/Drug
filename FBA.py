import matlab.engine

eng =  matlab.engine.start_matlab()



fluxdata = eng.matpy('PGL')