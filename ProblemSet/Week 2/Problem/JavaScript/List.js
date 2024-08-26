const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let kpop = [];

/**
 * Asks the user to enter the number of K-POP groups to add to the list
 * and then asks for each group individually.
 */
rl.question('Enter the number of K-POP groups to add to the list: ', (numGroups) => {
  numGroups = parseInt(numGroups);
  let count = 0;
  
  /**
   * Recursive function to ask for each K-POP group individually.
   */
  const askGroup = () => {
    rl.question(`Group ${count + 1}: `, (group) => {
      kpop.push(group);
      count++;
      if (count < numGroups) {
        askGroup(); // Recursively ask for the next group
      } else {
        console.log('List KPOP:');
        console.log(kpop.join(' '));
        askRemove(); // Move on to ask about removing a group
      }
    });
  };
  askGroup(); // Start asking for groups
});

/**
 * Asks the user if they want to remove a K-POP group from the list.
 */
const askRemove = () => {
  rl.question('Do you want to remove a K-POP group from the list? (yes/no): ', (removeGroup) => {
    if (removeGroup.toLowerCase() === 'yes') {
      rl.question('Enter the K-POP group to remove: ', (groupToRemove) => {
        const index = kpop.indexOf(groupToRemove);
        if (index !== -1) {
          kpop.splice(index, 1);
          console.log('Updated list KPOP:');
          console.log(kpop.join(' '));
        } else {
          console.log('Group not found in the list.');
        }
        askAdd(); // Move on to ask about adding a new group
      });
    } else {
      console.log('No K-POP group removed from the list.');
      askAdd(); // Move on to ask about adding a new group
    }
  });
};

/**
 * Asks the user if they want to add another K-POP group to the list.
 */
const askAdd = () => {
  rl.question('Do you want to add another K-POP group to the list? (yes/no): ', (addGroup) => {
    if (addGroup.toLowerCase() === 'yes') {
      rl.question('Enter the new K-POP group: ', (newGroup) => {
        kpop.push(newGroup);
        console.log('Updated list KPOP:');
        console.log(kpop.join(' '));
        rl.close(); // Close the readline interface
      });
    } else {
      console.log('No new K-POP group added to the list.');
      rl.close(); // Close the readline interface
    }
  });
};
