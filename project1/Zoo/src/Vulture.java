
public class Vulture extends Bird{
	
	Vulture(String vultureName){
		name = vultureName;
		type = "Vulture";
	}
	
	void makeNoise() {
		System.out.println(type + "-" + name + ": Hissss.");
	}

}
