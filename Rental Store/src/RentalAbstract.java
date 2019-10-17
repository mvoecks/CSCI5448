
import java.util.ArrayList;

import Tools.Tool;

public abstract class RentalAbstract {
	String description = "Unspecified Rental";
	private boolean isActive = true;
	private int daysDue;
	private int countDays = -1;
	private ArrayList<Tool> toolsRented;
	
	
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
	
	public void addDay() {
		countDays++;
		if (countDays == daysDue) {
			isActive = false;
		}
	}
	
	public abstract double cost();	
	
}
