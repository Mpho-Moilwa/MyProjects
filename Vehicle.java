public class Vehicle 
{
    private char typeVehicle;
    private String clientName;
    private String licencePlateNumber;
    private int duration;
    
    public Vehicle()
    {
        
    }
    
    public Vehicle(char typeVehicle, String clientName, String licencePlateNumber, int duration)
    {
        this.typeVehicle = typeVehicle;
        this.clientName = clientName;
        this.licencePlateNumber = licencePlateNumber;
        this.duration = duration;
    }
    
    public char getTypeVehicle()
    {
        return typeVehicle;
    }
    
    public String getClientName()
    {
        return clientName;
    }
    
    public String getLicencePlateNumber()
    {
        return licencePlateNumber;
    }
    
    public int getDuration()
    {
        return duration;
    }
    
    public String toString()
    {
        return String.format("%-15s %-10s %-5d", clientName, licencePlateNumber, duration);
    }
}