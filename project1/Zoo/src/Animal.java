
public abstract class Animal {

	// Create protected Strings to keep track of each animals name and type
	protected String name = "";
	protected String type = "";
	
	abstract void wakeup();
	
	abstract void makeNoise();
	
	abstract void roam();
	
	// Prints out gobble gobble for every animal
	void eat() {
		System.out.println(type + "-" + name + ": Gobble Gobble Gobble.");
		
	}
	
	// prints out zzzz.... for each animal
	void sleep() {
		System.out.println(type + "-" + name + ": Zzzzzzzz...");
	};
	
}
