#!/usr/bin/env python3
"""
Job deployal in PythonMonkey.
Testing memory usage and OOMage.
"""

import pythonmonkey as pm
dcp_client = pm.require('dcp-client')
shared_lib = pm.require('./shared-job-deploy.js')

async def pringle(): 
    dcp = pm.globalThis.dcp
    vals = await shared_lib.jobDeploy(dcp)

dcp_client['init'](pringle)
