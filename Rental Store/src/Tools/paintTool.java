package Tools;

// Abstract class that defiens all painting tools.
public abstract class paintTool implements Tool {
	
	// Set the type of tool to Painting and cost of all painting tools to $5.5
	private String type = "Painting";
	private String name = "";
	private double cost = 5.5;
	
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
	
	// Prints the name and type of the tool.
	public String getDescription() {
		return "Name: "+this.getName()+", Type: "+this.getType();
	}
	
}
