
public class Dog extends Canine {
	
	Dog(String dogName) {
		name = dogName;
		type = "Dog";
	}
	
	@Override
	void makeNoise() {
		System.out.println(type + "-" + name + ": Bark! Bark!");
		
	}

}
