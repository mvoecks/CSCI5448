
public class Crow extends Bird{

	Crow(String crowName){
		name = crowName;
		type = "Crow";
	}
	
	void makeNoise() {
		System.out.println(type + "-" + name + ": Caw! Caw! Caw!");
	}

}
