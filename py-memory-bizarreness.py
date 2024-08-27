#!/usr/bin/env python3
"""
Works at 1020000 elements, OOMs at 1030000 elements...
"""

import pythonmonkey as pm

oomer = pm.eval("""
/*async*/ function oomer()
{
  let arr_size; // change array size to different values
  //                    | (async|sync)  |     (async)   |    (sync)
  //                    | w/ dcp-client | wo/ dcp-client| wo/ dcp-client
  //                    |---------------+---------------+----------------
  arr_size = 1020000; //|     OOMs      |    success!   |    success!
  arr_size = 1030000; //|     OOMs      |  hangs 4ever  |      OOMs

  const bigArray = [];
  for (let i = 0; i < arr_size; i++)
    bigArray.push(i + 0.1 / (i + 0.123456)); // randomish floats, fattened up by json.stringify A LOT later


  //let seed = 1; bigArray.sort(() => (Math.sin(seed++) * 10000) % 1 - 0.5); // TODO unnecessary, remove later


  // these initial values don't really matter per se, it's more just about how they're serialized
  console.log(`Array length: ${bigArray.length}`);
  console.log(`Array bytes : ${bigArray.length * 8}`); // 8 bytes per js number??? 
  console.log(`Array MB    : ${bigArray.length * 8 / 1000000}`);

  // The following code is baed off of encodeJobValueList in dcp-client/job/index.js
  const jsonedElementsArray = [];
  for (let i = 0; i < bigArray.length; i++)
  {
    jsonedElementsArray.push(JSON.stringify(bigArray[i]));

    // logging
    if (i % 10000 === 0 && i > 600000) // skip first 600000 then only print every 10000 elements
      console.log(i, ' -- ', bigArray[i]);
  }

  // now we calculate the total length of all the strings in the array and see how much memory they use 
  console.log(`JSONed Array length: ${jsonedElementsArray.length}`);
  console.log(`JSONed Array bytes : ${jsonedElementsArray.reduce((acc, str) => acc + str.length, 0) * 2}`); // 2 bytes per character
  console.log(`JSONed Array MB    : ${jsonedElementsArray.reduce((acc, str) => acc + str.length, 0) * 2 / 1000000}`);
}
oomer
""")

####### async #######

##dcp_client = pm.require('dcp-client')
#async def pringle(): 
#    #dcp = pm.globalThis.dcp
#    vals = await oomer()
#
##dcp_client['init'](pringle)
#import asyncio
#asyncio.run(pringle())

####### sync  #######

oomer()

