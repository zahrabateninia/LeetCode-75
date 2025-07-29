// Given a positive integer millis, write an asynchronous function 
// that sleeps for millis milliseconds. It can resolve any value.
/**
 * @param {number} millis
 * @return {Promise}
 */

async function sleep(millis){
   await new Promise(resolve => setTimeout(resolve, millis)) 
}


let t = Date.now()
sleep(100).then(() => console.log(Date.now() - t)) // 100
// bcz  setTimeout in JavaScript is not perfectly precise—it only guarantees 
// a minimum delay, not an exact one, it may retrun 104, 107 ...