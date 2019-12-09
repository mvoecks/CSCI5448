package Tools;

// Abstract class that defines behavior for all yard tools.
public abstract class yardTool implements Tool {
	
	// Set the type of the tool to yardwork and the daily cost to $8.4
	private String type = "Yardwork";
	private String name = "";
	private double cost = 8.5;
	
	
	//Getters and Setters
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
	
	// Return the name and type of the tool
	public String getDescription() {
		return "Name: "+this.getName()+", Type: "+this.getType();
	}
	
}
