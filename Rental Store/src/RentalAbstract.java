
// Rental abstract class serves as the highest class in the Rental Decerator design pattern.
// This class specifies all the things a rental needs and also defines a few methods that will help.
import java.util.ArrayList;

import Tools.Tool;

public abstract class RentalAbstract {
	String description = "Unspecified Rental";
	private boolean isActive = true;
	private int daysDue;
	private int countDays = -1;
	private ArrayList<Tool> toolsRented;
	
	// Getters and setters for some private variables that need to be accessed.
	public void setDescription(String s) {
		description = s;
	}
	public String getDescription() {
		return description;
	}
	public boolean getActiveStatus() {
		return isActive;
	}
	public void setDaysDue(int due) {
		daysDue = due;
	}
	public int getDaysDue() {
		return daysDue;
	}
	public void setToolsRented(ArrayList<Tool> lst){
		toolsRented = lst;
	}
	public ArrayList<Tool> returnTools() {
		return toolsRented;
	}
	
	// Adds a day to the days the rental has been active. If this number exceeds the rental limit 
	// the isActive flag is set to false so the store can get its items back.
	public void addDay() {
		countDays++;
		if (countDays == daysDue) {
			isActive = false;
		}
	}
	
	// This will calculate the cost of the rental. For rentaldecerators this will add a flat fee to the order.
	public abstract double cost();	
	
	// This will get the customer type.
	public abstract String getCustomerType();
	
}
