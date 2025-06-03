"""
Copyright 2017 Robin Verschueren

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np

import cvxpy.interface as intf
import cvxpy.settings as s
from cvxpy.reductions.solution import Solution, failure_solution
from cvxpy.reductions.solvers.qp_solvers.qp_solver import QpSolver
from cvxpy.utilities.citations import CITATION_DICT

"""
NOTE: The FrankWolfe.jl package is built using Julia. To use this 
package in Python, the user must use the command commented out above
to install the frankewolfepy wrapper, which will install Julia and the
necessary packages required to use the solver.
"""

def helper_function_one():
    pass

class FWJL(QpSolver):
    """QP interface for the FW.jl solver"""
    MIP_CAPABLE = False 
    
    # FIXME: Map of FWJL status to CVXPY status.
    STATUS_MAP = {"...": s.OPTIMAL,
                  "..": s.INFEASIBLE,
                  ".": s.UNBOUNDED}
    
    """

    "apply stages data for solve_via_data, 
    solve_via_data calls the Awesome solver by way of the existing third-party AwesomePy package, 
    and invert transforms the output from AwesomePy into the format that CVXPY expects."

    """

    def name(self) -> str:
        "Returns name of solver"
        return s.FWJL
    
    def import_solver(self) -> None:
        """
        Imports python wrapper for FrankeWolfe solver
        """
        try:
            import frankwolfepy
            frankwolfepy
        except ImportError:
            print("Module 'frankwolfepy' not found.")
            print("To install it, go to https://github.com/ZIB-IOL/frankwolfe-py and follow installation instructions.")
        except Exception as e:
            print(f"An unexpected error occurred while importing the solver: {e}")

    def apply(self, problem): # Not sure if this will be necessary tbh
        pass


    def solve_via_data(self, data, warm_start: bool, verbose: bool, solver_opts, solver_cache=None):
        from frankwolfepy import frankwolfe as fw, wrapper as wrap

        
        

        pass
            
    def invert(self):
        pass

    def cite(self): #FIXME Implement this
        """Returns bibtex citation for the solver."""
        pass
        

        


