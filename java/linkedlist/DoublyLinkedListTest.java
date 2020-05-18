import java.io.*;

class Node {
	int value;
	Node next, prev;
	Node(int n){
		this.value = n;
		this.next = null;
		this.prev = null;
	}
}

class DoublyLinkedList {
	Node head;
	DoublyLinkedList(Node node){
		this.head = node;
	}

	void display(){
		Node temp = head;
		while(temp!=null){
			System.out.println(temp.value);
			temp = temp.next;
		}
	}
}

class DoublyLinkedListTest {
	public static void main(String args[]) throws IOException {
		BufferedReader br;
		Node head = null;
		String s = null;
		try(FileInputStream f = new FileInputStream(args[0])){
			br = new BufferedReader(new InputStreamReader(f));
			s = br.readLine();
			head = new Node(Integer.parseInt(s));
			Node tail = head;
			while(true){
				//System.out.println(s);
				s = br.readLine();
				if(s!=null){
					Node temp = new Node(Integer.parseInt(s));
				        tail.next = temp;
				        temp.prev = tail;
				        tail = temp;
				}
				else {break;}
			}
		}
		catch(Exception e){
			System.out.println(e);
		}

		DoublyLinkedList dlist = new DoublyLinkedList(head);
		dlist.display();

	}
}
