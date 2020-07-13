import scala.util.control.Breaks._

class Queue[T](val size: Int=10){
  private var queue: List[T] = Nil
  private var rear = -1

  def isEmpty = rear == -1

  def isFull = rear+1 == size

  def peek = {
    if(isEmpty) println("Queue is empty") else queue.head 
  }

  def enqueue(e: T) = {
    if(isFull){
      println("Queue is Full")
    }
    else if(isEmpty){
      rear += 1
      queue = queue :+ e
    }
    else{
      rear +=1
      queue = queue :+ e
    }
  }

  def dequeue = {
    if(isEmpty){
      println("Queue is Empty")
    }
    else {
      val ele = queue.head
      queue = queue.tail
      rear -= 1
      ele
    }
  }
}

object QueueTest extends App{
  val queue = new Queue[Int]
  println(s"Queue is empty: ${queue.isEmpty}")
  println("Adding elements to queue")
  for(x <- 1 to queue.size) {
    println(x)
    queue.enqueue(x)
  }
  println(s"Is Queue is Full: ${queue.isFull}")
  println("Removing elemnt from queue")
  println(queue.dequeue)
  println(queue.dequeue)
  println(queue.dequeue)
  println(s"Peeking queue:${queue.peek}")
}
