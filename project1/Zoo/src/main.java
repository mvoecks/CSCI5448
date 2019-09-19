import java.io.FileNotFoundException;
import java.io.PrintStream;

public class main {

	public static void main(String[] args) throws FileNotFoundException {
		
		// Set the output stream to output to the file dayatthezoo.out
		PrintStream streamOut = new PrintStream("./dayatthezoo.out");
		System.setOut(streamOut);
		
		// Create our zookeeper object
		ZooKeeper zach = new ZooKeeper();

		// Create our Canine objects, dog and wolf and add them to the zookeeper
		Dog doug = new Dog("Doug");
		Wolf wanda = new Wolf("Wanda");
		zach.addAnimal(doug);
		zach.addAnimal(wanda);
		
		// Create our Feline objects, cat and lion and add them to the zookeeper
		Cat cathy = new Cat("Cathy");
		Lion leo = new Lion("Leo");
		zach.addAnimal(cathy);
		zach.addAnimal(leo);
		
		// Create our Bird objects, crow and vulture and add them to the zookeeper
		Crow carl = new Crow("Carl");
		Vulture vera = new Vulture("Vera");
		zach.addAnimal(carl);
		zach.addAnimal(vera);
		
		// Make the zookeeper perform his responsibilities
		zach.performResponsibilities();
		
	}

}
