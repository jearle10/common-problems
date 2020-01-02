// Title: nth fibonacci
// Description: Find the nth fibonacci number and return it

function fibN(n) {
  fibArray = [0, 1];
  if (n <= 2) {
    return fibArray[n - 1];
  } else {
    console.log(fibN(n - 1) + fibN(n - 2));
  }
}

// Title: List of fibonacci numbers
// Description: Return a list of n fibonacci numbers

function fibList(n) {
  fibArray = [0, 1];
  if (n <= 2) {
    return fibArray;
  } else {
    for (var i = 2; i < n; i++) {
      fibArray.push(fibArray[i - 1] + fibArray[i - 2]);
    }
  }
  console.log(fibArray);
}
