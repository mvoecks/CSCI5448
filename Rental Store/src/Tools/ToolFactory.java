package Tools;

// Factory Design pattern is used to create tools. This class has one function which is to 
// accept a request from the rentalStore to create a the tool object they specify. if the tool
// does not exist an error is thrown.
public class ToolFactory {
	
	// Retrieves a tool specified by the paramters
	// - toolType : String (All Lowercase) The type of tool you want.
	// - toolName : String name that the tool will be refered to as. (Should be unique but it doesnt check)
	public Tool getTool(String toolType, String toolName) throws ClassNotFoundException {
		if(toolType == "brush") {
			return new Brush(toolName);
		}	
		else if (toolType == "roller") {
			return new Roller(toolName);
		}
		else if (toolType == "mixer") {
			return new Mixer(toolName);
		}
		else if (toolType == "jackhammer") {
			return new Jackhammer(toolName);
		}
		else if (toolType == "wrench") {
			return new Wrench(toolName);
		}
		else if (toolType == "plunger") {
			return new Plunger(toolName);
		}
		else if (toolType == "saw") {
			return new Saw(toolName);
		}
		else if (toolType == "sander") {
			return new Sander(toolName);
		}
		else if (toolType == "rake") {
			return new Rake(toolName);
		}
		else if (toolType == "shovel") {
			return new Shovel(toolName);
		}
		else{
			throw new ClassNotFoundException("Class: "+toolType+" is not a valid tool");
		}
	}
}
