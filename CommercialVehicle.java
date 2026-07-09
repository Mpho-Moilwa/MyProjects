public class CommercialVehicle extends Vehicle implements Rentable
{
    private double loadCapacityTons;
    private double dailyInsurance;

    public CommercialVehicle()
    {
        super();
        loadCapacityTons = 0;
        dailyInsurance = 0;
    }

    public CommercialVehicle(char typeVehicle,
                             String clientName,
                             String licencePlateNumber,
                             int duration,
                             double loadCapacityTons)
    {
        super(typeVehicle, clientName, licencePlateNumber, duration);

        this.loadCapacityTons = loadCapacityTons;
        this.dailyInsurance = calcDailyInsurance();
    }

    public double getLoadCapacityTons()
    {
        return loadCapacityTons;
    }

    public double getDailyInsurance()
    {
        return dailyInsurance;
    }

    public double calcDailyInsurance()
    {
        return 30 * loadCapacityTons;
    }

    @Override
    public double calcDailyRent()
    {
        return 1500 + (200 * loadCapacityTons);
    }

    @Override
    public String toString()
    {
        return String.format(
            "%-15s %-12s %4d %6.1f %12s %10s",
            getClientName(),
            getLicencePlateNumber(),
            getDuration(),
            loadCapacityTons,
            "R" + String.format("%.2f", dailyInsurance),
            "R" + String.format("%.2f", calcDailyRent())
    );
    }
}