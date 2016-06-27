# Sizing.py
#
# Created:  
# Modified: Feb 2016, Andrew Wendorff

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Core import Data, Results
from SUAVE.Analyses import Analysis


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

class Sizing(Analysis):
    """ SUAVE.Analyses.Sizing.Sizing()
    """
    def __defaults__(self):
        self.tag    = 'sizing'
        self.features = Data()
        self.settings = Data()
        
        
    def evaluate(self,conditions):
        return Results()
    
    __call__ = evaluate
        