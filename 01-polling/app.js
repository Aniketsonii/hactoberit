require('dotenv').config();

const { default: fetchURLMultipleTimes } = require('./fetchmultiplewithdelay');

fetchURLMultipleTimes(process.env.TOTAL_ITERATIONS, process.env.SLEEP_INTERVAL, process.env.SLEEP_DURATION, () => {
  console.log("All iterations completed");
});