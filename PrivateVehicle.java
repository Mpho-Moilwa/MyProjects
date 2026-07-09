public class PrivateVehicle extends Vehicle implements Rentable
{
    private char category;
    private int numSeats;
    private int numDoors;
    
    public PrivateVehicle()
    {
        super();
    }
    
    public PrivateVehicle(char typeVehicle, String clientName, String licencePlateNumber, int duration, char category, int numSeats, int numDoors)
    {
        super(typeVehicle, clientName, licencePlateNumber, duration);
        this.category = category;
        this.numSeats = numSeats;
        this.numDoors = numDoors;
    }
    
    public char getCategory()
    {
        return category;
    }
    
    public int getNumSeats()
    {
        return numSeats;
    }
    
    public int getNumDoors()
    {
        return numDoors;
    }
    
    public double calcDailyRent()
    {
        double rent = 0;
        
        if (category == 'S' || category == 's')
        {
            rent = 800 + (100 * numSeats);
        }
        
        else if (category == 'U' || category == 'u')
        {
            rent = 1500 + (200 * numSeats);
        }
        
        else if (category == 'B' || category == 'b')
        {
            rent = 1200 + (150 * numSeats);
        }
        
        return rent;
    }
    
   @Override
   public String toString()
   {
       return String.format(
            "%-15s %-12s %4d %6s %6d %6d  R%.2f",
            getClientName(),
            getLicencePlateNumber(),
            getDuration(),
            category,
            numSeats,
            numDoors,
            calcDailyRent()
            );
}
}