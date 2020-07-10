import scala.util.control.Breaks._
class Stack[T](val size: Int = 10){
  private var top = -1
  private var stack: List[T] = Nil
  def isEmpty = top == -1
  def isFull = top+1 == size
  def push(e: T) = {
    if(isFull) println("StackOverflow") 
    else {
      stack = stack :+ e
      top += 1
    }
  }
  def peek = stack.lastOption.getOrElse(None)
  def pop = {
    if(top == -1) println("Stack Empty")
    else {
      val e = stack.last
      stack = stack.slice(0, top)
      top -= 1
      e
    }
  }
}


object StackTest extends App {
  val stack =  new Stack[Int]
  println(s"Stack Empty: ${stack.isEmpty}")
  println("Pusing elemnts to Stack ...")
  breakable {
    for(x <- 1 to 20) {
      if(stack.isFull) break
      stack.push(x)
    }
  }
  println(s"stack is Full: ${stack.isFull}")
  println("Popping OUT all elements")
  breakable {
    while(true) {
      if(stack.isEmpty) break
      println(stack.pop)
    }
  }
  stack.pop
}
