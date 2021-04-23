function getMoneySpent(keyboards, drives, s){
    // Complete this function
    let max = -1;

    // I'm trying to get the total number of keyboard and drive
    // then compare to the money.
    for(let i = 0; i < keyboards.length; i++){
        var temp = 0;
        for(let j = 0; j < drives.length; j++){
            if(keyboards[i] + drives[j] <= s){
                temp = keyboards[i] + drives[j];
                max = temp > max ? temp : max;
            }
        }
    }

    return max;
}
