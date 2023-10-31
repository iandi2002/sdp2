public interface PricingStrategy {
    double calculatePrice(Product product);
}
public class RegularPricingStrategy implements PricingStrategy {
    @Override
    public double calculatePrice(Product product) {
        return product.getPrice();
    }
}

public class DiscountPricingStrategy implements PricingStrategy {
    private double discountPercentage;

    public DiscountPricingStrategy(double discountPercentage) {
        this.discountPercentage = discountPercentage;
    }

    @Override
    public double calculatePrice(Product product) {
        return product.getPrice() * (1 - discountPercentage / 100);
    }
}