package Tools;

// Wood abstract class that defines behavior for all wood tools.
public abstract class woodTool implements Tool {
	
	// Set the type to Woodwork and cost to $10 for all wood tools
	private String type = "Woodwork";
	private String name = "";
	private double cost = 10;
	
	
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
	
	// Return the name and type of the tool.
	public String getDescription() {
		return "Name: "+this.getName()+", Type: "+this.getType();
	}
	
}
