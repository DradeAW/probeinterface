from probeinterface import ProbeGroup
from probeinterface import generate_dummy_probe

import pytest

import numpy as np


def test_probegroup():
    probegroup = ProbeGroup()
    
    nchan = 0
    for i in range(3):
        probe = generate_dummy_probe()
        probe.move([i*100, i*80])
        n = probe.get_electrode_count()
        probe.set_device_channel_indices(np.arange(n)[::-1] + nchan)
        shank_ids = np.ones(n)
        shank_ids[:n//2] *= i * 2
        shank_ids[n//2:] *= i * 2 +1 
        probe.set_shank_ids(shank_ids)
        probegroup.add_probe(probe)
        
        
        nchan += n
    
    indices = probegroup.get_global_device_channel_indices()
    
    ids = probegroup.get_global_electrode_ids()
    
    df = probegroup.to_dataframe()
    #~ print(df['global_electrode_ids'])
    
    positions, device_indices = probegroup.get_groups(group_mode='by_probe')
    assert len(positions) == 3
    
    positions, device_indices = probegroup.get_groups(group_mode='by_shank')
    assert len(positions) == 6


def test_probegroup_3d():
    probegroup = ProbeGroup()
    
    for i in range(3):
        probe = generate_dummy_probe().to_3d()
        probe.move([i*100, i*80, i*30])
        probegroup.add_probe(probe)

    assert probegroup.ndim == 3
    
    
    
if __name__ == '__main__':
    test_probegroup()
    test_probegroup_3d()