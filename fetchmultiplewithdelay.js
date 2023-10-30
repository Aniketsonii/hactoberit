function fetchURLMultipleTimes(totalIterations, sleepInterval, sleepDuration, callback) {
    let iterationCount = 0;
  
    function fetchWithDelay() {
      if (iterationCount >= totalIterations) {
        callback();
        return;
      }
  
      // CREATE A FUNCTION AND FROM NETWORK TAB COPY AS FETCH AND PASTE
      fetch("")
        .then(response => {
          console.log(Iteration ${iterationCount + 1}: ${response.status});
          iterationCount++;
  
          if (iterationCount % sleepInterval === 0) {
            setTimeout(fetchWithDelay, sleepDuration); 
          } else {
            fetchWithDelay();
          }
        })
        .catch(error => {
          console.error(Error on iteration ${iterationCount + 1}: ${error});
          iterationCount++;
          fetchWithDelay(); 
        });
    }
  

    fetchWithDelay();
  }
  
//   PARAMS (N iterations, 
//           N set timeout after every N iterations, 
//           N milliseconds to set timeout)
  fetchURLMultipleTimes(29, 50, 60000, () => {
    console.log("All iterations completed");
  });
