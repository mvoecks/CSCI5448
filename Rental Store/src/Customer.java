
public abstract class Customer {
	private String name;
	private String type;
	
	public void setName(String n) {
		name = n;
	}
	
	public String getName() {
		return name;
	}
	
	public String getType() {
		return type;
	}
	
	public void setType(String t) {
		type = t;
	}
	
	abstract void rentTools(RentalStore store);
	
}
