import java.util.Random;

public class Cat extends Feline {

	Random rand;
	
	Cat(String catName){
		name = catName;
		type = "Cat";
		rand = new Random();
	}
	
	void makeNoise() {
		System.out.println(type + "-" + name + ": Purrrr, Purrrrr.");
		
	}

	// Random action when roaming	
	void roam() {
		
		//Generate a random number to decide what the cat will do when roaming today.
		int tempRand = rand.nextInt(5);
		switch(tempRand) {
			case 0:
				System.out.println(type + "-" + name + ": I'll just go back to sleep, zzzzzzzz...");
			break;
			case 1:
				System.out.println(type + "-" + name + ": Oh! I spotted a mouse I'll go chase.");
				break;
			case 2:
				System.out.println(type + "-" + name + ": Excercising is hard, can you just pet me instead?");
				break;
			case 3:
				System.out.println(type + "-" + name + ": I can get my excercise by running on somebody's keyboard!");
				break;
			case 4:
				System.out.println(type + "-" + name + ": Don't tell me what to do.");
				break;
		}
		
	}

}
