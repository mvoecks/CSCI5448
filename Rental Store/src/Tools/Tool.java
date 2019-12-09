package Tools;

// Tool interface. Defines the requirements that all tools must follow.
// Used as the interface for tools in the Factory Design pattern that 
// creates tools
public interface Tool {

	public double getCost();
	
	public String getDescription();
	
	
}
