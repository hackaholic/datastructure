/*
Given an unsorted array of integers, find a pair with given sum in it.
For example,
Input:
arr = [8, 7, 2, 5, 3, 1]
sum = 10

Output:
Pair found at index 0 and 2 (8 + 2)
or
Pair found at index 1 and 4 (7 + 3)
*/



object findPair extends App {

  val arr = Array[Int](8, 7, 2, 5, 3, 1)
  val value = 10
  println(arr.toList)
  val hash = scala.collection.mutable.Map[Int, Int]()
  for((x,i) <- arr.zipWithIndex) {
    if(hash.getOrElse(value-x, false) != false) 
      println(s"Pair found at index ${hash.getOrElse(value-x, -1)} and $i")
    hash(x) = i
  }
}
