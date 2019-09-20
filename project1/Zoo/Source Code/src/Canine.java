public abstract class Canine extends Animal{
	
	void roam() {
		System.out.println(type + "-" + name + ": I'll go explore for some food!");
	}
	
	void wakeup() {
		System.out.println(type + "-" + name + ": Woof! I'm ready for action.");
	}
}
