
public class ExtensionChord extends RentalDecerator{

	RentalAbstract rental;
	
	public ExtensionChord(RentalAbstract r) {
		rental = r;
		this.setDaysDue(r.getDaysDue());
		this.setToolsRented(r.returnTools());
	}
	
	@Override
	public String getDescription() {
		return rental.getDescription() +"\t\tWith an Extension Chord \n";
	}

	@Override
	public double cost() {
		return rental.cost() + 2.5;
	}

}
