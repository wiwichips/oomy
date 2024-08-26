#!/usr/bin/env node
/*
 * NodeJS Memory testing
 */
const shared_lib = require('./shared-job-deploy.js');

async function pringle()
{
    const dcp = await require('dcp-client').init();
    const vals = await shared_lib.jobDeploy(dcp);
}

pringle()

