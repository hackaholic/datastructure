/*

Find all duplicate element in an array

Input: {1, 2, 4, 2, 6, 1, 9, 3, 0, 4, 4}
output: {1, 2, 4}

 */

object FindDuplicates extends App {
  val arr = List(1, 2, 4, 2, 6, 1, 9, 3, 0, 4, 4)
  var dup: List[Int] = Nil
  val hash = scala.collection.mutable.Map[Int, Int]()
  for( x <- arr) {
    hash(x) = hash.getOrElse(x, 0) + 1
    if(hash(x) == 2) dup = dup :+ x
  }
  println(arr)
  println(s"duplicate elements: ${dup}")
}
