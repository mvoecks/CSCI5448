
public class Wolf extends Canine{

	Wolf(String wolfName){
		name = wolfName;
		type = "Wolf";
	}
	
	@Override
	void makeNoise() {
		System.out.println(type + "-" + name + ": HOWL!!!");
		
	}

}
