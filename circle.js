// Problem from HackerRank 10 Days of JavaScript.

function main() {
    // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
    
    const input = readLine();
    
    // Print the area of the circle:
    let area = (Math.PI * (Math.pow(input, 2)));
    // Print the perimeter of the circle:
    
    let perim = (2 * (Math.PI) * input);
    
    console.log(area);
    console.log(perim);
}
