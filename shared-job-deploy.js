async function test_2d_array(dcp)
{
  let arr_size = 2500
  arr_size = arr_size / 2 + arr_size / 4 + arr_size / 8 + arr_size / 16
  arr_size = parseInt(arr_size)
  //arr_size = 1500

  console.log(arr_size)

  lst2 = [];
  lst1 = [];
  for (let i = 0; i < arr_size; i++) {
      lst2.push([])
      for (let j = 0; j < arr_size; j++)
          lst2[i].push(i + j + (j + 0.1) / (i + j + 0.123456))
      lst1.push(i * i)
  }
  let args2 = [lst1, lst2]
  let data = [1]

  // function which will execute on each datum in the dataset remotely on dcp workers
  let work_function = `
  function myEpicWorkFn(datum, arg1, arg2)
  {
      progress();
      return arg1.length + arg2.length; + datum
  }`;


  async function main()
  {
    const job = dcp.compute.for(data, work_function, args2);
    job.on('readystatechange', console.log);
    job.on('result', console.log);
    const rizzle = await job.exec();
    return rizzle;
  }
  return await main();
}

exports.jobDeploy = test_2d_array;

