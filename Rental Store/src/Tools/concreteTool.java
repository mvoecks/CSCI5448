package Tools;

// Defines the abstract class for all concrete tools
public abstract class concreteTool implements Tool {
	
	// Set the type of tool to Concrete and the cost of the tool to $20
	private String type = "Concrete";
	private String name = "";
	private double cost = 20;
	
	// Getters and setters
	public String getType() {
		return type;
	}
	public String getName() {
		return name;
	}
	public double getCost() {
		return cost;
	}
	public void setName(String name) {
		this.name = name;
	}
	
	// Returns the name and type of the tool.
	public String getDescription() {
		return "Name: "+this.getName()+", Type: "+this.getType();
	}
	
}
