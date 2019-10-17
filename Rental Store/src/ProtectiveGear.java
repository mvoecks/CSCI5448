
public class ProtectiveGear extends RentalDecerator{

	RentalAbstract rental;
	
	public ProtectiveGear(RentalAbstract r) {
		rental = r;
		this.setDaysDue(r.getDaysDue());
		this.setToolsRented(r.returnTools());
	}
	
	@Override
	public String getDescription() {
		return rental.getDescription() +"\t\tWith a Protective Gear Pack\n";
	}

	@Override
	public double cost() {
		return rental.cost() + 10;
	}

}
