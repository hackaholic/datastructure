/*
Given an array of integers, print all sub-arrays with 0 sum.

For example,
Input: { 4, 2, -3, -1, 0, 4 }
Sub-arrays with 0 sum are
{ -3, -1, 0, 4 }
{ 0 }

Input: { 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
Sub-arrays with 0 sum are
{ 3, 4, -7 }
{ 4, -7, 3 }
{ -7, 3, 1, 3 }
{ 3, 1, -4 }
{ 3, 1, 3, 1, -4, -2, -2 }
{ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 }
*/

object main extends App {
  //val arr = List[Int](4, 2, -3, -1, 0, 4)
  val arr = List[Int](3, 4, -7, 3, 1, 3, 1, -4, -2, -2)
  val value = 0
  for( k <- 0 to arr.length-1) {
    var total = 0
    for( (x,i) <- arr.slice(k, arr.length).zipWithIndex) {
      total += x
      if(total == value) println(s"Subarray ${arr.slice(k, k+i+1)}")
    }
  }
}
