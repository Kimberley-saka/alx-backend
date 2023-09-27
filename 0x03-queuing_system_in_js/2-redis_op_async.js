import { createClient, print } from 'redis';
import {promisify} from 'util';

const client = createClient()
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
  })
  .on('connect', () => console.log('Redis client connected to the server'));
  
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);

  } catch (error) {
    console.log(error);
  }
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
