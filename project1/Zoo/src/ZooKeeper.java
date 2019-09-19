import java.util.ArrayList;

public class ZooKeeper {
	
	// A list of all the animals we are keeping track of and the total number of animals in the list
	private ArrayList<Animal> animalList;
	private int numAnimals;
	
	// Constructor if no animals are added when initializing
	ZooKeeper(){
		animalList = new ArrayList<Animal>();
		numAnimals = 0;
	}
	
	// Overriden constructor if there is already a list of animals
	ZooKeeper(ArrayList<Animal> animals){
		animalList = animals;
		numAnimals = animals.size();
	}
	
	// This option adds an animal to the list the zookeeper is keeping track of
	void addAnimal(Animal animal) {
		animalList.add(animal);
		numAnimals++;
	}
	
	
	// A master function that runs through the responsibilities of the zookeeper, while also printing out their status
	void performResponsibilities(){
		// Wake up animals
		System.out.println("\n Zookeeper: I'm waking up all the animals.");
		this.wakeAnimals();
		
		// Perform animal roll call
		System.out.println("\n Zookeeper: Zoo animals, roll call!");
		this.animalRollCall();
		
		// Feed all the animals
		System.out.println("\n Zookeeper: Time for food, eat up.");
		this.feedAnimals();
		
		// Excercise the animals
		System.out.println("\n Zookeeper: Feel free to roam around.");
		this.excerciseAnimals();
		
		// Shut down zoo
		System.out.println("\n Zookeeper: Wrap it up, I'm shutting down the zoo.");
		this.shutdownZoo();
	}
	
	
	// Iterate through the list of animals and wake them up
	void wakeAnimals() {
		for (int i=0; i<numAnimals; i++) {
			animalList.get(i).wakeup();
		}
	}
	
	//Iterate through the list of animals and have them make a noise
	void animalRollCall() {
		for (int i=0; i<numAnimals; i++) {
			animalList.get(i).makeNoise();
		}
	}
	
	// Iterate through the list of animals and feed them
	void feedAnimals() {
		for (int i=0; i<numAnimals; i++) {
			animalList.get(i).eat();
		}
	}
	
	// Excrcise every animal in the list
	void excerciseAnimals() {
		for (int i=0; i<numAnimals; i++) {
			animalList.get(i).roam();
		}
	}

	// Make each animal go to sleep
	void shutdownZoo() {
		for (int i=0; i<numAnimals; i++) {
			animalList.get(i).sleep();
		}
	}

}
