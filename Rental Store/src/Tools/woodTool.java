package Tools;

public abstract class woodTool implements Tool {
	private String type = "Woodwork";
	private String name = "";
	private double cost = 10;
	
	public String getType() {
		return type;
	}
	public String getName() {
		return name;
	}
	public double getCost() {
		return cost;
	}
	
	public String getDescription() {
		return "Name: "+this.getName()+", Type: "+this.getType();
	}
	
	public void setName(String name) {
		this.name = name;
	}
}
