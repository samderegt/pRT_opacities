import numpy as np

database = 'ExoMol'
species  = 'AlH'
mass = 27.98948 # (in .json file)
isotopologue_id = {'Al':27, 'H':1}

# Instructions to download from ExoMol database
url_def_json = 'https://www.exomol.com/db/AlH/27Al-1H/AloHa/27Al-1H__AloHa.def.json'
url_broad = [
    'https://www.exomol.com/db/AlH/27Al-1H/27Al-1H__H2.broad', 
    'https://www.exomol.com/db/AlH/27Al-1H/27Al-1H__He.broad'
]

# Input/output-directories
input_dir  = f'./input_data/{database}/{species}/'
output_dir = f'./cross_sec_outputs/{species}/'

files = dict(
    transitions = f'{input_dir}/27Al-1H__AloHa.trans.bz2', 
    states      = f'{input_dir}/27Al-1H__AloHa.states.bz2', 

    partition_function = f'{input_dir}/27Al-1H__AloHa.pf', 
)

# Pressure-broadening information
broadening = dict(
    H2 = dict(
        VMR=0.85, file=f'{input_dir}/27Al-1H__H2.broad', # read from file
        ), 
    He = dict(
        VMR=0.15, file=f'{input_dir}/27Al-1H__He.broad', # read from file
        ), 
)

P_grid = np.logspace(-5,2,8) # [bar]   # can be given in cmd, one point at a time
T_grid = np.array([1000,])   # [K]     # can be given in cmd, one point at a time

wave_min = 1.0/3.0; wave_max = 50.0 # [um]
delta_nu = 0.01 # [cm^-1]

# Switch to sparser wavenumber grid for high broadening?
adaptive_nu_grid = True

# Line-strength cutoffs
local_cutoff  = 0.35
global_cutoff = 1e-45

# gamma_V [cm^-1], P [bar]
#wing_cutoff = lambda _, P: 25 if P<=200 else 100 # Gharib-Nezhad et al. (2024) DEFAULT