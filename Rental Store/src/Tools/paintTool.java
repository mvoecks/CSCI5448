package Tools;

public abstract class paintTool implements Tool {
	private String type = "Painting";
	private String name = "";
	private double cost = 5.5;
	
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
