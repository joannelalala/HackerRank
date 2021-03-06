'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'divisibleSumPairs' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER_ARRAY ar
 */

function divisibleSumPairs(n, k, ar) {
    // Write your code here
    const map = new Map() ;
    // initialize numOfPairs
    let numOfPairs = 0 ;

    for (let i = 0; i < ar.length; i ++){
        const remainder  = ar[i] % k ;
        let diff = k - remainder ;
        if (diff === k){
            diff = 0; // means ar[i] is diversible by k
        }

        if map.has(diff){
            numOfPairs += map.get(diff);
        }

        if map.has(remainder){
            let count = map.get(remainder);
            map.set(remainder, count + 1) ; 
        } else {
            map.set(remainder, 1);
        }
    }
    return numOfPairs;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const k = parseInt(firstMultipleInput[1], 10);

    const ar = readLine().replace(/\s+$/g, '').split(' ').map(arTemp => parseInt(arTemp, 10));

    const result = divisibleSumPairs(n, k, ar);

    ws.write(result + '\n');

    ws.end();
}
