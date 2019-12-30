//  nth fibonacci

function fibN(n) {
  fibArray = [0, 1];
  if (n <= 2) {
    return fibArray[n - 1];
  } else {
    return fibN(n - 2) + fibN(n - 1);
  }
}
