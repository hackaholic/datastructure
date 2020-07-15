import scala.util.control.Breaks._
import scala.util.control._

class CircularQueue[T](val size: Int = 10){
  private var queue = scala.collection.mutable.MutableList[T]()
  private var front = -1
  private var rear = -1

  def isEmpty = queue.isEmpty

  def isFull = size == queue.length

  def peek = if(!isEmpty) queue.head else None

  def display = {
    if(isEmpty) println("Queue is Empty")
    else {
      println(queue)
    }
  }

  def enqueue(e: T) = {
    if(isEmpty){
      queue = queue :+ e
      front += 1
      rear += 1
    }
    else if(isFull) {
      println("Queue is Full")
    }
    else{
      queue = queue :+ e
      rear = (rear+1) % 1
    }
  }

  def dequeue = {
    if(isEmpty) println("Queue is Empty")
    else if(queue.length == 1) {
      val e = peek
      front = -1
      rear = -1
      queue = queue.tail
    }
    else {
      val e = peek
      front = (front+1) % size
      queue = queue.tail
      e
    }
  }
}


object CircularQueueTest extends App {
  val queue = new CircularQueue[Int]

  def instruction = println(""" 
  Choose Options ...
  1 -> Enqueue
  2 -> Dequeue
  3 -> Peek
  4 -> Display
  9 -> Quit
  """)

  breakable {
    while(true) {
      try {
        instruction
        val input = scala.io.StdIn.readInt
        if(input == 1) {
          if(!queue.isFull) {
            val e = scala.io.StdIn.readInt
            queue.enqueue(e)
          }
          else println("Queue isFull")
        }
        if(input == 2) queue.dequeue
        if(input == 3) println(queue.peek)
        if(input == 4) queue.display
        if(input == 9) {
          println("Exiting the program")
          break
        }
      }
      catch {
        case e: ControlThrowable => System.exit(0)
        case default: Throwable  => default.printStackTrace
      }
    }
  }
}
