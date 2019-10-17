
public class AccessoryKit extends RentalDecerator{

	RentalAbstract rental;
	
	public AccessoryKit(RentalAbstract r) {
		rental = r;
		this.setDaysDue(r.getDaysDue());
		this.setToolsRented(r.returnTools());
	}
	
	@Override
	public String getDescription() {
		return rental.getDescription() +"\t\tWith an Accessory Kit \n";
	}

	@Override
	public double cost() {
		return rental.cost() + 7.25;
	}

}
