
public class Lion extends Feline{

	Lion(String lionName){
		name = lionName;
		type = "Lion";
	}
	
	void makeNoise() {
		System.out.println(type + "-" + name + ": ROAR!");
		
	}

	@Override
	void roam() {
		System.out.println(type + "-" + name + ": That looks like a nice tree to climb today.");
		
	}

}
