package Tools;

// Abstract class that defines all plumbing tools. 
public abstract class plumbingTool implements Tool {
	
	// Set the type of tool to Plumbing and the cost to $7
	private String type = "Plumbing";
	private String name = "";
	private double cost = 7;
	
	
	// Getters and Setters
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
	
	// Print the name and type of the tool.
	public String getDescription() {
		return "Name: "+this.getName()+", Type: "+this.getType();
	}
	
}
